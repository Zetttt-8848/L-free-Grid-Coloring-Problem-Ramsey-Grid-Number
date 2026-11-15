"""Standard-library checks independent of SAT and linear optimization."""
import itertools,json,math
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

ROOT=Path(__file__).parent

def witness():
    w=json.loads((ROOT/'translated_probe.json').read_text())
    A=set(w['A']);z={(x,y):e for x,y,e in w['colors']}
    assert set(z)=={(x,y) for x in A for y in A if y<x}
    assert set(z.values())<={0,1}
    total=0
    for x,y in z:
        for d in range(1,max(A)-x+1):
            if (x+d,y) in z and (x+d,y+d) in z:
                assert len({z[x,y],z[x+d,y],z[x+d,y+d]})>1
                total+=1
    H={h for h in range(1,w['T']) if z.get((h,0))==0 and z.get((w['T'],w['T']-h))==0}
    assert {11,12,14,15}<=H
    low=sorted(h for h in H if 2*h<w['T'])
    diffs=[b-a for a,b in itertools.combinations(low,2)]
    assert len(diffs)>len(set(diffs))
    return dict(marks=len(A),cells=len(z),physical_Ls=total,actual_requests=sorted(H),lower_half=low)

def finite():
    words=0;checks=0
    for n in range(1,9):
        for word in itertools.product((-1,0,1),repeat=n):
            words+=1;r=sum(x>=0 for x in word)
            for s in range(1,n+1):
                m=2*(n+s);q,a=divmod((s+1)*r,m)
                lower=m*q*(q-1)//2+a*q
                actual=sum(s+1-(j-i) for i in range(n) for j in range(i+1,min(n,i+s+1)) if word[i]>=0 and word[i]==word[j])
                assert lower<=actual
                checks+=1
    return dict(words=words,width_checks=checks,max_positions=8)

def duals():
    data=json.loads((ROOT/'demand_certificates.json').read_text());results=[]
    r=data['coarse_correlations'];b=data['dilation'];a0=int(data['normalization'])
    for row in data['rows']:
        widths=row['widths'];nums=row['numerators'];D=int(row['denominator']);h=row['h']
        assert D>0 and all(x>=0 for x in nums)
        limit=max(widths);lhs=sum(x*s for x,s in zip(nums,widths));slope=sum(nums)
        endings=Counter()
        for s,x in zip(widths,nums):endings[s]+=x
        for delta in range(1,limit+1):
            j,u=divmod(h+delta,b)
            weight=(b-u)*r[j]+u*(r[j+1] if j+1<len(r) else 0)
            assert lhs*a0<=weight*D,(h,delta)
            lhs-=slope;slope-=endings[delta]
        assert lhs==slope==0
        numerator=0
        for s,x in zip(widths,nums):
            m=2*(data['positions']-h+s);q,a=divmod((s+1)*row['hypothetical_r'],m)
            numerator+=x*(m*q*(q-1)//2+a*q)
        assert F(numerator,D)==F(row['demand'])
        results.append(dict(h=h,every_integer_constraint_checked=limit,positive_widths=sum(x>0 for x in nums)))
    return results

def gate():
    data=json.loads((ROOT/'demand_certificates.json').read_text());p=data['positions'];S=data['support']
    previous=0;demand=0;budget=0
    for lo,hi,r in data['hypothetical_profile_runs']:
        assert lo==previous+1 and hi>=lo
        for h in range(lo,hi+1):
            cap=math.isqrt(4*h)
            if cap*cap<4*h:cap+=1
            # The author's chosen upper scenario uses 2*ceil(sqrt(h)).
            cap+=cap%2
            budget+=cap*r;s=S-h
            if s:
                slots=2*(p-h+s);N=(s+1)*r;q=N//slots;a=N%slots
                lower=slots*q*(q-1)//2+a*q
                demand+=(lower+s-1)//s
        previous=hi
    assert previous==S
    g=data['rectangular_gate']
    assert demand==g['proved_demand_formula_value'] and budget==g['hypothetical_request_budget']
    assert F(demand,budget)==F(g['demand_over_budget'])
    return dict(demand=demand,hypothetical_budget=budget,profile_provenance='supplied profile; capacity derivation not independently reimplemented')

if __name__=='__main__':
    out=dict(witness=witness(),finite_sliding_window=finite(),exact_duals=duals(),rectangular_gate=gate())
    (ROOT/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
