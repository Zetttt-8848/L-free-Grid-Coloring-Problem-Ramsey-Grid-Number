"""Fresh exact scalar and bounded geometry checks for the universal G proof.
Universal implications are audited in REVIEW.md, not inferred from this run.
"""
import fractions
import hashlib
import itertools
import json
import math
import pathlib
import time
import sympy as sp

F=fractions.Fraction
ROOT=pathlib.Path(__file__).resolve().parents[3]
OUT=pathlib.Path(__file__).resolve().parent

def c1(q):
    return {1:F(1),2:F(17,16),3:F(3,2),4:F(11,5)}.get(q,F(q-2))

def c2(q):
    if q<=6:
        return {1:F(1),2:F(101,100),3:F(57,40),4:F(207,100),5:F(72,25),6:F(19,5)}[q]
    return F(q-2)-F(1,q-2)

def scalar(k,minus=False):
    b=k*(k-2)-int(minus)
    N=b**(2**(k-1))
    coeff=c2 if minus else c1
    deficit=b*b-k*k*(k-1)*coeff(k-1)
    delta=deficit/(b*b)
    t=2*k*b*b if minus else 10*k*(k-2)**2
    # Computed directly from the summed partition inequality.
    margin=delta*N*(t-1)-F(t*t-1,3)-(k-1)*N
    assert 1<t<=N and margin>0
    assert N<=k**(2**k-2)
    if minus:
        assert deficit >= 1 and b>=3*k
        assert b**(2**(k-3))>=16*k**4
        assert delta*(t-1)-(k-1)>k
    else:
        assert delta >= F(1,5*(k-2)**2)
        assert b**(2**(k-3))>=16*k*k
    return dict(k=k,b=b,N=str(N),t=t,delta=str(delta),margin=str(margin),deficit=str(deficit))

def symbolic_checks():
    r,k,t,d=sp.symbols('r k t d', integer=True)
    identities={
      'tail_capacity':((r-1/r)**2-(r+1)*(r-1-1/(r-1)),1/r**2+2/(r-1)),
      'tail_deficit':((k*(k-2)-1)**2-k*k*(k-1)*(k-3-1/(k-3)),2*k*k/(k-3)+4*k+1),
      'unit_mass':(sp.summation(t-d,(d,1,t-1)),t*(t-1)/2),
      'unit_first_moment':(sp.summation(d*(t-d),(d,1,t-1)),t*(t*t-1)/6),
    }
    results={}
    for label,(left,right) in identities.items():
        assert sp.factor(left-right)==0
        var=r if label=='tail_capacity' else k if label=='tail_deficit' else t
        points=[]
        for value in [0,1,2,6,1000]:
            l=left.subs(var,value); rr=right.subs(var,value)
            defined=not(l.has(sp.zoo,sp.nan,sp.oo,-sp.oo) or rr.has(sp.zoo,sp.nan,sp.oo,-sp.oo))
            if defined:
                assert sp.simplify(l-rr)==0
            points.append(dict(input=value,in_algebraic_domain=defined))
        results[label]=dict(symbolic_difference='0',points=points)
    # Exact algebraic justification of the finite-difference integration used in F.
    i,T,D=sp.symbols('i T D')
    f=lambda v:v*(T+1-v)*(v+D)*(T+1-v-D)
    row=[sp.expand(f(j)) for j in range(5)]
    expansion=0
    for j in range(5):
        falling=sp.prod(i-a for a in range(j))/math.factorial(j)
        expansion+=row[0]*falling
        row=[sp.expand(b-a) for a,b in zip(row,row[1:])]
    assert sp.expand(expansion-f(i))==0
    for point in [0,1,1000]:
        assert (expansion-f(i)).subs({i:point,T:1000,D:1}).expand()==0
    results['F_Newton_quartic_identity']=dict(symbolic_difference='0',exact_points=[0,1,1000])
    return results

