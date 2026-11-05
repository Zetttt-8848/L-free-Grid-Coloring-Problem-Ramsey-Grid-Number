"""Explore a proved six-mark rule on literal previous candidate families."""
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
prior=json.loads((ROOT/'research_round3/cap/pair_search_log.json').read_text(encoding='utf-8'))

def obstruction(B,C):
    B=set(B); C=set(C)
    for left,right,label in [(C,B,'C_then_B'),(B,C,'B_then_C')]:
        L={v-u:u for u,v in itertools.combinations(sorted(left),2)}
        R={v-u:u for u,v in itertools.combinations(sorted(right),2)}
        for h in sorted(L.keys()&R.keys()):
            p,q=L[h],R[h]
            if p>=q: continue
            for u in sorted(right):
                if p<u<q and u+h in left:
                    return dict(orientation=label,h=h,p=p,u=u,q=q,
                                left_marks=[p,p+h,u+h],right_marks=[u,q,q+h])
    return None

cases=[]
for order,ruler in prior['rulers'].items():
    for reflected in (False,True):
        other=[ruler[-1]-x for x in reversed(ruler)] if reflected else ruler
        for shift in range(1,463-ruler[-1]):
            B=ruler; C=[x+shift for x in other]
            if set(B)&set(C): continue
            cases.append(dict(order=int(order),reflected=reflected,shift=shift,
                              obstruction=obstruction(B,C)))
result=dict(scope='specified literal pairs only; not all Golomb rulers',
            cases=len(cases),detected=sum(x['obstruction'] is not None for x in cases),
            records=cases)
Path(__file__).with_name('mixed_interval_probe.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
print(json.dumps(dict(surviving_cases=[x for x in cases if x['obstruction'] is None],
                      first_examples=[x for x in cases if x['obstruction'] is not None][:3])))
