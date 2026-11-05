"""Gate-only certificate verification. No prior checker is imported or executed."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from functools import reduce
from math import gcd
import hashlib,json,time,sys

if not __debug__:
    raise RuntimeError('Certificate verification requires active assertions; do not use optimization mode.')

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'research_round3'
OUT=ROOT/sys.argv[1] if len(sys.argv)>1 else ROOT/'research_round4'/'audits'/'certificates'
OUT.mkdir(parents=True,exist_ok=True)
READ={}
def load(rel):
    p=SRC/rel;READ[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text(encoding='utf-8'))

def board(marks,weak=False):
    # Source convention: increasing second coordinate then first coordinate.
    return [(v,u) for u in marks for v in marks if (u<=v if weak else u<v)]

def geometry(cells):
    domain=set(cells);corners=[]
    rows=sorted({p[0] for p in cells})
    for x,y in cells:
        for z in rows:
            if z>x and (z,y) in domain and (z,y+z-x) in domain:
                corners.append(((x,y),(z,y),(z,y+z-x)))
    return corners

def clauses(cells):
    ids={p:i+1 for i,p in enumerate(cells)}
    out=[]
    for corner in geometry(cells):
        c=tuple(ids[p] for p in corner)
        out.extend([c,tuple(-x for x in c)])
    if cells:out.append((1,))
    return out

def unit_conflict(formula,negated_clause):
    values={}
    for lit in negated_clause:
        var=abs(lit);value=lit<0
        if var in values and values[var]!=value:return True
        values[var]=value
    while True:
        changed=False
        for clause in formula:
            undecided=[];satisfied=False
            for lit in clause:
                if abs(lit) not in values:undecided.append(lit)
                elif values[abs(lit)]==(lit>0):satisfied=True;break
            if satisfied:continue
            if not undecided:return True
            if len(undecided)==1:
                lit=undecided[0];var=abs(lit);value=lit>0
                if var in values and values[var]!=value:return True
                if var not in values:values[var]=value;changed=True
        if not changed:return False

def rup_verify(cells,proof):
    f=clauses(cells)
    assert proof and not proof[-1], 'Final empty clause is required'
    for i,c in enumerate(proof):
        assert len(set(c))==len(c) and all(1<=abs(x)<=len(cells) for x in c)
        assert unit_conflict(f,c),('invalid RUP',i,c)
        f.append(tuple(c))
    return len(proof)

def proof_file(stem):
    p=SRC/'joint'/f'{stem}.rup';READ[str(p.relative_to(SRC))]=hashlib.sha256(p.read_bytes()).hexdigest()
    proof=[]
    for line in p.read_text().splitlines():
        if not line.strip() or line.startswith('c'):continue
        row=[int(x) for x in line.split()];assert row[-1]==0
        proof.append(row[:-1])
    return proof

def norm(marks):
    a=[x-min(marks) for x in marks]
    g=reduce(gcd,a)
    return tuple(x//g for x in a)

start=time.perf_counter();result={}
cores={}
for stem,expected in [('triangle_core',(36,55,111,151)),('triangle_core_v2',(45,79,159,427)),('triangle_core_v3',(45,51,103,1297)),('triangle_core_v4',(36,46,93,157))]:
    o=load(f'joint/{stem}.json');cells=board(o['marks']);g=geometry(cells)
    assert cells==[tuple(x) for x in o['cells']]
    assert {(p[0],p[1],q[0]-p[0]) for p,q,r in g}=={tuple(x) for x in o['corners']}
    proof=proof_file(stem);count=rup_verify(cells,proof)
    actual=(len(cells),len(g),len(clauses(cells)),count);assert actual==expected,(stem,actual)
    cores[stem]={'marks':o['marks'],'counts':actual,'all_RUP_additions_valid':True}
    print('verified',stem,actual,flush=True)
result['fixed_cores']=cores

# Uniform algebraic lift, derived from source marks and the stated formulas.
lifts={}
for stem,hcoeff,bcoeff,kbound in [
    ('triangle_core_v3',[0,1,2,4,5,6,0,3,4,5],[0]*6+[1]*4,6),
    ('triangle_core_v4',[0,1,2,4,0,1,2,3,4],[0]*4+[1]*5,4)]:
    marks=cores[stem]['marks'];expr={x:(1,h,b) for x,h,b in zip(marks,hcoeff,bcoeff)}
    rows=[]
    for p,q,r in geometry(board(marks)):
        rd=tuple(a-b for a,b in zip(expr[q[0]],expr[p[0]]))
        cd=tuple(a-b for a,b in zip(expr[r[1]],expr[q[1]]))
        assert rd==cd and rd[0]==0
        _,dh,db=rd
        assert db>=0 and dh+kbound*db>=0 and (db>0 or dh+kbound*db>0)
        rows.append({'corner':[p,q,r],'step_coefficients':rd,'positive_on_domain':True})
    lifts[stem]={'h_min':1,'b_gt_multiple_h':kbound,'all_coefficient_identities':rows,'count':len(rows),'scope':'Infinite parameter domain justified algebraically; no sampled-parameter inference'}
result['parametric_lifts']=lifts

W=load('joint/window13.json');w=W['width'];assert w==13
bad_masks=[];good_masks=[];rup_count=0
for j,o in enumerate(W['minimal_bad']):
    marks=[i for i in range(w) if o['mask']>>i&1];assert marks==o['marks']
    rup_count+=rup_verify(board(marks),o['proof']);bad_masks.append(o['mask'])
    if j%25==0:print('window bad proofs',j+1,flush=True)
for o in W['maximal_good']:
    marks=[i for i in range(w) if o['mask']>>i&1];assert marks==o['marks']
    cells=board(marks);colors=o['colors'];assert len(cells)==len(colors) and set(colors)<={0,1}
    col=dict(zip(cells,colors))
    assert all(len({col[p] for p in C})>1 for C in geometry(cells))
    good_masks.append(o['mask'])
assert len(set(bad_masks))==len(bad_masks) and len(set(good_masks))==len(good_masks)
classes={}
for mask in range(1<<w):
    has_bad=any(mask&b==b for b in bad_masks)
    in_good=any(mask&g==mask for g in good_masks)
    assert has_bad != in_good, ('coverage or consistency failure',mask)
    classes[mask]='bad' if has_bad else 'good'
derived_minbad={m for m,v in classes.items() if v=='bad' and all(classes[m^(1<<i)]=='good' for i in range(w) if m>>i&1)}
derived_maxgood={m for m,v in classes.items() if v=='good' and all(classes[m|(1<<i)]=='bad' for i in range(w) if not m>>i&1)}
assert derived_minbad==set(bad_masks) and derived_maxgood==set(good_masks)
caps=[max(m.bit_count() for m in range(1<<width) if classes[m]=='good') for width in range(1,w+1)]
counts=Counter(classes.values());actual=(len(classes),counts['good'],counts['bad'],len(bad_masks),len(good_masks),rup_count)
assert actual==(8192,7147,1045,109,334,31605)
assert caps==[1,2,3,4,5,5,6,7,7,8,9,9,10]
patterns=sorted({norm([i for i in range(w) if m>>i&1]) for m in bad_masks})
assert len(patterns)==56
result['window13']={'counts':actual,'caps':caps,'exact_labeled_coverage':True,'normalized_pattern_count':len(patterns)}
print('window complete',actual,flush=True)

H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
q=lambda m:max(j for j,x in enumerate(H) if x<=m)
witnesses={}
for name in ['witness_464','witness_464_parametric']:
    o=load(f'joint/{name}.json');a=o['marks'];A=set(a);n=464
    assert a==sorted(A) and len(a)==155 and min(a)>=1 and max(a)<=n
    diffs=Counter(y-x for x,y in combinations(a,2));assert sum(diffs.values())==11935
    assert all(diffs[d]<=2*q(n-d) for d in range(1,n))
    ap6=[(x,d) for d in range(1,(n-1)//5+1) for x in range(1,n-5*d+1) if all(x+i*d in A for i in range(6))]
    ap5={d:[x for x in range(1,n-4*d+1) if all(x+i*d in A for i in range(5))] for d in range(1,(n-1)//4+1)}
    assert not ap6
    row={'marks':len(a),'pair_count':sum(diffs.values()),'ap6_bad':len(ap6),'ap6_tests':sum(n-5*d for d in range(1,(n-1)//5+1)),
         'first_three_differences':[diffs[d] for d in [1,2,3]],'exceeds_45_first27':sum(diffs[d]>45 for d in range(1,28)),
         'AP5_repeated_steps':[d for d,starts in ap5.items() if len(starts)>1]}
    if name.endswith('parametric'):
        assert all(len(starts)<=1 for starts in ap5.values())
        pattern_tests=0
        for p in patterns:
            for d in range(1,(n-1)//max(p)+1):
                for x in range(1,n-max(p)*d+1):
                    pattern_tests+=1
                    assert not all(x+d*i in A for i in p)
        assert pattern_tests==543170
        # Fully enumerate all translations and block separations in [1,464].
        family_tests=0;bad_family=[]
        for h in range(1,43):
            left=[x for x in range(1,n-6*h+1) if all(x+h*j in A for j in [0,1,2,4,5,6])]
            right=[z for z in range(1,n-5*h+1) if all(z+h*j in A for j in [0,3,4,5])]
            reflected=[z for z in range(1,n-5*h+1) if all(z+h*j in A for j in [0,1,2,5])]
            for x in left:
                for z in right:
                    family_tests+=1
                    if z>x+6*h:bad_family.append((x,z,h,'forward'))
                for z in reflected:
                    family_tests+=1
                    if x>z+5*h:bad_family.append((x,z,h,'reflected'))
        assert not bad_family
        assert set(cores['triangle_core_v4']['marks'])<=A
        row.update({'affine_pattern_tests':pattern_tests,'parametric_block_pair_tests':family_tests,'parametric_bad':bad_family,'violates_later_hook_family':True})
    witnesses[name]=row
result['witnesses']=witnesses

# Geometric forcing traces for the complete prescribed ruler-pair family.
P=load('cap/pair_forcing_certificate.json');rulers={int(k):v for k,v in P['rulers'].items()}
expected_cases={}
for size,S in rulers.items():
    assert len(S)==size and S==sorted(set(S))
    diffs=[y-x for x,y in combinations(S,2)];assert len(diffs)==len(set(diffs))
    for refl in [False,True]:
        base={max(S)-x if refl else x for x in S}
        for t in range(1,462-max(S)+1):
            B={x+t for x in base}
            if not set(S)&B:expected_cases[size,refl,t]=(set(S),B)
assert len(expected_cases)==60
seen=set();steps_count=0;apfree=0
for case in P['cases']:
    key=case['order'],case['reflected'],case['shift'];assert key in expected_cases and key not in seen;seen.add(key)
    A,B=expected_cases[key];F=A|B;assert sorted(F)==case['F']
    domain=set(board(sorted(F),True));color={(x,x):0 for x in A};color.update({(x,x):1 for x in B})
    def check_corner(C):
        C=[tuple(p) for p in C];assert len(set(C))==3 and all(p in domain for p in C)
        found=False
        for p in C:
            for q0 in C:
                d=q0[0]-p[0]
                if d>0 and q0[1]==p[1] and set(C)=={p,q0,(q0[0],p[1]+d)}:found=True
        assert found
        return C
    for step in case['steps']:
        C=check_corner(step['corner']);p=tuple(step['point']);v=step['color']
        assert p in C and p not in color and v in [0,1]
        other=[q0 for q0 in C if q0!=p];assert all(q0 in color for q0 in other)
        assert color[other[0]]==color[other[1]]==1-v
        color[p]=v;steps_count+=1
    C=check_corner(case['conflict']);assert all(p in color for p in C) and len({color[p] for p in C})==1
    aps=sum(all(x+i*d in F for i in range(5)) for d in range(1,(max(F)-min(F))//4+1) for x in F if x+4*d<=max(F))
    assert aps==case['five_ap_count'];apfree+=aps==0
assert seen==set(expected_cases) and steps_count==16425 and apfree==59
result['ruler_pairs']={'family_count':len(seen),'forcing_steps':steps_count,'AP5_free_unions':apfree,'scope':'Only equal-order positive shifts/reflections specified in the source'}
result['provenance']={'base':'R4-GATE-0001','python':sys.version,'source_hashes':READ,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer arithmetic only; runtime is metadata','claimant_code_imported':False,
                      'python_optimize':sys.flags.optimize,'assertions_active':__debug__}
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('ALL ASSERTED CERTIFICATE CHECKS PASSED',flush=True)
