"""Reconstruct the four-color capacity certificate using only Python integers.

Read the small file of (start lag, cap, rank parameter) witnesses. Every cap
is re-proved from the elementary rank inequalities; see FOUR_COLOR.md.
"""
import json
from bisect import bisect_left, bisect_right
from pathlib import Path

SIDE = 21_987_409
SUPPORT = 35_000
REFERENCE_SIDE = 21_991_300  # index origin for the lag intervals, not a theorem input
HERE = Path(__file__).resolve().parent


def checked(value, message):
    if not value:
        raise ValueError(message)


def golomb_spans():
    """Certified lower spans g[s]. The entry at 0 is a sentinel."""
    g = [0,0]
    for size in range(2,4901):
        lower = g[-1]+1
        endpoints = 0
        total = 0
        for rank in range(1,min(size-1,130)+1):
            total += g[rank]
            endpoints += total
            pairs = rank*size-rank*(rank+1)//2
            numerator = pairs*(pairs+1)+4*endpoints
            denominator = rank*(rank+1)
            lower = max(lower,(numerator+denominator-1)//denominator)
        g.append(lower)
    return g


def binary_spans(g, limit):
    """Small-span recursion for any set supporting a proper binary strict source."""
    lengths=[0,0]
    for size in range(2,limit+1):
        lower=lengths[-1]+1
        total=endpoints=0
        for rank in range(1,min(size-1,80)+1):
            total+=lengths[rank]
            endpoints+=total
            pairs=rank*size-rank*(rank+1)//2
            while True:
                cap=2*(bisect_right(g,lower-1)-1)
                full,extra=divmod(pairs,cap)
                cheapest=cap*full*(full+1)//2+extra*(full+1)
                if 2*cheapest+4*endpoints <= lower*rank*(rank+1):
                    break
                lower+=1
            # Every rejected integer below 'lower' has failed a rank inequality.
        lengths.append(lower)
    return lengths


def exact_margin():
    runs=json.loads((HERE/"four_capacity_runs.json").read_text(encoding="utf-8"))
    checked(runs and runs[0][0]==1,"first capacity index")
    last_lag=REFERENCE_SIDE-SIDE+SUPPORT-1+11
    checked(runs[-1][0]<=last_lag,"unused capacity runs")
    g=golomb_spans()
    cap=lambda span: bisect_right(g,span)-1
    checked(g[-1]>REFERENCE_SIDE,"upper Golomb sentinel")
    lengths=binary_spans(g,max(row[2] for row in runs))
    # At main lag v, the h-th internal difference has at most
    # Q(N-v-h-1) + Q(N-v-h-2) occurrences. Prefix arrays indexed by v+h.
    stop=last_lag+55_000
    count=[0]*(stop+1)
    moment=[0]*(stop+1)
    for u in range(1,stop+1):
        multiplicity=cap(REFERENCE_SIDE-u-1)+cap(REFERENCE_SIDE-u-2)
        count[u]=count[u-1]+multiplicity
        moment[u]=moment[u-1]+u*multiplicity
    caps=[0]
    for idx,(start,bound,rank) in enumerate(runs):
        end=runs[idx+1][0]-1 if idx+1<len(runs) else last_lag
        checked(start==len(caps) and start<=end and 1<=rank<bound+1,"run domain")
        span=REFERENCE_SIDE-start-1
        h=rank*(bound+1)-rank*(rank+1)//2
        frontier=bisect_left(count,count[start]+h,lo=start+1)
        checked(frontier<=stop,"profile tail")
        used=count[frontier-1]-count[start]
        cheapest=(moment[frontier-1]-moment[start]-start*used
                  +(frontier-start)*(h-used))
        correction=sum((rank-i)*lengths[i+1] for i in range(rank))
        checked(2*cheapest+4*correction>span*rank*(rank+1),
                f"unproved capacity at index {start}")
        caps.extend([bound]*(end-start+1))
    checked(len(caps)==last_lag+1,"incomplete active profile")

    # Closed autocorrelation of w_i=i*(t+1-i), 1<=i<=t.
    t=SUPPORT
    def corr(d):
        m=t+1-d
        return m*(m*m-1)*(m*m+1+5*d*(t+1))//30
    checked(corr(0)==sum((i*(t+1-i))**2 for i in range(1,t+1)),
            "parabola normalization")
    offset=REFERENCE_SIDE-SIDE
    margin=-3*SIDE*corr(0)
    for d in range(1,t):
        upper=sum(caps[offset+d:offset+d+12])
        margin+=2*(SIDE-d-4*upper)*corr(d)
    checked(margin==2_727_455_661_705_377_936_113_840 and margin>0,
            "final margin")
    print(f"side {SIDE:,}; support {t:,}; {len(runs)} rank witnesses; "
          f"{t-1:,} active lags; doubled margin {margin:,}")
    return margin


if __name__=="__main__":
    exact_margin()
