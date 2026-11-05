"""Seek a positive word meeting aggregate caps; a nonzero score proves nothing."""
import bisect,json,math,time
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parent
source=json.loads((root.parent.parent/'research_round3/joint/partition600.best.json').read_text(encoding='utf-8'))
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
word=np.array(source['word'],dtype=np.int16);n=len(word);rng=np.random.default_rng(2026091104)
cap=np.array([0]+[min(n-d,6*(bisect.bisect_right(H,n-d)-1)) for d in range(1,n)],dtype=np.int16)
counts=np.array([0]+[np.count_nonzero(word[:-d]==word[d:]) for d in range(1,n)],dtype=np.int16)
penalty=lambda v:np.maximum(v-cap,0).astype(np.int64)
cost=int(penalty(counts)@penalty(counts));best=cost;best_word=word.copy();history=[dict(iteration=0,cost=cost)]
start=time.monotonic();attempts=0
while best and time.monotonic()-start<50:
    attempts+=1;p=int(rng.integers(n));old=int(word[p]);new=(old+int(rng.integers(1,3)))%3
    change=np.zeros(n,dtype=np.int16)
    left=word[:p][::-1];right=word[p+1:]
    change[1:p+1]+=(left==new).astype(np.int16)-(left==old).astype(np.int16)
    change[1:n-p]+=(right==new).astype(np.int16)-(right==old).astype(np.int16)
    trial=counts+change;z=penalty(trial);newcost=int(z@z)
    phase=(attempts%60000)/60000
    temp=0.2+5*(1-phase)**2
    if newcost<=cost or rng.random()<math.exp((cost-newcost)/temp):
        word[p]=new;counts=trial;cost=newcost
    if cost<best:
        best=cost;best_word=word.copy();history.append(dict(iteration=attempts,cost=best))
        if best==0:break
    if attempts%60000==0:
        word=best_word.copy();counts=np.array([0]+[np.count_nonzero(word[:-d]==word[d:]) for d in range(1,n)],dtype=np.int16);cost=best
literal=best_word.tolist()
profile=[sum(literal[i]==literal[i+d] for i in range(n-d)) for d in range(1,n)]
violations=[dict(d=d,count=profile[d-1],cap=int(cap[d])) for d in range(1,n) if profile[d-1]>cap[d]]
out=dict(purpose='bounded construction discriminator for aggregate diagonal caps only',n=n,seed=2026091104,
         status='literal aggregate-cap word' if not violations else 'undecided',seconds=time.monotonic()-start,
         attempts=attempts,best_cost=best,history=history,word=literal,profile=profile,violations=violations)
(root/'aggregate_word_probe.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('word','profile','history')}))
