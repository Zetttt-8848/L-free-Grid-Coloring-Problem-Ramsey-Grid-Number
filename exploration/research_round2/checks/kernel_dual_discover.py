"""K1 numerical discovery only; exact verification is a separate program."""
from pathlib import Path
from bisect import bisect_right
import json
import numpy as np
from scipy.optimize import linprog

H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,
   217,247,284,334,357,373,426,481,493,554,586]
n=464
D=463
theta=np.linspace(0,np.pi,4096)
c=np.array([n-d-18*(bisect_right(H,n-d)-1) for d in range(1,D+1)])
mat=2*np.cos(np.outer(np.arange(1,D+1),theta))
res=linprog(np.ones(len(theta)),A_ub=mat,b_ub=-c-0.01,
            bounds=(0,None),method='highs')
out={'label':'UNVERIFIED LP discovery','n':n,'degree':D,'status':res.status,
     'coefficient_margin':'1/100','mesh_points':len(theta)}
if res.success:
    ix=np.flatnonzero(res.x>1e-9)
    out.update(objective=float(res.fun),nodes=[{'mesh_index':int(i),
        'x':float(np.cos(theta[i])),'lambda':float(res.x[i])} for i in ix],
        maximum_residual=float(max(mat@res.x+c)))
Path(__file__).with_name('kernel_dual_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='nodes'}))
print('nonzero_nodes',len(out.get('nodes',[])))
