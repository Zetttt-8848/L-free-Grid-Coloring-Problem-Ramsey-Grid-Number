"""Find literal one-rainbow triangles at symmetry representatives, for discovery."""
import itertools, json, threading, time
from pathlib import Path
from pysat.solvers import Solver

root=Path(__file__).resolve().parent
n=10; cells=[(v,u) for v in range(1,n) for u in range(v)]
ix={(q,c):3*i+c+1 for i,q in enumerate(cells) for c in range(3)}
clauses=[]; corners=[]
for q in cells:
    clauses.append([ix[q,c] for c in range(3)])
    clauses.extend([[-ix[q,a],-ix[q,b]] for a,b in itertools.combinations(range(3),2)])
for x,y in cells:
    for d in range(1,n-x):
        tr=((x,y),(x+d,y),(x+d,y+d));corners.append((tr,d))
        clauses.extend([[-ix[q,c] for q in tr] for c in range(3)])
selectors=[]
for j,(tr,d) in enumerate(corners):
    s=3*len(cells)+j+1;selectors.append(s)
    clauses.extend([[-s]+[-ix[q,c] for q,c in zip(tr,colors)] for colors in itertools.permutations(range(3))])
clauses.append([ix[cells[0],0]])
results=[]
with Solver(name='g3',bootstrap_with=clauses) as solver:
    for a in range(7):
        for b in range(a,7):
            c=6-a-b
            if c<b:continue
            # Base (a,b,c) and step 2 on the gap-coordinate simplex of degree 8.
            def rc(g): return (g[0]+g[1]+1,g[0])
            wanted=frozenset(rc(g) for g in ((a+2,b,c),(a,b+2,c),(a,b,c+2)))
            j=next(j for j,(tr,d) in enumerate(corners) if frozenset(tr)==wanted)
            assumptions=[s if i!=j else -s for i,s in enumerate(selectors)]
            timer=threading.Timer(4,solver.interrupt)
            timer.start();start=time.monotonic()
            ok=solver.solve_limited(assumptions=assumptions,expect_interrupt=True)
            timer.cancel();solver.clear_interrupt()
            row=dict(base=[a,b,c],step=2,orbit_size=len(set(itertools.permutations((a,b,c)))),status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
            if ok:
                model=set(solver.get_model());z={q:next(c for c in range(3) if ix[q,c] in model) for q in cells}
                rainbows=[tr for tr,d in corners if len({z[q] for q in tr})==3]
                assert all(len({z[q] for q in tr})>1 for tr,d in corners)
                assert len(rainbows)==1 and frozenset(rainbows[0])==wanted
                row['rows']=[''.join(str(z[v,u]) for u in range(v)) for v in range(1,n)]
                row['rainbow']=rainbows[0]
            results.append(row)
            print(json.dumps({k:v for k,v in row.items() if k not in ('rows','rainbow')}),flush=True)
(root/'one_rainbow_orbit_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
