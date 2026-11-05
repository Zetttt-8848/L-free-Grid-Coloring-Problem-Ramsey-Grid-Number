"""Finite discovery for an equality/order type rule on B x {0,1}^3."""
from pathlib import Path
from itertools import product,combinations
from pysat.solvers import Solver
from threading import Timer
import json,time

records=[]
for m,typed in [(2,True),(3,False),(4,False)]:
    B=[0,1,3,7][:m]  # all distinct positive differences for m<=4
    H=2*max(B)+1
    weights=[1,H,3*H,9*H]
    points=list(product(B,range(2),range(2),range(2)))
    enc=lambda p:sum(a*b for a,b in zip(p,weights))
    points.sort(key=enc)
    cellpairs=[(y,x) for y in points for x in points if enc(x)<enc(y)]
    def cellkey(y,x):
        if not typed:return (y,x)
        return ((x[0]>y[0])-(x[0]<y[0]),x[1:],y[1:])
    variables={}
    for y,x in cellpairs:
        key=cellkey(y,x)
        if key not in variables:variables[key]=len(variables)+1
    keyvar=lambda y,x:variables[cellkey(y,x)]
    byval={enc(p):p for p in points}
    fibers={}
    for y,x in cellpairs:fibers.setdefault(enc(y)-enc(x),[]).append((y,x))
    clauses=[];edges=[]
    for d,ps in fibers.items():
        for (y,x),(yp,xp) in combinations(sorted(ps,key=lambda p:enc(p[1])),2):
            h=(keyvar(y,x),keyvar(yp,x),keyvar(yp,xp))
            clauses.append(list(h));clauses.append([-i for i in h]);edges.append(h)
    clauses.append([1])
    start=time.monotonic()
    with Solver(name='g4',bootstrap_with=clauses) as solver:
        timer=Timer(8,solver.interrupt);timer.start()
        try:ans=solver.solve_limited(expect_interrupt=True)
        finally:timer.cancel()
        rec=dict(m=m,typed=typed,variables=len(variables),cells=len(cellpairs),corners=len(edges),answer=ans,seconds=time.monotonic()-start)
        if ans:
            positive={q for q in solver.get_model() if q>0}
            rec['type_rule']=[dict(key=key,value=int(v in positive)) for key,v in variables.items()]
            rec['source']=sorted(byval)
            rec['rows']=[''.join(str(int(keyvar(y,x) in positive)) for x in points if enc(x)<enc(y)) for y in points[1:]]
    records.append(rec)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Bounded construction discriminator; raw negatives are not mathematical obstructions.',cases=records),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('type_rule','rows','source')}),flush=True)
