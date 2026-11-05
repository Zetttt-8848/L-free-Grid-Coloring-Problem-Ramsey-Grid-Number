"""Seek explicit low-rainbow proper colorings of the strict ten-mark triangle."""
import itertools,json,threading,time
from pathlib import Path
from pysat.card import CardEnc
from pysat.solvers import Solver
root=Path(__file__).resolve().parent;n=10
cells=[(v,u) for v in range(n) for u in range(v)];ix={(q,c):3*i+c+1 for i,q in enumerate(cells) for c in range(3)}
base=[];corners=[];flags=[]
for q in cells:
    base.append([ix[q,c] for c in range(3)])
    base.extend([[-ix[q,a],-ix[q,b]] for a,b in itertools.combinations(range(3),2)])
for x,y in cells:
    for d in range(1,n-x):
        tr=((x,y),(x+d,y),(x+d,y+d));corners.append(tr);flag=3*len(cells)+len(corners);flags.append(flag)
        base.extend([[-ix[q,c] for q in tr] for c in range(3)])
        base.extend([[flag]+[-ix[q,c] for q,c in zip(tr,colors)] for colors in itertools.permutations(range(3))])
base.append([ix[cells[0],0]])
for j,q in enumerate(cells):base.append([-ix[q,2]]+[ix[p,1] for p in cells[:j]])
results=[]
for budget in (6,2,1):
    card=CardEnc.atmost(flags,bound=budget,top_id=flags[-1])
    with Solver(name='g3',bootstrap_with=base+card.clauses) as solver:
        timer=threading.Timer(10,solver.interrupt);timer.start();start=time.monotonic()
        ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
        row=dict(n=n,budget=budget,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
        if ok:
            vals=set(x for x in solver.get_model() if x>0);z={q:next(c for c in range(3) if ix[q,c] in vals) for q in cells}
            assert all(len({z[q] for q in tr})>1 for tr in corners)
            rainbow=[tr for tr in corners if len({z[q] for q in tr})==3];assert len(rainbow)<=budget
            row.update(colors=[[v,u,c] for (v,u),c in z.items()],rainbows=rainbow)
    results.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ('colors','rainbows')}),flush=True)
    if ok is False:break
(root/'rainbow_budget_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
