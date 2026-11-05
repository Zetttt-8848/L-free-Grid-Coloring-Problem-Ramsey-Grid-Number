"""Test whether a changed scalar order gives a high-energy root source.

Bounded construction discovery, with no claims from negative answers.
"""
from itertools import combinations
from pathlib import Path
from threading import Timer
from pysat.solvers import Glucose4
import json, random, time

randomizer=random.Random(20260912)
records=[]
for case in range(6):
    rank=8
    weights=sorted(randomizer.sample(range(1,10**9),rank))
    A=sorted({u-v for u in weights for v in weights if u!=v})
    ids={(v,u):i+1 for i,(u,v) in enumerate(combinations(A,2))}
    fibers={}
    for v,u in ids: fibers.setdefault(v-u,[]).append(u)
    clauses=[]
    for d, starts in fibers.items():
        for u,v in combinations(sorted(starts),2):
            e=[ids[u+d,u],ids[v+d,u],ids[v+d,v]]
            clauses.extend((e,[-x for x in e]))
    start=time.monotonic()
    with Glucose4(bootstrap_with=clauses) as solver:
        timer=Timer(3,solver.interrupt)
        timer.start()
        try: answer=solver.solve_limited(expect_interrupt=True)
        finally: timer.cancel()
        rec=dict(case=case,weights=weights,source=A,cells=len(ids),
                 corners=len(clauses)//2,answer=answer,
                 seconds=time.monotonic()-start)
        if answer is True:
            pos={x for x in solver.get_model() if x>0}
            rec['colors']=[int(i in pos) for i in ids.values()]
    records.append(rec)
    print(json.dumps({k:v for k,v in rec.items()
                      if k not in ('weights','source','colors')}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Bounded discovery. Negative answers are not proofs.',
        cases=records),indent=2)+'\n',encoding='utf-8')
    if answer is True: break
