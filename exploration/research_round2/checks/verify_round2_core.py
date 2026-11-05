"""Portable exact checker for the central Round2 certificates.

Run from any directory: python /absolute/path/research_round2/checks/verify_round2_core.py
No solver, NumPy, floating point, or network is needed. This checks finite
certificates; universal proofs, including the general-k induction, are in the report.
"""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import json,os,runpy,sys

ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT.parent)
sys.set_int_max_str_digits(10000)
data=json.loads((ROOT/'certificates/weights_four_22006246.json').read_text())
n,t=data['n'],data['t']
assert (n,t)==(22006246,36000)
B=t+1
correlations=[]
for d in range(t):
    m=t-d
    p1=m*(m+1)//2
    p2=m*(m+1)*(2*m+1)//6
    p3=p1*p1
    p4=m*(m+1)*(2*m+1)*(3*m*m+3*m-1)//30
    correlations.append(p4-2*(B-d)*p3+(B*B-3*B*d+d*d)*p2+B*d*(B-d)*p1)
assert min(correlations)>0
assert correlations[0]==2015819151552432004800==data['a0']

def excluded(s,L,V,c):
    assert s>c>=1 and V>=1 and L>=0
    h=c*s-c*(c+1)//2
    a,b=divmod(h,V)
    return V*a*(a+1)+2*b*(a+1)>L*c*(c+1)

next_d=1;left=0
for run in data['runs']:
    lo,hi,q,k=[run[key] for key in ('lo','hi','q','K')]
    assert lo==next_d and lo<=hi<t
    assert excluded(q+1,n-lo-1,1,62)
    assert excluded(k+1,n-lo-1,2*q,662)
    left+=2*sum((n-d-48*k)*correlations[d] for d in range(lo,hi+1))
    next_d=hi+1
assert next_d==t
right=3*n*correlations[0]
assert left==133088683635976942314364072128==data['doubled_lhs']
assert right==133081836421722301787705942400==data['doubled_rhs']
assert left-right==6847214254640526658129728==data['doubled_margin']

primes=[998244353,1004535809,469762049]
transform_size=1
while transform_size<2*t-1:transform_size*=2
for p in primes:
    assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
    assert (p-1)%transform_size==0
    root=pow(3,(p-1)//transform_size,p)
    assert pow(root,transform_size,p)==1
    assert pow(root,transform_size//2,p)!=1
assert t*max(i*(t+1-i) for i in range(1,t+1))**2<primes[0]*primes[1]*primes[2]

print('PASS: final R4 power-sum certificate and NTT arithmetic prerequisites',flush=True)
for name in ('kernel_dual_verify.py','structural_sixap_verify.py',
             'structural_five_verify.py','structural_moment_verify.py','general_neighbor_verify.py'):
    runpy.run_path(str(ROOT/'checks'/name),run_name='__main__')
result={'status':'PASS','R4_upper_bound':n,'R3_interval':[21,465],
        'general_bound':'k^(2^k) for k>=3; universal proof required',
        'dual_normalized_upper_bound':-16,'exact_R3':'UNRESOLVED',
        'scope':'Finite integer certificates and finite supplemental identity checks; not global search exhaustion.'}
(ROOT/'checks/core_verified.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
