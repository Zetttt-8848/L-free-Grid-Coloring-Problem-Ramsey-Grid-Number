"""Floating-point discovery only; no rational LP certificate is asserted."""
from bisect import bisect_right
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from time import perf_counter
G=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
def cap(n,h):return 2*(bisect_right(G,n-h)-1)
def solve(n,c):
 m=(n+2)//3;xs=[(j,d) for j in range(1,c+1) for d in range(j,n-m+j+1)];L=len(xs)
 er=[];ec=[];ev=[];ur=[];uc=[];uv=[]
 for ix,(j,d) in enumerate(xs):
  er.append(j-1);ec.append(ix);ev.append(1)
  ur.extend([d-1,n-1+j-1]);uc.extend([ix,ix]);uv.extend([1,d])
 for j in range(1,c+1):ur.append(n-1+j-1);uc.append(L);uv.append(-j)
 ae=coo_matrix((ev,(er,ec)),shape=(c,L+1)).tocsr()
 au=coo_matrix((uv,(ur,uc)),shape=(n-1+c,L+1)).tocsr()
 b=[cap(n,d) for d in range(1,n)]+[min(j,m-j)*(n-min(j,m-j)) for j in range(1,c+1)]
 obj=np.zeros(L+1);obj[-1]=1
 r=linprog(obj,A_ub=au,b_ub=b,A_eq=ae,b_eq=[m-j for j in range(1,c+1)],bounds=[(0,None)]*L+[(None,None)],method='highs')
 print(n,c,r.status,r.fun,flush=True)
 if r.success and r.fun>0:
  import json,pathlib
  pathlib.Path(__file__).with_name('lp_candidate.json').write_text(json.dumps({'n':n,'c':c,'fun':r.fun,'dual_ineq':r.ineqlin.marginals.tolist(),'dual_eq':r.eqlin.marginals.tolist()}))
for n in [493,492,490,487,481,475]:
 for c in [(n+2)//3-1]:solve(n,c)
