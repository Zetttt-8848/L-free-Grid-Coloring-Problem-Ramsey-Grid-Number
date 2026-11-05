"""Keep all monochromatic exclusions; shrink only the rainbow hitting set."""
import itertools,json,threading,time
from pathlib import Path
from pysat.solvers import Solver
root=Path(__file__).resolve().parent;n=10
cells=[(v,u) for v in range(n) for u in range(v)];ix={(q,c):3*i+c+1 for i,q in enumerate(cells) for c in range(3)}
clauses=[];corners=[]
for q in cells:
    clauses.append([ix[q,c] for c in range(3)])
    clauses.extend([[-ix[q,a],-ix[q,b]] for a,b in itertools.combinations(range(3),2)])
for x,y in cells:
    for d in range(1,n-x):
        tr=((x,y),(x+d,y),(x+d,y+d));corners.append(tr);sel=3*len(cells)+len(corners)
        clauses.extend([[-ix[q,c] for q in tr] for c in range(3)])
        clauses.extend([[-sel]+[-ix[q,c] for q,c in zip(tr,colors)] for colors in itertools.permutations(range(3))])
clauses.append([ix[cells[0],0]])
for j,q in enumerate(cells):clauses.append([-ix[q,2]]+[ix[p,1] for p in cells[:j]])
start=time.monotonic();history=[];tested=0
with Solver(name='g4',bootstrap_with=clauses) as solver:
    timer=threading.Timer(30,solver.interrupt);timer.start()
    active=list(range(3*len(cells)+1,3*len(cells)+len(corners)+1))
    ok=solver.solve_limited(assumptions=active,expect_interrupt=True)
    if ok is False:
        active=sorted(solver.get_core());history.append(dict(stage='initial core',rainbow_corners=len(active)))
        for sel in active.copy():
            if sel not in active:continue
            trial=[a for a in active if a!=sel];tested+=1
            value=solver.solve_limited(assumptions=trial,expect_interrupt=True)
            if value is None:break
            if value is False:active=sorted(solver.get_core())
        history.append(dict(stage='deletion end',rainbow_corners=len(active),tested=tested))
    timer.cancel()
out=dict(n=n,seconds=time.monotonic()-start,initial_status='raw negative' if ok is False else 'undecided',
         scope='candidate rainbow hitting set under all proper-coloring constraints; no analytic proof supplied',history=history)
if ok is False:
    chosen=[corners[a-3*len(cells)-1] for a in active]
    mult={h:sum(h%(tr[1][0]-tr[0][0])==0 for tr in chosen) for h in range(1,463)}
    out.update(rainbow_corners=chosen,edge_count=len(chosen),max_multiplicity_at_464=max(mult.values()))
(root/'rainbow_hitting_core.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rainbow_corners'}))
