"""Bounded discovery: which small step sets exclude zero-sum-free triangles?"""
import itertools, json, threading, time
from pathlib import Path
from pysat.solvers import Solver

root = Path(__file__).resolve().parent
results = []
for steps, n in [((1,2,3),10), ((1,2,3),16), ((1,2,3),24),
                 ((1,2,3,4),12), ((1,2,3,4),18)]:
    cells = [(v,u) for v in range(1,n) for u in range(v)]
    ix = {(q,c): 3*j+c+1 for j,q in enumerate(cells) for c in range(3)}
    clauses = []
    corners = []
    for q in cells:
        clauses.append([ix[q,c] for c in range(3)])
        clauses.extend([[-ix[q,a],-ix[q,b]] for a,b in itertools.combinations(range(3),2)])
    for x,y in cells:
        for d in steps:
            if x+d >= n: continue
            tr = ((x,y),(x+d,y),(x+d,y+d))
            corners.append(tr)
            for colors in itertools.product(range(3),repeat=3):
                if sum(colors)%3 == 0:
                    clauses.append([-ix[q,c] for q,c in zip(tr,colors)])
    clauses.append([ix[cells[0],0]])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        timer = threading.Timer(6,solver.interrupt)
        timer.start(); start=time.monotonic()
        ok=solver.solve_limited(expect_interrupt=True)
        timer.cancel()
        row=dict(steps=steps,n=n,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
        if ok:
            model=set(solver.get_model())
            z={q:next(c for c in range(3) if ix[q,c] in model) for q in cells}
            assert all(sum(z[q] for q in tr)%3 for tr in corners)
            row['rows']=[''.join(str(z[v,u]) for u in range(v)) for v in range(1,n)]
    results.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='rows'}),flush=True)
(root/'zero_sum_scale_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
