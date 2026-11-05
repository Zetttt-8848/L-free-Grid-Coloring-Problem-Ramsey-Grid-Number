"""Bounded discovery on dissociated encodings of planar paraboloids.

The finite SAT answers are discovery data. In particular a negative solver
answer is not a pencil-and-paper obstruction used in the research proof.
"""
from itertools import combinations
from pathlib import Path
from pysat.solvers import Glucose4
import json
import time
from threading import Timer

records = []
for side in range(3, 13):
    base = 8 * side * side + 1
    labeled = sorted((x + base*y + base*base*(x*x+y*y), (x, y))
                     for x in range(side) for y in range(side))
    source = [a for a, _ in labeled]
    ids = {(v, u): j+1 for j, (u, v) in enumerate(combinations(source, 2))}
    fibers = {}
    for v, u in ids:
        fibers.setdefault(v-u, []).append(u)
    clauses = []
    for d, starts in fibers.items():
        for u, v in combinations(sorted(starts), 2):
            edge = [ids[u+d, u], ids[v+d, u], ids[v+d, v]]
            clauses.extend((edge, [-t for t in edge]))
    before = time.monotonic()
    with Glucose4(bootstrap_with=clauses) as solver:
        solver.conf_budget(20000)
        timer = Timer(5.0, solver.interrupt)
        timer.start()
        try:
            answer = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        rec = dict(side=side, base=base, labels=labeled,
                   marks=len(source), cells=len(ids), corners=len(clauses)//2,
                   answer=answer, seconds=time.monotonic()-before)
        if answer is True:
            positive = {i for i in solver.get_model() if i > 0}
            rec['colors'] = [int(i in positive) for i in ids.values()]
    records.append(rec)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Bounded discovery only. Negative solver output is not a proof.',
        cases=records), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in rec.items()
                      if k not in ('labels', 'colors')}), flush=True)
    if answer is False or answer is None:
        break
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
    scope='Bounded discovery only. Negative solver output is not a proof.',
    cases=records), indent=2)+'\n', encoding='utf-8')
