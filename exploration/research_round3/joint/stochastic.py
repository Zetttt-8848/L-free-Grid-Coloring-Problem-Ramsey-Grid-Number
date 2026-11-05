"""Swap annealing for all cap excesses and forbidden six-APs; heuristic only."""
from pathlib import Path
import argparse,bisect,json,time
import numpy as np
from numba import njit
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

@njit
def sweep(x,counts,apcounts,caps,aps,inc,incnum,weight,temperature,steps,bestx,bestscore):
    n=len(x);accepted=0;dd=np.zeros(n,np.int64)
    for step in range(steps):
        u=np.random.randint(1,n)
        while x[u]==0:u=np.random.randint(1,n)
        v=np.random.randint(1,n)
        while x[v]==1:v=np.random.randint(1,n)
        dd[:]=0
        for k in range(n):
            if x[k] and k!=u:
                dd[abs(k-u)]-=1;dd[abs(k-v)]+=1
        dc=0
        for d in range(1,n):
            old=max(0,counts[d]-caps[d]);new=max(0,counts[d]+dd[d]-caps[d]);dc+=new*new-old*old
        da=0
        for ii in range(incnum[u]):
            p=inc[u,ii]
            if apcounts[p]==6:da-=1
            apcounts[p]-=1
        for ii in range(incnum[v]):
            p=inc[v,ii]
            if apcounts[p]==5:da+=1
            apcounts[p]+=1
        delta=dc+weight*da
        if delta<=0 or np.random.random()<np.exp(-delta/temperature):
            accepted+=1;x[u]=0;x[v]=1;counts+=dd;bestscore[1]+=delta
            if bestscore[1]<bestscore[0]:bestscore[0]=bestscore[1];bestx[:]=x
            if bestscore[0]==0:return accepted,step+1
        else:
            for ii in range(incnum[u]):apcounts[inc[u,ii]]+=1
            for ii in range(incnum[v]):apcounts[inc[v,ii]]-=1
    return accepted,steps

@njit
def seed_rng(seed):np.random.seed(seed)

def initialize(n,s,seed,aps,caps,weight,marks=None):
    rng=np.random.default_rng(seed);x=np.zeros(n,np.int64);x[0]=1
    if marks is None:x[rng.choice(np.arange(1,n),size=s-1,replace=False)]=1
    else:x[np.array(marks)-1]=1
    counts=np.zeros(n,np.int64)
    for u in range(n):
        for v in range(u+1,n):counts[v-u]+=x[u]*x[v]
    ac=x[aps].sum(axis=1);score=int(np.maximum(counts-caps,0)@np.maximum(counts-caps,0)+weight*np.count_nonzero(ac==6))
    return x,counts,ac,score

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--n',type=int,default=464);pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--seed',type=int,default=20260910);pa.add_argument('--weight',type=int,default=8);pa.add_argument('--hint');pa.add_argument('--tag',default='anneal600');args=pa.parse_args()
    n=args.n;s=(n+2)//3;caps=np.array([0]+[2*(bisect.bisect_right(H,n-d)-1) for d in range(1,n)],np.int64)
    aps=np.array([[i+j*d for j in range(6)] for d in range(1,(n-1)//5+1) for i in range(n-5*d)],np.int64)
    incidence=[[] for _ in range(n)]
    for j,ap in enumerate(aps):
        for u in ap:incidence[u].append(j)
    incnum=np.array([len(t) for t in incidence],np.int64);inc=np.zeros((n,max(incnum)),np.int64)
    for i,t in enumerate(incidence):inc[i,:len(t)]=t
    marks=json.loads(Path(args.hint).read_text())['marks'] if args.hint else None
    x,counts,ac,score=initialize(n,s,args.seed,aps,caps,args.weight,marks);bestx=x.copy();bs=np.array([score,score],np.int64);initial=score;seed_rng(args.seed)
    # Compile before starting the declared search clock; one pilot proposal is included in telemetry.
    sweep(x,counts,ac,caps,aps,inc,incnum,args.weight,1.0,1,bestx,bs)
    start=time.time();iters=1;accepted=0;prev=initial;lastlog=0;base=ROOT/f'stochastic_{n}_{args.tag}';events=[]
    print(json.dumps(dict(event='start',initial_score=initial,arguments=vars(args),aps=len(aps))),flush=True)
    while time.time()-start<args.seconds and bs[0]>0:
        elapsed=time.time()-start;phase=(elapsed%60)/60
        # Periodic reheating changes the search basin while retaining the global best.
        temp=0.25+5.75*(1-phase)**2
        acc,num=sweep(x,counts,ac,caps,aps,inc,incnum,args.weight,temp,10000,bestx,bs);accepted+=acc;iters+=num
        if bs[0]<prev or elapsed-lastlog>=10:
            event=dict(seconds=time.time()-start,iterations=iters,accepted=accepted,current_score=int(bs[1]),best_score=int(bs[0]),temperature=temp);events.append(event);print(json.dumps(event),flush=True);lastlog=elapsed
            if bs[0]<prev:
                prev=int(bs[0]);base.with_suffix('.best.json').write_text(json.dumps(dict(n=n,size=s,marks=(np.flatnonzero(bestx)+1).tolist(),score=int(bs[0]),weight=args.weight,arguments=vars(args)),indent=2)+'\n')
    out=dict(n=n,size=s,marks=(np.flatnonzero(bestx)+1).tolist(),initial_score=initial,best_score=int(bs[0]),weight=args.weight,iterations=iters,accepted=accepted,runtime_seconds=time.time()-start,arguments=vars(args),events=events,label='UNVERIFIED candidate; exact independent checker required')
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('marks','events')}),flush=True)

if __name__=='__main__':main()
