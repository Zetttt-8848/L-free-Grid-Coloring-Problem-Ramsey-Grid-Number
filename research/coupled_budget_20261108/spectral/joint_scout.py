"""Joint centered autocorrelation SDP outer approximation; discovery only."""
import argparse, hashlib, json, math, time
from pathlib import Path
import numpy as np
from scipy.linalg import toeplitz,eigh
from scipy.optimize import linprog


def run(n,seconds):
    start=time.monotonic()
    # Only the externally established Golomb span lower bounds 425 and480.
    caps=[min(n-h,144 if n-h-1>=425 else 138) for h in range(1,n)]
    rows=[];rhs=[]
    for t in range(2,n+1):
        total=[min(t,x+1,n+t-1-x,n) for x in range(n+t-1)]
        lower=sum((3-r)*q*q+r*(q+1)*(q+1) for q,r in (divmod(v,3) for v in total))
        rows.append([-2*(t-h) if h<t else 0 for h in range(1,n)])
        rhs.append(n*t-lower)
    q,r=divmod(n,3)
    min_pairs=(3-r)*q*(q-1)//2+r*q*(q+1)//2
    rows.append([-1]*(n-1));rhs.append(-min_pairs)
    cuts=[];hist=[];last=None
    while time.monotonic()-start<seconds:
        lp=linprog(np.zeros(n-1),A_ub=rows,b_ub=rhs,bounds=[(0,c) for c in caps],method='highs',options={'time_limit':max(1,seconds-(time.monotonic()-start))})
        if not lp.success:
            hist.append({'status':lp.status,'message':lp.message});break
        R=lp.x;last=R.tolist()
        centered=np.r_[2*n,[3*R[h-1]-(n-h) for h in range(1,n)]]
        vals,vecs=eigh(toeplitz(centered),subset_by_index=[0,7])
        hist.append({'cuts':len(cuts),'minimum_eigenvalue':float(vals[0])})
        if vals[0]>=-1e-7:break
        added=0
        for val,v in zip(vals,vecs.T):
            if val>=-1e-7:continue
            z=np.rint(v/np.max(np.abs(v))*1000).astype(np.int64).tolist()
            g=math.gcd(*z);z=[v//g for v in z]
            a=[sum(z[i]*z[i+h] for i in range(n-h)) for h in range(1,n)]
            b=2*n*sum(v*v for v in z)-2*sum((n-h)*a[h-1] for h in range(1,n))
            row=[-6*v for v in a]
            if sum(x*y for x,y in zip(row,R))<=b+1e-4:continue
            scale=max(abs(v) for v in row)
            rows.append([v/scale for v in row]);rhs.append(b/scale);cuts.append(z);added+=1
        if not added:break
    return {'n':n,'status':'UNDECIDED_FLOATING_SCOUT','elapsed_seconds':time.monotonic()-start,'history':hist,'integer_cut_vectors':cuts,'last_relaxed_profile':last,'non_claim':'Neither a feasible diagonal word nor an exact infeasibility certificate is claimed.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=464);p.add_argument('--seconds',type=float,default=120);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=run(a.n,a.seconds);result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('integer_cut_vectors','last_relaxed_profile','history')}));print(result['history'][-1])
