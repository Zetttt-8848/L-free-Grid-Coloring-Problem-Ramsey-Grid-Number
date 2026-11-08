"""Bounded discovery of complete-source parity frustration; no UNSAT claims."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json,time
from pysat.solvers import Solver
from pysat.card import CardEnc

def clauses(a):
    cells=[(v,u) for v in a for u in a if u<v]
    ids={p:i+1 for i,p in enumerate(cells)}; fs=defaultdict(list); out=[]
    for (v,u),i in ids.items(): fs[v-u].append(i)
    for x,y in cells:
        for u,v in cells:
            if v==y and u>x and (u,y+u-x) in ids:
                t=[ids[x,y],ids[u,y],ids[u,y+u-x]]
                out.extend([t,[-z for z in t]])
    return cells,fs,out

def main():
    start=time.monotonic(); checked=0; examples=[]
    for span in range(5,13):
        for count in range(5,min(10,span+2)):
            for mid in combinations(range(1,span),count-2):
                a=[0,*mid,span];cells,fs,cnf=clauses(a);checked+=1
                with Solver(name='g4',bootstrap_with=cnf) as s:
                    if not s.solve():continue
                    model=s.get_model()[:len(cells)]
                top=len(cells);bc=[]
                for f in fs.values():
                    enc=CardEnc.atmost(f,bound=(len(f)+1)//2,top_id=top);top=max(top,enc.nv);bc+=enc.clauses
                    enc=CardEnc.atleast(f,bound=len(f)//2,top_id=top);top=max(top,enc.nv);bc+=enc.clauses
                with Solver(name='g4',bootstrap_with=cnf+bc) as s:
                    if not s.solve():
                        examples.append({'A':a,'cells':cells,'proper_model':model});break
                if time.monotonic()-start>50:break
            if examples or time.monotonic()-start>50:break
        if examples or time.monotonic()-start>50:break
    result={'checked':checked,'elapsed':time.monotonic()-start,'examples':examples,
            'scope':'raw SAT discovery only; negative balance statuses not certified'}
    Path(__file__).with_name('balance_scan.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
