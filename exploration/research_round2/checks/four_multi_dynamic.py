"""Dynamic span capacities and exact optimization over unit windows."""
from four_multi_certify import capacity
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def coefficients(n,max_t,cq=62,c=662):
    for d in range(1,max_t):
        length=n-d-1
        q=capacity(length,1,cq)
        k=capacity(length,2*q,c)
        yield d,n-d-48*k,q,k

def optimize(n,max_t=100000,cq=62,c=662):
    total=moment=0
    best=(-3*n,1)
    for d,coeff,q,k in coefficients(n,max_t,cq,c):
        total+=coeff
        moment+=d*coeff
        t=d+1
        margin=2*(t*total-moment)-3*n*t
        best=max(best,(margin,t))
    return dict(n=n,doubled_margin=best[0],t=best[1],cq=cq,c=c,max_t=max_t)

def main():
    scan=[]
    first=None
    for n in range(21980000,22008001,1000):
        rec=optimize(n)
        scan.append(rec)
        if rec['doubled_margin']>0:
            first=rec
            break
    out=dict(scan=scan,first=first,range=[21980000,22008000,1000])
    (ROOT/'certificates'/'four_multi_dynamic_windows.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
