"""Exact unit weights with shorter remaining span in every difference cap."""
from four_multi_certify import capacity
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def score(n,t=28000,v=9522,c=662):
    caps=[capacity(n-d-1,v,c) for d in range(1,t)]
    weighted=sum((n-d-48*k)*(t-d) for d,k in enumerate(caps,1))
    return dict(n=n,t=t,V=v,c=c,q_reference_n=22021611,
                doubled_weighted_lhs=2*weighted,doubled_weighted_rhs=3*n*t,
                doubled_margin=2*weighted-3*n*t,
                min_K=min(caps),max_K=max(caps))

def main():
    scan=[score(n) for n in range(22000000,22021612,1000)]
    out=dict(scan_range=[22000000,22021611,1000],scan=scan)
    (ROOT/'certificates'/'four_multi_length_scan.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
