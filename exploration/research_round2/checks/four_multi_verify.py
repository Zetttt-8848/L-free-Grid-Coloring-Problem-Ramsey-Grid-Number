"""Independent certificate-only verifier; no imports from search or cap code.

Uses arbitrary-precision Python integers, direct first-forbidden-size checks,
and run-polynomial weight sums, not the generator's pointwise accumulation.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def excludes(size,length,v,c):
    assert size>c>=1 and v>=1
    h=c*size-c*(c+1)//2
    blocks=h//v
    rest=h-blocks*v
    # Values 1,...,blocks repeated v times; remaining values blocks+1.
    lower=blocks*(blocks+1)*v//2+rest*(blocks+1)
    return 2*lower>length*c*(c+1)

def sums(lo,hi):
    count=hi-lo+1
    first=(lo+hi)*count//2
    def sq(x):return x*(x+1)*(2*x+1)//6
    return count,first,sq(hi)-sq(lo-1)

def main():
    path=ROOT/'certificates'/'four_multi_final.json'
    data=json.loads(path.read_text())
    n,t=data['n'],data['t']
    cq,c=data['golomb_neighbor_parameter'],data['capacity_neighbor_parameter']
    assert 1<=t<=n
    next_d=1
    total=0
    for block in data['runs']:
        lo,hi,q,k=(block[x] for x in ('lo','hi','q','K'))
        assert lo==next_d and lo<=hi<t
        length=n-lo-1  # longest span in this run; proves every distance in it.
        assert excludes(q+1,length,1,cq)
        assert excludes(k+1,length,2*q,c)
        count,d1,d2=sums(lo,hi)
        a=n-48*k
        total+=2*(a*t*count-(a+t)*d1+d2)
        next_d=hi+1
    assert next_d==t
    rhs=3*n*t
    assert total>rhs
    assert (total,rhs,total-rhs)==(data['doubled_lhs'],data['doubled_rhs'],data['doubled_margin'])
    # Independent entire-grid naive-extension counterexample test.
    bad=[]
    for x in range(1,5):
      for y in range(1,5):
       for d in range(1,5):
        if x+d<=4 and y+d<=4:
            cols=((x-y)%4,(x+d-y)%4,(x-y)%4)
            if len(set(cols))==1:bad.append((x,y,d))
    assert not bad
    # Verify overlap witness from its literal colored coordinate list.
    overlap=json.loads((ROOT/'certificates'/'four_multi_overlap.json').read_text())['witness']
    col={(x,y):cc for x,y,cc in overlap['colors']}
    corner_count=0
    for x,y in col:
      for xx,yy in col:
        if xx-x==yy-y>0:
            assert (xx,y) in col
            assert len({col[x,y],col[xx,y],col[xx,yy]})>1
            corner_count+=1
    out=dict(verdict='PASS',n=n,t=t,runs=len(data['runs']),
             doubled_lhs=total,doubled_rhs=rhs,doubled_margin=total-rhs,
             overlap_region_corners=corner_count,
             scope='Exact certificate arithmetic and literal finite witnesses; universal proof in four_multi_core.md')
    (ROOT/'certificates'/'four_multi_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
