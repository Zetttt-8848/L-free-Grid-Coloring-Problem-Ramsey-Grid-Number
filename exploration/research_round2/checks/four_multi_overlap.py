"""Definition-level overlap geometry and small valid-region witness."""
from itertools import combinations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def region_corners(region):
    return [(p,(q[0],p[1]),q) for p,q in combinations(sorted(region),2)
            if q[0]-p[0]==q[1]-p[1]>0 and (q[0],p[1]) in region]

def find_witness(marks,d,e):
    tri={(v,u) for u,v in combinations(marks,2)}
    u,w=marks[0],marks[-1]
    prescribed={(u+d,u):1,(w,w-d):1,(u+e,u):1,(w,w-e):1,(w,u):2}
    assert set(prescribed)<=tri
    free=sorted(tri-set(prescribed))
    triples=region_corners(tri)
    for bits in product((1,2),repeat=len(free)):
        color=prescribed|dict(zip(free,bits))
        if all(len({color[p] for p in t})>1 for t in triples):
            full=color|{(a,a):0 for a in marks}
            assert all(len({full[p] for p in t})>1 for t in region_corners(set(full)))
            # Verify completion closure directly on this exact region.
            assert all((q[0],p[1]) in full for p,q in combinations(sorted(full),2)
                       if q[0]-p[0]==q[1]-p[1]>0)
            fibers={str(h):[a for a in marks if a+h in marks and color.get((a+h,a))==1]
                    for h in (d,e)}
            images={str(h):sorted((b+h,a) for a,b in combinations(fibers[str(h)],2))
                    for h in (d,e)}
            assert (w,u) in images[str(d)] and (w,u) in images[str(e)]
            return dict(marks=marks,d=d,e=e,colors=[[*p,c] for p,c in sorted(full.items())],
                        triangle_corner_count=len(triples),fibers=fibers,images=images,
                        common_image=[w,u])
    return None

def main():
    # Pure geometry: maps within each diagonal are injective; cross-diagonal
    # intersections have exactly the asserted endpoint equations.
    family_count=pair_comparisons=0
    for n in range(1,9):
      for size in range(n+1):
       for marks in combinations(range(1,n+1),size):
        maps=[]
        for delta in range(n):
            pairs=[(u,v) for u,v in combinations(marks,2) if v+delta<=n]
            outputs=[(v+delta,u) for u,v in pairs]
            assert len(outputs)==len(set(outputs))
            maps.extend((delta,u,v,(v+delta,u)) for u,v in pairs)
            family_count+=1
        for (delta,u,v,z),(epsilon,p,q,y) in combinations(maps,2):
            assert (z==y)==(u==p and v+delta==q+epsilon)
            pair_comparisons+=1
    witness=find_witness([1,4,8,14,18,21],3,7)
    assert witness is not None
    out=dict(geometry_range_n=[1,8],families=family_count,
             pair_comparisons=pair_comparisons,witness=witness)
    (ROOT/'certificates'/'four_multi_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
