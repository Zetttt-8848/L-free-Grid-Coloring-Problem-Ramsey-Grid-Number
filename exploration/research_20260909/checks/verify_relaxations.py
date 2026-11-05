"""Reproduce the specified one-color benchmark and two exact refinements."""
from bisect import bisect_right
from pathlib import Path
import json

H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,
   217,247,284,334,357,373,426,481,493,554,586]


def mass(n,c):
    m=(n+2)//3
    remaining=c*m-c*(c+1)//2
    lower=0
    for d in range(1,n):
        cap=2*(bisect_right(H,n-d)-1)
        used=min(remaining,cap)
        lower+=d*used
        remaining-=used
        if not remaining:
            return lower, sum(j*(n-j) for j in range(1,c+1))
    raise ValueError('Insufficient cap capacity')


def main():
    first=None
    for n in range(100,494):
        for c in range(1,min(49,(n+2)//3-1)+1):
            lo,hi=mass(n,c)
            if lo>hi:
                first=n
                break
        if first is not None:break
    assert first==493
    assert mass(493,13)==(44102,44044)
    lo,hi=mass(490,13)
    correction=2*sum((14-i)*((i-1)//5) for i in range(1,14))
    assert (lo,hi,correction,lo-(hi-correction))==(43735,43771,84,48)
    def b(s):
        q,r=divmod(s,3)
        return 3*q*q+r*(2*q+1)
    lower466=399*b(68)+2*sum(b(s) for s in range(1,68))
    upper466=466*68+12*(24*sum(68-d for d in range(1,41))
                              +23*sum(68-d for d in range(41,68)))
    assert (lower466,upper466)==(683658,683216)
    out=dict(table=H,benchmark_scan={'n':[100,493],'c':'1..min(49,ceil(n/3)-1)',
            'first_contradiction':first,'n493_c13':[44102,44044]},
            structural490={'lower':lo,'upper':hi-correction,'gap':48},
            unweighted466={'lower':lower466,'upper':upper466,'gap':442})
    Path(__file__).with_name('relaxations_result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
