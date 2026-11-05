"""Exploratory numerical search, followed by integer-only certificate checking.

No floating spectral result itself proves a Ramsey bound.
"""
import json
import numpy as np
from scipy.linalg import eigh, toeplitz
from shifted_sets_scan import cap

def exact_score(n,w):
    aa=[sum(w[i]*w[i+d] for i in range(len(w)-d)) for d in range(len(w))]
    return sum((n-d-9*cap(n,d))*aa[d] for d in range(1,len(w)))-n*aa[0]

def search(n,t):
    mat=toeplitz([-n]+[(n-d-9*cap(n,d))/2 for d in range(1,t)])
    vals,vecs=eigh(mat,subset_by_index=[t-1,t-1])
    v=vecs[:,0]
    if v.sum()<0:v=-v
    # Negative correlations invalidate the simple cap substitution.
    if min(v)<-1e-9:return None
    w=list(map(int,np.rint(1000*v/max(v))))
    return {'n':n,'t':t,'eigenvalue':float(vals[-1]),'exact_score':exact_score(n,w),'weights':w}

if __name__=='__main__':
    found=[]
    for n in range(400,467):
        best=None
        for t in range(20,151,2):
            rec=search(n,t)
            if rec and (best is None or rec['exact_score']>best['exact_score']):best=rec
        if best and best['exact_score']>0:
            found.append(best)
            break
    print(json.dumps(found,indent=2))
