"""Bounded discovery of signed, symmetry-invariant local rainbow functionals.

LP proposals are separated by a finite proper-coloring optimization model.
All results are discovery evidence, not mathematical impossibility proofs.
"""
import itertools,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from ortools.sat.python import cp_model

root=Path(__file__).resolve().parent;n=10
cells=[(v,u) for v in range(1,n) for u in range(v)]
corners=[];keys=[]
for v,u in cells:
    for d in range(1,n-v):
        corners.append(((v,u),(v+d,u),(v+d,u+d)))
        keys.append((d,tuple(sorted((u,v-u-1,9-v-d)))))
orbits=sorted(set(keys));oi={key:i for i,key in enumerate(orbits)}
sizes=np.array([keys.count(key) for key in orbits])

model=cp_model.CpModel()
color={p:model.new_int_var(0,2,f'c_{p[0]}_{p[1]}') for p in cells}
rainbow=[]
allowed=[(*cs,int(len(set(cs))==3)) for cs in itertools.product(range(3),repeat=3) if len(set(cs))>1]
for j,tr in enumerate(corners):
    r=model.new_bool_var(f'r_{j}');rainbow.append(r)
    model.add_allowed_assignments([color[p] for p in tr]+[r],allowed)
model.add(color[cells[0]]==0)

seeds=[['0','10','120','0002','01111','222210','0021102','01022111','200120122']]
seeds += [a['rows'] for a in json.loads((root/'rainbow_orbit_packing_probe.json').read_text())['groups']]
def vector(rr):
    z={(v,u):int(rr[v-1][u]) for v,u in cells}
    vv=[0]*len(orbits)
    for j,tr in enumerate(corners):
        assert len({z[p] for p in tr})>1
        if len({z[p] for p in tr})==3:vv[oi[keys[j]]]+=1
    return vv
witnesses=[dict(rows=rr,vector=vector(rr)) for rr in seeds]
iterations=[];start=time.monotonic();last=None
for iteration in range(80):
    if time.monotonic()-start>=55:break
    aa=np.array([w['vector'] for w in witnesses],dtype=float)
    lp=linprog(sizes,A_ub=-aa,b_ub=-np.ones(len(aa)),bounds=[(-1,1)]*len(orbits),method='highs')
    if not lp.success:
        iterations.append(dict(iteration=iteration,status='master stopped',message=lp.message));break
    fractions=[Fraction(float(w)).limit_denominator(120) for w in lp.x]
    scale=1
    import math
    for f in fractions:scale=math.lcm(scale,f.denominator)
    if scale>1000000:
        fractions=[Fraction(round(float(w)*1000),1000) for w in lp.x];scale=1000
    coef=[int(f*scale) for f in fractions]
    model.minimize(sum(coef[oi[keys[j]]]*r for j,r in enumerate(rainbow)))
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=min(2.0,max(.05,55-(time.monotonic()-start)))
    solver.parameters.num_search_workers=4;solver.parameters.random_seed=iteration
    status=solver.solve(model)
    row=dict(iteration=iteration,master_mass=float(lp.fun),scale=scale,separator_status=solver.status_name(status),seconds=time.monotonic()-start)
    last=dict(weights=[str(f) for f in fractions],mass=str(sum(Fraction(int(s))*f for s,f in zip(sizes,fractions))))
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        rr=[''.join(str(solver.value(color[v,u])) for u in range(v)) for v in range(1,n)]
        vv=vector(rr);obj=sum(a*b for a,b in zip(coef,vv))
        row.update(objective_numerator=obj,threshold=scale,best_bound=solver.best_objective_bound)
        if obj<scale:
            witnesses.append(dict(rows=rr,vector=vv))
        else:
            row['candidate_only']=True
            iterations.append(row);print(json.dumps(row),flush=True);break
    else:
        iterations.append(row);print(json.dumps(row),flush=True);break
    iterations.append(row);print(json.dumps(row),flush=True)
result=dict(orbits=orbits,sizes=sizes.tolist(),iterations=iterations,last_candidate=last,witnesses=witnesses,elapsed=time.monotonic()-start)
(root/'signed_rainbow_functional_probe.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
