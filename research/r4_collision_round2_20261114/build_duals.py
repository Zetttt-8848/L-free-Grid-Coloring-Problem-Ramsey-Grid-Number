"""Discover finite demand certificates; certify rational feasibility separately."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
from bisect import bisect_right
from scipy.optimize import linprog

ROOT=Path(__file__).parent
SRC=ROOT.parent/'boundary_certificates_20261115'
sys.path.insert(0,str(SRC))
from verify_four_window import load_window,REFERENCE
from verify_four_double import sidon_length
import verify_four_edges as edge

def bal(m,N):
    q,a=divmod(N,m)
    return m*q*(q-1)//2+a*q

def main():
    den,r,alpha=load_window()
    thresholds=[sidon_length(k,den,r,alpha,52,lambda k,p,b:edge.domain_check(edge.INNER,k,p,b)) for k in range(4600,4801)]
    offset,K,b=json.loads((SRC/'four_edge_runs.json').read_text())[0]
    p=REFERENCE-offset; S=200*b-1; a0=b*r[0]
    def weight(t):
        j,u=divmod(t,b)
        return (b-u)*r[j]+u*(r[j+1] if j+1<len(r) else 0)
    rows=[]
    for h in (1,S//4,S//2):
        count=9198+bisect_right(thresholds,p-h)+bisect_right(thresholds,p-h-1)
        n=p-h; limit=S-h
        widths=sorted({max(1,j*limit//24) for j in range(1,25)}|{2**j for j in range(limit.bit_length())})
        points=sorted({1,limit}|{x for s in widths for x in (s,s+1) if x<=limit}|{j*b-h for j in range(201) if 1<=j*b-h<=limit})
        B=[bal(2*(n+s),(s+1)*count) for s in widths]
        matrix=[[max(0,s+1-d) for s in widths] for d in points]
        bound=[float(F(weight(h+d),a0)) for d in points]
        scale=max(F(x,s) for x,s in zip(B,widths))
        scaled_matrix=[[x/s for x,s in zip(row,widths)] for row in matrix]
        lp=linprog([-float(F(x,s)/scale) for x,s in zip(B,widths)],A_ub=scaled_matrix,b_ub=bound,bounds=(0,None),method='highs',options={'threads':1})
        assert lp.success, lp.message
        D=10**18; nums=[max(0,math.floor(float(x)*D/s)) for x,s in zip(lp.x,widths)]
        factor=F(1)
        for d,row in zip(points,matrix):
            lhs=sum(x*y for x,y in zip(nums,row))
            if lhs:factor=min(factor,F(weight(h+d)*D,a0*lhs))
        nums=[x*factor.numerator for x in nums];D*=factor.denominator
        div=math.gcd(D,math.gcd(*nums));D//=div;nums=[x//div for x in nums]
        objective=F(sum(x*y for x,y in zip(nums,B)),D)
        one=[min(F(weight(h+d),a0*(s+1-d)) for d in points if d<=s) for s in widths]
        best=max(range(len(widths)),key=lambda i:one[i]*B[i])
        single=one[best]*B[best]
        selected='optimized rational dual'
        if objective<single:
            nums=[0]*len(widths);nums[best]=one[best].numerator;D=one[best].denominator
            objective=single;selected='exact single-width fallback'
        rows.append(dict(h=h,hypothetical_r=count,widths=widths,numerators=nums,denominator=str(D),
            demand=str(objective),best_single_width_demand=str(single),ratio=str(objective/single),
            approximate_ratio=float(objective/single),checked_breakpoints=len(points),selected=selected))
    short_demand=0;hypothetical_budget=0;profile_runs=[]
    for h in range(1,S+1):
        count=9198+bisect_right(thresholds,p-h)+bisect_right(thresholds,p-h-1)
        if not profile_runs or profile_runs[-1][2]!=count:profile_runs.append([h,h,count])
        else:profile_runs[-1][1]=h
        root=math.isqrt(h);root+=int(root*root<h)
        hypothetical_budget+=2*root*count
        s=S-h
        if s:
            short_demand+=(bal(2*(p-h+s),(s+1)*count)+s-1)//s
    gate=dict(status='HYPOTHETICAL; NOT A SOURCE OR A NEW CAP',target_weights='1 for 1<=t<=support, zero otherwise',
        hypothesis='r_h equals staggered profile on support; m_t <= 2*ceil(sqrt(t))',
        proved_demand_formula_value=short_demand,hypothetical_request_budget=hypothetical_budget,
        demand_over_budget=str(F(short_demand,hypothetical_budget)),excludes_profile=short_demand>hypothetical_budget)
    result=dict(status='EXACT DUALS; SATURATED PROFILE IS HYPOTHETICAL',positions=p,old_binary_cap=K,
        dilation=b,support=S,normalization=str(a0),coarse_correlations=r,rows=rows)
    result['rectangular_gate']=gate
    result['hypothetical_profile_runs']=profile_runs
    (ROOT/'demand_certificates.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('positions','old_binary_cap','dilation','support')},indent=2))
    print([(x['h'],x['approximate_ratio']) for x in rows])

if __name__=='__main__':main()
