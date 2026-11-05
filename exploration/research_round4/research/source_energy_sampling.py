"""Discovery by literal high-energy sources; no negative conclusion."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from pysat.solvers import Glucose4
import random
import json
import time

ROOT=Path(__file__).resolve().parent
rng=random.Random(2026091209)
start=time.monotonic()
statistics=Counter()
witness=None
for n,m in [(18,11),(22,12),(26,14),(30,15)]:
    for _ in range(250):
        if time.monotonic()-start>25: break
        A=sorted(rng.sample(range(n),m))
        A=[x-A[0] for x in A]
        fibers={}
        ids={}
        for u,v in combinations(A,2):
            ids[v,u]=len(ids)+1
            fibers.setdefault(v-u,[]).append(u)
        T=sum(len(f)*(len(f)-1)//2 for f in fibers.values())
        M=len(ids)
        statistics["sampled"]+=1
        if T<=2*M: continue
        clauses=[]
        for d,f in fibers.items():
            for u,v in combinations(f,2):
                e=[ids[u+d,u],ids[v+d,u],ids[v+d,v]]
                clauses.extend((e,[-x for x in e]))
        statistics["coloring_calls"]+=1
        with Glucose4(bootstrap_with=clauses) as solver:
            solver.conf_budget(25000)
            answer=solver.solve_limited()
            if answer is True:
                positive=set(x for x in solver.get_model() if x>0)
                witness=dict(marks=A,corners=T,pairs=M,excess=T-2*M,
                             rows={str(v):{str(u):int(ids[v,u] in positive)
                                           for u in A if u<v} for v in A})
                break
            statistics["raw_negative" if answer is False else "undecided"]+=1
    if witness is not None or time.monotonic()-start>25: break
out=dict(seconds=time.monotonic()-start,statistics=dict(statistics),witness=witness,
         scope="Bounded sampling only; absence of a witness is not a theorem.")
(ROOT/"source_energy_sampling.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({**out,"witness":None if witness is None else {k:v for k,v in witness.items() if k!="rows"}}))
