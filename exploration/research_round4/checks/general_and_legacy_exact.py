"""Independent Round-4 arithmetic from definitions; no claimant code imported."""
from pathlib import Path
from fractions import Fraction as F
from math import comb, isqrt
import json, hashlib, platform, sys
import sympy as sp

if not __debug__:
    raise RuntimeError('Exact verification requires active assertions; do not use optimization mode.')

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / sys.argv[1] if len(sys.argv)>1 else ROOT / 'research_round4' / 'audits' / 'general'
OUT.mkdir(parents=True, exist_ok=True)
results = {}

def record(name, actual, claimed, method):
    results[name] = {'actual': str(actual), 'claimed': str(claimed),
                     'verdict': 'PASS' if actual == claimed else 'FAIL', 'method': method}

# Scalar capacity gaps: reconstruct C from adjacent coefficients.
c = {1:F(1), 2:F(17,16), 3:F(3,2), 4:F(11,5), 5:F(3)}
targets = {3:F(59,40), 4:F(87,40), 5:F(119,40)}
claimed_gaps = {3:F(81,1600), 4:F(369,1600), 5:F(81,1600)}
for q in targets:
    record(f'first_gap_q{q}', targets[q]**2-(q-1)*c[q-1], claimed_gaps[q], 'Square rational proposed root bound; subtract independently assembled fiber coefficient')
c2 = {1:F(1), 2:F(101,100), 3:F(57,40), 4:F(207,100), 5:F(72,25), 6:F(19,5), 7:F(24,5)}
gaps = {3:F(243,31250), 4:F(5761,1000000), 5:F(8641,1000000), 6:F(32401,1000000), 7:F(230401,1000000)}
for q in gaps:
    record(f'sharp_gap_q{q}', (c2[q]-F(1,1000))**2-(q-1)*c2[q-1], gaps[q], 'Exact adjacent coefficient reconstruction')

for k,b,t,coef,expected_n,expected_margin in [
    (5,15,450,F(11,5),6568408355712890625,F(117793456512450969376,3)),
    (6,23,6348,F(72,25),37608910510519071039902074217516707306379521,F(68925828964323664149419624101576583553901223087,15))]:
    n = b**(2**(k-1))
    delta = 1-F(k*k*(k-1))*coef/(b*b)
    # Direct unit-weight distance sum, rather than trusting a closed margin.
    raw = 2*sum((delta*n-d)*(t-d) for d in range(1,t))-(k-1)*n*t
    normalized = raw/t
    record(f'N_k{k}',n,expected_n,'Exact integer exponentiation')
    record(f'margin_k{k}',normalized,expected_margin,'Sum every unit-weight distance term exactly, then normalize by t')
    results[f'delta_k{k}'] = str(delta)

r,k = sp.symbols('r k')
identities = {
    'tail_coefficient': ((r-1/r)**2-(r+1)*(r-1-1/(r-1)), 1/r**2+2/(r-1),r,6),
    'delta_tail': ((k*(k-2)-1)**2-k*k*(k-1)*(k-3-1/(k-3)),2*k*k/(k-3)+4*k+1,k,8),
}
for name,(lhs,rhs,var,lower) in identities.items():
    diff=sp.cancel(lhs-rhs)
    record(name, diff, sp.Integer(0), 'Independent polynomial/rational simplification')
    samples={}
    for x in [0,1,lower,lower+1,100000]:
        if x<lower:
            samples[str(x)]='outside the stated theorem domain; not a counterexample'
        else:
            samples[str(x)]=str(sp.cancel(lhs.subs(var,x)-rhs.subs(var,x)))
            assert sp.cancel(lhs.subs(var,x)-rhs.subs(var,x)) == 0
    results[name]['samples']=samples
record('delta_numerator_k6',23**2-36*5*c2[5],F(53,5),'Exact coefficients at k=6')
record('delta_numerator_k7',34**2-49*6*c2[6],F(194,5),'Exact coefficients at k=7')

# Legacy Lemma 1: smallest b with choose(b,2)>n-2, derived by integer loop.
def forbidden_b(n):
    b=1
    while comb(b,2)<=n-2: b+=1
    return b
def printed_b(n):
    b=1
    while b*(b-1)<2*(n-2): b+=1
    return b
legacy=[]
for n in range(3,2001):
    b=forbidden_b(n)
    closed=(1+isqrt(8*n-15))//2+1
    assert b==closed
    if printed_b(n)!=b: legacy.append({'n':n,'printed_b':printed_b(n),'strict_b':b})
results['legacy_rounding']={'first_failure':legacy[0],'failures_through_2000':legacy,'scope':'The printed ceiling does not implement a strict inequality when the root is integral.'}

