"""Bounded discriminator for possible extra structure of the four-step system."""
import itertools,json,threading,time
from pathlib import Path
from pysat.solvers import Solver
results=[]
cases=[(10,5,None),(14,5,None),(20,5,None),(32,4,((8,8),(14,8)))]
for n,maxstep,unequal in cases:
    m=n-2; cells=[(x,y) for x in range(m+1) for y in range(m+1-x)]
    ix={(p,c):3*i+c+1 for i,p in enumerate(cells) for c in range(3)}
    clauses=[];edges=[]
    for p in cells:
        clauses.append([ix[p,c] for c in range(3)])
        clauses.extend([[-ix[p,a],-ix[p,b]] for a,b in itertools.combinations(range(3),2)])
        x,y=p
        for d in range(1,min(maxstep,m-x-y)+1):
            tr=(p,(x+d,y),(x,y+d));edges.append(tr)
            for cs in itertools.product(range(3),repeat=3):
                if sum(cs)%3==0:clauses.append([-ix[q,c] for q,c in zip(tr,cs)])
    clauses.append([ix[cells[0],0]])
    if unequal:
        clauses.extend([[-ix[unequal[0],c],-ix[unequal[1],c]] for c in range(3)])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        timer=threading.Timer(5,solver.interrupt);timer.start();start=time.monotonic()
        ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
        row=dict(n=n,maxstep=maxstep,unequal=unequal,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
        if ok:
            model=set(solver.get_model());z={p:next(c for c in range(3) if ix[p,c] in model) for p in cells}
            assert all(sum(z[p] for p in tr)%3 for tr in edges)
            if unequal:assert z[unequal[0]]!=z[unequal[1]]
            row['colors']=[[x,y,z[x,y]] for x,y in cells]
    results.append(row);print(json.dumps({k:v for k,v in row.items() if k!='colors'}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
