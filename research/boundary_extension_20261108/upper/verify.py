"""Standard-library verification of explicit geometric potential reversal.

No SAT imports. Enumerates all unordered cell triples, then recognizes the
directed equal-leg L shape. Recomputes energy and parity lower bounds.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import time

HERE=Path(__file__).resolve().parent

def require(ok,message):
    if not ok: raise ValueError(message)

def physical_corners(cells):
    out=[]
    for triple in combinations(cells,3):
        pts=set(triple)
        for x,y in triple:
            for u,v in triple:
                if v==y and u>x and (u,y+u-x) in pts:
                    out.append(((x,y),(u,y),(u,y+u-x)))
    require(len(out)==len(set(out)),'Corner multiplicity')
    return out

def sums(cells,colors,selected):
    out=defaultdict(int)
    for (x,y),c in zip(cells,colors):
        if (x,y) in selected: out[x-y]+=1-2*c
    return dict(sorted(out.items()))

def main():
    started=time.monotonic()
    raw=(HERE/'witnesses.json').read_bytes()
    data=json.loads(raw)
    checks=[]
    for w in data['witnesses']:
        a,q=w['A'],w['Q']
        require(a==sorted(set(a)) and set(q)<=set(a),'Invalid marks')
        cells=[(x,y) for x in a for y in a if y<x]
        require(cells==list(map(tuple,w['cells'])),'Incomplete source')
        corners=physical_corners(cells)
        internal={(x,y) for x,y in cells if x in q and y in q}
        exterior=set(cells)-internal
        before,after=w['before'],w['after']
        for colors in [before,after]:
            require(len(colors)==len(cells) and set(colors)<={0,1},'Bad colors')
            mapping=dict(zip(cells,colors))
            require(all(len({mapping[p] for p in t})>1 for t in corners),'Monochromatic L')
        changes=[p for p,c,d in zip(cells,before,after) if c!=d]
        require(changes==[tuple(w['flipped_cell'])] and changes[0] in internal,'Not single internal flip')
        sq=[sums(cells,c,internal) for c in [before,after]]
        sa=[sums(cells,c,set(cells)) for c in [before,after]]
        se=[sums(cells,c,exterior) for c in [before,after]]
        require(se[0]==se[1],'Exterior changed')
        pq=[sum(v*v for v in s.values()) for s in sq]
        pa=[sum(v*v for v in s.values()) for s in sa]
        require(pq==w['phi_Q'] and pa==w['phi_A'],'Incorrect potential metadata')
        require(pq[1]<pq[0] and pa[1]>pa[0],'Not a reversal')
        counts_a=defaultdict(int); counts_q=defaultdict(int)
        for x,y in cells:
            counts_a[x-y]+=1
            if (x,y) in internal: counts_q[x-y]+=1
        parity_a=sum(v%2 for v in counts_a.values())
        parity_q=sum(v%2 for v in counts_q.values())
        require(pa[0]==parity_a,'Start not globally parity optimal')
        require(pq[1]==parity_q,'End not block-balanced')
        # Every block-balanced coloring has s_Q(d)=0 on even fibers, +/-1 on odd.
        # This relaxed field-aware bound ignores legality, hence remains valid
        # for every legal coloring with the same exterior.
        balanced_bound=0
        terms={}
        for d in counts_a:
            if d not in counts_q: allowed=[0]
            else: allowed=[-1,1] if counts_q[d]%2 else [0]
            cost=min((s+se[0].get(d,0))**2 for s in allowed)
            balanced_bound+=cost
            terms[d]=cost
        require(pa[1]==balanced_bound,'Witness fails to attain balanced lower bound')
        rows=[]
        for x in a[1:]:
            rows.append({'mark':x,
                'before':''.join(str(before[i]) for i,p in enumerate(cells) if p[0]==x),
                'after':''.join(str(after[i]) for i,p in enumerate(cells) if p[0]==x)})
        checks.append({'cells':len(cells),'corners':len(corners),'rows':rows,
            'phi_Q':pq,'phi_A':pa,'parity_lower_bound_Q':parity_q,
            'parity_lower_bound_A':parity_a,'internal_fiber_sizes':dict(counts_q),
            'external_signed_sums':se[0],'before_internal_sums':sq[0],
            'before_global_sums':sa[0],'after_global_sums':sa[1],
            'balanced_fixed_exterior_lower_bound':balanced_bound,
            'balanced_bound_terms':terms,
            'exact_fixed_exterior_minimum':pa[0],
            'exact_fixed_exterior_Q_balanced_minimum':pa[1],
            'all_geometric_corners':corners})
    result={'status':'PASS','assertion_tested':'All explicit before/after source colorings are proper; the attained parity and field bounds prove the two exact minima.',
        'checks':checks,'provenance':{'python':platform.python_version(),
          'input_sha256':hashlib.sha256(raw).hexdigest(),
          'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'elapsed_seconds':time.monotonic()-started},
        'scope':'Explicit witnesses and analytical bounds only; no exhaustive enumeration of all legal colorings or universal Ramsey upper bound.'}
    (HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'summaries':[{k:v for k,v in c.items() if k in ['cells','corners','phi_Q','phi_A','parity_lower_bound_A','balanced_fixed_exterior_lower_bound']} for c in checks]},indent=2))

if __name__=='__main__': main()
