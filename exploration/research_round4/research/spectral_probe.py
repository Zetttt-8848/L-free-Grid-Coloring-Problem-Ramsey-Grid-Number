"""Exploratory floating eigenvalues; not proof evidence for any upper bound."""
import json
import numpy as np
from pathlib import Path

def probe(A):
    A=sorted(A); aset=set(A)
    cells=[(v,u) for v in A for u in A if u<v]
    ix={q:i for i,q in enumerate(cells)}
    M=len(cells)
    K=np.zeros((M,M))
    ds=sorted({v-u for v,u in cells})
    F=np.array([[int(v-u==d) for v,u in cells] for d in ds],dtype=float)
    for i,(v,u) in enumerate(cells):
        for a in A:
            d=a-u
            if 0<d<v-u and v-d in aset:
                K[i,ix[(u+d,u)]]+=0.5
                K[i,ix[(v,v-d)]]+=0.5
    Q=F.T@F+2*(K+K.T)
    rs=F.sum(axis=1)
    threshold=2-float(rs@rs)/M
    least=float(np.linalg.eigvalsh(Q)[0])
    return dict(A=A,cells=M,threshold=threshold,least_eigenvalue=least,
                exploratory_margin=least-threshold)

cases=[list(range(m)) for m in range(4,13)]
cases += [[1,2,3,5,10,11,12,13,14], [0,1,3,4,9,10,12,13]]
result={"purpose":"route discrimination; floating values are not certificates",
        "cases":[probe(A) for A in cases]}
out=Path(__file__).with_name('spectral_probe.json')
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
