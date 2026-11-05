"""Produce the compressed final four-color certificate from exact cap rules."""
from pathlib import Path
from four_multi_certify import capacity
import json

ROOT=Path(__file__).resolve().parents[1]
N,T,CQ,C=22007053,28443,62,662

def main():
    runs=[]
    direct=0
    for d in range(1,T):
        length=N-d-1
        q=capacity(length,1,CQ)
        k=capacity(length,2*q,C)
        direct+=2*(N-d-48*k)*(T-d)
        if runs and (q,k)==(runs[-1]['q'],runs[-1]['K']):
            runs[-1]['hi']=d
        else:
            runs.append(dict(lo=d,hi=d,q=q,K=k))
    out=dict(statement='R_4(L) <= 22007053',corner='(x,y),(x+d,y),(x+d,y+d), d>0',
             n=N,t=T,golomb_neighbor_parameter=CQ,capacity_neighbor_parameter=C,
             weights='t consecutive unit weights',runs=runs,
             doubled_lhs=direct,doubled_rhs=3*N*T,doubled_margin=direct-3*N*T)
    assert out['doubled_margin']>0
    path=ROOT/'certificates'/'four_multi_final.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='runs'}|dict(run_count=len(runs)),indent=2))

if __name__=='__main__':main()
