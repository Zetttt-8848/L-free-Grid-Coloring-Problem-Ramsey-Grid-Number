"""Discover forcing-subgraph packings for saved color classes, not all T13."""
from pathlib import Path
from collections import deque
from fractions import Fraction
import itertools, random, json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

N=13
cells=[(v,u) for v in range(1,N) for u in range(v)]
ix={p:i for i,p in enumerate(cells)}
edges=[tuple(ix[p] for p in ((v,u),(v+d,u),(v+d,u+d)))
       for v,u in cells for d in range(1,N-v)]
rows=['0','11','101','2112','20120','020101','2211222','11022000',
      '000202111','2220010122','11002121000','101021021020']
colors=[int(rows[v-1][u]) for v,u in cells]
records=[]
rng=random.Random(11213)
for c in range(3):
    U=[i for i in range(len(cells)) if colors[i]!=c]
    he=[e for e in edges if all(i in U for i in e)]
    gedges=sorted({tuple(sorted(i for i in e if i in U)) for e in edges
                  if sum(i in U for i in e)==2})
    ei={e:i for i,e in enumerate(gedges)}
    adj={u:[] for u in U}
    for (u,v),k in ei.items():
        adj[u].append((v,k)); adj[v].append((u,k))
    candidates={}
    for rep in range(8):
        for u in U: rng.shuffle(adj[u])
        for root in U:
            paths={root:frozenset()}
            queue=deque([root])
            while queue:
                u=queue.popleft()
                for v,k in adj[u]:
                    if v not in paths:
                        paths[v]=paths[u]|{k}; queue.append(v)
            for h in he:
                if all(u in paths for u in h):
                    keys=frozenset().union(*(paths[u] for u in h))
                    # Remove nonterminal leaves; connectivity of the terminals stays.
                    changed=True
                    while changed:
                        changed=False
                        degree={}
                        for k in keys:
                            for u in gedges[k]: degree[u]=degree.get(u,0)+1
                        drop={k for k in keys if any(degree[u]==1 and u not in h
                                                     for u in gedges[k])}
                        if drop: keys=keys-drop; changed=True
                    if keys and len(keys)<=8: candidates.setdefault(tuple(sorted(keys)),h)
    cols=list(candidates)
    rr=[]; cc=[]
    for j,ks in enumerate(cols):
        rr.extend(ks); cc.extend([j]*len(ks))
    mat=coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(gedges),len(cols))).tocsr()
    result=linprog(-np.ones(len(cols)),A_ub=mat,b_ub=np.ones(len(gedges)),
                   bounds=(0,None),method='highs',options={'time_limit':20})
    rec=dict(fixed_color=c,candidates=len(cols),status=int(result.status))
    if result.x is not None:
        active=[(j,Fraction(float(x)).limit_denominator(100000))
                for j,x in enumerate(result.x) if x>1e-9]
        loads=[sum(w for j,w in active if k in cols[j]) for k in range(len(gedges))]
        scale=max([Fraction(1)]+loads)
        active=[(j,w/scale) for j,w in active]
        mass=sum(w for _,w in active)
        rec.update(raw_mass=float(-result.fun),rational_mass=str(mass),
                   graph_edges=[list(e) for e in gedges],
                   packing=[dict(weight=str(w),edges=list(cols[j]),
                                 hyperedge=list(candidates[cols[j]])) for j,w in active])
    records.append(rec)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Fixed saved classes only; no universal F13 conclusion.',
        cells=[list(p) for p in cells],seed=rows,cases=records),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('graph_edges','packing')}),flush=True)
