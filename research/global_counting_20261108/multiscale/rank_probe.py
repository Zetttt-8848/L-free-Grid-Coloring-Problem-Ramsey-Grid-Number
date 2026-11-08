"""Floating rank-distance transport on six disjoint Golomb classes.

No LP status is a mathematical certificate. Tests a relaxation only.
"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

# Occupied-position values already recorded in the parent package.
G=[0,0,1,3,6,11,17,25,34,44,55,72,85,106,127,151,177,199,216,246,283,333,356,372,425,480]

def run(p,m=24,q=6):
    pairs=[]
    for j in range(1,m):
        for r in range(m-j):
            lower=G[j+1]
            upper=p-1-G[r+1]-G[m-r-j]
            for d in range(lower,upper+1):pairs.append((r,j,d))
    nr=m*(m-1)//2
    key={(r,j):i for i,(r,j) in enumerate((r,j) for j in range(1,m) for r in range(m-j))}
    er=[];ec=[];ev=[];ur=[];uc=[];uv=[]
    for i,(r,j,d) in enumerate(pairs):
        er.append(key[r,j]);ec.append(i);ev.append(1)
        ur.extend([d-1,p-1+j-1]);uc.extend([i,i]);uv.extend([1,d])
    ae=coo_matrix((ev,(er,ec)),shape=(nr,len(pairs))).tocsr()
    au=coo_matrix((uv,(ur,uc)),shape=(p-1+m-1,len(pairs))).tocsr()
    upper=[q]*(p-1)+[q*min(j,m-j)*(p-q*min(j,m-j)) for j in range(1,m)]
    res=linprog(np.zeros(len(pairs)),A_eq=ae,b_eq=[q]*nr,A_ub=au,b_ub=upper,bounds=(0,None),method='highs')
    out={'positions':p,'classes':q,'class_size':m,'variables':len(pairs),'status':int(res.status),'message':res.message,'scope':'floating relaxation only; no theorem from feasibility/infeasibility'}
    print(json.dumps(out),flush=True)
    return out

if __name__=='__main__':
    rows=[run(p) for p in [425,426,430,431,435,440,450,460,463]]
    Path(__file__).with_name('rank_probe.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
