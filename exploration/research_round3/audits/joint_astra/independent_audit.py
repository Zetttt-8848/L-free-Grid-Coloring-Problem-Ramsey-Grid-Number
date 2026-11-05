"""Independent stdlib-only reconstruction; imports no project code."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter, deque
import json, hashlib, sys, platform

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
inputs={}
def read(rel):
    p=ROOT/rel; b=p.read_bytes(); inputs[rel]=hashlib.sha256(b).hexdigest()
    return json.loads(b)
def textread(rel):
    p=ROOT/rel; b=p.read_bytes(); inputs[rel]=hashlib.sha256(b).hexdigest()
    return b.decode('utf-8-sig')
def save(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def check(v,label):
    if not v: raise AssertionError(label)
def cnew(q):
    return {1:F(1),2:F(101,100),3:F(57,40),4:F(207,100),5:F(72,25),6:F(19,5)}.get(q,F(q-2)-F(1,max(1,q-2)))
def general():
    for f in ['refined_constants_proof.md','refined_minus_one.md','square_root_barrier.md']:
        textread('general/'+f)
    old=[F(a,40)**2-v for a,v in [(59,F(17,8)),(87,F(9,2)),(119,F(44,5))]]
    gaps=[(cnew(q)-F(1,1000))**2-(q-1)*cnew(q-1) for q in range(3,8)]
    src=read('general/minus_one_exact.json')
    for row,gap in zip(src['coefficient_checks'],gaps):
        check(F(row['squared_gap'])==gap and gap>0,('gap',row))
    scalars=[]
    for row in src['scalar_checks']:
        k=row['k']; b=k*(k-2)-1; N=b**(2**(k-1)); t=2*k*b*b
        delta=1-F(k*k*(k-1))*cnew(k-1)/b**2
        margin=delta*N*(t-1)-F(t*t-1,3)-(k-1)*N
        check((b,N,t,delta,margin)==(row['b'],int(row['N']),row['t'],F(row['delta']),F(row['margin'])),('scalar',k))
        check(margin>0 and t<=N and delta>=F(1,b*b),('scalar sign',k))
        scalars.append({'k':k,'b':b,'t':t,'delta':str(delta),'margin':str(margin)})
    repro=read('general/scalar_reproduction.json')
    check(list(map(str,old))==repro['old_squared_gaps'],'old gaps')
    check(list(map(str,gaps))==repro['new_squared_gaps'],'new gaps')
    check(15**16==int(repro['N5']),'N5')
    cand=read('general/exact_candidate.json')
    check(cand['N5']==15**16 and cand['N6']==24**32 and cand['t5']==450 and F(cand['delta5'])==F(1,45),'old exact candidate')
    margin5=F(1,45)*(15**16)*449-F(450**2-1,3)-4*(15**16)
    check(margin5==F(cand['normalized_margin5']),'old margin5')
    # Rational identity after formal cancellation, also evaluated at 0,1,100.
    for k in [0,1,6,7,8,100]:
        lhs=(k*(k-2)-1)**2-k*k*(k-1)*(F(k-3)-F(1,k-3))
        rhs=F(2*k*k,k-3)+4*k+1
        check(lhs==rhs,('coefficient identity',k))
    prime_checks=[]
    for p in range(3,32,2):
        if any(p%d==0 for d in range(2,p)): continue
        S=[2*p*i+(i*i%p) for i in range(p)]
        diffs=[b-a for a,b in combinations(S,2)]
        check(len(set(diffs))==len(diffs) and max(S)<2*p*p,('Golomb',p))
        pts={(x,y):int(x>y) for x in S for y in S if x>=y}
        cs=corners(pts)
        check(not any(len({pts[z] for z in c})==1 for c in cs),('Golomb colors',p))
        prime_checks.append({'p':p,'span':max(S),'differences':len(diffs),'corners':len(cs)})
    return {'status':'PASS','old_gaps':list(map(str,old)),'new_gaps':list(map(str,gaps)),
        'N5':str(15**16),'scalars':scalars,'prime_checks':prime_checks,
        'scope':'Universal proofs audited separately in REPORT.md; finite checks are diagnostics only.'}

def corners(points):
    P=set(points); out=[]
    # A mandated corner is determined by its first and last same-diagonal cells.
    diag={}
    for x,y in P: diag.setdefault(x-y,[]).append((x,y))
    for pts in diag.values():
        for p,q in combinations(sorted(pts),2):
            r=(q[0],p[1])
            if r in P: out.append((p,r,q))
    return out
def iscorner(c):
    if len(set(c))!=3:return False
    return any((x+d,y) in c and (x+d,y+d) in c
               for x,y in c for d in [max(t[0] for t in c)-x] if d>0)
def fiveaps(S):
    S=set(S)
    return sum(all(x+i*d in S for i in range(5)) for x in S
               for d in range(1,(max(S)-x)//4+1)) if S else 0
def triangles():
    textread('cap/ap5_uniqueness.md')
    rows=[]
    for m in [4,5]:
        pts=[(x,y) for x in range(m) for y in range(x+1)]
        index={p:i for i,p in enumerate(pts)}
        cs=corners(pts); masks=[sum(1<<index[p] for p in c) for c in cs]
        sat=[v for v in range(1<<len(pts)) if all(v&c not in (0,c) for c in masks)]
        check(len(sat)=={4:36,5:0}[m],('weak triangle',m))
        rows.append({'m':m,'points':len(pts),'corners':len(cs),'raw_colorings':1<<len(pts),'valid':len(sat)})
    check(sum(464-4*a for a in range(1,116))==26680,'AP5 count')
    return rows
def forcing():
    textread('cap/PREDICTIONS.md'); cert=read('cap/pair_forcing_certificate.json')
    rulers={int(k):v for k,v in cert['rulers'].items()}
    expected=set()
    for order,A in rulers.items():
        check(len(A)==order and min(A)==0,'ruler size')
        ds=[b-a for a,b in combinations(sorted(A),2)]
        check(len(set(ds))==len(ds),'ruler uniqueness')
        for refl in [False,True]:
            B0=[max(A)-a for a in A] if refl else A
            for shift in range(1,463-max(A)):
                B={b+shift for b in B0}
                if not set(A)&B:expected.add((order,refl,shift))
    seen=set(); steps=0; apfree=0; cases=[]
    for case in cert['cases']:
        order,refl,h=case['order'],case['reflected'],case['shift']
        key=(order,refl,h);check(key not in seen,'duplicate pair'); seen.add(key)
        A=set(rulers[order]); B={(max(A)-a if refl else a)+h for a in A}; S=A|B
        check(not A&B and sorted(S)==case['F'] and max(S)-min(S)<=462,'pair source')
        known={(a,a):0 for a in A};known.update({(b,b):1 for b in B})
        for j,step in enumerate(case['steps']):
            p=tuple(step['point']); cs=[tuple(z) for z in step['corner']]; color=step['color']
            check(iscorner(cs) and p in cs and all(x in S and y in S and x>=y for x,y in cs),('corner',key,j))
            check(p not in known and color in (0,1),('new forced variable',key,j))
            check(all(known.get(z)==1-color for z in cs if z!=p),('forcing',key,j))
            known[p]=color;steps+=1
        conflict=[tuple(z) for z in case['conflict']]
        check(iscorner(conflict) and all(z in known for z in conflict),'conflict geometry')
        check(len({known[z] for z in conflict})==1,('final contradiction',key))
        ap=fiveaps(S);check(ap==case['five_ap_count'],('AP5 diagnostic',key))
        apfree+=int(ap==0);cases.append({'order':order,'reflected':refl,'shift':h,'steps':len(case['steps']),'AP5':ap})
    check(seen==expected and len(seen)==60,'frozen positive pair coverage')
    check(steps==16425 and apfree==59,'forcing totals')
    return {'status':'PASS','scope':'CAP-P1 positive shifts only, not arbitrary translations/rulers',
            'cases':cases,'total_steps':steps,'AP5_free_unions':apfree}

HT=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)
WINDOW=(1,2,3,4,5,5,6,7,7,8,9,9,10) # External J dependency, NOT independently certified here.
def spacing(maxi):
    ell=[0]
    for i in range(1,maxi+1):
        ell.append(max([i]+[w for w,h in enumerate(WINDOW,1) if h<=i]+[ell[j]+ell[i-j] for j in range(1,i)]))
    return ell
ELL=spacing(465)
def profile(n,kind):
    ans=[]
    for d in range(1,n):
        v=2*max(j for j,h in enumerate(HT) if h<=n-d)
        if kind=='45' and d<=27:v=min(v,45)
        elif kind!='inherited' and kind!='45':
            check(kind=='46' or kind in ['46+1','46+2','46+3','46+4'],('unknown profile',kind))
            if d<=27:v=min(v,46)
            shave=0 if kind=='46' else int(kind.split('+')[1])
            if d<=shave:v=min(v,45)
        ans.append(v)
    return ans
def endpoint_row(n,s,kind,window):
    mult=[d for d,v in enumerate(profile(n,kind),1) for _ in range(v)]
    sums=[0]
    for d in mult:sums.append(sums[-1]+d)
    best=None
    for c in range(1,s):
        H=c*s-c*(c+1)//2
        check(H<len(sums),('capacity exhausted',n,s,c))
        corr=2*sum((c-i)*(ELL[i] if window else i) for i in range(c))
        upper=(n-1)*c*(c+1)//2-corr
        row={'c':c,'H':H,'minimum':sums[H],'upper':upper,'margin':sums[H]-upper,'last_distance':mult[H-1],'correction':corr}
        if best is None or row['margin']>best['margin']:best=row
    return best
def endpoint():
    textread('cap/endpoint_neighbor.md')
    src=read('cap/endpoint_exact.json'); desc=read('cap/conditional_descent.json')
    check(src['ell_window']==ELL[:len(src['ell_window'])],'spacing DP')
    rows=src['rows']+desc['rows']
    check(len(desc['rows'])==460 and {r['n'] for r in desc['rows']}==set(range(6,466)),'conditional descent coverage')
    for r in rows:
        got=endpoint_row(r['n'],r['s'],r['profile'],r['window'])
        check(got==r['best'] and (got['margin']>0)==r['excluded'],('endpoint row',r,got))
    identities=0
    for n in range(2,11):
        for s in range(2,n+1):
            for A in combinations(range(n),s):
                for c in range(1,s):
                    direct=sum(A[h+j]-A[h] for j in range(1,c+1) for h in range(s-j))
                    telesc=sum((c-i)*(A[s-i-1]-A[i]) for i in range(c))
                    check(direct==telesc,'endpoint telescope'); identities+=1
    bound=[]
    for s in [158,159]:bound.append({'s':s,**endpoint_row(464,s,'inherited',True)})
    check(bound[0]['margin']<=0<bound[1]['margin'],'158 bound')
    plain=[{'s':s,**endpoint_row(464,s,'inherited',False)} for s in [158,159]]
    check(plain[0]['margin']<=0<plain[1]['margin'] and plain[1]['margin']==271,'158 bound without window')
    check(all(not r['excluded'] for r in desc['rows'] if r['n']<=453),'conditional lower range')
    chosen=[r for r in rows if (r['n'],r['profile'],r['window']) in [(454,'45',True),(464,'46+3',True)]]
    return {'status':'PASS','rows_recomputed':len(rows),'small_identity_checks':identities,'ell':ELL[:31],
        'n464_inherited_boundary':bound,'n464_inherited_no_window_boundary':plain,'selected':chosen,
        'external_dependency':'WINDOW values are J author input; this reviewer does not independently certify J.'}

def overlap():
    textread('overlap/ordered_overlap.md'); src=read('overlap/exact_overlap.json')
    cases=total=0
    for n in range(1,8):
        for mask in range(1<<n):
            A={i+1 for i in range(n) if mask>>i&1}
            for d,e in combinations(range(1,n),2):
                Fd=sorted(u for u in A if u+d in A); Fe=sorted(u for u in A if u+e in A)
                for md in range(1<<len(Fd)):
                    Bd={u for i,u in enumerate(Fd) if md>>i&1}; Qd={(v+d,u) for u,v in combinations(sorted(Bd),2)}
                    for me in range(1<<len(Fe)):
                        Be={u for i,u in enumerate(Fe) if me>>i&1}; Qe={(v+e,u) for u,v in combinations(sorted(Be),2)}
                        C=Bd&Be;D=Be&{v-(e-d) for v in Bd}
                        exact=sum(u<q for q in D for u in C)
                        check(exact==len(Qd&Qe),'overlap identity')
                        X={u for u in A if u+d in A and u+e in A}
                        Y={u for u in A if u+e-d in A and u+e in A}
                        J=sum(u<q for u in X for q in Y)
                        vmin=min(sum(u+t in A for u in A) for t in [d,e,e-d])
                        check(exact<=min(len(Qd),len(Qe),J,vmin*vmin),'coarse overlap')
                        cases+=1;total+=exact
    check(cases==src['cases'] and total==src['sum_overlap'],'overlap finite totals')
    A={1,4,8,14,18,21};Bd={1,18};Be={1,14}
    Qd={(v+3,u) for u,v in combinations(sorted(Bd),2)};Qe={(v+7,u) for u,v in combinations(sorted(Be),2)}
    check(Qd==Qe=={(21,1)},'saturation')
    inherited=read('../research_round2/certificates/four_multi_overlap.json')['witness']
    colored={(x,y):c for x,y,c in inherited['colors']}
    check(set(colored)=={(x,y) for x in A for y in A if x>=y},'saturation domain')
    check(all(colored[(a,a)]==0 for a in A),'saturation source color')
    for p,q in combinations(sorted(colored),2):
        if q[0]-p[0]==q[1]-p[1]>0:check((q[0],p[1]) in colored,'saturation closure')
    cs=corners(colored)
    check(all(len({colored[p] for p in c})>1 for c in cs),'saturation cornerfree')
    check({u for u in A if u+3 in A and colored[(u+3,u)]==1}==Bd,'saturation Bd')
    check({u for u in A if u+7 in A and colored[(u+7,u)]==1}==Be,'saturation Be')
    return {'status':'PASS','cases':cases,'sum_overlap':total,'saturation':{'M':2,'O':1,'union':1,'output':[21,1],'region_points':len(colored),'region_corners':len(cs),'completion_closed':True,'monochromatic_corners':0},'scope':'Sharpness holds in the literal completion-closed region; no full-grid coloring conclusion.'}

def parsecnf(raw):
    clauses=[]; buf=[]; header=None
    for line in raw.splitlines():
        if not line or line[0]=='c':continue
        if line[0]=='p':header=tuple(map(int,line.split()[2:]));continue
        for x in map(int,line.split()):
            if x:buf.append(x)
            else:clauses.append(tuple(buf));buf=[]
    check(not buf and header==(1323,len(clauses)),'DIMACS format')
    return clauses
def unitprop(clauses,units):
    # Fresh occurrence-list residual-count propagation; no SAT library.
    occ={}; remain=[len(c) for c in clauses];satisfied=[False]*len(clauses)
    for j,c in enumerate(clauses):
        for lit in c:occ.setdefault(lit,[]).append(j)
    q=deque((lit,None) for lit in units)
    q.extend((c[0],j) for j,c in enumerate(clauses) if len(c)==1)
    known={};trace=[]
    while q:
        lit,reason=q.popleft();v=abs(lit)
        if v in known:
            if known[v]!=(lit>0):return True,trace,{'opposite_literal':lit,'reason':reason}
            continue
        known[v]=(lit>0);trace.append([lit,reason])
        for j in occ.get(lit,[]):satisfied[j]=True
        for j in occ.get(-lit,[]):
            if satisfied[j]:continue
            remain[j]-=1
            if remain[j]==0:return True,trace,{'empty_clause':j}
            if remain[j]==1:
                un=[z for z in clauses[j] if abs(z) not in known]
                check(len(un)==1,'residual propagation invariant');q.append((un[0],j))
    return False,trace,None
def lower():
    for f in ['ENCODING.md','AFFINE_CONSTRUCTIONS.md','SUBTASK_REPORT.md','MAPLECM_DISPOSITION.md']:
        textread('lower/'+f)
    raw=textread('lower/n21_exact.cnf');cs=parsecnf(raw)
    n=21;var=lambda x,y,c:3*(n*x+y)+c+1
    expected=[]
    for x,y in product(range(n),repeat=2):
        vs=[var(x,y,c) for c in range(3)];expected.append(tuple(vs))
        expected.extend((-a,-b) for a,b in combinations(vs,2))
    geo=[]
    for x,y in product(range(n),repeat=2):
        for d in range(1,min(n-x,n-y)):
            pts=((x,y),(x+d,y),(x+d,y+d));geo.append(pts)
            expected.extend(tuple(-var(a,b,c) for a,b in pts) for c in range(3))
    expected.append((1,))
    expected.extend(tuple([-3*p-3]+[3*q+2 for q in range(1,p)]) for p in range(1,n*n))
    canonical=lambda cc:Counter(tuple(sorted(c)) for c in cc)
    check(len(geo)==2870 and len(cs)==10815 and canonical(cs)==canonical(expected),'independent CNF reconstruction')
    cubes=read('lower/n21_cubes.json');cr=cubes['records'];cells=[(0,1),(1,0),(1,1),(20,20)]
    check(cubes['split_cells_0_based']==list(map(list,cells)),'cube cells')
    check({tuple(r['cube_colors_0_based']) for r in cr}==set(product(range(3),repeat=4)) and len(cr)==81,'cube coverage')
    byorder={r['order']:r for r in cr};check(set(byorder)==set(range(81)),'cube order')
    up=[];hard=[]
    for r in cr:
        units=[var(x,y,c) for (x,y),c in zip(cells,r['cube_colors_0_based'])]
        check(units==r['assumption_literals'],'cube literal mapping')
        contradiction,trace,conflict=unitprop(cs,units)
        # Replay each generated reason directly, without propagation machinery.
        assignments={}
        for lit,reason in trace:
            if reason is None:check(lit in units,'trace initial unit')
            else:
                check(lit in cs[reason] and all(assignments.get(abs(z))==(z<0) for z in cs[reason] if z!=lit),'trace unit reason')
            check(abs(lit) not in assignments,'trace new assignment');assignments[abs(lit)]=lit>0
        if contradiction:
            if 'empty_clause' in conflict:bad=conflict['empty_clause']
            else:bad=conflict['reason']
            check(bad is not None and all(assignments.get(abs(z))==(z<0) for z in cs[bad]),'trace final falsified clause')
        (up if contradiction else hard).append(r['order'])
        if contradiction:save('up_cube_%02d.json'%r['order'],{'order':r['order'],'units':units,'trace':trace,'conflict':conflict,'clause_index_base':0})
    quick=read('lower/n21_quick_cube_proofs.json');stage1=read('lower/n21_stage1_maplechrono.json');merged=read('lower/n21_stage2_portfolio_merged.json')
    check(stage1['cnf_sha256']==inputs['lower/n21_exact.cnf'] and stage1['cube_manifest_sha256']==inputs['lower/n21_cubes.json'],'source hash binding')
    check(len(stage1['records'])==81 and {r['order'] for r in stage1['records']}==set(byorder),'stage1 full coverage')
    check(sum(r['stage1_cap_seconds'] for r in cr)==546,'stage1 nominal cap sum')
    check(len(up)==33 and set(up)=={r['order'] for r in quick['records']},'33 direct UP refutations')
    check({r['order'] for r in stage1['records'] if r['status']=='RAW_UNSAT_UNVERIFIED'}==set(up),'stage1 easy mapping')
    check({r['order'] for r in merged['records']}==set(hard) and len(hard)==48,'48 hard coverage')
    workers=[];wrs=[]
    for name in ['glucose4','maplecm','glucose3_recovery']:
        worker=read('lower/n21_stage2_'+name+'.json');rr=worker['records'];wrs.extend(rr)
        workers.append({'name':name,'records':len(rr),'conflicts':sum(r['stats']['conflicts'] for r in rr),'stored_status':worker['mathematical_status']})
    check(len(wrs)==48 and len({r['order'] for r in wrs})==48,'worker exact cover')
    check({r['order']:r for r in wrs}=={r['order']:r for r in merged['records']},'merge record identity')
    for r in wrs:
        check(r['status']=='INTERRUPTED_UNDECIDED','hard outcome')
        check(r['assumption_literals']==byorder[r['order']]['assumption_literals'] and r['cube_colors_0_based']==byorder[r['order']]['cube_colors_0_based'],'worker cube mapping')
    matrix=[list(map(int,line.split())) for line in textread('lower/difference_circulant_n3.txt').splitlines() if line.strip()]
    check(matrix==[[1+(y-x)%3 for y in range(3)] for x in range(3)],'circulant literal')
    c3=corners(product(range(3),repeat=2));check(len(c3)==5,'n3 corner count')
    check(all(len({matrix[x][y] for x,y in c})>1 for c in c3),'n3 cornerfree')
    epochs=[read('lower/affine_scan_m2_m50'+suffix+'.json') for suffix in ['', '_epoch2','_epoch3']]
    offset=0
    for epoch in epochs:
        check(epoch.get('start_pair_index',0)==offset,'affine epoch continuity');offset+=epoch['pairs_attempted']
        check(epoch['raw_unsat_unverified']==epoch['pairs_attempted'] and epoch['witness'] is None,'affine raw semantics')
    check(offset==26103 and sum(m*m for m in range(2,51))==42924,'affine counts')
    return {'status':'PASS','variables':1323,'clauses':len(cs),'geometric_corners':len(geo),'symmetry_clauses':441,
        'UP_refuted_orders':sorted(up),'hard_UNDECIDED_orders':sorted(hard),'workers':workers,
        'circulant_side':3,'circulant_corners':5,'affine_attempted_raw_only':offset,'affine_unattempted':42924-offset,
        'global_n21_status':'UNDECIDED: 33 certified refutations plus 48 interrupted branches, no global result'}

if __name__=='__main__':
    task=sys.argv[1]
    funcs={'G':general,'C_triangle':triangles,'C_forcing':forcing,'C_endpoint':endpoint,'C_overlap':overlap,'L':lower}
    try:
        result=funcs[task]();save(task+'_result.json',result)
        save(task+'_provenance.json',{'python':platform.python_version(),'input_sha256':inputs,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'independence':'No project module imported or executed.'})
        print(task,'PASS')
    except Exception as e:
        save(task+'_FAIL.json',{'status':'HALTED','error':repr(e),'input_sha256':inputs});raise
