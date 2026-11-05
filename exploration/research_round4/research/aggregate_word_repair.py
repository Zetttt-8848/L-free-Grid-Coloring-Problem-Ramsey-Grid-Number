"""Bounded large-neighborhood construction search for aggregate caps only."""
import bisect,json,time
from pathlib import Path
import numpy as np
from ortools.sat.python import cp_model
root=Path(__file__).resolve().parent
data=json.loads((root/'aggregate_word_probe.json').read_text(encoding='utf-8'));word=data['word'];n=len(word)
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
caps=[0]+[min(n-d,6*(bisect.bisect_right(H,n-d)-1)) for d in range(1,n)]
def profile(w):return [0]+[sum(w[i]==w[i+d] for i in range(n-d)) for d in range(1,n)]
def score(w):return sum(max(0,r-c) for r,c in zip(profile(w),caps))
best=score(word);history=[];rng=np.random.default_rng(2026091105);start=time.monotonic()
for attempt in range(18):
    if best==0:break
    free=sorted(int(x) for x in rng.choice(n,size=65,replace=False));fs=set(free)
    model=cp_model.CpModel();z={i:model.new_int_var(0,2,f'z{i}') for i in free}
    lit={(i,c):model.new_bool_var(f'b{i}_{c}') for i in free for c in range(3)}
    for i in free:
        model.add_exactly_one(lit[i,c] for c in range(3))
        for c in range(3):model.add(z[i]==c).only_enforce_if(lit[i,c])
        model.add_hint(z[i],word[i])
    slacks=[]
    for d in range(1,n):
        if caps[d]>=n-d:continue
        constant=0;terms=[]
        for i in range(n-d):
            j=i+d
            if i not in fs and j not in fs:constant+=word[i]==word[j]
            elif i in fs and j not in fs:terms.append(lit[i,word[j]])
            elif j in fs and i not in fs:terms.append(lit[j,word[i]])
            else:
                eq=model.new_bool_var(f'e{i}_{j}')
                model.add(z[i]==z[j]).only_enforce_if(eq)
                model.add(z[i]!=z[j]).only_enforce_if(eq.negated());terms.append(eq)
        slack=model.new_int_var(0,best,f's{d}');slacks.append(slack)
        model.add(constant+sum(terms)<=caps[d]+slack)
    model.add(sum(slacks)<=best);model.minimize(sum(slacks))
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=1;solver.parameters.num_search_workers=1
    solver.parameters.random_seed=attempt+1;status=solver.solve(model)
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        candidate=word.copy()
        for i in free:candidate[i]=solver.value(z[i])
        value=score(candidate)
        if value<=best:word=candidate;best=value
    history.append(dict(attempt=attempt,solver_status=solver.status_name(status),best_excess=best))
    print(json.dumps(history[-1]),flush=True)
p=profile(word)
out=dict(purpose='bounded construction search, not a nonexistence proof',status='literal aggregate-cap word' if best==0 else 'undecided',
         n=n,seconds=time.monotonic()-start,best_excess=best,history=history,word=word,profile=p[1:],
         violations=[dict(d=d,count=p[d],cap=caps[d]) for d in range(1,n) if p[d]>caps[d]])
(root/'aggregate_word_repair.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
