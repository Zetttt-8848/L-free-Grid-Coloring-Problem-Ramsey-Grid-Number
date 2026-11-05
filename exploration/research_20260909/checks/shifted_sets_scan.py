"""Exact shifted-translates second-moment inequalities for a diagonal set.

Input: exact Golomb minimum-span table copied from supplied MSY PDF Algorithm 3.
All arithmetic integer; finite scan of the stated n,m,t family only.
"""
import json

G = [0,0,1,3,6,11,17,25,34,44,55,72,85,106,127,151,177,199,216,246,283,333,356,372,425,480,492,553,585]

def q(length):
    assert 0 <= length < G[-1]
    return max(i for i,g in enumerate(G) if g <= length)

def cap(n,d):
    return min(n-d,2*q(n-d-1))

def min_square_with_bounds(total,bounds):
    # Discrete convex minimization over integers 0 <= f_j <= bound_j.
    # At level ell, filling each not-full location once costs 2*ell+1.
    cost=0
    for ell in range(max(bounds)):
        available=sum(b>ell for b in bounds)
        used=min(total,available)
        cost+=used*(2*ell+1)
        total-=used
        if not total:
            return cost
    assert total==0
    return cost

def second_moment(n,m,t,edge_bounds=True):
    N=n+t-1
    bounds=[min(t,j,N+1-j,m) if edge_bounds else min(t,m) for j in range(1,N+1)]
    lower=min_square_with_bounds(m*t,bounds)
    upper=m*t+2*sum((t-d)*cap(n,d) for d in range(1,min(t,n)))
    return lower-upper,lower,upper

def scan(n):
    m=(n+2)//3
    best=None
    s0=s1=0
    for t in range(1,n+1):
        if t>1:
            v=cap(n,t-1)
            s0+=v
            s1+=(t-1)*v
        upper=m*t+2*(t*s0-s1)
        N=n+t-1
        total=m*t
        lower=0
        for level in range(1,min(t,m)+1):
            filled=min(total,N-2*(level-1))
            lower+=(2*level-1)*filled
            total-=filled
            if not total: break
        assert total==0
        rec=(lower-upper,t,lower,upper)
        if best is None or rec>best: best=rec
    return {'n':n,'m':m,'margin':best[0],'t':best[1],'lower':best[2],'upper':best[3]}

def balanced_square(s,k=3):
    a,r=divmod(s,k)
    return (k-r)*a*a+r*(a+1)*(a+1)

def scan_all_colors(n):
    # At every position, the three sliding counts sum to the fixed window size.
    best=None
    s0=s1=edge=0
    for t in range(1,n+1):
        if t>1:
            v=cap(n,t-1)
            s0+=v
            s1+=(t-1)*v
            edge+=2*balanced_square(t-1)
        upper=n*t+6*(t*s0-s1)
        lower=(n-t+1)*balanced_square(t)+edge
        rec=(lower-upper,t,lower,upper)
        if best is None or rec>best: best=rec
    return {'n':n,'margin':best[0],'t':best[1],'lower':best[2],'upper':best[3]}

if __name__=='__main__':
    selected=[scan(n) for n in [450,480,490,491,492,493,500,510,520,530,540,550]]
    first=next((scan(n) for n in range(450,586) if scan(n)['margin']>0),None)
    result={'Golomb_minimum_spans':G,'selected':selected,'first_contradiction_n_in_450_to_585':first}
    result['all_colors_first_contradiction']=next((scan_all_colors(n) for n in range(3,586) if scan_all_colors(n)['margin']>0),None)
    result['all_colors_selected']=[scan_all_colors(n) for n in [400,440,450,460,470,475,480,490,491,492,493]]
    print(json.dumps(result,indent=2))
