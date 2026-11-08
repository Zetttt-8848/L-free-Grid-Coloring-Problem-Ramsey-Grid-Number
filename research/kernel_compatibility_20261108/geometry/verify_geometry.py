"""Finite independent checks of physical six-class geometry and joint packing."""
from itertools import combinations,product
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def golomb(marks):
    ds=[v-u for u,v in combinations(sorted(marks),2)]
    return len(ds)==len(set(ds))


def classes(rows):
    n=len(rows);result=[]
    for d in range(1,n):
        groups={(c,b):[] for c in range(3) for b in range(3) if c!=b}
        for u in range(n-d):
            c=rows[u][u]
            if rows[u+d][u+d]!=c:continue
            b=rows[u+d][u]
            assert b!=c
            groups[c,b].append(u)
        occupied=sum(groups.values(),[])
        assert len(occupied)==len(set(occupied))
        assert all(golomb(v) for v in groups.values())
        expected=sum(rows[u][u]==rows[u+d][u+d] for u in range(n-d))
        assert len(occupied)==expected
        result.append({'d':d,'R_d':expected,'classes':[
            {'diagonal_color':c,'completion_color':b,'marks':v}
            for (c,b),v in groups.items()]})
    return result


def check_small_geometry():
    # Full weak triangle of side4 contains exactly the cells needed by the
    # diagonal/completion argument. No upper-triangle extension is asserted.
    n=4;pts=[(x,y) for x in range(n) for y in range(x+1)]
    triples=[]
    for ids in combinations(range(len(pts)),3):
        a,b,c=sorted(pts[i] for i in ids)
        if a[1]==b[1] and b[0]==c[0] and b[0]-a[0]==c[1]-b[1]>0:
            triples.append(ids)
    proper=0
    for colors in product(range(3),repeat=len(pts)):
        if any(colors[i]==colors[j]==colors[k] for i,j,k in triples):continue
        rows=[[None]*n for _ in range(n)]
        for (x,y),c in zip(pts,colors):rows[x][y]=c
        classes(rows);proper+=1
    return {'positions':len(pts),'physical_Ls':len(triples),'assignments':3**len(pts),
            'proper_colorings_checked':proper,'domain':'full weak4 triangle; no symmetry quotient'}


def exact_small_packing():
    p=12;good=[];card=[0]*(1<<p);best_subset=[0]*(1<<p)
    for mask in range(1<<p):
        marks=[i for i in range(p) if mask>>i&1]
        if golomb(marks):
            good.append(mask);card[mask]=len(marks);best_subset[mask]=mask
    for bit in range(p):
        for mask in range(1<<p):
            if mask>>bit&1 and card[mask^(1<<bit)]>card[mask]:
                card[mask]=card[mask^(1<<bit)];best_subset[mask]=best_subset[mask^(1<<bit)]
    # card[mask] now equals maximum Golomb subset size in that literal mask.
    scores=[(a.bit_count()+card[((1<<p)-1)^a],a,best_subset[((1<<p)-1)^a]) for a in good]
    value,a,b=max(scores)
    assert value==9 and not a&b
    g12=card[(1<<12)-1];g11=card[(1<<11)-1]
    assert (g12,g11)==(5,4) and value==g12+g11<2*g12
    return {'positions':12,'classes':2,'subsets_checked':1<<p,
            'golomb_subsets':len(good),'separate_capacity':2*g12,
            'joint_capacity':g12+g11,'exact_optimum':value,
            'witness':[[i for i in range(p) if m>>i&1] for m in (a,b)]}


def main():
    path=ROOT/'.agents/skills/directed-l-grid-research/assets/paper20.json'
    rows=json.loads(path.read_text(encoding='utf-8'))['rows'];n=len(rows)
    assert n==20 and all(len(r)==n for r in rows)
    assert all(type(c) is int and c in range(3) for r in rows for c in r)
    corners=0
    for x in range(n):
        for y in range(n):
            for d in range(1,min(n-x,n-y)):
                assert len({rows[x][y],rows[x+d][y],rows[x+d][y+d]})>1
                corners+=1
    paper_classes=classes(rows)
    record={'status':'PASS','paper20_corners':corners,'paper20_six_classes':paper_classes,
            'small_geometry':check_small_geometry(),'small_packing':exact_small_packing(),
            'scope':'Finite formula audits; universal claims use the written proof',
            'sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (path,Path(__file__),HERE/'SIX_CLASS_LEMMA.md')}}
    (HERE/'geometry_verification.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:record[k] for k in ('status','paper20_corners','small_geometry','small_packing')}))


if __name__=='__main__':main()
