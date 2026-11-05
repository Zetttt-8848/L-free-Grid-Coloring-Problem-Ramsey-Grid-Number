"""Bounded discovery of diagonal surrogates; never claims grid feasibility."""
import numpy as np
from bisect import bisect_right
from pathlib import Path
import json,time

H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,
217,247,284,334,357,373,426,481,493,554,586]
rng=np.random.default_rng(20260909)
results=[]
for n in [464,450]:
    word=rng.integers(0,3,n)
    cap=np.array([0]+[2*(bisect_right(H,n-d)-1) for d in range(1,n)])
    R=np.zeros((3,n),dtype=np.int64)
    for d in range(1,n):
        for c in range(3):
            R[c,d]=np.sum((word[:-d]==c)&(word[d:]==c))
    objective=lambda A:int(np.sum(np.maximum(A-cap,0)**2))
    value=objective(R); best=value;bestword=word.copy(); tick=time.perf_counter()
    for step in range(20000):
        p=int(rng.integers(n)); old=int(word[p]); new=(old+int(rng.integers(1,3)))%3
        deltaold=np.zeros(n,dtype=np.int64);deltanew=deltaold.copy()
        deltaold[1:p+1]+=(word[p-1::-1]==old)
        deltanew[1:p+1]+=(word[p-1::-1]==new)
        deltaold[1:n-p]+=(word[p+1:]==old)
        deltanew[1:n-p]+=(word[p+1:]==new)
        oldscore=objective(R[old])+objective(R[new])
        newscore=objective(R[old]-deltaold)+objective(R[new]+deltanew)
        diff=newscore-oldscore
        temp=max(1.0,30*(1-(step%5000)/5000))
        if diff<=0 or rng.random()<np.exp(-diff/temp):
            R[old]-=deltaold;R[new]+=deltanew;word[p]=new;value+=diff
            if value<best:best=value;bestword=word.copy()
        if best==0:break
    item={'label':'UNVERIFIED discovery; UNDECIDED unless exact witness verified',
        'n':n,'steps':step+1,'seed':20260909,'objective':best,
        'runtime_seconds':time.perf_counter()-tick,'word':bestword.tolist()}
    results.append(item)
    print(n,best,step+1,flush=True)
Path(__file__).with_name('structural_word_search.json').write_text(json.dumps(results,indent=2)+'\n')
