"""One bounded discovery pass for new dense Cartesian candidates.

Not a verification pass. Raw SAT assignments are candidate inputs for a
subsequent explicit construction argument; negative solves prove no family
bound. Distinct candidates receive at most one solve.
"""
import json
import random
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
from pysat.solvers import Solver

rng = random.Random(202609121117)
out = Path(__file__).with_suffix('.json')
started = time.monotonic()
seen = set()
records = []
models = []
draws = 0

def profile(a):
    return Counter(y-x for i,x in enumerate(a) for y in a[i+1:])

while len(records) < 1000 and draws < 10000 and time.monotonic()-started < 45:
    draws += 1
    width = rng.randrange(9, 22)
    b = rng.randrange(6, min(13, width)+1)
    c = rng.randrange(6, min(13, width)+1)
    B = tuple(sorted(rng.sample(range(width), b)))
    C = tuple(sorted(rng.sample(range(width), c)))
    B = tuple(x-B[0] for x in B)
    C = tuple(x-C[0] for x in C)
    if (B,C) in seen:
        continue
    seen.add((B,C))
    rb,rc=profile(B),profile(C)
    U=sum(v*rc.get(h,0) for h,v in rb.items())
    if 2*U <= 3*b*c:
        continue
    cells=[(x,y) for x in B for y in C]
    idx={p:i+1 for i,p in enumerate(cells)}
    Bs,Cs=set(B),set(C)
    clauses=[]
    for x in B:
        for h in rb:
            if x+h not in Bs:
                continue
            for y in C:
                if y+h in Cs:
                    tri=[idx[x,y],idx[x+h,y],idx[x+h,y+h]]
                    clauses.extend([tri,[-j for j in tri]])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        solver.conf_budget(3000)
        answer=solver.solve_limited()
        model=solver.get_model() if answer is True else None
    status='SAT' if answer is True else ('UNSAT' if answer is False else 'UNKNOWN')
    record={'B':B,'C':C,'U':U,'cells':b*c,'ratio':str(Fraction(U,b*c)),'status':status}
    records.append(record)
    if model is not None:
        truth=set(j for j in model if j>0)
        record['colors']=[[int(idx[x,y] in truth) for y in C] for x in B]
        models.append(record)
        if U>2*b*c:
            break

result={'purpose':'new bounded dense-candidate discovery, not a universal certificate',
        'candidate_limit':1000,'draw_limit':10000,'wall_limit_seconds':45,
        'conflict_budget_per_solve':3000,'draws':draws,'distinct_draws':len(seen),
        'solves':len(records),'elapsed_seconds':time.monotonic()-started,
        'status_counts':dict(Counter(r['status'] for r in records)),
        'models':models,'records':records}
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('models','records')}))
print(json.dumps({'best_raw_sat':max(models,key=lambda r:Fraction(r['ratio']),default=None)}))
