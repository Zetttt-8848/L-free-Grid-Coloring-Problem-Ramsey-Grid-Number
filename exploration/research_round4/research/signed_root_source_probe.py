"""Bounded source-coloring discovery on signed differences of powers.

No solver-negative answer is an obstruction theorem.
"""
from itertools import combinations
from pathlib import Path
from threading import Timer
from pysat.solvers import Glucose4
import json
import time

records=[]
for r in range(3,9):
    A=sorted({5**i-5**j for i in range(r) for j in range(r) if i!=j})
    ids={(v,u):i+1 for i,(u,v) in enumerate(combinations(A,2))}
    fibers={}
    for v,u in ids:
        fibers.setdefault(v-u,[]).append(u)
    clauses=[]
    for d, starts in fibers.items():
        for u,v in combinations(sorted(starts),2):
            e=[ids[u+d,u],ids[v+d,u],ids[v+d,v]]
            clauses.extend((e,[-x for x in e]))
    start=time.monotonic()
    with Glucose4(bootstrap_with=clauses) as solver:
        timer=Timer(3,solver.interrupt)
        timer.start()
        try:
            answer=solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        rec=dict(rank=r,source=A,cells=len(ids),corners=len(clauses)//2,
                 answer=answer,seconds=time.monotonic()-start)
        if answer is True:
            pos={x for x in solver.get_model() if x>0}
            rec['colors']=[int(i in pos) for i in ids.values()]
    records.append(rec)
    print(json.dumps({k:v for k,v in rec.items() if k not in ('source','colors')}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Bounded discovery. Raw negative output is not a theorem.',
        cases=records),indent=2)+'\n',encoding='utf-8')
    if answer is not True:
        break
