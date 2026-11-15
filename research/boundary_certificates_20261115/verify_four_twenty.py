"""Check the 20-distance shared-prefix bound, using the companion window certificate."""
from bisect import bisect_right
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from verify_four_window import HERE, REFERENCE, WIDTH, correlation, require, main as audit_windows

SIDE=21_948_402
BLOCK=20


@lru_cache(None)
def budget(histogram):
    if not sum(histogram):return 0
    # Twice the upper bound for any two words. The final step contributes
    # the largest possible column plus its row's three-per-color quota.
    best=0
    for i,x in enumerate(histogram):
        if x:
            parent=list(histogram)
            parent[i]-=1
            best=max(best,budget(tuple(sorted(parent))))
    return best+max(histogram)+sum(min(3,x) for x in histogram)


def outer_twenty(rows,side,width,kernel=correlation):
    max_twice=max(budget(h) for h in combinations_with_replacement(range(BLOCK+1),4)
                  if sum(h)==BLOCK)
    baseline=sum(min(i,12) for i in range(1,BLOCK+1))
    loss=baseline-max_twice//2
    require((baseline,max_twice,loss)==(174,267,41),"20-distance inequality")
    starts=[a for a,_,_ in rows]
    offset=REFERENCE-side
    require(starts[0]<=offset+1 and starts[-1]>=offset+width+10,"profile coverage")
    raw=-3*side*kernel(width,0)
    for d in range(1,width):
        u=sum(rows[bisect_right(starts,offset+d+j)-1][1] for j in range(12))
        raw+=2*(side-d-4*u)*kernel(width,d)
    centers=[]
    bonus=0
    for i in range(1,len(rows)-1):
        v,cap,_=rows[i]
        D=v-offset
        if (rows[i-1][1]==cap+1 and v-starts[i-1]>=BLOCK
            and starts[i+1]-v>=12 and D-BLOCK>=1 and D-1<width):
            centers.append(D)
            bonus+=8*loss*min(kernel(width,D-s) for s in range(1,BLOCK+1))
    require(all(b-a>=BLOCK for a,b in zip(centers,centers[1:])),"disjoint blocks")
    return len(centers),raw,bonus,loss


def main():
    audit_windows()
    rows=json.loads((HERE/"four_window_runs.json").read_text())
    count,raw,bonus,loss=outer_twenty(rows,SIDE,WIDTH)
    require((count,raw,bonus)==(544,-116_299_243_654_456_808_241_433_200,
                 128_738_682_276_347_489_324_958_496),"final exact sum")
    require(raw+bonus>0,"four-color margin")
    print(f"At least {loss} matches lost per 20 shifts, side {SIDE:,}, "
          f"doubled margin {raw+bonus:,}.")

if __name__=="__main__":main()
