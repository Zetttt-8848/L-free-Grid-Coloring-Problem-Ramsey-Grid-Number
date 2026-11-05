"""Exact audit of the four-mark-hook plus five-AP uniform obstruction."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
core=json.loads((ROOT/'triangle_core_v4.json').read_text());check=json.loads((ROOT/'triangle_core_v4.check.json').read_text());assert check['verdict']=='PASS'
for name,digest in check['sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
A=core['marks'];assert A==[1,2,3,5,10,11,12,13,14]
vectors=[(1,k,0) for k in [0,1,2,4]]+[(1,k,1) for k in range(5)];images=dict(zip(A,vectors))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
records=[]
for x,y,d in core['corners']:
    horizontal=sub(images[x+d],images[x]);vertical=sub(images[y+d],images[y]);assert horizontal==vertical;xx,hh,bb=horizontal
    assert xx==0 and bb>=0 and hh+4*bb>=0 and (bb>0 or hh+4*bb>0)
    records.append(dict(corner=[x,y,d],step_h_coefficient=hh,step_b_coefficient=bb,identity=list(sub(horizontal,vertical))))
for a,b in zip(vectors,vectors[1:]):
    xx,hh,bb=sub(b,a);assert xx==0 and bb>=0 and hh+4*bb>=0 and (bb>0 or hh+4*bb>0)
assert len(records)==46
tests=[]
for xx,hh,bb in [(0,0,0),(1,1,1),(1,1,5),(1,1,9),(2,2,9),(1000,99,100000)]:
    for x,y,d in core['corners']:
        u=sub(images[x+d],images[x]);v=sub(images[y+d],images[y]);assert sum(a*b for a,b in zip(u,(xx,hh,bb)))==sum(a*b for a,b in zip(v,(xx,hh,bb)))
    domain=hh>=1 and bb>4*hh
    if domain:
        marks=[xx+hc*hh+bc*bb for _,hc,bc in vectors];assert marks==sorted(set(marks))
    tests.append(dict(x=xx,h=hh,b=bb,identities='PASS',positive_order_domain=domain))
out=dict(verdict='PASS',family='(x+h*{0,1,2,4}) union (x+b+h*{0,1,2,3,4})',domain='integer x; integer h>=1; integer b>4h',marks=9,cells=36,corners=46,rup_additions=157,coefficient_checks=records,boundary_checks=tests,scope='Uniform two-parameter forbidden family from the same verified RUP clauses; no new feasibility search with this premise has been performed')
(ROOT/'parametric_ap5_core.check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('coefficient_checks','boundary_checks')},indent=2))
