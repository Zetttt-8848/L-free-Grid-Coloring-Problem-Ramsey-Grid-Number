"""Discover a monochromatic-set implication via its forced outside vertices."""
from pathlib import Path
from itertools import combinations
from collections import deque
import json,time,random

N=9
cells=[(v,u) for v in range(1,N) for u in range(v)]
ix={p:i for i,p in enumerate(cells)}
edges=[tuple(ix[p] for p in ((v,u),(v+d,u),(v+d,u+d)))
       for v,u in cells for d in range(1,N-v)]
pair={}
for h in edges:
    for j in range(3):pair[tuple(sorted(h[:j]+h[j+1:]))]=h[j]
start=time.monotonic();count=0;found=None
rng=random.Random(13005)
for k in (4,5,6):
    # Exhaust the smaller search; bounded random sampling for the larger ones.
    samples=combinations(range(len(cells)),k) if k==4 else (
        tuple(sorted(rng.sample(range(len(cells)),k))) for _ in range(250000))
    for Ct in samples:
        count+=1;C=set(Ct);F={};bad=False
        for pp in combinations(Ct,2):
            if pp in pair:
                z=pair[pp]
                if z in C:bad=True;break
                F.setdefault(z,pp)
        if bad or len(F)<5:continue
        adj={u:[] for u in F};labels={}
        for a,b in combinations(F,2):
            pp=tuple(sorted((a,b)));label=pair.get(pp)
            if label in C:
                adj[a].append(b);adj[b].append(a);labels[pp]=label
        he=[h for h in edges if all(u in F for u in h)]
        for root in F:
            paths={root:()};queue=deque([root])
            while queue:
                a=queue.popleft()
                for b in adj[a]:
                    if b not in paths:
                        paths[b]=paths[a]+(tuple(sorted((a,b))),);queue.append(b)
            for h in he:
                if all(u in paths for u in h):
                    js=set().union(*(paths[u] for u in h))
                    if len(js)<=4:
                        verts=set().union(*map(set,js))
                        found=dict(side=N,C=[cells[u] for u in Ct],
                          forced=[dict(cell=cells[u],pair=[cells[z] for z in F[u]]) for u in sorted(verts)],
                          terminal_corner=[cells[u] for u in h],
                          tree=[dict(pair=[cells[u] for u in pp],label=cells[labels[pp]]) for pp in sorted(js)])
                        break
            if found:break
        if found or time.monotonic()-start>15:break
    if found or time.monotonic()-start>15:break
out=dict(scope='Bounded motif discovery; a missing witness is not a theorem.',
         examined=count,seconds=time.monotonic()-start,witness=found)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2),flush=True)
