"""Retained weight-discovery scans; exact certificate.py is independent."""
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, toeplitz

HERE=Path(__file__).resolve().parent
G=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)


def gap(n,w,caps):
    a=[sum(w[i]*w[i+d] for i in range(len(w)-d)) for d in range(len(w))]
    return sum((n-d-3*caps[d-1])*a[d] for d in range(1,len(w)))-n*a[0]


def main():
    spectral=[]
    for n in range(460,466):
        caps=[min(n-d,6*(bisect_right(G,n-d)-1),138+min(6,max(0,n-d-425))) for d in range(1,n)]
        best=None
        for length in range(50,121):
            mat=toeplitz(np.r_[-n,[(n-d-3*caps[d-1])/2 for d in range(1,length)]])
            vals,vecs=eigh(mat,subset_by_index=[length-1,length-1])
            w=np.abs(vecs[:,0]);score=float(w@mat@w)
            if best is None or score>best['score']:
                best={'n':n,'length':length,'score':score,'status':'FLOATING_DISCOVERY'}
        spectral.append(best)
    families=[];n=464
    caps=[min(n-d,138+min(6,max(0,n-d-425))) for d in range(1,n)]
    for family in ('tent','parabola','shiftparabola'):
        best=None
        for length in range(60,111):
            for q in (range(11) if family=='shiftparabola' else (0,)):
                if family=='tent':w=[min(i,length+1-i) for i in range(1,length+1)]
                elif family=='parabola':w=[i*(length+1-i) for i in range(1,length+1)]
                else:w=[max(0,10*i*(length+1-i)-q*length) for i in range(1,length+1)]
                g=gap(n,w,caps);den=sum(v*v for v in w);score=Fraction(g,den)
                if best is None or score>Fraction(best['gap'],best['a0']):
                    best={'family':family,'length':length,'q':q,'gap':g,'a0':den}
        families.append(best)
    output={'spectral_range':{'n':[460,465],'length':[50,120]},'spectral':spectral,
            'family_range':{'n':464,'length':[60,110],'shift_q':[0,10]},'families':families,
            'non_claim':'No optimality claim outside these finite families; floating rows are discovery only.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'kernel_scan.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(families))


if __name__=='__main__':main()
