"""Bounded witness search for the refined T13 rainbow threshold.

A SAT witness would refute F13. A negative answer is not used as a proof.
"""
from pathlib import Path
from threading import Timer
from itertools import permutations
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
import json,time

N=13
cells=[(v,u) for v in range(1,N) for u in range(v)]
vid={cell:i for i,cell in enumerate(cells)}
def var(cell,color): return 3*vid[cell]+color+1
clauses=[]
for cell in cells:
    triple=[var(cell,c) for c in range(3)]
    clauses.append(triple)
    clauses.extend([[-triple[i],-triple[j]] for i in range(3) for j in range(i)])
clauses.append([var(cells[0],0)])
for i,cell in enumerate(cells):
    clauses.append([-var(cell,2)]+[var(cells[j],1) for j in range(i)])
corners=[]
for x,y in cells:
    for d in range(1,N-x):
        corners.append(((x,y),(x+d,y),(x+d,y+d)))
top=3*len(cells)
rainbow_vars=[]
for i,edge in enumerate(corners):
    rb=top+i+1
    rainbow_vars.append(rb)
    for c in range(3): clauses.append([-var(cell,c) for cell in edge])
    for colors in permutations(range(3)):
        clauses.append([-var(cell,c) for cell,c in zip(edge,colors)]+[rb])
bound=CardEnc.atmost(rainbow_vars,16,top_id=top+len(corners),encoding=EncType.seqcounter)
clauses.extend(bound.clauses)
seed=['0','11','101','2112','20120','020101','2211222','11022000',
      '000202111','2220010122','11002121000','101021021020']
phases=[var((v,u),c)*(1 if int(seed[v-1][u])==c else -1)
        for v,u in cells for c in range(3)]
records=[]
for name in ('g4','mcb'):
    start=time.monotonic()
    with Solver(name=name,bootstrap_with=clauses) as solver:
        solver.set_phases(phases)
        timer=Timer(20,solver.interrupt)
        timer.start()
        try: answer=solver.solve_limited(expect_interrupt=True)
        finally: timer.cancel()
        rec=dict(solver=name,answer=answer,seconds=time.monotonic()-start)
        if answer is True:
            pos={x for x in solver.get_model() if x>0}
            colors={cell:next(c for c in range(3) if var(cell,c) in pos) for cell in cells}
            rec['rows']=[''.join(str(colors[v,u]) for u in range(v)) for v in range(1,N)]
            rec['rainbows']=[[e[0][0],e[0][1],e[1][0]-e[0][0]]
                             for e in corners if len({colors[t] for t in e})==3]
    records.append(rec)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Bounded construction search; negative output is not a theorem.',
        side=N,target=16,cases=records),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in rec.items() if k!='rainbows'}),flush=True)
    if answer is True: break
