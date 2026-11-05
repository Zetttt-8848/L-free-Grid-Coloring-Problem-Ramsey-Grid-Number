"""Joint set search with compact two-parameter block relations and reflection."""
from pathlib import Path
import argparse,bisect,json,time
import numpy as np
from numba import njit
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

@njit
def prefix(tree,k):
    k=min(max(k,0),len(tree)-1);total=0
    while k:total+=tree[k];k-=k&-k
    return total

@njit
def relation_change(trees,code,start,change,n):
    kind=code//1000-1;h=code%1000
    if kind==0:related=prefix(trees[1,h],n)-prefix(trees[1,h],start+6*h+1)+prefix(trees[2,h],start-5*h)
    elif kind==1:related=prefix(trees[0,h],start-6*h)
    else:related=prefix(trees[0,h],n)-prefix(trees[0,h],start+5*h+1)
    i=start+1
    while i<=n:trees[kind,h,i]+=change;i+=i&-i
    return change*related

@njit
def seed_rng(seed):np.random.seed(seed)

@njit
def sweep(x,counts,ec,thresholds,groups,starts,trees,gcount,caps,inc,incnum,weight,temp,steps,best,score):
    n=len(x);accepted=0;dd=np.zeros(n,np.int64);gd=np.zeros(len(gcount),np.int64)
    for step in range(steps):
        u=np.random.randint(1,n)
        while x[u]==0:u=np.random.randint(1,n)
        v=np.random.randint(1,n)
        while x[v]==1:v=np.random.randint(1,n)
        dd[:]=0;gd[:]=0
        for k in range(n):
            if x[k] and k!=u:dd[abs(k-u)]-=1;dd[abs(k-v)]+=1
        dc=0
        for d in range(1,n):
            old=max(0,counts[d]-caps[d]);new=max(0,counts[d]+dd[d]-caps[d]);dc+=new*new-old*old
        threshold=-temp*np.log(np.random.random())
        if dc-(score[1]-score[2])>threshold:continue
        score[3]+=1;de=0;dp=0
        for ii in range(incnum[u]):
            p=inc[u,ii];g=groups[p]
            if ec[p]==thresholds[p]:
                if g>=1000:dp+=relation_change(trees,g,starts[p],-1,n)
                elif g>=0:gd[g]-=1
                else:de-=1
            ec[p]-=1
        for ii in range(incnum[v]):
            p=inc[v,ii];g=groups[p]
            if ec[p]==thresholds[p]-1:
                if g>=1000:dp+=relation_change(trees,g,starts[p],1,n)
                elif g>=0:gd[g]+=1
                else:de+=1
            ec[p]+=1
        dg=0
        for g in range(1,len(gcount)):
            old=max(0,gcount[g]-1);new=max(0,gcount[g]+gd[g]-1);dg+=new*new-old*old
        delta=dc+weight*(de+dg+dp)
        if delta<=threshold:
            accepted+=1;x[u]=0;x[v]=1;counts+=dd;gcount+=gd;score[1]+=delta;score[2]+=dc
            if score[1]<score[0]:score[0]=score[1];best[:]=x
            if score[0]==0:return accepted,step+1
        else:
            for ii in range(incnum[v]-1,-1,-1):
                p=inc[v,ii];g=groups[p]
                if g>=1000 and ec[p]==thresholds[p]:relation_change(trees,g,starts[p],-1,n)
                ec[p]-=1
            for ii in range(incnum[u]-1,-1,-1):
                p=inc[u,ii];g=groups[p]
                if g>=1000 and ec[p]==thresholds[p]-1:relation_change(trees,g,starts[p],1,n)
                ec[p]+=1
    return accepted,steps

