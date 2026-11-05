"""Exact-int64 bounded search; candidates verified separately by Python ints."""
import json
from pathlib import Path
import numpy as np
from four_multi_certify import capacity
from four_multi_dynamic import optimize

ROOT=Path(__file__).resolve().parents[1]
LOW,HIGH,TMAX=22007000,22008000,100000
LMIN=LOW-TMAX

def main():
    profile=[]
    for length in range(LMIN,HIGH):
        q=capacity(length,1,62)
        k=capacity(length,2*q,662)
        profile.append(length+1-48*k)
    prof=np.array(profile,dtype=np.int64)
    d=np.arange(1,TMAX,dtype=np.int64)
    t=d+1
    # All intermediate sums are strictly below 2^63 in absolute value.
    arithmetic_bound=2*TMAX*TMAX*int(np.max(np.abs(prof)))+3*HIGH*TMAX
    assert arithmetic_bound < 2**63
    first=None
    best_negative=None
    for n in range(LOW,HIGH+1):
        co=prof[n-2-LMIN-np.arange(TMAX-1)]
        margins=2*(t*np.cumsum(co)-np.cumsum(d*co))-3*n*t
        ix=int(np.argmax(margins))
        rec=dict(n=n,t=int(t[ix]),doubled_margin=int(margins[ix]))
        if rec['doubled_margin']>0:
            first=rec
            break
        best_negative=rec
    assert first is not None
    direct=optimize(first['n'])
    assert first['t']==direct['t'] and first['doubled_margin']==direct['doubled_margin']
    out=dict(search_n=[LOW,HIGH],search_t=[2,TMAX],arithmetic_bound=arithmetic_bound,
             first=first,preceding=best_negative,independent_integer_prefix=direct)
    (ROOT/'certificates'/'four_multi_refined_windows.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