def partition_check():
    cases=0
    for n in range(1,7):
        for k in range(1,4):
            for coloring in itertools.product(range(k),repeat=n):
                for t in [1,n]:
                    w=list(range(1,t+1))
                    ac=[sum(w[i]*w[i+d] for i in range(t-d)) for d in range(t)]
                    multiplicities=[sum(coloring[i]==coloring[i+d] for i in range(n-d)) for d in range(1,t)]
                    mass=0; energy=0
                    for z in range(-t,n+1):
                        bycolor=[sum(w[i-z] for i in range(n) if 0<=i-z<t and coloring[i]==c) for c in range(k)]
                        mass+=sum(bycolor)**2
                        energy+=sum(a*a for a in bycolor)
                    assert energy==n*ac[0]+2*sum(ac[d]*multiplicities[d-1] for d in range(1,t))
                    assert mass==n*ac[0]+2*sum((n-d)*ac[d] for d in range(1,t))
                    assert mass<=k*energy
                    cases+=1
    return cases

def rulers():
    results=[]
    for p in [3,5,7,11,13,17,19,23,29,31]:
        assert all(p%d for d in range(2,math.isqrt(p)+1))
        A=[2*p*i+(i*i)%p for i in range(p)]
        assert A==sorted(A) and len(set(A))==p
        diffs=[y-x for x,y in itertools.combinations(A,2)]
        assert len(set(diffs))==len(diffs)
        cells={(x,y):int(x>y) for x in A for y in A if x>=y}
        corners=0
        for y in A:
            for x,z in itertools.combinations([a for a in A if a>=y],2):
                d=z-x
                if (z,y+d) in cells:
                    assert len({cells[x,y],cells[z,y],cells[z,y+d]})>1
                    corners+=1
        N=A[-1]-A[0]+1
        assert N==2*p*p-2*p+2 and N<=2*p*p
        results.append(dict(p=p,marks=A,span=N-1,ambient_N=N,unique_differences=len(diffs),cells=len(cells),corners=corners))
    return results

def main():
    start=time.perf_counter()
    oldgaps=[F(59,40)**2-F(17,8),F(87,40)**2-F(9,2),F(119,40)**2-F(44,5)]
    newgaps=[(c2(q)-F(1,1000))**2-(q-1)*c2(q-1) for q in range(3,8)]
    assert all(a>0 for a in oldgaps+newgaps)
    original=[scalar(k) for k in range(5,13)]
    refined=[scalar(k,True) for k in range(6,13)]
    # Compare only after independent values have been computed.
    other=ROOT/'research_round3/general/minus_one_exact.json'
    claimed=json.loads(other.read_text())
    assert newgaps==[F(a['squared_gap']) for a in claimed['coefficient_checks']]
    assert [{k:v for k,v in a.items() if k!='deficit'} for a in refined]==claimed['scalar_checks']
    assert original[0]['N']=='6568408355712890625'
    assert original[0]['margin']=='117793456512450969376/3'
    assert original[0]['t']==450
    paths=['general/refined_constants_proof.md','general/refined_minus_one.md','general/square_root_barrier.md',
           'general/minus_one_exact.json','report_general.tex','report_four_final.tex']
    result=dict(verdict='PASS',scope='Exact scalar checks for k=5..12 and stated bounded geometries; universal proof separately reconstructed in REVIEW.md',
                old_squared_gaps=list(map(str,oldgaps)),new_squared_gaps=list(map(str,newgaps)),
                first_bound=original,minus_one_bound=refined,
                symbolic_checks=symbolic_checks(),partition_identity_cases=partition_check(),
                rulers=rulers(),
                small_color_comparisons=dict(R3_upper=465,three_power=3**6,R4_inherited_upper=22006246,four_power=4**14),
                input_sha256={f'research_round3/{p}':hashlib.sha256((ROOT/'research_round3'/p).read_bytes()).hexdigest() for p in paths},
                runtime_seconds=time.perf_counter()-start)
    (OUT/'G_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(verdict='PASS',old_squared_gaps=result['old_squared_gaps'],new_squared_gaps=result['new_squared_gaps'],
                         k5=original[0],k6=refined[0],k7=refined[1],partition_identity_cases=result['partition_identity_cases'],
                         symbolic_identities=len(result['symbolic_checks']),literal_rulers=len(result['rulers'])),indent=2))

if __name__=='__main__':
    main()
