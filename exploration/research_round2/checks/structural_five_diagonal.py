from pysat.solvers import Solver
from itertools import combinations
from pathlib import Path
import json
n=5
v=lambda r,c,k:3*(n*r+c)+k+1
clauses=[]
for r in range(n):
    for c in range(n):
        clauses.append([v(r,c,k) for k in range(3)])
        for a,b in combinations(range(3),2):clauses.append([-v(r,c,a),-v(r,c,b)])
for d in range(1,n):
    for r in range(n-d):
        for c in range(n-d):
            for k in range(3):clauses.append([-v(r,c,k),-v(r+d,c,k),-v(r+d,c+d,k)])
for i in range(n):clauses.append([v(i,i,0)])
with Solver(name='maplechrono',bootstrap_with=clauses) as sol:
    result=sol.solve()
    out={'label':'UNVERIFIED discovery','SAT':result}
    if result:
        positive=set(sol.get_model())
        out['grid']=[[next(k for k in range(3) if v(r,c,k) in positive) for c in range(n)] for r in range(n)]
Path('research_round2/certificates/structural_five_diagonal.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
