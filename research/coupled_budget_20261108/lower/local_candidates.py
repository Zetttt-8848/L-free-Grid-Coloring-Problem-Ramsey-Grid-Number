"""Bounded weighted local-search discovery; every saved candidate is explicit.

Established breakout/min-conflict machinery, used as a complementary probe.
The objective is exactly the full set of 2,870 L constraints; no frozen cells.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import numba
from numba import njit
from adaptive_repair import encode,write,PRIOR


@njit(cache=False)
def search(colors, edges, adjacent, sizes, weights, steps, seed):
    np.random.seed(seed)
    count=len(edges); cells=len(colors)
    costs=np.zeros((cells,3),dtype=np.int64)
    bad=np.zeros(count,dtype=np.int64);positions=np.full(count,-1,dtype=np.int64);nbad=0
    for e in range(count):
        a,b,c=edges[e]
        if colors[b]==colors[c]:costs[a,colors[b]]+=weights[e]
        if colors[a]==colors[c]:costs[b,colors[a]]+=weights[e]
        if colors[a]==colors[b]:costs[c,colors[a]]+=weights[e]
        if colors[a]==colors[b] and colors[b]==colors[c]:bad[nbad]=e;positions[e]=nbad;nbad+=1
    best=colors.copy();bestn=nbad
    for step in range(steps):
        if nbad==0:return colors,weights,best,bestn,step
        e=bad[np.random.randint(nbad)]
        choices=np.empty((6,2),dtype=np.int64);nc=0;bestdelta=10**18
        for j in range(3):
            v=edges[e,j];old=colors[v]
            for col in range(3):
                if col==old:continue
                delta=costs[v,col]-costs[v,old]
                if delta<bestdelta:bestdelta=delta;nc=0
                if delta==bestdelta:choices[nc,0]=v;choices[nc,1]=col;nc+=1
        if np.random.random()<0.07:
            v=edges[e,np.random.randint(3)];col=(colors[v]+1+np.random.randint(2))%3
        else:
            pick=np.random.randint(nc);v=choices[pick,0];col=choices[pick,1]
        if bestdelta>=0:
            for j in range(nbad):
                f=bad[j];weights[f]+=1
                for k in range(3):costs[edges[f,k],colors[edges[f,k]]]+=1
        for idx in range(sizes[v]):
            f=adjacent[v,idx];a,b,c=edges[f]
            if colors[b]==colors[c]:costs[a,colors[b]]-=weights[f]
            if colors[a]==colors[c]:costs[b,colors[a]]-=weights[f]
            if colors[a]==colors[b]:costs[c,colors[a]]-=weights[f]
        colors[v]=col
        for idx in range(sizes[v]):
            f=adjacent[v,idx];a,b,c=edges[f]
            if colors[b]==colors[c]:costs[a,colors[b]]+=weights[f]
            if colors[a]==colors[c]:costs[b,colors[a]]+=weights[f]
            if colors[a]==colors[b]:costs[c,colors[a]]+=weights[f]
            violated=colors[a]==colors[b] and colors[b]==colors[c]
            if violated and positions[f]<0:positions[f]=nbad;bad[nbad]=f;nbad+=1
            elif not violated and positions[f]>=0:
                pos=positions[f];nbad-=1;bad[pos]=bad[nbad];positions[bad[pos]]=pos;positions[f]=-1
        if nbad<bestn:bestn=nbad;best=colors.copy()
    return colors,weights,best,bestn,steps


def main():
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=float,default=90)
    p.add_argument('--seed',type=int,default=71);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():raise ValueError('Fresh output required')
    paper=json.loads((PRIOR/'paper20.json').read_text(encoding='utf-8'))['rows']
    _,triples=encode(21);edges=np.array(triples,dtype=np.int64)
    lists=[[] for _ in range(441)]
    for e,t in enumerate(triples):
        for v in t:lists[v].append(e)
    sizes=np.array(list(map(len,lists)),dtype=np.int64)
    adjacent=np.full((441,max(sizes)),-1,dtype=np.int64)
    for v,es in enumerate(lists):adjacent[v,:len(es)]=es
    rng=np.random.default_rng(args.seed);colors=rng.integers(0,3,size=441,dtype=np.int64)
    for x in range(20):
        for y in range(20):colors[x*21+y+1]=paper[x][y]
    weights=np.ones(2870,dtype=np.int64)
    compile_start=time.monotonic()
    # Compile without changing the actual start state.
    search(colors.copy(),edges,adjacent,sizes,weights.copy(),0,args.seed)
    compile_seconds=time.monotonic()-compile_start
    begin=time.monotonic();bestn=2871;history=[];steps=0;chunk=0
    record={'status':'RUNNING','seed':args.seed,'budget_seconds':args.seconds,'compile_seconds':compile_seconds,
        'software':{'numpy':np.__version__,'numba':numba.__version__},'history':history,
        'non_claim':'No positive construction unless independent full geometry has zero violations.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    while time.monotonic()-begin<args.seconds:
        colors,weights,best,score,done=search(colors,edges,adjacent,sizes,weights,250000,args.seed+chunk)
        steps+=done;chunk+=1
        if score<bestn:
            bestn=int(score);record['grid']=best.reshape(21,21).tolist();record['violations']=bestn
            history.append({'step':steps,'elapsed':time.monotonic()-begin,'violations':bestn})
        record['elapsed_seconds']=time.monotonic()-begin;record['steps']=steps
        write(args.output,record)
        if bestn==0:break
    record['status']='SAT_CANDIDATE' if bestn==0 else 'IMPROPER_CANDIDATE_UNDECIDED'
    write(args.output,record)
    print(json.dumps({k:record[k] for k in ('status','violations','steps','elapsed_seconds')}))


if __name__=='__main__':main()
