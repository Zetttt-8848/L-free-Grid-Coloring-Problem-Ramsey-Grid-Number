"""New bounded periodic-strip discovery; no saved witness is rechecked."""
import json
import time
from pathlib import Path
from pysat.solvers import Solver

started=time.monotonic()
columns=[
    [0,2,3,5,7,9], [0,1,4,9,11], [0,1,4,10,12,17],
    [0,1,3,7,15], [0,1,3,7,15,31], [0,1,4,5,11],
    [0,1,3,4,9], [0,1,3,4,9,10], [0,2,5,7,11],
    [0,1,4,6,11,13], [0,1,3,8,12,14],
]
periods=[4,6,8,10,12,16,20,24,32,48,64]
records=[]
for C in columns:
    for period in periods:
        if time.monotonic()-started>45:
            break
        index={(x,c):1+x*len(C)+i for x in range(period) for i,c in enumerate(C)}
        clauses=[]
        for i,c in enumerate(C):
            for d in C[i+1:]:
                h=d-c
                for x in range(period):
                    v=[index[x,c],index[(x+h)%period,c],index[(x+h)%period,d]]
                    clauses.extend([v,[-j for j in v]])
        with Solver(name='g3',bootstrap_with=clauses) as solver:
            solver.conf_budget(10000)
            answer=solver.solve_limited()
            truth=set(j for j in solver.get_model() if j>0) if answer is True else None
        rec={'C':C,'period':period,'status':'SAT' if answer is True else 'UNSAT' if answer is False else 'UNKNOWN'}
        if truth is not None:
            rec['row_words']=[''.join(str(int(index[x,c] in truth)) for c in C) for x in range(period)]
            rec['column_words']=[''.join(str(int(index[x,c] in truth)) for x in range(period)) for c in C]
        records.append(rec)
        if truth is not None:
            break
result={'purpose':'periodic-strip construction discovery, not a proof from SAT status',
        'wall_cap_seconds':45,'conflict_budget_per_solve':10000,
        'elapsed_seconds':time.monotonic()-started,'records':records}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'solves':len(records),'seconds':result['elapsed_seconds'],'SAT':[r for r in records if r['status']=='SAT']}))
