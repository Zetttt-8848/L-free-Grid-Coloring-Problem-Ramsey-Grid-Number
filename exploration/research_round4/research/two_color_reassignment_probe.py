"""Bounded discovery in exact fixed-third-color subspaces; no lower-bound claim."""
from pathlib import Path
from itertools import combinations
from ortools.sat.python import cp_model
import json, time

N=13
cells=[(v,u) for v in range(1,N) for u in range(v)]
edges=[((v,u),(v+d,u),(v+d,u+d)) for v,u in cells for d in range(1,N-v)]
seed=['0','11','101','2112','20120','020101','2211222','11022000',
      '000202111','2220010122','11002121000','101021021020']
colors={p:int(seed[p[0]-1][p[1]]) for p in cells}
records=[]

def record_coloring(col):
    assert all(len({col[p] for p in e})>1 for e in edges)
    rainbows=[[e[0][0],e[0][1],e[1][0]-e[0][0]] for e in edges
              if len({col[p] for p in e})==3]
    return dict(rows=[''.join(str(col[v,u]) for u in range(v)) for v in range(1,N)],
                rainbow_count=len(rainbows),rainbows=rainbows)

best=record_coloring(colors)
for sweep in range(3):
    improved=False
    for c in range(3):
        start=time.monotonic()
        a,b=[t for t in range(3) if t!=c]
        model=cp_model.CpModel()
        bits={p:model.new_bool_var(f'b_{p[0]}_{p[1]}') for p in cells if colors[p]!=c}
        weights={}
        hcount=0
        for e in edges:
            outside=[p for p in e if p in bits]
            if len(outside)==3:
                model.add(sum(bits[p] for p in outside)>=1)
                model.add(sum(bits[p] for p in outside)<=2)
                hcount+=1
            elif len(outside)==2:
                key=tuple(sorted(outside))
                weights[key]=weights.get(key,0)+1
        terms=[]
        for (u,v),w in weights.items():
            cut=model.new_bool_var(f'cut_{u}_{v}')
            model.add_allowed_assignments([bits[u],bits[v],cut],
                                         [(0,0,0),(0,1,1),(1,0,1),(1,1,0)])
            terms.append(w*cut)
        # Swapping a,b globally is immaterial; keep the first one fixed.
        p=next(iter(bits))
        model.add(bits[p]==int(colors[p]==b))
        for p,bit in bits.items(): model.add_hint(bit,int(colors[p]==b))
        model.minimize(sum(terms))
        solver=cp_model.CpSolver()
        solver.parameters.max_time_in_seconds=8
        solver.parameters.num_search_workers=4
        status=solver.solve(model)
        rec=dict(sweep=sweep,fixed_color=c,vertices=len(bits),hyperedges=hcount,
                 graph_edges=len(weights),graph_weight=sum(weights.values()),
                 status=solver.status_name(status),seconds=time.monotonic()-start)
        if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
            candidate={p:(b if solver.value(bits[p]) else a) if p in bits else c for p in cells}
            data=record_coloring(candidate)
            rec.update(data)
            rec['raw_lower_bound']=solver.best_objective_bound
            if data['rainbow_count']<best['rainbow_count']:
                colors=candidate
                best=data
                improved=True
        records.append(rec)
        Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
            scope='Bounded construction search; solver bounds are not global theorems.',
            best=best,cases=records),indent=2)+'\n',encoding='utf-8')
        print(json.dumps({k:v for k,v in rec.items() if k not in ('rows','rainbows')}),flush=True)
        if best['rainbow_count']<=16: break
    if best['rainbow_count']<=16 or not improved: break
