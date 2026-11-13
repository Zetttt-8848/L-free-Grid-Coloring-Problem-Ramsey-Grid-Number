"""Bounded discovery scan; floating eigenvectors are not proof certificates."""
from bisect import bisect_right
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, toeplitz

HERE = Path(__file__).resolve().parent
POSITIONS = (0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481)

def g(p):
    return bisect_right(POSITIONS, max(0, p))-1

def caps(n):
    return [min(n-d, sum(g(n-d-j) for j in range(6))) for d in range(1,n)]

def run():
    results=[]
    for n in (400,420,440,450,455,460,461,462,463,464):
        u=caps(n)
        rows=[]
        for length in sorted(set(list(range(40,161,5))+list(range(180,n+1,20))+[n])):
            mat=toeplitz(np.r_[-n,[(n-d-3*u[d-1])/2 for d in range(1,length)]])
            vals,vecs=eigh(mat,subset_by_index=[length-1,length-1])
            w=np.abs(vecs[:,0])
            rows.append({'length':length,'absolute_vector_score':float(w@mat@w),
                         'unconstrained_top_eigenvalue':float(vals[0])})
        results.append({'n':n,'best':max(rows,key=lambda x:x['absolute_vector_score']),'rows':rows})
    out={'status':'FLOATING_DISCOVERY_ONLY','method':'all six disjoint minima at every tabulated threshold',
         'inputs':'POSITIONS external table in prior numerical provenance; no fresh Golomb exhaustive checks',
         'non_claim':'A negative score is not an impossibility theorem for other weights or methods.',
         'results':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'threshold_scan.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps([{'n':r['n'],**r['best']} for r in results]))

if __name__=='__main__':
    run()
