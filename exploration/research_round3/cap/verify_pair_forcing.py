from pathlib import Path
from itertools import combinations
import json
OUT=Path(__file__).parent
data=json.loads((OUT/'pair_forcing_certificate.json').read_text())
expected=set();counter=0
for size,r in data['rulers'].items():
    assert len(r)==int(size) and r==sorted(set(r)) and r[0]==0
    diffs=[y-x for x,y in combinations(r,2)]
    assert len(diffs)==len(set(diffs))
    for reflect in [False,True]:
        for sh in range(1,463-r[-1]):
            other=[sh+(r[-1]-x if reflect else x) for x in r]
            if not set(other)&set(r):expected.add((int(size),reflect,sh))
seen=set();ap5free=[]
def geometric(tri,F):
    p,q,r=map(tuple,tri)
    gap=q[0]-p[0]
    return gap>0 and q[1]==p[1] and r==(q[0],p[1]+gap) and all(x in F and y in F and x>=y for x,y in (p,q,r))
for row in data['cases']:
    key=(row['order'],row['reflected'],row['shift']);assert key in expected and key not in seen;seen.add(key)
    blue=data['rulers'][str(row['order'])]
    green=[row['shift']+(blue[-1]-x if row['reflected'] else x) for x in blue]
    F=set(blue+green);assert sorted(F)==row['F'] and max(F)-min(F)<=462
    assign={(x,x):0 for x in blue};assign.update({(x,x):1 for x in green})
    for step in row['steps']:
        p=tuple(step['point']);tri=list(map(tuple,step['corner']))
        assert geometric(tri,F) and p in tri and p not in assign
        rest=[q for q in tri if q!=p]
        assert len(rest)==2 and all(q in assign for q in rest)
        assert assign[rest[0]]==assign[rest[1]]==1-step['color']
        assign[p]=step['color'];counter+=1
    tri=list(map(tuple,row['conflict']));assert geometric(tri,F) and all(p in assign for p in tri)
    assert len({assign[p] for p in tri})==1
    apcount=0
    for x,y in combinations(sorted(F),2):
        step=y-x
        if all(x+j*step in F for j in (2,3,4)):apcount+=1
    assert apcount==row['five_ap_count']
    if not apcount:ap5free.append(key)
assert seen==expected
result={'status':'PASS','cases':len(seen),'verified_forcing_steps':counter,'five_ap_free_unions':len(ap5free),'first_order24_AP5_free':next((x for x in ap5free if x[0]==24),None),'coverage':'every specified disjoint translation/reflection, no solver used'}
(OUT/'pair_forcing_checked.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
