"""Independent literal finite checks of the analytic reflected-Sidon family.

No loops over the ambient interval: every physical directed L in V(A) is
enumerated by its x, y and endpoint x+d in the mark set.
"""
import json
from collections import Counter
from pathlib import Path

def verify(r, family):
    B=({0}|{5**i for i in range(1,r+1)}) if family=='powers' else {(r*r+1)*i+i*i for i in range(r+1)}
    t=5*max(B)
    A=sorted(B|{t-b for b in B}); marks=set(A)
    cells={(x,y):int(x+y==t) for x in A for y in A if y<x}
    Ls=0
    for x,y in cells:
        for end in A:
            d=end-x
            if d>0 and y+d in marks:
                triple=[cells[x,y],cells[end,y],cells[end,y+d]]
                assert len(set(triple))==2
                assert triple==[0,1,0]
                Ls+=1
    classes={}
    for (x,y),e in cells.items():classes.setdefault((x-y,e),set()).add(y)
    # Check all Golomb start classes directly, including repeated-endpoint cases.
    for C in classes.values():
        diffs=[b-a for a in C for b in C if a<b]
        assert len(diffs)==len(set(diffs))
    # Enumerate all source-colored pairs and their forced target, not just t.
    requests={}
    for (h,e),C in classes.items():
        for u in C:
            for v in C:
                if v>u:
                    target=h+v-u
                    assert u in classes.get((target,1-e),set())
                    requests.setdefault((target,e),Counter())[u]+=1
    largest=0
    for (target,e),counts in requests.items():
        for u,m in counts.items():
            between=sum(u<a<u+target for a in A)
            assert m<=between<=len(A)-2
            largest=max(largest,m)
        assert sum(m*m for m in counts.values()) <= (len(A)-2)*sum(counts.values())
    counts=requests[t,0]
    assert counts==Counter({0:2*r})
    assert classes[t,1]=={0}
    expected={(t-2*b,0):Counter({b:2*(r-i)}) for i,b in enumerate(sorted(B)) if i<r}
    assert requests==expected
    R=sum(sum(c.values()) for c in requests.values())
    E=sum(sum(m*m for m in c.values()) for c in requests.values())
    assert R==r*(r+1) and E==2*r*(r+1)*(2*r+1)//3 and Ls==R
    return dict(family=family,r=r,marks=A,span=t,source_cells=len(cells),directed_Ls=Ls,
                global_request_count=R,global_request_energy=E,
                target=t,request_count=2*r,request_energy=4*r*r,
                target_union=1,max_collision=largest,
                formula='z(x,y)=1 iff x+y=span; otherwise 0')

rows=[verify(r,'powers') for r in range(1,13)]+[verify(r,'polynomial') for r in (1,2,4,8,16,32,40)]
out=dict(status='FINITE-CHECKED examples; universal statements require THEORY.md',examples=rows)
Path(__file__).with_name('collision_examples.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 19 examples, all physical Ls, all Golomb classes, all forcing targets, exact global energies.')
