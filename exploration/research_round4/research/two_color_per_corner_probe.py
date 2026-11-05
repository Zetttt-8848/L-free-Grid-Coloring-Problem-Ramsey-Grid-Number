"""Discovery: color full strict triangles with exactly two colors per corner."""
import itertools,json,time
from pathlib import Path
from ortools.sat.python import cp_model
root=Path(__file__).resolve().parent
results=[]
for n in range(6,16):
    model=cp_model.CpModel();cells=[(v,u) for v in range(n) for u in range(v)];z={q:model.new_int_var(0,2,f'z{q[0]}_{q[1]}') for q in cells}
    allowed=[list(v) for v in itertools.product(range(3),repeat=3) if len(set(v))==2]
    corners=[]
    for x,y in cells:
        for d in range(1,n-x):
            tr=((x,y),(x+d,y),(x+d,y+d));corners.append(tr)
            model.add_allowed_assignments([z[q] for q in tr],allowed)
    model.add(z[1,0]==0)
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=5;solver.parameters.num_search_workers=1
    start=time.monotonic();status=solver.solve(model)
    row=dict(n=n,variables=len(cells),corners=len(corners),status=solver.status_name(status),seconds=time.monotonic()-start)
    if status in (cp_model.FEASIBLE,cp_model.OPTIMAL):
        colors={q:solver.value(v) for q,v in z.items()}
        assert all(len({colors[q] for q in tr})==2 for tr in corners)
        row['colors']=[[v,u,c] for (v,u),c in colors.items()]
    results.append(row);print(json.dumps({k:v for k,v in row.items() if k!='colors'}),flush=True)
    if status==cp_model.INFEASIBLE:break
(root/'two_color_per_corner_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
