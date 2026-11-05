"""Discover small proof structures; raw SAT answers are not theorem evidence."""
from itertools import product, combinations
from pathlib import Path
from pysat.solvers import Solver
import json, random

def instance(B):
    H=2*max(B)+1
    pts=sorted(product(B,range(2),range(2),range(2)),key=lambda p:p[0]+H*(p[1]+3*p[2]+9*p[3]))
    val={p:p[0]+H*(p[1]+3*p[2]+9*p[3]) for p in pts}
    cells=[(y,x) for y in pts for x in pts if val[x]<val[y]]
    ids={c:i+1 for i,c in enumerate(cells)}
    fibers={}
    for y,x in cells:fibers.setdefault(val[y]-val[x],[]).append((y,x))
    edges=[]
    for pairs in fibers.values():
        for (y,x),(v,u) in combinations(sorted(pairs,key=lambda p:val[p[1]]),2):
            edges.append((ids[y,x],ids[v,x],ids[v,u]))
    return cells,edges,val

cells,edges,val=instance([0,1])
clauses=[list(e) for e in edges]+[[-v for v in e] for e in edges]
ids={c:i+1 for i,c in enumerate(cells)}
relations=[]
with Solver(name='g4',bootstrap_with=clauses) as s:
    for y,x in cells:
        if y[0]!=0 or x[0]!=0:continue
        yy=(1,)+y[1:];xx=(1,)+x[1:]
        a,b=ids[y,x],ids[yy,xx]
        equal=s.solve(assumptions=[a,b])
        different=s.solve(assumptions=[a,-b])
        if not equal or not different:
            relations.append(dict(cell=(y,x),opposite=not equal,equal=not different))
print('forced slice relations',json.dumps(relations),flush=True)

cells,edges,val=instance([0,1,3]);n=len(cells)
clauses=[]
for i,e in enumerate(edges):
    a=n+i+1
    clauses.extend([list(e)+[-a],[-v for v in e]+[-a]])
with Solver(name='g4',bootstrap_with=clauses) as s:
    allids=list(range(len(edges)))
    assert not s.solve(assumptions=[n+i+1 for i in allids])
    active=[a-n-1 for a in s.get_core()]
    random.Random(419).shuffle(active)
    for i in active.copy():
        trial=[j for j in active if j!=i]
        if not s.solve(assumptions=[n+j+1 for j in trial]):
            core={a-n-1 for a in s.get_core()}
            active=[j for j in trial if j in core]
    used=sorted({v for i in active for v in edges[i]})
    renum={v:i+1 for i,v in enumerate(used)}
    result=dict(scope='Discovery only; no obstruction theorem from raw unsatisfiability.',forced_relations=relations,
        vertices=[dict(id=renum[v],cell=cells[v-1],scalar=[val[p] for p in cells[v-1]]) for v in used],
        edges=[[renum[v] for v in edges[i]] for i in active])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('core',len(used),'vertices',len(active),'corners',flush=True)
    print(json.dumps(result),flush=True)
