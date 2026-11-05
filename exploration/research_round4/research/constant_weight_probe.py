"""Discovery on constant-weight source layers, not a negative proof."""
from pathlib import Path
from itertools import combinations
from pysat.solvers import Glucose4
import json,time

root=Path(__file__).resolve().parent
results=[]
for dimension,weight in [(6,3),(7,3),(8,3),(8,4),(9,4)]:
    A=sorted(sum(3**i for i in s) for s in combinations(range(dimension),weight))
    ids={(v,u):j+1 for j,(u,v) in enumerate(combinations(A,2))}
    fibers={}
    for v,u in ids: fibers.setdefault(v-u,[]).append(u)
    clauses=[]
    for d,f in fibers.items():
        for u,v in combinations(sorted(f),2):
            e=[ids[u+d,u],ids[v+d,u],ids[v+d,v]]
            clauses.extend((e,[-x for x in e]))
    start=time.monotonic()
    with Glucose4(bootstrap_with=clauses) as solver:
        solver.conf_budget(100000)
        answer=solver.solve_limited()
        out=dict(dimension=dimension,weight=weight,marks=A,cells=len(ids),
                 corners=len(clauses)//2,answer=answer,seconds=time.monotonic()-start)
        if answer is True:
            positive={x for x in solver.get_model() if x>0}
            out['colors']=[int(ids[v,u] in positive) for v,u in ids]
    results.append(out)
    print(json.dumps({k:v for k,v in out.items() if k not in ('marks','colors')}),flush=True)
(root/'constant_weight_probe.json').write_text(json.dumps(dict(
    scope='Bounded discovery. Raw negatives and search bounds are not theorems.',
    cases=results),indent=2)+'\n',encoding='utf-8')
