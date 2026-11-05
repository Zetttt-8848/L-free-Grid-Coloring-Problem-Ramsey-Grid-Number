"""Bounded discovery for mixed-endpoint corner counts in proper two-color sources."""
from pathlib import Path
from itertools import combinations
from ortools.sat.python import cp_model
import json,time

sources=[('cube4',sorted(sum(3**i for i in range(4) if mask>>i&1) for mask in range(16))),
         ('ten_mark',[0,1,3,4,6,7,8,10,11,13])]
records=[]
for name,A in sources:
    cells=[(v,u) for v in A for u in A if u<v]
    ix={p:i for i,p in enumerate(cells)}
    fibers={}
    for p in cells:fibers.setdefault(p[0]-p[1],[]).append(p)
    edges=[]
    for d,ps in fibers.items():
        for p,r in combinations(sorted(ps),2):
            edges.append((ix[p],ix[(r[0],p[1])],ix[r]))
    model=cp_model.CpModel()
    z=[model.new_bool_var(f'z{i}') for i in range(len(cells))]
    model.add(z[0]==0)
    terms=[]
    for j,(p,q,r) in enumerate(edges):
        model.add(z[p]+z[q]+z[r]>=1);model.add(z[p]+z[q]+z[r]<=2)
        x=model.new_bool_var(f'mixed{j}')
        model.add_allowed_assignments([z[p],z[r],x],[(0,0,0),(0,1,1),(1,0,1),(1,1,0)])
        terms.append(x)
    model.maximize(sum(terms))
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=8
    solver.parameters.num_search_workers=4
    start=time.monotonic();status=solver.solve(model)
    rec=dict(name=name,A=A,M=len(cells),T=len(edges),status=solver.status_name(status),seconds=time.monotonic()-start)
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        col=[solver.value(t) for t in z]
        rec.update(X=sum(col[p]!=col[r] for p,q,r in edges),
                   H=sum(col[p]==col[r] for p,q,r in edges),
                   rows=[''.join(str(col[ix[v,u]]) for u in A if u<v) for v in A[1:]])
    records.append(rec)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
       scope='Finite constructions or raw search results only; no universal inequality.',cases=records),indent=2)+'\n',encoding='utf-8')
    print(json.dumps(rec),flush=True)
