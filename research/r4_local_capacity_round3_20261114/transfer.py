"""Propagate certified finite caps by hereditary rank inequalities."""
import json,sys
from pathlib import Path
from bisect import bisect_left,bisect_right
from functools import lru_cache
ROOT=Path(__file__).parent;SRC=ROOT.parent/'boundary_certificates_20261115'
sys.path.insert(0,str(SRC))
import verify_four_rank as rank
import verify_four_edges as edge
from verify_four_window import load_window

def spans(g,seeds,limit=600):
    q=lambda L:max(0,bisect_right(g,L)-1)
    @lru_cache(None)
    def profile(L):
        count=[0];cost=[0]
        for h in range(1,L+1):
            v=q(L-h)+q(L-h-1)
            count.append(count[-1]+v);cost.append(cost[-1]+h*v)
        return count,cost
    lengths=[0,0]
    for size in range(2,limit+1):
        lower=max(lengths[-1]+1,seeds.get(size,0));total=endpoints=0
        for c in range(1,min(size-1,80)+1):
            total+=lengths[c];endpoints+=total
            H=c*size-c*(c+1)//2
            while True:
                count,cost=profile(lower)
                h=bisect_left(count,H)
                if h<len(count):
                    P=cost[h-1]+h*(H-count[h-1])
                    if 2*P+4*endpoints<=lower*c*(c+1):break
                lower+=1
        lengths.append(lower)
    return lengths

def main():
    g=rank.golomb_spans();old=edge.local_cap
    seeds={8:8,10:12,12:16,15:20}
    variants={'uniform_inherited':rank.binary_spans(g,600),
              'nonuniform_no_finite':spans(g,{}),'nonuniform_with_finite':spans(g,seeds)}
    den,r,a=load_window();samples=edge.read_samples();records={}
    for name,b in variants.items():
        assert b[-1]>1820
        edge.local_cap=lambda n,flag:min(old(n,True),bisect_right(b,n-1)-1) if flag else old(n,False)
        D=edge.variance_certificate(samples,a,edge.BINARY,True)
        records[name]=dict(binary_spans=b,D=str(D),floor_D=D.numerator//D.denominator,
                          capacities={n:edge.local_cap(n,True) for n in (8,12,16,20,32,64,128,256,512,1024,1820)})
        print(name,float(D),records[name]['floor_D'],records[name]['capacities'],flush=True)
    edge.local_cap=old
    (ROOT/'transfer_results.json').write_text(json.dumps(dict(seeds=seeds,variants=records),indent=2)+'\n')

if __name__=='__main__':main()
