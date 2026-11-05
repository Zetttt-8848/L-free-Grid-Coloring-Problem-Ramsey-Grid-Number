"""R2-P5a-v2. Exact finite arithmetic, not a grid-feasibility claim."""
from pathlib import Path
import json

out=[]
for s in range(13):
    triples=[(a,b,s-a-b) for a in range(s+1) for b in range(s-a+1)]
    q,r=divmod(s,3)
    expected2=3*q*q+r*(2*q+1)
    expected4=(3-r)*q**4+r*(q+1)**4
    assert min(sum(x*x for x in v) for v in triples)==expected2
    assert min(sum(x**4 for x in v) for v in triples)==expected4
    out.append([s,expected2,expected4])
w=[min(i,94-i) for i in range(1,94)]
n=464
W=[0]*(n+len(w)-1)
for x in range(n):
    for j,v in enumerate(w):
        W[x+j]+=v
imbalance=sum(2 if v%3 else 0 for v in W)
result={'label':'PROVED finite arithmetic','integer_moments_s0to12':out,
 'n':n,'weights':'min(i,94-i),1<=i<=93','pointwise_slack':imbalance,
 'nonzero_windows':sum(v%3!=0 for v in W),
 'tent_score_deficit':1557434,
 'maximum_improvement_supplied_by_pointwise_integer_minimum':{'numerator':imbalance,'denominator':2}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