# Theorem 2's literal fractional averages versus integer pigeonhole counts.
def legacy_fractional_b(n): return F(n*(n-3),36*(n-1))
def legacy_integer_b(n):
    count=comb((n+2)//3,2)
    return (count+2*(n-1)-1)//(2*(n-1))
for name,bfun,expected in [('fractional',legacy_fractional_b,2631),('integer',legacy_integer_b,2557)]:
    first=next(n for n in range(3,3001) if F(bfun(n)*(bfun(n)-1),2)>n-2)
    record('legacy_2593_first_'+name,first,expected,'Exact scan of the displayed model; not an optimization of the grid Ramsey number')
record('legacy_2593_fractional_margin',legacy_fractional_b(2593)*(legacy_fractional_b(2593)-1)/2-2591,F(-161026416287,4353564672),'Substitute n=2593 into the literal fractional formula')
record('legacy_2593_integer_margin',comb(legacy_integer_b(2593),2)-2591,37,'Integer pigeonhole rounding at both levels gives s=865 and B=73')

# Re-derive the existing corollary's k=3 case without external Golomb tables.
record('corollary_k3_table_free_margin',F(135*80)-F(81*81-1,3)-2*729,F(21466,3),'Unit-weight partition with N=729, t=81 and each difference cap=66; the written proof gives this cap')
matrix=[[(x-y)%3 for y in range(3)] for x in range(3)]
corners=[((x,y),(x+d,y),(x+d,y+d)) for d in range(1,3) for x in range(3-d) for y in range(3-d)]
bad=[C for C in corners if len({matrix[x][y] for x,y in C})==1]
record('legacy_counterexample_bad_corners',len(bad),0,'All directed corners of literal 3 by 3 coloring')
results['legacy_counterexample']={'matrix':matrix,'all_corners':corners,'diagonal_color':0,'forced_blue_cells':[[1,0],[2,1]],'blue':1,'n':3,'printed_b':printed_b(3),'correct_b':forbidden_b(3)}

def min_nonnegative_intervals(count,capacity):
    # Explicit sorted list rather than claimant quotient formula.
    return sum(j//capacity for j in range(count))
historical={}
for typ in ['adjacent','alternate']:
    for n in range(3,2001):
        s=(n+2)//3
        count=s-1 if typ=='adjacent' else s-1+(s-1)//2
        fixed=s if typ=='adjacent' else s+(s-1)//2+1
        scale=1 if typ=='adjacent' else 2
        minimum=fixed+min_nonnegative_intervals(count,2*(forbidden_b(n)-1))
        if minimum>scale*n:
            historical[typ]={'first_side':n,'b':forbidden_b(n),'count':count,'minimum':minimum,'bound':scale*n,'margin':minimum-scale*n}
            break
record('historical_adjacent_side',historical['adjacent']['first_side'],1804,'Exhaustive n=3 upward using repaired strict threshold and explicit packed intervals')
record('historical_alternate_side',historical['alternate']['first_side'],1573,'Exhaustive n=3 upward using repaired strict threshold and explicit packed intervals')
results['historical_details']=historical

# Baseline setup and declared sensitivity model only; no new profile search.
table=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
def lookup(m):return max(j for j,v in enumerate(table) if v<=m)
def prefix(caps):
    out=[0]
    for d,cap in enumerate(caps,1):
        for _ in range(cap):out.append(out[-1]+d)
    return out
def excludes(n,s,pref,c_only=None):
    ans=[]
    for c in ([c_only] if c_only is not None else range(1,s)):
        H=c*s-c*(c+1)//2
        if H>=len(pref) or 2*pref[H]>(n-1)*c*(c+1):ans.append(c)
    return ans
setup={}
for V,expected in [(48,159),(46,156),(45,154)]:
    pref=prefix([V]*463)
    s=next(s for s in range(2,465) if excludes(464,s,pref))
    record(f'uniform_setup_V{V}',s-1,expected,'Explicit allowed-difference multiset; all rank gaps at each candidate cardinality')
    setup[str(V)]={'bound':s-1,'exclusion_rank_gaps':excludes(464,s,pref),'predecessor_all_gaps_pass':not excludes(464,s-1,pref)}
ladder=[]
for n in range(450,466):
    pref=prefix([min(45,2*lookup(n-d)) if d<=27 else 2*lookup(n-d) for d in range(1,n)])
    if excludes(n,(n+2)//3,pref):ladder.append(n)
record('old_conditional_ladder',ladder,[463,464,465],'Exact declared cap-45 prefix, all c at n=450..465')
thresholds={}
for mode in ['all_c','fixed_c8']:
    for r0 in range(28):
        pref=prefix([min(45 if d<=r0 else 46,2*lookup(464-d)) if d<=27 else 2*lookup(464-d) for d in range(1,464)])
        valid=excludes(464,155,pref,8 if mode=='fixed_c8' else None)
        if valid:thresholds[mode]={'earliest_shaves':r0,'c':valid};break
record('sensitivity_reoptimized',thresholds['all_c']['earliest_shaves'],17,'Declared prefix-shave model only; all c=1..154')
record('sensitivity_fixed8',thresholds['fixed_c8']['earliest_shaves'],18,'Same declared prefix-shave model; c=8 fixed')
results['setup']={'uniform':setup,'sensitivity':thresholds}

# The supplied theorem 5 states 2b-1 but its earlier argument proves 2(b-1).
for cap_label,cap in [('valid',2*(forbidden_b(772)-1)),('printed_weak',2*forbidden_b(772)-1)]:
    s=(772+2)//3; c=12; H=c*s-c*(c+1)//2
    minimum=sum((j+cap-1)//cap for j in range(1,H+1))
    upper=(772-1)*c*(c+1)//2
    results[f'legacy_772_{cap_label}']={'cap':cap,'H':H,'packed_distance_sum':minimum,'uncorrected_neighbor_upper':upper,'margin':minimum-upper}

pref=prefix([2*lookup(493-d) for d in range(1,493)])
H=12*165-12*13//2
results['legacy_493']={'H':H,'packed_mass':pref[H],'uncorrected_upper':492*78,'repaired_upper':492*78-2*comb(13,3),'repaired_margin':pref[H]-(492*78-2*comb(13,3))}
assert results['legacy_493']['repaired_margin']==32
assert results['legacy_772_valid']['margin']+2*comb(13,3)==338

# Supplemental bounded audit of the source's odd-prime construction instances.
prime_checks=[]
for p in [3,5,7,11,13,17,19,23,29,31]:
    assert all(p%d for d in range(2,isqrt(p)+1))
    S=[2*p*i+(i*i)%p for i in range(p)]
    differences=[S[j]-S[i] for i in range(p) for j in range(i+1,p)]
    assert len(set(differences))==comb(p,2) and S==sorted(set(S)) and max(S)-min(S)<2*p*p
    region={(x,y):(0 if x==y else 1) for x in S for y in S if x>=y}
    corner_count=0
    for x,y in region:
        for z in S:
            d=z-x
            if d>0 and (z,y) in region and (z,y+d) in region:
                corner_count+=1
                assert len({region[x,y],region[z,y],region[z,y+d]})>1
    prime_checks.append({'p':p,'marks':len(S),'span':S[-1]-S[0],'region_cells':len(region),'all_corners':corner_count,'bad_corners':0})
results['prime_family_finite_checks']=prime_checks

# R3=465 tent certificate, direct correlation expansion.
w=[min(i,94-i) for i in range(1,94)]
a=[sum(w[i]*w[i+d] for i in range(93-d)) for d in range(93)]
score=sum((465-d-18*(24 if d<=39 else 23))*a[d] for d in range(1,93))-465*a[0]
for name,actual,expected in [('tent_a0',a[0],69231),('tent_P',sum(a[1:40]),2038439),('tent_Q',sum(a[40:]),366786),('tent_D',sum(d*a[d] for d in range(1,93)),53496528),('tent_score',score,285630)]:
    record(name,actual,expected,'Direct integer products of all original tent weights')

results['source_hashes']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'research_round3'/'L-free Grid_Upper bound Research.pdf',ROOT/'2502.05162v1.pdf',ROOT/'research_round2'/'round2_report.tex',ROOT/'research_20260909'/'grid_L_upper_bounds.tex']}
results['provenance']={'python':platform.python_version(),'python_optimize':sys.flags.optimize,'assertions_active':__debug__,'arithmetic':'integers, fractions.Fraction, SymPy exact symbolic expressions','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'claimant_code_imported':False,'scope':'Finite arithmetic and displayed rational identities only. Universal inequalities need the accompanying written proof.'}
(OUT/'exact_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for name,row in results.items():
    if isinstance(row,dict) and 'verdict' in row:
        print(f"CLAIM: {name} | MY VALUE: {row['actual']} | THEIR VALUE: {row['claimed']} | VERDICT: {row['verdict']} | METHOD: {row['method']}")
print(json.dumps({x:results[x] for x in ['historical_details','legacy_counterexample','legacy_772_valid','legacy_772_printed_weak']},indent=2))
