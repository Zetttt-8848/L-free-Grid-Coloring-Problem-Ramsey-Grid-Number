"""Exact arithmetic for extremal-shape span cost; no solver dependencies."""
from itertools import combinations
import hashlib
import json
from pathlib import Path

Q=(0,9,33,37,38,97,122,129,140,142,152,191,205,208,252,278,
   286,326,332,353,368,384,403,425)

def golomb(a):
    ds=[b-a for a,b in combinations(sorted(a),2)]
    return len(ds)==len(set(ds))

def old_cap(p):
    return min(p,138+min(6,max(0,p-425)))

def new_cap(p):
    assert 1<=p<=480
    feasible=[t for t in range(7) if 425*t+max(0,t-2)<=t*(p-t)]
    return min(p,138+max(feasible))

def corr(d,N=86):
    return sum(i*(N-i)*(i+d)*(N-i-d) for i in range(1,N-d))

def gap(n,cap):
    return sum((n-d-3*cap(n-d))*corr(d) for d in range(1,85))-n*corr(0)

def occurrence_bound(n):
    W=sum(i*(86-i) for i in range(1,86))
    a0=corr(0)
    S=2*sum((48 if n-d>=426 else 46)*corr(d) for d in range(1,85))
    allowed_m=[m for m in range(n+1) if m*m*W*W<=(n+84)*(m*a0+S)]
    mmax=max(allowed_m)
    allowed_t=[t for t in range(n-425+1)
               if 24*t-t*(t-1)//2<=mmax and 576*t<=mmax*(t+23)]
    tmax=max(allowed_t)
    # Verify the moment identities literally for several occurrence sets,
    # including all possible starts; this tests the exact geometric formula.
    examples=[]
    for starts in ([0],[0,1],list(range(8)),list(range(n-425))):
        multiplicity={}
        for s in starts:
            for q in Q:multiplicity[q+s]=multiplicity.get(q+s,0)+1
        t=len(starts)
        assert sum(multiplicity.values())==24*t
        assert sum(v*v for v in multiplicity.values())==t*(t+23)
        assert len(multiplicity)*(t+23)>=576*t
        examples.append({'starts':starts,'union_size':len(multiplicity),
                         'incidence_second_moment':sum(v*v for v in multiplicity.values())})
    return {'n':n,'W':W,'a0':a0,'S':S,'max_color_class':mmax,
            'max_occurrences_per_orientation':tmax,
            'max_extremal_completion_classes_both_orientations':tmax*(tmax-1),
            'old_independent_extremal_class_count':2*(n-426),
            'literal_moment_examples':examples}

def main():
    assert len(Q)==24 and Q[-1]-Q[0]==425 and golomb(Q)
    ds={b-a for a,b in combinations(Q,2)}
    assert all(d in ds for d in range(1,128)) and 128 not in ds
    pair=[sorted(x+1 for x in Q),sorted(425-x for x in Q)]
    assert set(pair[0]).isdisjoint(pair[1])
    assert all(golomb(a) for a in pair)
    # Literal intersection check for every allowed translation displacement
    # used in the theorem; both orientations have the same differences.
    for d in range(128):
        assert set(Q)&{x+d for x in Q}
    rows=[]
    for p in range(1,481):
        a,b=old_cap(p),new_cap(p)
        assert b<=a
        if a!=b:rows.append({'positions':p,'old':a,'new':b})
    assert rows==[{'positions':p,'old':p-287,'new':p-288} for p in range(428,432)]
    margins=[{'n':n,'old_gap':gap(n,old_cap),'shape_cost_gap':gap(n,new_cap),
              'gain':gap(n,new_cap)-gap(n,old_cap)} for n in (463,464)]
    occurrences=[occurrence_bound(n) for n in (463,464)]
    assert all(r['max_color_class']==164 and r['max_occurrences_per_orientation']==8 for r in occurrences)
    result={'status':'PASS','external_dependencies':[
        {'claim':'G(24)=425 and uniqueness up to reflection','source':'https://blogs.distributed.net/2004/11/','not_recomputed':True},
        {'claim':'G(25)>=480','source':'https://blogs.distributed.net/2008/10/','not_recomputed':True}],
        'optimal_ruler':list(Q),'positive_differences':len(ds),'first_missing_difference':128,
        'two_ruler_packing_in_427_positions':pair,'capacity_changes':rows,'kernel_margins':margins,
        'global_occurrence_counts':occurrences,
        'scope':'Exact finite arithmetic and literal ruler checks; external optimum and uniqueness are cited inputs, not locally proved.',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
