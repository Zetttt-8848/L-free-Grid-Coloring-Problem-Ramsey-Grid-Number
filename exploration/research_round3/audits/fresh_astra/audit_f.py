"""Fresh four-color certificate verifier, with no author imports.

Autocorrelations use exact Newton finite-difference summation, independent of
the supplied polynomial-power-sum and NTT programs. Capacity runs are witnesses,
not trusted optimization outputs. This program does not certify optimality.
"""
import bisect
import hashlib
import itertools
import json
import math
import pathlib
import time

ROOT=pathlib.Path(__file__).resolve().parents[3]
OUT=pathlib.Path(__file__).resolve().parent
SOURCE=ROOT/'research_round3/four/r4_profile_endpoint_21991300.json'

def tau(s):
    values=[]
    for c in range(1,s):
        # H is rebuilt as the sum of rank-j pair counts, in closed form.
        H=c*s-c*(c+1)//2
        numerator=H*(H+1)+2*(c+1)*c*(c-1)//3-1
        values.append(numerator//(c*(c+1)))
    best=max(values)
    return best,[c for c,v in enumerate(values,1) if v==best]

def correlation(t,d):
    # For f(i)=i(t+1-i)(i+d)(t+1-i-d), Newton's finite difference
    # expansion f(i)=sum_j Delta^j f(0) binom(i,j) has degree four.
    # Hockey-stick summation gives sum_{i=0}^m f(i); f(0)=0.
    m=t-d
    row=[i*(t+1-i)*(i+d)*(t+1-i-d) for i in range(5)]
    value=0
    for j in range(5):
        value+=row[0]*math.comb(m+1,j+1)
        row=[b-a for a,b in zip(row,row[1:])]
    return value

def direct_correlation(t,d):
    return sum(i*(t+1-i)*(i+d)*(t+1-i-d) for i in range(1,t-d+1))

def self_tests():
    # Every lag including t-1, and the empty support limit d=t.
    for t in range(1,51):
        for d in range(t+1):
            assert correlation(t,d)==direct_correlation(t,d)
    # Endpoint identities, including overlaps of the endpoint blocks.
    cases=0
    for size in range(2,9):
        for A in itertools.combinations(range(9),size):
            for c in range(1,size):
                direct=sum(A[i+j]-A[i] for j in range(1,c+1) for i in range(size-j))
                endpoint=sum((c-i)*(A[size-1-i]-A[i]) for i in range(c))
                bound=(A[-1]-A[0])*c*(c+1)//2-2*math.comb(c+1,3)
                assert direct==endpoint and direct<=bound
                cases+=1
    # Exact small Golomb thresholds: Q(0)=1, Q(1)=2, Q(2)=2.
    small=[tau(s)[0] for s in range(2,7)]
    assert [bisect.bisect_left(small,S)+1 for S in range(3)] == [1,2,2]
    return cases

def main():
    start=time.perf_counter()
    identity_cases=self_tests()
    cert=json.loads(SOURCE.read_text())
    n,t=cert['n'],cert['t']
    assert n==21991300 and t==36000 and n>=t
    # A valid cap suffices. Scan the full admissible c range for each supplied
    # threshold size; additionally prove earlier sizes cannot enter by monotonicity.
    thresholds=[]; maximizers=[]
    for s in range(4600,4901):
        value,params=tau(s)
        thresholds.append(value); maximizers.append(params)
    assert all(a<b for a,b in zip(thresholds,thresholds[1:]))
    previous_tau=tau(4599)[0]
    assert previous_tau < thresholds[0]
    def Q(S):
        index=bisect.bisect_left(thresholds,S)
        assert index<len(thresholds) and S>previous_tau
        return 4599+index
    checked_transitions=[]
    for record in cert['golomb_transition_records_used']:
        index=record['excluded_size']-4600
        independent=dict(excluded_size=index+4600,max_span=thresholds[index],maximizing_c=maximizers[index])
        assert independent==record
        checked_transitions.append(independent)
    print('Golomb thresholds rebuilt from rank-neighbor counts',flush=True)
    expanded=[]; rows=[]
    next_d=1
    max_frontier=0
    for row in cert['runs']:
        lo,hi,K,c=(row[k] for k in ['lo','hi','K','c'])
        assert lo==next_d and lo<=hi<t and 1<=c<K+1
        L=n-lo-1
        H=c*(K+1)-c*(c+1)//2
        remaining=H; total=0; h=0; q_used=set()
        while remaining:
            h+=1
            assert h<=L
            q=Q(L-h); q_used.add(q)
            take=min(2*q,remaining)
            total+=take*h
            remaining-=take
        correction=4*math.comb(c+1,3)
        rhs=L*c*(c+1)-correction
        lhs=2*total
        margin=lhs-rhs
        assert margin>0
        measured=dict(H=H,K=K,c=c,doubled_endpoint_correction=correction,hi=hi,
                      lhs=lhs,lo=lo,longest_span=L,margin=margin,minsum=total,
                      profile_frontier=h,rhs=rhs)
        assert measured==row, ('run mismatch',lo,measured,row)
        rows.append(dict(lo=lo,hi=hi,K=K,c=c,margin=margin,frontier=h,q_min=min(q_used),q_max=max(q_used)))
        expanded.extend([K]*(hi-lo+1))
        next_d=hi+1
        max_frontier=max(max_frontier,h)
    assert next_d==t and len(expanded)==35999 and len(rows)==561
    print('561 strict run inequalities independently checked',flush=True)
    correlations=[correlation(t,d) for d in range(t)]
    assert all(a>0 for a in correlations)
    # Direct evaluations verify the finite-difference sum at extreme and interior lags.
    for d in [0,1,2,3,17999,18000,18001,35997,35998,35999]:
        assert correlations[d]==direct_correlation(t,d)
    terms=[(n-d-48*K)*correlations[d] for d,K in enumerate(expanded,1)]
    a0=correlations[0]
    lhs=2*sum(terms); rhs=3*n*a0; margin=lhs-rhs
    assert (a0,correlations[1],correlations[-1])==(cert['a0'],cert['a1'],cert['a_last'])
    assert (lhs,rhs,margin)==(cert['doubled_lhs'],cert['doubled_rhs'],cert['doubled_margin'])
    assert margin>0 and 22006246-n==14946
    # Independently define serialization for our arrays and save them as evidence.
    arrays=dict(correlations=correlations,K=expanded,score_terms=terms)
    payload=json.dumps(arrays,separators=(',',':'))+'\n'
    (OUT/'F_exact_arrays.json').write_text(payload)
    result=dict(verdict='PASS',scope='561 valid run witnesses and all 35999 exact score terms; no outer-c optimality claim',
                bound=n,window=t,runs=len(rows),distances=len(terms),a0=a0,a1=correlations[1],a_last=correlations[-1],
                doubled_lhs=lhs,doubled_rhs=rhs,doubled_margin=margin,improvement=22006246-n,
                run_margin_min=min(r['margin'] for r in rows),run_margin_max=max(r['margin'] for r in rows),
                max_frontier=max_frontier,thresholds_checked=301,golomb_c_pairs_checked=sum(range(4599,4900)),
                golomb_transition_records=checked_transitions,
                endpoint_identity_cases=identity_cases,
                run_witnesses=rows,
                input_sha256={str(SOURCE.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
                array_sha256=hashlib.sha256(payload.encode()).hexdigest(),runtime_seconds=time.perf_counter()-start)
    (OUT/'F_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['run_witnesses','golomb_transition_records']},indent=2),flush=True)

if __name__=='__main__':
    main()