def tree_selfcheck():
    rng=np.random.default_rng(971);n=20;trees=np.zeros((3,4,n+1),np.int64);occupied=np.zeros((3,4,n),np.int64);count=0
    def direct():
        return sum(int(occupied[0,h,x]*occupied[1,h,z]) for h in range(1,4) for x in range(n) for z in range(n) if z>x+6*h)+sum(int(occupied[2,h,y]*occupied[0,h,x]) for h in range(1,4) for x in range(n) for y in range(n) if x>y+5*h)
    for _ in range(500):
        kind=int(rng.integers(3));h=int(rng.integers(1,4));start=int(rng.integers(n));change=1 if occupied[kind,h,start]==0 else -1
        count+=relation_change(trees,(kind+1)*1000+h,start,change,n);occupied[kind,h,start]+=change;assert count==direct()
    return dict(operations=500,verdict='PASS',method='Fenwick relation deltas matched direct pair enumeration after every random toggle')

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--n',type=int,default=464);pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--seed',type=int,default=20260916);pa.add_argument('--weight',type=int,default=8);pa.add_argument('--patterns',default=str(ROOT/'patterns_window13.json'));pa.add_argument('--tag',default='parametric600');pa.add_argument('--hint',default=str(ROOT/'witness_464_window_ap5.json'));args=pa.parse_args();n=args.n;s=(n+2)//3
    sanity=tree_selfcheck();patterns=json.loads(Path(args.patterns).read_text())['patterns'];edges=[];groups=[];starts=[];numbers=[]
    for pattern in patterns:
        before=len(edges)
        for d in range(1,(n-1)//max(pattern)+1):
            for start in range(n-max(pattern)*d):edges.append([start+o*d for o in pattern]);groups.append(-1);starts.append(-1)
        numbers.append(len(edges)-before)
    for d in range(1,(n-1)//4+1):
        for start in range(n-4*d):edges.append([start+j*d for j in range(5)]);groups.append(d);starts.append(-1)
    param_counts=[];maxh=(n-2)//11
    for kind,pattern in enumerate([(0,1,2,4,5,6),(0,3,4,5),(0,1,2,5)]):
        before=len(edges)
        for h in range(1,maxh+1):
            for start in range(n-max(pattern)*h):edges.append([start+j*h for j in pattern]);groups.append((kind+1)*1000+h);starts.append(start)
        param_counts.append(len(edges)-before)
    groups=np.array(groups,np.int64);starts=np.array(starts,np.int64);caps=np.array([0]+[2*(bisect.bisect_right(H,n-d)-1) for d in range(1,n)],np.int64);thresholds=np.array([len(e) for e in edges],np.int64)
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
    ec=np.array([sum(x[i] for i in e) for e in edges],np.int64);gcount=np.zeros((n-1)//4+1,np.int64);trees=np.zeros((3,maxh+1,n+1),np.int64);param_violations=0
    for j,g in enumerate(groups):
        if 0<=g<1000 and ec[j]==5:gcount[g]+=1
        if g>=1000 and ec[j]==thresholds[j]:param_violations+=relation_change(trees,g,starts[j],1,n)
    excess=np.maximum(counts-caps,0);initial=int(np.sum(excess*excess)+args.weight*(np.count_nonzero((ec==thresholds)&(groups<0))+np.sum(np.maximum(gcount-1,0)**2)+param_violations));score=np.array([initial,initial,int(np.sum(excess*excess)),0],np.int64);best=x.copy();seed_rng(args.seed)
    sweep(x,counts,ec,thresholds,groups,starts,trees,gcount,caps,inc,incnum,args.weight,1.,1,best,score);start=time.time();iters=1;accepted=0;prev=initial;lastlog=0;events=[];base=ROOT/args.tag
    setup=dict(n=n,size=s,patterns=patterns,pattern_copy_counts=numbers,ap5_occurrences=int(np.count_nonzero((groups>=0)&(groups<1000))),parametric_h_count=maxh,parametric_block_occurrence_counts=param_counts,initial_parametric_violations=int(param_violations),tree_selfcheck=sanity,arguments=vars(args),initial_score=initial);base.with_suffix('.setup.json').write_text(json.dumps(setup,indent=2)+'\n');print(json.dumps(dict(event='start',**setup)),flush=True)
    while time.time()-start<args.seconds and score[0]>0:
        elapsed=time.time()-start;phase=(elapsed%120)/120;temp=.25+5.75*(1-phase)**2
        acc,num=sweep(x,counts,ec,thresholds,groups,starts,trees,gcount,caps,inc,incnum,args.weight,temp,10000,best,score);accepted+=acc;iters+=num
        if score[0]<prev or elapsed-lastlog>=10:
            event=dict(seconds=time.time()-start,iterations=iters,accepted=accepted,current_score=int(score[1]),best_score=int(score[0]),temperature=temp,expensive_evaluations=int(score[3]));events.append(event);print(json.dumps(event),flush=True);lastlog=elapsed
            if score[0]<prev:
                prev=int(score[0]);base.with_suffix('.best.json').write_text(json.dumps(dict(n=n,size=s,marks=(np.flatnonzero(best)+1).tolist(),score=int(score[0]),weight=args.weight,patterns=patterns,ap5_unique=True,parametric_family=True,arguments=vars(args)),indent=2)+'\n')
    out=dict(n=n,size=s,marks=(np.flatnonzero(best)+1).tolist(),initial_score=initial,best_score=int(score[0]),weight=args.weight,patterns=patterns,ap5_unique=True,parametric_family=True,iterations=iters,accepted=accepted,runtime_seconds=time.time()-start,arguments=vars(args),events=events,expensive_evaluations=int(score[3]),label='UNVERIFIED until independent checker passes')
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('marks','events','patterns')}),flush=True)

if __name__=='__main__':main()
