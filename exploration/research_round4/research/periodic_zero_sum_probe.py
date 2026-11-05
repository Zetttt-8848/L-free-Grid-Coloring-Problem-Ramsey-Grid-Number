"""Seek uniform periodic constructions that separate restricted-step hypotheses."""
import itertools,json,threading,time
from pathlib import Path
from pysat.solvers import Solver
root=Path(__file__).resolve().parent; results=[]
for dimension,q in [(1,q) for q in range(5,17)]+[(2,q) for q in (5,6,7,8,9,10,12)]:
    cells=list(range(q)) if dimension==1 else list(itertools.product(range(q),repeat=2))
    ix={(p,c):3*i+c+1 for i,p in enumerate(cells) for c in range(3)}
    clauses=[]; edges=set()
    for p in cells:
        clauses.append([ix[p,c] for c in range(3)])
        clauses.extend([[-ix[p,a],-ix[p,b]] for a,b in itertools.combinations(range(3),2)])
        for d in (1,2,3,4):
            tr=(p,(p+d)%q,(p+2*d)%q) if dimension==1 else (p,((p[0]+d)%q,p[1]),((p[0]+d)%q,(p[1]+d)%q))
            edges.add(tr)
    for tr in edges:
        for colors in itertools.product(range(3),repeat=3):
            if sum(colors)%3==0:clauses.append([-ix[p,c] for p,c in zip(tr,colors)])
    clauses.append([ix[cells[0],0]])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        timer=threading.Timer(2,solver.interrupt);timer.start();start=time.monotonic()
        ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
        row=dict(dimension=dimension,period=q,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
        if ok:
            model=set(solver.get_model());z={p:next(c for c in range(3) if ix[p,c] in model) for p in cells}
            assert all(sum(z[p] for p in tr)%3 for tr in edges)
            row['colors']=[z[p] for p in cells]
    results.append(row);print(json.dumps({k:v for k,v in row.items() if k!='colors'}),flush=True)
    if ok:break
(root/'periodic_zero_sum_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
