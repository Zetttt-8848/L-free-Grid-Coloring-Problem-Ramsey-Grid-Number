"""Bounded discovery: do Golomb splitting + the six-mark rule suffice?"""
import itertools,json,random
from pathlib import Path
from pysat.solvers import Solver

RNG=random.Random(20260911)

def ruler(n,m,avoid):
    marks=[]; diffs=set()
    candidates=list(set(range(n))-set(avoid)); RNG.shuffle(candidates)
    for x in candidates:
        new=[abs(x-y) for y in marks]
        if len(set(new))==len(new) and not(diffs & set(new)):
            marks.append(x); diffs.update(new)
            if len(marks)==m: return sorted(marks)
    return None

def six(B,C):
    for L,R in [(set(B),set(C)),(set(C),set(B))]:
        dl={b-a:a for a,b in itertools.combinations(sorted(L),2)}
        dr={b-a:a for a,b in itertools.combinations(sorted(R),2)}
        for h in dl.keys() & dr.keys():
            p,q=dl[h],dr[h]
            if any(p<u<q and u+h in L for u in R):return True
    return False

def instance(B,C):
    S=sorted(B+C); ss=set(S)
    cells=[(v,u) for v in S for u in S if u<=v]
    ix={q:i+1 for i,q in enumerate(cells)}
    corners=[]
    for d in sorted({v-u for u,v in itertools.combinations(S,2)}):
        starts=[u for u in S if u+d in ss]
        for y in starts:
            for x in starts:
                if y<=x: corners.append(((x,y),(x+d,y),(x+d,y+d)))
    clauses=[]
    for tr in corners:
        ids=[ix[q] for q in tr]
        clauses.extend([ids,[-a for a in ids]])
    pins={**{(b,b):0 for b in B},**{(c,c):1 for c in C}}
    clauses.extend([[ix[q] if v else -ix[q]] for q,v in pins.items()])
    return cells,corners,clauses,pins

def propagate(corners,pins):
    colors=dict(pins); steps=[]
    while True:
        changed=False
        for tr in corners:
            known=[(q,colors[q]) for q in tr if q in colors]
            if len(known)==3 and len({x[1] for x in known})==1:
                return dict(steps=steps,conflict=tr)
            if len(known)==2 and known[0][1]==known[1][1]:
                q=next(q for q in tr if q not in colors)
                value=1-known[0][1]; colors[q]=value
                steps.append(dict(point=q,color=value,corner=tr));changed=True
        if not changed:return None

counts=dict(attempts=0,ruler_pairs=0,six_free=0,sat=0,unsat=0)
found=None
for attempt in range(3000):
    counts['attempts']+=1
    n,m=RNG.choice([(25,5),(35,6),(50,7),(70,8)])
    B=ruler(n,m,[])
    if B is None:continue
    C=ruler(n,m,B)
    if C is None:continue
    counts['ruler_pairs']+=1
    if six(B,C):continue
    counts['six_free']+=1
    cells,corners,clauses,pins=instance(B,C)
    chain=propagate(corners,pins)
    if chain is not None:
        found=dict(B=B,C=C,source='direct forced-color contradiction',**chain)
        break
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        ok=solver.solve()
    counts['sat' if ok else 'unsat']+=1
    if not ok:
        found=dict(B=B,C=C,source='solver negative only; not a proved counterexample')
        break
result=dict(purpose='bounded route discrimination, not a grid bound',seed=20260911,
            counts=counts,found=found)
Path(__file__).with_name('mixed_rule_discriminator.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
