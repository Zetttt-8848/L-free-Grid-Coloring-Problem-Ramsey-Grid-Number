"""Bounded discovery of high-energy properly colored cube subsets."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from pysat.solvers import Glucose4
import json,random,time

root=Path(__file__).resolve().parent
rng=random.Random(2026091210)
start=time.monotonic(); stats=Counter(); witness=None
for dim,m in [(5,27),(5,28),(5,26),(6,45),(6,42)]:
    pool=sorted(sum(bit*3**i for i,bit in enumerate(bits))
                for bits in product([0,1],repeat=dim))
    for _ in range(300):
        if time.monotonic()-start>30: break
        A=sorted(rng.sample(pool,m)); fibers={}
        ids={(v,u):j+1 for j,(u,v) in enumerate(combinations(A,2))}
        for v,u in ids: fibers.setdefault(v-u,[]).append(u)
        T=sum(len(f)*(len(f)-1)//2 for f in fibers.values())
        stats['sampled']+=1
        if T<=2*len(ids): continue
        clauses=[]
        for d,f in fibers.items():
            for u,v in combinations(sorted(f),2):
                e=[ids[u+d,u],ids[v+d,u],ids[v+d,v]]
                clauses.extend((e,[-x for x in e]))
        with Glucose4(bootstrap_with=clauses) as solver:
            solver.conf_budget(50000)
            answer=solver.solve_limited()
            stats['calls']+=1
            if answer is True:
                positive={x for x in solver.get_model() if x>0}
                witness=dict(dimension=dim,marks=A,cells=len(ids),corners=T,
                             rows={str(v):{str(u):int(ids[v,u] in positive)
                                           for u in A if u<v} for v in A})
                break
            stats['raw_negative' if answer is False else 'undecided']+=1
    if witness or time.monotonic()-start>30: break
out=dict(seconds=time.monotonic()-start,statistics=dict(stats),witness=witness,
         scope='Finite discovery; negatives and absence of witnesses are not proofs.')
(root/'cube_energy_probe.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({**out,'witness':None if witness is None else {k:v for k,v in witness.items() if k!='rows'}}))
