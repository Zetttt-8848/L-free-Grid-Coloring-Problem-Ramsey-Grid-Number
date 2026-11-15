"""Exact hypothetical binary-input sensitivity; no new bound is claimed."""
from pathlib import Path
import sys,json
from fractions import Fraction as F
from bisect import bisect_right,bisect_left

HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'boundary_certificates_20261115'
sys.path.insert(0,str(SRC))
import verify_four_rank as rank
import verify_four_edges as edge
from verify_four_window import load_window,REFERENCE
from verify_four_double import sidon_length

def elementary():
    rows=json.loads((SRC/'four_capacity_runs.json').read_text())
    g=rank.golomb_spans()
    e=rank.binary_spans(g,max(r[2] for r in rows))
    out=[]
    for ix in (0,len(rows)//2,len(rows)-1):
        start,K,c=rows[ix]; L=rank.REFERENCE_SIDE-start-1
        v=[bisect_right(g,L-h)+bisect_right(g,L-h-1)-2 for h in range(1,55001)]
        count=[0];moment=[0]
        for h,cap in enumerate(v,1):
            count.append(count[-1]+cap);moment.append(moment[-1]+h*cap)
        correction=4*sum((c-i)*e[i+1] for i in range(c))
        def margin(k,ppm):
            factor=F(1000000-ppm,1000000)
            H=c*k-c*(c+1)//2
            target=F(H)/factor
            h=bisect_left(count,target)
            assert h<len(count)
            P=factor*moment[h-1]+h*(H-factor*count[h-1])
            return 2*P+correction-L*c*(c+1)
        assert margin(K+1,0)>0
        for k in (K,99*K//100):
            lo,hi=0,100000
            assert margin(k,hi)>0
            while lo<hi:
                mid=(lo+hi)//2
                if margin(k,mid)>0:hi=mid
                else:lo=mid+1
            out.append(dict(row=ix,positions=L+1,old_cap=K,excluded_size=k,
                new_cap_if_proved=k-1,minimum_ppm_on_tested_grid=lo,
                exact_positive_rank_margin=str(margin(k,lo)),
                hypothesis='r_A(h) <= (1-eps)*v_h for every h used by rank argument'))
    return out

def windows():
    den,r,alpha=load_window()
    thresholds=[sidon_length(k,den,r,alpha,52,lambda k,p,b:edge.domain_check(edge.INNER,k,p,b))
                for k in range(4600,4801)]
    rows=json.loads((SRC/'four_edge_runs.json').read_text())
    out=[]
    for ix in (0,len(rows)//2,len(rows)-1):
        offset,K,b=rows[ix];p=REFERENCE-offset
        edge.domain_check(edge.BINARY,K+1,p,b)
        Q=lambda t:4599+bisect_right(thresholds,t)
        X=0
        for h in range(1,200*b):
            j,t=divmod(h,b)
            ah=(b-t)*r[j]+t*(r[j+1] if j+1<len(r) else 0)
            assert 0<bisect_right(thresholds,p-h)<201
            assert 0<bisect_right(thresholds,p-h-1)<201
            X+=2*(Q(p-h)+Q(p-h-1))*ah
        W=den*b*b; a0=b*r[0];P=p-213+b*alpha
        def gap(k):return k*k*W-P*(k*a0+X)
        assert gap(K+1)>0
        for k in (K,99*K//100):
            # The edge discrepancy certificate requires k >= 455000.
            if k<edge.BINARY[3]:
                out.append(dict(row=ix,excluded_size=k,status='outside edge k domain; not evaluated'))
                continue
            critical=-gap(k)/(P*X)
            out.append(dict(row=ix,positions=p,old_cap=K,excluded_size=k,
                new_cap_if_proved=k-1,epsilon_must_exceed=str(critical),
                approximate_ppm=float(critical*1000000),
                hypothesis='2 sum r_A(h)*a_h <= (1-eps)*2 sum v_h*a_h',
                near_extremality='none; edge parameters and k domain still required'))
    return out

result=dict(status='HYPOTHETICAL SENSITIVITY ONLY',elementary=elementary(),window=windows())
(HERE/'sensitivity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
