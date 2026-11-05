"""P2d discovery. Solver witness independently checked below, no UNSAT claim."""
from pathlib import Path
from threading import Timer
from pysat.solvers import Solver
from itertools import combinations
import json,time

n=464
var=lambda i,c:3*i+c+1
clauses=[]
for i in range(n):
    clauses.append([var(i,c) for c in range(3)])
    for a,b in combinations(range(3),2):clauses.append([-var(i,a),-var(i,b)])
for i in range(0,n-2,3):
    for j,k in combinations(range(i,i+3),2):
        for c in range(3):clauses.append([-var(j,c),-var(k,c)])
for d in range(1,(n-1)//5+1):
    for x in range(n-5*d):
        for c in range(3):clauses.append([-var(x+j*d,c) for j in range(6)])
for c in range(3):clauses.append([var(c,c)])
start=time.perf_counter()
with Solver(name='maplechrono',bootstrap_with=clauses) as solver:
    timer=Timer(45,solver.interrupt)
    timer.start()
    result=solver.solve_limited(expect_interrupt=True)
    timer.cancel()
    output={'label':'UNDECIDED' if result is None else 'UNVERIFIED solver outcome',
        'solver_result':result,'n':n,'clauses':len(clauses),'wall_limit_seconds':45,
        'runtime_seconds':time.perf_counter()-start}
    if result:
        model=set(solver.get_model())
        word=[next(c for c in range(3) if var(i,c) in model) for i in range(n)]
        output['word']=word
Path('research_round2/certificates/structural_sixap_word.json').write_text(json.dumps(output,indent=2)+'\n')
print({k:v for k,v in output.items() if k!='word'})
