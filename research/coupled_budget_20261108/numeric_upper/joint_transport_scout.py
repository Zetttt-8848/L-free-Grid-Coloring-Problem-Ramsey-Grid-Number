"""Floating-point discovery only; saved duals are not proof certificates."""
from capacities import difference_cap
import numpy as np,json
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from pathlib import Path

def solve(n,c):
 xs=[(j,d) for j in range(1,c+1) for d in range(j,n)];L=len(xs)
 er=[];ec=[];ev=[];ur=[];uc=[];uv=[]
 for ix,(j,d) in enumerate(xs):
  er.append(j-1);ec.append(ix);ev.append(1)
  ur.extend([d-1,n-1+j-1]);uc.extend([ix,ix]);uv.extend([1,d])
 for j in range(1,c+1):ur.append(n-1+j-1);uc.append(L);uv.append(-j)
 ae=coo_matrix((ev,(er,ec)),shape=(c,L+1)).tocsr();au=coo_matrix((uv,(ur,uc)),shape=(n-1+c,L+1)).tocsr()
 b=[3*difference_cap(n,d) for d in range(1,n)]+[3*j*(n-3*j) for j in range(1,c+1)]
 obj=np.zeros(L+1);obj[-1]=1
 r=linprog(obj,A_ub=au,b_ub=b,A_eq=ae,b_eq=[n-3*j for j in range(1,c+1)],bounds=[(0,None)]*L+[(None,None)],method='highs')
 print(n,c,r.status,r.fun,flush=True)
 if r.success:
  Path(f'joint_lp_{n}_{c}.json').write_text(json.dumps({'n':n,'c':c,'fun':r.fun,'dual_ineq':r.ineqlin.marginals.tolist(),'dual_eq':r.eqlin.marginals.tolist()}))
for n in [466,465,464,463,462,460]:solve(n,40)
