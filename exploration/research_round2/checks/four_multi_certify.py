"""Exact finite certificates for FM1--FM4; no numerical optimizer or SAT."""
from math import isqrt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def corners(n):
    return [((x,y),(x+d,y),(x+d,y+d))
            for d in range(1,n) for x in range(1,n-d+1)
            for y in range(1,n-d+1)]

def minsum(h,v):
    a,b=divmod(h,v)
    return v*a*(a+1)//2+b*(a+1)

def capacity(length,v,c):
    """Upper bound K on marks; continuous quadratic then exact residue."""
    h=(isqrt(v*v+4*v*length*c*(c+1))-v)//2
    k=max(c,(h+c*(c+1)//2)//c)
    # The exact balanced minimum may rule out the continuous endpoint.
    while k>c and 2*minsum(c*k-c*(c+1)//2,v)>length*c*(c+1):
        k-=1
    hp=c*(k+1)-c*(c+1)//2
    assert 2*minsum(hp,v)>length*c*(c+1)
    return k

def best_capacity(length,v,crange):
    return min((capacity(length,v,c),c) for c in crange)

def exact_certificate(n):
    length=n-1
    # Golomb capacity is the V=1 case of the same proved neighbor inequality.
    # Fixed, completely specified bounded parameter searches; not global optima.
    q,cq=best_capacity(length,1,range(1,201))
    v=2*q
    k,c=best_capacity(length,v,range(1,2001))
    delta=n-48*k
    t=max(1,min(n,3*delta//2))
    lhs=3*delta*(t-1)-(t*t-1)
    rhs=9*n
    hq=cq*(q+1)-cq*(cq+1)//2
    hk=c*(k+1)-c*(c+1)//2
    return dict(n=n,q=q,cq=cq,V=v,K=k,c=c,t=t,delta=delta,
                golomb_lhs=2*minsum(hq,1),golomb_rhs=length*cq*(cq+1),
                capacity_lhs=2*minsum(hk,v),capacity_rhs=length*c*(c+1),
                weighted_lhs=lhs,weighted_rhs=rhs,margin=lhs-rhs,
                proved=lhs>rhs)

def main():
    grid=[[((x-y)%4) for x in range(1,5)] for y in range(1,5)]
    triples=corners(4)
    assert all(len({grid[y-1][x-1] for x,y in tri})>1 for tri in triples)
    fiber=[u for u in range(1,4)
           if grid[u-1][u-1]==grid[u][u]==0 and grid[u-1][u]==1]
    assert fiber==[1,2,3]
    scan=[exact_certificate(b**4) for b in range(60,81)]
    positives=[r for r in scan if r['proved']]
    assert positives and min(r['n'] for r in positives)<30_000_000
    result=dict(naive_counterexample=dict(n=4,rows_y_columns_x=grid,
                triples=len(triples),fiber=fiber,repeated_difference=1),
                range_b=[60,80],scan=scan,first=min(positives,key=lambda r:r['n']))
    path=ROOT/'certificates'/'four_multi_first.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(counterexample=result['naive_counterexample'],first=result['first']),indent=2))

if __name__=='__main__':
    main()
