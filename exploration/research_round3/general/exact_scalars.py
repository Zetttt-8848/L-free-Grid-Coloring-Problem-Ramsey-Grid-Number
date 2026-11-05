"""Exact scalar claims only; universal proofs are separate mathematical inputs."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
OUT=Path(__file__).parent
gaps_old=[F(59,40)**2-F(17,8),F(87,40)**2-F(9,2),F(119,40)**2-F(44,5)]
assert gaps_old==[F(81,1600),F(369,1600),F(81,1600)]
c={1:F(1),2:F(101,100),3:F(57,40),4:F(207,100),5:F(72,25),6:F(19,5),7:F(24,5)}
gaps=[(c[q]-F(1,1000))**2-(q-1)*c[q-1] for q in range(3,8)]
assert all(g>0 for g in gaps)
rows=[]
for k in range(6,13):
    b=k*(k-2)-1;N=b**(2**(k-1));t=2*k*b*b
    cc=c[k-1] if k-1<=7 else F(k-3)-F(1,k-3)
    delta=1-F(k*k*(k-1),b*b)*cc
    margin=delta*N*(t-1)-F(t*t-1,3)-(k-1)*N
    assert delta>=F(1,b*b) and t<=N and margin>0
    rows.append({'k':k,'b':b,'N':str(N),'t':t,'delta':str(delta),'margin':str(margin)})
old=json.loads((OUT/'minus_one_exact.json').read_text())
assert old['scalar_checks']==rows
assert [str(g) for g in gaps]==[x['squared_gap'] for x in old['coefficient_checks']]
first=json.loads((OUT/'exact_candidate.json').read_text())
assert first['N5']==15**16 and first['N6']==24**32
assert F(first['normalized_margin5'])==F(1,45)*15**16*449-F(450**2-1,3)-4*15**16
barrier=json.loads((OUT/'golomb_barrier_exact.json').read_text())
for row in barrier['rows']:
    p=row['p'];S=[2*p*i+i*i%p for i in range(p)]
    assert S==row['S'] and S[-1]<2*p*p
    differences=[y-x for x,y in combinations(S,2)]
    assert len(differences)==len(set(differences))==row['positive_differences']
    assert row['cells']==p*(p+1)//2 and row['corners']==p*(p-1)//2
result={'status':'PASS','old_squared_gaps':list(map(str,gaps_old)),'new_squared_gaps':list(map(str,gaps)),'scalar_k_range':[6,12],'golomb_primes':[x['p'] for x in barrier['rows']],'N5':str(15**16),'N6_new':str(23**32),'k6_margin':rows[0]['margin'],'universal_proof_not_replaced_by_finite_checks':True}
(OUT/'scalar_reproduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
