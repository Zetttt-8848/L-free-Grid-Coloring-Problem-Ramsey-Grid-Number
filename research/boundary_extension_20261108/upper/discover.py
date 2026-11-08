"""Discover legal local/global potential reversals; SAT is used only for witnesses."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import time
from pysat.solvers import Solver
import pysat

HERE = Path(__file__).resolve().parent

def source(marks):
    cells = [(x,y) for x in marks for y in marks if y < x]
    ids = {p:i+1 for i,p in enumerate(cells)}
    triples = []
    for x,y in cells:
        for h in range(1,max(marks)-x+1):
            if (x+h,y) in ids and (x+h,y+h) in ids:
                triples.append([ids[x,y],ids[x+h,y],ids[x+h,y+h]])
    return cells,ids,triples

def phi(cells, colors, subset):
    sums = {}
    for (x,y),c in zip(cells,colors):
        if x in subset and y in subset:
            sums[x-y]=sums.get(x-y,0)+1-2*c
    return sum(s*s for s in sums.values())

def search(q,a):
    cells,ids,triples=source(a)
    internal={i for p,i in ids.items() if set(p)<=set(q)}
    for d in sorted({x-y for x,y in cells}):
        fi=[ids[x,y] for x,y in cells if x-y==d and ids[x,y] in internal]
        fe=[ids[x,y] for x,y in cells if x-y==d and ids[x,y] not in internal]
        if len(fi)<2 or len(fe)<2: continue
        for bit in fi:
            clauses=[c for t in triples for c in [t,[-v for v in t]]]
            for t in triples:
                t2=[-v if v==bit else v for v in t]
                clauses += [t2,[-v for v in t2]]
            with Solver(name='g4',bootstrap_with=clauses) as solver:
                # Enumerate only the relevant fiber; all other colors remain free.
                for k in range(1<<len(fi+fe)):
                    fc=[(k>>i)&1 for i in range(len(fi+fe))]
                    if fc[fi.index(bit)]!=0: continue
                    sq=len(fi)-2*sum(fc[:len(fi)])
                    se=len(fe)-2*sum(fc[len(fi):])
                    if sq<2 or sq+se>0: continue
                    assumptions=[v if c else -v for v,c in zip(fi+fe,fc)]
                    if solver.solve(assumptions=assumptions):
                        model=set(solver.get_model())
                        before=[int(i in model) for i in range(1,len(cells)+1)]
                        after=before.copy(); after[bit-1]^=1
                        return {'Q':q,'A':a,'cells':cells,'before':before,'after':after,
                            'flipped_cell':cells[bit-1],'difference':d,
                            'phi_Q':[phi(cells,c,q) for c in [before,after]],
                            'phi_A':[phi(cells,c,a) for c in [before,after]],
                            'fiber_sums_before':{'internal':sq,'exterior':se}}
    return None

def main():
    start=time.monotonic()
    trials=[]; witnesses=[]
    cases=[([0,1,3,4],[0,1,2,3,4]),
           ([0,1,5,6,25,26,30,31],[0,1,2,3,5,6,25,26,30,31])]
    for q,a in cases:
        w=search(q,a)
        trials.append({'Q':q,'A':a,'found':w is not None})
        if w: witnesses.append(w)
    result={'status':'WITNESSES_FOUND' if witnesses else 'NO_WITNESS_IN_TESTED_CASES',
        'trials':trials,'witnesses':witnesses,
        'provenance':{'python':platform.python_version(),'python_sat':pysat.__version__,
            'solver':'Glucose4 via PySAT','elapsed_seconds':time.monotonic()-start,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        'scope':'Existential SAT witnesses only. No SAT UNSAT claim is certified.'}
    (HERE/'witnesses.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='witnesses'},indent=2))

if __name__=='__main__': main()
