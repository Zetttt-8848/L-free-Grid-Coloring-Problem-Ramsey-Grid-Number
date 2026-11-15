"""Exact transport of improved endpoint corrections to the R4 consumer."""
import json,sys
from pathlib import Path
from bisect import bisect_right
from functools import lru_cache
from fractions import Fraction as F
ROOT=Path(__file__).parent;SRC=ROOT.parent/'boundary_certificates_20261115'
sys.path.insert(0,str(SRC))
from verify_four_window import load_window,REFERENCE,verify_profile
from verify_four_double import sidon_length
from verify_four_twenty import outer_twenty
import verify_four_edges as edge

def main():
    den,r,alpha=load_window();thresholds=[sidon_length(k,den,r,alpha,52,lambda k,p,b:edge.domain_check(edge.INNER,k,p,b)) for k in range(4600,4801)]
    original=json.loads((SRC/'four_edge_runs.json').read_text());weights=edge.quartic_correlations(edge.WIDTH)
    @lru_cache(None)
    def cumulative(b):
        w=r+[0];out=[0]*201
        for j in reversed(range(200)):out[j]=out[j+1]+b*((b+1)*w[j]+(b-1)*w[j+1])
        return out
    def tail(h,b):
        j,t=divmod(h,b)
        if j>=200:return 0
        nr=r[j+1] if j+1<200 else 0
        return cumulative(b)[j+1]+(b-t)*((b-t+1)*r[j]+(b+t-1)*nr)
    def accepts(p,k,b,D):
        edge.domain_check(edge.BINARY,k,p,b)
        Q=lambda t:4599+bisect_right(thresholds,t)
        gamma=Q(p-1)+Q(p-2);W=den*b*b
        E=(k-gamma)*b*r[0]+gamma*W
        events=[h for L in thresholds for h in (p-L,p-L+1) if 2<=h<200*b]
        assert Q(p-200*b+1)+Q(p-200*b)==gamma-len(events)
        E-=sum(tail(h,b) for h in events)
        return k*k*W>(p-D+b*alpha)*E
    out={}
    transfer=json.loads((ROOT/'transfer_results.json').read_text())
    exact_rank_D=F(transfer['variants']['nonuniform_no_finite']['D'])
    for name,D in [('rank_only',F(219)),('rank_only_exact',exact_rank_D),('finite_seeded',F(1097,5))]:
        rows=[];gains=[]
        for offset,cap,b in original:
            p=REFERENCE-offset;assert accepts(p,cap+1,b,D)
            gain=0
            while gain<32 and accepts(p+gain+1,cap+1,b,D):gain+=1
            rows.append([offset-gain,cap,b]);gains.append(gain)
        assert all(x[0]<y[0] for x,y in zip(rows,rows[1:]))
        # The final bound remains valid on shorter intervals by heredity.
        rows.append([rows[-1][0]+1000,rows[-1][1],rows[-1][2]])
        verify_profile(rows,den,r,alpha,thresholds,D)
        def margin(n):
            count,raw,bonus,loss=outer_twenty(rows,n,edge.WIDTH,lambda t,d:weights[d])
            return raw+bonus,(count,raw,bonus,loss)
        lo=edge.SIDE-100;hi=edge.SIDE
        assert margin(lo)[0]<0 and margin(hi)[0]>0
        while hi-lo>1:
            mid=(lo+hi)//2
            if margin(mid)[0]>0:hi=mid
            else:lo=mid
        val,parts=margin(hi)
        out[name]=dict(D=str(D),side=hi,margin=val,outer_parts=parts,previous_test=dict(side=lo,margin=margin(lo)[0]),
                      row_extensions=dict(min=min(gains),max=max(gains)),rows=rows)
        print(name,'D',D,'side',hi,'gain',edge.SIDE-hi,'margin',val,flush=True)
    (ROOT/'consumer_results.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
