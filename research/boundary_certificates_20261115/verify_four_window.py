"""Verify the nonuniform four-color bound using the exact COT window data.

The optional argument points to the authors' asymptotic directory. See the
accompanying theorem for its revision, the discrete lifting, and the separate
twelve-letter finite inequality.
"""
from bisect import bisect_right
from fractions import Fraction
from functools import lru_cache
from math import lcm
from pathlib import Path
import json
import sys

from verify_four_sidon import lower_length

HERE = Path(__file__).resolve().parent
REFERENCE = 21_975_000
SIDE = 21_948_404
WIDTH = 34_950


def require(condition, message):
    if not condition:
        raise ValueError(message)


def derive_window(folder):
    def matrix(name):
        return [[Fraction(x) for x in line.strip().split(",")]
                for line in (folder / (name+".txt")).read_text().splitlines()]
    g, table, probability = matrix("G"), matrix("H"), matrix("p")[0]
    k, m = len(g), len(g[0])
    require(k == len(table) == len(probability) == 6 and m == 200, "matrix dimensions")
    require(all(len(r)==m for r in g) and all(len(r)==3*m for r in table), "matrix rows")
    require(min(probability)>0 and sum(probability)==1, "probabilities")
    require(all(min(r)>=0 for r in g+table), "strong window/table")
    require(all(all(v==1 for v in r[m:2*m]) for r in table), "constant middle")
    mass = sum(g[0])
    require(mass>0 and all(sum(row)==mass for row in g), "window normalization")
    # Integer arithmetic checks all 401 coarse alignments without rational
    # reductions at every product. Between these alignments the overlap is linear.
    dg=lcm(*(x.denominator for row in g for x in row))
    dt=lcm(*(x.denominator for row in table for x in row))
    dp=lcm(*(x.denominator for x in probability))
    gi=[[int(x*dg) for x in row] for row in g]
    tj=[[int(x*dt) for x in row] for row in table]
    pi=[int(x*dp) for x in probability]
    for j in range(2*m+1):
        val=sum(pr*sum(x*y for x,y in zip(row,edge[j:j+m]))
                for pr,row,edge in zip(pi,gi,tj))
        require(val>=mass*dg*dt*dp,"coarse lower coverage")
    r=[sum(pr*sum(a*b for a,b in zip(row,row[h:])) for pr,row in zip(pi,gi))
       for h in range(m)]
    r=[Fraction(v,dp*dg**2)/mass**2 for v in r]
    a=sum(pr*sum(x*x for x in row) for pr,row in zip(probability,table))-2*m
    den=lcm(*(v.denominator for v in r))
    return den,[int(v*den) for v in r],a


def load_window(folder=None):
    values=json.loads((HERE/"four_window_correlations.json").read_text())
    den=int(values["denominator"])
    r=list(map(int,values["correlations"]))
    a=Fraction(values["table_excess"])
    require(len(r)==200 and min(r)>=0 and a>0 and 2*sum(r)-r[0]==den,
            "correlation mass and positivity")
    if folder is not None:
        require(derive_window(folder)==(den,r,a),"disagreement with authors' exact tables")
    return den,r,a


def correlation(t,d):
    m=t+1-d
    return m*(m*m-1)*(m*m+1+5*d*(t+1))//30


def main():
    den,r,alpha=load_window(Path(sys.argv[1]) if len(sys.argv)>1 else None)
    rows=json.loads((HERE/"four_window_runs.json").read_text())
    offsets=[v for v,_,_ in rows]
    require(all(v<u for v,u in zip(offsets,offsets[1:])),"order of offsets")
    require(offsets[0]<=REFERENCE-SIDE+1 and offsets[-1]>=REFERENCE-SIDE+WIDTH+10,
            "window count covers all outer shifts and neighbors")
    thresholds=[lower_length(k) for k in range(4600,4801)]
    def golomb(positions):
        j=bisect_right(thresholds,positions)
        require(0<j<len(thresholds),"ordinary Sidon range")
        return 4599+j
    @lru_cache(None)
    def accumulated(block):
        # Twice the tail sum in units of 1/(den*block^2), at block boundaries.
        w=r+[0]
        out=[0]*(len(r)+1)
        for j in reversed(range(len(r))):
            out[j]=out[j+1]+block*((block+1)*w[j]+(block-1)*w[j+1])
        return out
    def tail2(h,b):
        j,t=divmod(h,b)
        if j>=len(r):return 0
        next_r=r[j+1] if j+1<len(r) else 0
        return accumulated(b)[j+1]+(b-t)*((b-t+1)*r[j]+(b+t-1)*next_r)
    def audit(p,k,b):
        require(p-1>=2*len(r)*b and b>0,"room for the stretched table")
        weight=den*b*b
        at_zero=b*r[0]
        gamma=golomb(p-1)+golomb(p-2)
        e=(k-gamma)*at_zero+gamma*weight
        # q(p-h) drops at h=p-L+1 and q(p-h-1) at h=p-L.
        events=sorted(h for length in thresholds for h in (p-length,p-length+1)
                      if 2<=h<len(r)*b)
        require(golomb(p-len(r)*b+1)+golomb(p-len(r)*b)==gamma-len(events),
                "all capacity drops found")
        for h in events:e-=tail2(h,b)
        return k*k*weight*alpha.denominator > (p*alpha.denominator+b*alpha.numerator)*e
    for v,cap,b in rows:
        require(audit(REFERENCE-v,cap+1,b),f"failed interval witness at offset {v}")
    def capacity(v):return rows[bisect_right(offsets,v)-1][1]
    outer=REFERENCE-SIDE
    raw=-3*SIDE*correlation(WIDTH,0)
    for d in range(1,WIDTH):
        u=sum(capacity(outer+d+j) for j in range(12))
        raw+=2*(SIDE-d-4*u)*correlation(WIDTH,d)
    blocks=[]; savings=0
    for i in range(1,len(rows)-1):
        v,cap,_=rows[i]
        D=v-outer
        if (rows[i-1][1]==cap+1 and v-offsets[i-1]>=12 and offsets[i+1]-v>=12
                and 1<=D-12 and D-1<WIDTH):
            # verify_quota12.c proves sum M_s <= 48 out of 78.
            blocks.append(D)
            savings+=8*30*min(correlation(WIDTH,D-s) for s in range(1,13))
    require(all(y-x>=12 for x,y in zip(blocks,blocks[1:])),"disjoint lag blocks")
    require((len(blocks),raw,savings)==(544,-90_422_183_662_414_011_960_985_072,
                 94_186_029_099_831_697_780_548_480),"outer margin regression")
    require(raw+savings>0,"positive final margin")
    print(f"{len(rows)} window bounds, {len(blocks)} disjoint blocks, "
          f"{WIDTH-1:,} distances, side {SIDE:,}, doubled margin {raw+savings:,}.")


if __name__=="__main__":
    main()
