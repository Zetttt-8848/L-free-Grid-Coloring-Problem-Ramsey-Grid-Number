"""Independent K1 verification using integers only; no numerical solver.

For x=X/Q, represent T_d(x)=P_d/Q^d. Recurrence:
P_0=1,P_1=X,P_(d+1)=2X P_d-Q^2 P_(d-1).
Every stated inequality is checked after clearing its positive denominator.
"""
from pathlib import Path
from bisect import bisect_right
from hashlib import sha256
from fractions import Fraction
import json

src=Path('research_round2/certificates/kernel_dual_464.json')
data=json.loads(src.read_text())
Q,R=data['node_denominator'],data['mass_denominator']
nodes=data['nodes'];n=data['n'];D=data['degree'];H=data['table_position_counts']
assert (n,D)==(464,463)
assert Q>0 and R>0
assert all(type(x)==int and type(l)==int and abs(x)<=Q and l>=0 for x,l in nodes)
mass=sum(l for x,l in nodes)
assert mass<=448*R
Pprev=[1]*len(nodes);Pnow=[x for x,l in nodes];den=Q
max_numerator=None
for d in range(1,D+1):
    q=bisect_right(H,n-d)-1
    c=n-d-18*q
    numerator=c*R*den+2*sum(l*p for (x,l),p in zip(nodes,Pnow))
    assert 1000*numerator<=-R*den, ('coefficient failure',d)
    Pnext=[2*x*p-Q*Q*pp for (x,l),p,pp in zip(nodes,Pnow,Pprev)]
    Pprev,Pnow=Pnow,Pnext
    den*=Q
result={'label':'PROVED exact certificate inequalities','source_sha256':sha256(src.read_bytes()).hexdigest(),
 'n':n,'max_weight_length':D+1,'nodes':len(nodes),
 'mass':str(Fraction(mass,R)),'mass_upper_bound':448,
 'score_upper_bound_normalized':-16,'coefficient_checks':D,'coefficient_margin':'1/1000',
 'scope':'Every real weight vector of length<=464 with all positive-distance autocorrelations nonnegative.',
 'non_claim':'Not an exact optimum value; no claim about longer windows or improved caps.'}
Path(__file__).with_name('kernel_dual_verified.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
