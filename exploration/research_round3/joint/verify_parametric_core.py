"""Exact coefficient audit of a uniform two-block forbidden family."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
core=json.loads((ROOT/'triangle_core_v3.json').read_text());proof=json.loads((ROOT/'triangle_core_v3.check.json').read_text());assert proof['verdict']=='PASS'
for name,digest in proof['sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
A=core['marks'];assert A==[2,3,4,6,7,8,22,25,26,27]
# Coordinate triples encode x + h_coeff*h + b_coeff*b.
vectors=[(1,k,0) for k in [0,1,2,4,5,6]]+[(1,k,1) for k in [0,3,4,5]]
images=dict(zip(A,vectors))
def sub(v,w):return tuple(a-b for a,b in zip(v,w))
identities=[]
for x,y,d in core['corners']:
    horizontal=sub(images[x+d],images[x]);vertical=sub(images[y+d],images[y]);assert horizontal==vertical
    xx,hh,bb=horizontal;assert xx==0
    # For b>=6h+1, a step hh*h+bb*b is positive if bb>=0,
    # hh+6bb>=0, and at least one coefficient bound is strictly positive.
    assert bb>=0 and hh+6*bb>=0 and (bb>0 or hh+6*bb>0)
    identities.append(dict(original_corner=[x,y,d],step_h_coefficient=hh,step_b_coefficient=bb,zero_difference=list(sub(horizontal,vertical))))
# The same test checks strict global rank order across both blocks.
for first,second in zip(vectors,vectors[1:]):
    xx,hh,bb=sub(second,first);assert xx==0 and bb>=0 and hh+6*bb>=0 and (bb or hh+6*bb)
assert len(identities)==51
specializations=[]
for h,b in [(1,7),(1,20),(2,13),(3,100)]:
    marks=[1+hc*h+bc*b for _,hc,bc in vectors];assert marks==sorted(set(marks));specializations.append(dict(h=h,b=b,marks=marks))
identity_boundary_checks=[]
for xx,hh,bb in [(0,0,0),(1,1,1),(1000,99,100000)]:
    for x,y,d in core['corners']:
        u=sub(images[x+d],images[x]);v=sub(images[y+d],images[y]);assert sum(a*b for a,b in zip(u,(xx,hh,bb)))==sum(a*b for a,b in zip(v,(xx,hh,bb)))
    identity_boundary_checks.append(dict(x=xx,h=hh,b=bb,identities='PASS',positive_order_domain=hh>=1 and bb>6*hh))
out=dict(verdict='PASS',family='(x+h*{0,1,2,4,5,6}) union (x+b+h*{0,3,4,5})',domain='integer x; integer h>=1; integer b>6h',mark_count=10,preserved_cells=45,preserved_corners=51,existing_rup_additions=1297,identities=identities,specializations=specializations,identity_boundary_checks=identity_boundary_checks,scope='All51 original corner clauses hold identically; strict order holds on stated domain, so the checked fixed-label RUP refutation proves the whole two-parameter family forbidden')
(ROOT/'parametric_core.check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('identities','specializations')},indent=2))
