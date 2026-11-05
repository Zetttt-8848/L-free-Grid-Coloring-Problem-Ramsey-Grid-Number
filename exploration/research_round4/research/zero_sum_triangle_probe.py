"""Bounded construction search for few zero-sum corners, allowing monochromatic ones."""
from pathlib import Path
import json, random, math, time

N=13
cells=[(v,u) for v in range(1,N) for u in range(v)]
ix={p:i for i,p in enumerate(cells)}
edges=[tuple(ix[p] for p in ((v,u),(v+d,u),(v+d,u+d)))
       for v,u in cells for d in range(1,N-v)]
incident=[[] for _ in cells]
for j,e in enumerate(edges):
    for i in e:incident[i].append(j)
rng=random.Random(130013)
seed=['0','11','101','2112','20120','020101','2211222','11022000',
      '000202111','2220010122','11002121000','101021021020']
best=[int(c) for row in seed for c in row]
bestscore=sum(sum(best[i] for i in e)%3==0 for e in edges)
start=time.monotonic();steps=0;restarts=0
while time.monotonic()-start<12 and bestscore>16:
    col=best.copy() if restarts%3 else [rng.randrange(3) for _ in cells]
    sums=[sum(col[i] for i in e)%3 for e in edges]
    score=sum(s==0 for s in sums)
    for k in range(12000):
        steps+=1
        i=rng.randrange(len(cells));delta=rng.choice((1,2))
        change=sum(((sums[e]+delta)%3==0)-(sums[e]==0) for e in incident[i])
        temp=0.18+1.7*(1-k/12000)**2
        if change<=0 or rng.random()<math.exp(-change/temp):
            col[i]=(col[i]+delta)%3
            for e in incident[i]:sums[e]=(sums[e]+delta)%3
            score+=change
            if score<bestscore:
                bestscore=score;best=col.copy()
                print(json.dumps(dict(best=bestscore,steps=steps,seconds=time.monotonic()-start)),flush=True)
                if bestscore<=16:break
    restarts+=1
rec=dict(scope='Literal discovery with monochromatic corners allowed. No proper-coloring bound.',
         side=N,steps=steps,restarts=restarts,seconds=time.monotonic()-start,
         rows=[''.join(str(best[ix[v,u]]) for u in range(v)) for v in range(1,N)],
         zero_sum_count=bestscore,zero_corners=[])
for e in edges:
    if sum(best[i] for i in e)%3==0:
        a,b,c=(cells[i] for i in e)
        rec['zero_corners'].append(dict(base=list(a),step=b[0]-a[0],
               kind='monochromatic' if len({best[i] for i in e})==1 else 'rainbow'))
Path(__file__).with_suffix('.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rec),flush=True)
