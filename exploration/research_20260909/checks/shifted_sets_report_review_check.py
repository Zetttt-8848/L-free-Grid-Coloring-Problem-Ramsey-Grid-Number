"""Bounded independent check of the current report's first-three-section tables."""
from itertools import product
import json

triples='abc adf agj ako bde bgi bkn cef chj clo dgh dkm ehi eln fij fmo gkl hlm imn jno'.split()
rows=[
 ('b0 d0','c1 f1 e1','cef'),
 ('b0 d1 h0 k0','c1 o1 n1 l0 g1 m1 i0 j0 e1 f1','fmo'),
 ('b0 d1 h0 k1','c1 m0 l1 o0 f1 g0 j1 i1 e0','fij'),
 ('b0 d1 h1','c1 j0 g0','agj'),
 ('b1 n0 f0','d1 e0 c1 l1 o0 m1 h0 j1 k1','dkm'),
 ('b1 n0 f1 g0','j1 i0 m1 o0 k1 d0 h1 l0 c0','clo'),
 ('b1 n0 f1 g1','i0 m1 o0 j1 k1 d0 l0 c1 e1','cef'),
 ('b1 n1','k0 o1 j0 g1 i0 f1 m0 d1 e0 h0','ehi'),
]
parsed=[]
forcing=[]
for assumptions,steps,conflict in rows:
    v={'a':0,**{x[0]:int(x[1]) for x in assumptions.split()}}
    parsed.append(dict(v))
    used=[]
    for instruction in steps.split():
        x,val=instruction[0],int(instruction[1])
        assert x not in v
        edge=next((tr for tr in triples if x in tr and all(y in v and v[y]==1-val for y in tr if y!=x)),None)
        assert edge, (assumptions,instruction,v)
        v[x]=val
        used.append(edge)
    assert all(x in v for x in conflict) and len({v[x] for x in conflict})==1
    forcing.append(used)
for bits in product(range(2),repeat=14):
    v=dict(zip('abcdefghijklmno',[0,*bits]))
    assert sum(all(v[x]==b for x,b in assumptions.items()) for assumptions in parsed)==1

coords={}
letters=iter('abcdefghijklmno')
for i in range(1,6):
    for j in range(i):coords[next(letters)]=(i,j)
labels={v:k for k,v in coords.items()}
computed=[]
for (i,j),label in labels.items():
    for d in range(1,6-i):computed.append(label+labels[(i+d,j)]+labels[(i+d,j+d)])
assert computed==triples
T5='0011000011'
v=dict(zip('abcdefghij',map(int,T5)))
assert not any(len({v[x] for x in tr})==1 for tr in triples if set(tr)<=set(v))
mass=50*sum(range(1,10))+48*sum(range(10,43))+7*43
penalty=2*sum((14-i)*((i-1)//5) for i in range(1,14))
budget=490*sum(range(1,14))-sum(i*i for i in range(1,14))-penalty
assert (mass,budget,mass-budget,penalty)==(43735,43687,48,84)
def b3(s):
    u,v=divmod(s,3)
    return 3*u*u+v*(2*u+1)
lower466=399*b3(68)+2*sum(b3(s) for s in range(1,68))
upper466=466*68+12*(24*sum(68-d for d in range(1,41))+23*sum(68-d for d in range(41,68)))
assert (lower466,upper466)==(683658,683216)
print(json.dumps({'report_branch_forcing_triples':forcing,'branch_coverage_assignments':2**14,
 'triangular_triples':computed,'T5_witness_verified':True,'490_mass':mass,'490_budget':budget,
 '466_lower':lower466,'466_upper':upper466,'result':'all mathematical checks passed'},indent=2))
