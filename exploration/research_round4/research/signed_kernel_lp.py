"""Discovery of a two-sided Fourier envelope for all real weight vectors."""
import argparse,bisect,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parent
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
parser=argparse.ArgumentParser();parser.add_argument('--nodes',type=int,default=1001);args=parser.parse_args()
n=464;d=np.arange(1,n);theta=np.linspace(0,np.pi,args.nodes)
C=2*np.cos(d[:,None]*theta[None,:])
cap=np.array([min(6*(bisect.bisect_right(H,n-int(h))-1),n-int(h)) for h in d])
lo=n-d-3*cap;hi=n-d
start=time.monotonic()
margin=0.001
sol=linprog(np.ones(len(theta)),A_ub=np.vstack([C,-C]),b_ub=np.r_[-lo-margin,hi-margin],
            bounds=(0,None),method='highs-ipm',options={'time_limit':30})
out=dict(n=n,theta_count=len(theta),required_coefficient_margin=margin,status=int(sol.status),message=sol.message,seconds=time.monotonic()-start)
if sol.success:
    chosen=np.flatnonzero(sol.x>1e-9)
    out.update(mass=float(sol.fun),score_upper=float(sol.fun-n),
               nodes=[[float(np.cos(theta[j])),float(sol.x[j])] for j in chosen],
               max_float_violation=float(max(np.max(C@sol.x+lo),np.max(-C@sol.x-hi))))
(root/f'signed_kernel_lp_{args.nodes}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='nodes'}))
