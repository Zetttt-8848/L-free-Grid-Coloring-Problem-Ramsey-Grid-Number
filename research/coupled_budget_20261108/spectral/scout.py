"""Discover integer autocorrelation cuts; floating LP statuses are not proofs."""
import argparse
import hashlib
import json
import math
import time
from bisect import bisect_right
from pathlib import Path
import numpy as np
from scipy.linalg import toeplitz, eigh
from scipy.optimize import linprog

G=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)


def water(caps, mass):
    lo,hi=0,max(caps)
    while lo<hi:
        mid=(lo+hi+1)//2
        if sum(min(mid,c) for c in caps)<=mass: lo=mid
        else: hi=mid-1
    vals=[min(lo,c) for c in caps]
    return sum(v*v for v in vals)+(mass-sum(vals))*(2*lo+1)


def run(n,seconds):
    started=time.monotonic();m=(n+2)//3
    caps=[min(m,n-h,2*(bisect_right(G,n-h)-1)) for h in range(1,n)]
    rows=[];rhs=[]
    for t in range(2,n+1):
        cap=[min(t,x+1,n+t-1-x,m) for x in range(n+t-1)]
        lower=water(cap,m*t)
        rows.append([-2*(t-h) if h<t else 0 for h in range(1,n)])
        rhs.append(m*t-lower)
    cuts=[];history=[];last=None
    while time.monotonic()-started<seconds:
        lp=linprog(np.zeros(n-1),A_ub=np.array(rows,dtype=float),b_ub=np.array(rhs,dtype=float),
                   A_eq=np.ones((1,n-1)),b_eq=[m*(m-1)//2],bounds=[(0,c) for c in caps],method='highs',options={'time_limit':max(1,seconds-(time.monotonic()-started))})
        if not lp.success:
            history.append({'lp_status':lp.status,'message':lp.message});break
        r=lp.x;last=r.tolist()
        values,vectors=eigh(toeplitz(np.r_[m,r]),subset_by_index=[0,min(7,n-1)])
        history.append({'cut_count':len(cuts),'min_eigenvalue':float(values[0])})
        if values[0]>=-1e-7: break
        added=0
        for val,v in zip(values,vectors.T):
            if val>=-1e-7: continue
            z=np.rint(v/np.max(np.abs(v))*1000).astype(np.int64).tolist()
            gcd=math.gcd(*z);z=[a//gcd for a in z]
            c=[sum(z[i]*z[i+h] for i in range(n-h)) for h in range(1,n)]
            bound=m*sum(a*a for a in z)
            if bound+2*sum(a*b for a,b in zip(c,r)) >=-1e-5: continue
            row=[-2*a for a in c]
            scale=max(abs(a) for a in row)
            rows.append([a/scale for a in row]);rhs.append(bound/scale)
            cuts.append(z);added+=1
        if not added: break
    return {'n':n,'m':m,'status':'SCOUT_ONLY','elapsed_seconds':time.monotonic()-started,
            'history':history,'integer_cut_vectors':cuts,'last_relaxed_profile':last,
            'non_claim':'No global coloring or nonexistence certificate follows from floating LP status.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=492);p.add_argument('--seconds',type=float,default=90);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    result=run(args.n,args.seconds)
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('integer_cut_vectors','last_relaxed_profile')}))
