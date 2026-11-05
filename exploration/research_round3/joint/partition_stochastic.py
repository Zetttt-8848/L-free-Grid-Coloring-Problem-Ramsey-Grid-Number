"""Balanced ternary partition witness search, every cap and every six-AP."""
from pathlib import Path
import argparse,bisect,json,time
import numpy as np
from numba import njit
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

@njit
def seed_rng(seed):np.random.seed(seed)

@njit
def sweep(word,counts,apcounts,caps,inc,incnum,weight,temp,steps,best,score):
    n=len(word);dd=np.zeros((3,n),np.int64);accepted=0
    for step in range(steps):
        u=np.random.randint(n);v=np.random.randint(n)
        while word[u]==word[v]:v=np.random.randint(n)
        cu=word[u];cv=word[v];dd[:]=0
        for k in range(n):
            if k==u or k==v:continue
            ck=word[k]
            if ck==cu:dd[cu,abs(k-u)]-=1;dd[cu,abs(k-v)]+=1
            if ck==cv:dd[cv,abs(k-v)]-=1;dd[cv,abs(k-u)]+=1
        dc=0
        for c in range(3):
            for d in range(1,n):
                old=max(0,counts[c,d]-caps[d]);new=max(0,counts[c,d]+dd[c,d]-caps[d]);dc+=new*new-old*old
        da=0
        for ii in range(incnum[u]):
            p=inc[u,ii]
            if apcounts[p,cu]==6:da-=1
            if apcounts[p,cv]==5:da+=1
            apcounts[p,cu]-=1;apcounts[p,cv]+=1
        for ii in range(incnum[v]):
            p=inc[v,ii]
            if apcounts[p,cv]==6:da-=1
            if apcounts[p,cu]==5:da+=1
            apcounts[p,cv]-=1;apcounts[p,cu]+=1
        delta=dc+weight*da
        if delta<=0 or np.random.random()<np.exp(-delta/temp):
            word[u]=cv;word[v]=cu;counts+=dd;score[1]+=delta;accepted+=1
            if score[1]<score[0]:score[0]=score[1];best[:]=word
            if score[0]==0:return accepted,step+1
        else:
            for ii in range(incnum[u]):apcounts[inc[u,ii],cu]+=1;apcounts[inc[u,ii],cv]-=1
            for ii in range(incnum[v]):apcounts[inc[v,ii],cv]+=1;apcounts[inc[v,ii],cu]-=1
    return accepted,steps

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--n',type=int,default=464);pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--seed',type=int,default=20260911);pa.add_argument('--weight',type=int,default=8);pa.add_argument('--tag',default='partition600');args=pa.parse_args();n=args.n
    caps=np.array([0]+[2*(bisect.bisect_right(H,n-d)-1) for d in range(1,n)],np.int64)
    aps=np.array([[i+j*d for j in range(6)] for d in range(1,(n-1)//5+1) for i in range(n-5*d)],np.int64)
    incidence=[[] for _ in range(n)]
    for j,ap in enumerate(aps):
        for u in ap:incidence[u].append(j)
    incnum=np.array([len(t) for t in incidence],np.int64);inc=np.zeros((n,max(incnum)),np.int64)
    for i,t in enumerate(incidence):inc[i,:len(t)]=t
    rng=np.random.default_rng(args.seed);word=np.arange(n,dtype=np.int64)%3;rng.shuffle(word);counts=np.zeros((3,n),np.int64)
    for u in range(n):
        for v in range(u+1,n):
            if word[u]==word[v]:counts[word[u],v-u]+=1
    ac=np.zeros((len(aps),3),np.int64)
    for c in range(3):ac[:,c]=(word[aps]==c).sum(axis=1)
    excess=np.maximum(counts-caps,0);initial=int(np.sum(excess*excess)+args.weight*np.count_nonzero(ac==6));score=np.array([initial,initial],np.int64);best=word.copy();seed_rng(args.seed)
    sweep(word,counts,ac,caps,inc,incnum,args.weight,1.,1,best,score);start=time.time();iters=1;accepted=0;prev=initial;lastlog=0;events=[];base=ROOT/args.tag
    print(json.dumps(dict(event='start',arguments=vars(args),initial_score=initial)),flush=True)
    while time.time()-start<args.seconds and score[0]>0:
        elapsed=time.time()-start;phase=(elapsed%120)/120;temp=.25+11.75*(1-phase)**2
        acc,num=sweep(word,counts,ac,caps,inc,incnum,args.weight,temp,10000,best,score);accepted+=acc;iters+=num
        if score[0]<prev or elapsed-lastlog>=10:
            event=dict(seconds=time.time()-start,iterations=iters,accepted=accepted,current_score=int(score[1]),best_score=int(score[0]),temperature=temp);events.append(event);print(json.dumps(event),flush=True);lastlog=elapsed
            if score[0]<prev:
                prev=int(score[0]);base.with_suffix('.best.json').write_text(json.dumps(dict(n=n,word=best.tolist(),score=int(score[0]),weight=args.weight,arguments=vars(args)),indent=2)+'\n')
    out=dict(n=n,word=best.tolist(),initial_score=initial,best_score=int(score[0]),weight=args.weight,iterations=iters,accepted=accepted,runtime_seconds=time.time()-start,arguments=vars(args),events=events,label='HEURISTIC until independent checker passes')
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('word','events')}),flush=True)

if __name__=='__main__':main()
