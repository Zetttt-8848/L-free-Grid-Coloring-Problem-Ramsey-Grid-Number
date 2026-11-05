"""A bounded SAT discriminator for the small rainbow-forcing question."""
import itertools,json,threading,time
from pathlib import Path
from pysat.solvers import Solver
root=Path(__file__).resolve().parent;results=[]
for n in (10,12):
    cells=[(v,u) for v in range(n) for u in range(v)];ix={(q,c):3*i+c+1 for i,q in enumerate(cells) for c in range(3)}
    clauses=[];corners=[]
    for q in cells:
        clauses.append([ix[q,c] for c in range(3)])
        clauses.extend([[-ix[q,a],-ix[q,b]] for a,b in itertools.combinations(range(3),2)])
    for x,y in cells:
        for d in range(1,n-x):
            tr=((x,y),(x+d,y),(x+d,y+d));corners.append(tr)
            clauses.extend([[-ix[q,c] for q in tr] for c in range(3)])
            clauses.extend([[-ix[q,c] for q,c in zip(tr,colors)] for colors in itertools.permutations(range(3))])
    clauses.append([ix[cells[0],0]])
    for j,q in enumerate(cells):clauses.append([-ix[q,2]]+[ix[p,1] for p in cells[:j]])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        timer=threading.Timer(10,solver.interrupt);timer.start();start=time.monotonic()
        ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
        row=dict(n=n,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start,stats=solver.accum_stats())
        if ok:
            values=set(v for v in solver.get_model() if v>0);z={q:next(c for c in range(3) if ix[q,c] in values) for q in cells}
            assert all(len({z[q] for q in tr})==2 for tr in corners)
            row['colors']=[[v,u,c] for (v,u),c in z.items()]
    results.append(row);print(json.dumps({k:v for k,v in row.items() if k!='colors'}),flush=True)
    if ok is False:break
(root/'two_color_per_corner_sat.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
