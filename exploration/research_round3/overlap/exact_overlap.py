from itertools import combinations
from pathlib import Path
import json
OUT=Path(__file__).parent
def subsets(S):
    S=sorted(S)
    return [set(S[i] for i in range(len(S)) if mask>>i&1) for mask in range(1<<len(S))]
def image(B,d):return {(v+d,u) for u,v in combinations(sorted(B),2)}
tests=0;sumoverlap=0
for n in range(1,8):
    for A in subsets(range(1,n+1)):
        fibers={d:{x for x in A if x+d in A} for d in range(1,n)}
        for d,e in combinations(range(1,n),2):
            delta=e-d
            X={x for x in A if x+d in A and x+e in A}
            Y={x for x in A if x+delta in A and x+e in A}
            J=sum(u<q for u in X for q in Y)
            v=min(len(fibers[d]),len(fibers[e]),len(fibers[delta]))
            assert len(X)<=v and len(Y)<=v
            for Bd in subsets(fibers[d]):
                Qd=image(Bd,d)
                for Be in subsets(fibers[e]):
                    Qe=image(Be,e)
                    C=Bd&Be;D={q for q in Be if q+delta in Bd}
                    raw=len(Qd&Qe);ordered=sum(u<q for u in C for q in D)
                    assert raw==ordered and raw<=min(len(Qd),len(Qe),J,v*v)
                    tests+=1;sumoverlap+=raw
literal=json.loads(Path('research_round2/certificates/four_multi_overlap.json').read_text())['witness']
colors={(x,y):c for x,y,c in literal['colors']};A=set(literal['marks'])
d,e=literal['d'],literal['e']
Bd={u for u in A if u+d in A and colors[(u+d,u)]==1}
Be={u for u in A if u+e in A and colors[(u+e,u)]==1}
Qd=image(Bd,d);Qe=image(Be,e);M=len(Qd)+len(Qe);O=len(Qd&Qe)
assert (M,O,len(Qd|Qe))==(2,1,1)
result={'status':'PASS','range_n':[1,7],'universe':'all source subsets, all positive d<e<n, all independent subsets B_d of F_d and B_e of F_e; no quotient or pruning','cases':tests,'sum_overlap':sumoverlap,'literal_saturation':{'Bd':sorted(Bd),'Be':sorted(Be),'M':M,'O':O,'union':len(Qd|Qe)}}
(OUT/'exact_overlap.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'enumeration.log').write_text(f'RANGE n=1..7; all source and fiber subsets; no pruning or symmetry\nCASES {tests}\nSTATUS PASS\nRUN COMPLETE\n')
print(json.dumps(result,indent=2))
