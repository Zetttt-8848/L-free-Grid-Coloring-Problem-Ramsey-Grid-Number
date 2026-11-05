"""Exact-cardinality local search with certified forbidden affine patterns."""
from pathlib import Path
import argparse,bisect,json,time
import numpy as np
from numba import njit
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

@njit
def seed_rng(seed):np.random.seed(seed)

@njit
def sweep(x,counts,edgecounts,thresholds,caps,inc,incnum,weight,temp,steps,best,score):
    n=len(x);accepted=0;dd=np.zeros(n,np.int64)
    for step in range(steps):
        u=np.random.randint(1,n)
        while x[u]==0:u=np.random.randint(1,n)
        v=np.random.randint(1,n)
        while x[v]==1:v=np.random.randint(1,n)
        dd[:]=0
        for k in range(n):
            if x[k] and k!=u:dd[abs(k-u)]-=1;dd[abs(k-v)]+=1
        dc=0
        for d in range(1,n):
            old=max(0,counts[d]-caps[d]);new=max(0,counts[d]+dd[d]-caps[d]);dc+=new*new-old*old
        de=0
        for ii in range(incnum[u]):
            p=inc[u,ii]
            if edgecounts[p]==thresholds[p]:de-=1
            edgecounts[p]-=1
        for ii in range(incnum[v]):
            p=inc[v,ii]
            if edgecounts[p]==thresholds[p]-1:de+=1
            edgecounts[p]+=1
        delta=dc+weight*de
        if delta<=0 or np.random.random()<np.exp(-delta/temp):
            accepted+=1;x[u]=0;x[v]=1;counts+=dd;score[1]+=delta
            if score[1]<score[0]:score[0]=score[1];best[:]=x
            if score[0]==0:return accepted,step+1
        else:
            for ii in range(incnum[u]):edgecounts[inc[u,ii]]+=1
            for ii in range(incnum[v]):edgecounts[inc[v,ii]]-=1
    return accepted,steps

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--n',type=int,default=464);pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--seed',type=int,default=20260912);pa.add_argument('--weight',type=int,default=8);pa.add_argument('--patterns',default=str(ROOT/'patterns_v1.json'));pa.add_argument('--tag',default='pattern_v1_600');pa.add_argument('--hint');args=pa.parse_args();n=args.n;s=(n+2)//3
    patterns=json.loads(Path(args.patterns).read_text())['patterns'];edges=[];numbers=[]
    for pattern in patterns:
        before=len(edges)
        for d in range(1,(n-1)//max(pattern)+1):
            for start in range(n-max(pattern)*d):edges.append([start+o*d for o in pattern])
        numbers.append(len(edges)-before)
    caps=np.array([0]+[2*(bisect.bisect_right(H,n-d)-1) for d in range(1,n)],np.int64);thresholds=np.array([len(e) for e in edges],np.int64)
    incidence=[[] for _ in range(n)]
    for j,e in enumerate(edges):
        for u in e:incidence[u].append(j)
    incnum=np.array([len(t) for t in incidence],np.int64);inc=np.zeros((n,max(incnum)),np.int64)
    for i,t in enumerate(incidence):inc[i,:len(t)]=t
    rng=np.random.default_rng(args.seed);x=np.zeros(n,np.int64);x[0]=1
    if args.hint:x[np.array(json.loads(Path(args.hint).read_text())['marks'])-1]=1
    else:x[rng.choice(np.arange(1,n),size=s-1,replace=False)]=1
    counts=np.zeros(n,np.int64)
    for u in range(n):
        for v in range(u+1,n):counts[v-u]+=x[u]*x[v]
    ec=np.array([sum(x[i] for i in e) for e in edges],np.int64);excess=np.maximum(counts-caps,0);initial=int(np.sum(excess*excess)+args.weight*np.count_nonzero(ec==thresholds));score=np.array([initial,initial],np.int64);best=x.copy();seed_rng(args.seed)
    sweep(x,counts,ec,thresholds,caps,inc,incnum,args.weight,1.,1,best,score);start=time.time();iters=1;accepted=0;prev=initial;lastlog=0;events=[];base=ROOT/args.tag
    setup=dict(n=n,size=s,patterns=patterns,pattern_copy_counts=numbers,total_hyperedges=len(edges),arguments=vars(args),initial_score=initial);base.with_suffix('.setup.json').write_text(json.dumps(setup,indent=2)+'\n');print(json.dumps(dict(event='start',**setup)),flush=True)
    while time.time()-start<args.seconds and score[0]>0:
        elapsed=time.time()-start;phase=(elapsed%60)/60;temp=.25+5.75*(1-phase)**2
        acc,num=sweep(x,counts,ec,thresholds,caps,inc,incnum,args.weight,temp,10000,best,score);accepted+=acc;iters+=num
        if score[0]<prev or elapsed-lastlog>=10:
            event=dict(seconds=time.time()-start,iterations=iters,accepted=accepted,current_score=int(score[1]),best_score=int(score[0]),temperature=temp);events.append(event);print(json.dumps(event),flush=True);lastlog=elapsed
            if score[0]<prev:
                prev=int(score[0]);base.with_suffix('.best.json').write_text(json.dumps(dict(n=n,size=s,marks=(np.flatnonzero(best)+1).tolist(),score=int(score[0]),weight=args.weight,patterns=patterns,arguments=vars(args)),indent=2)+'\n')
    out=dict(n=n,size=s,marks=(np.flatnonzero(best)+1).tolist(),initial_score=initial,best_score=int(score[0]),weight=args.weight,patterns=patterns,iterations=iters,accepted=accepted,runtime_seconds=time.time()-start,arguments=vars(args),events=events,label='UNVERIFIED until independent checker passes')
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('marks','events','patterns')}),flush=True)

if __name__=='__main__':main()
