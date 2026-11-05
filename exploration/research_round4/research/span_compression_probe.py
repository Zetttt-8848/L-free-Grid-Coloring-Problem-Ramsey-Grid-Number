"""Seek a literal counterexample to G(|B|)+G(|C|)<=span(S)."""
import argparse,json
from pathlib import Path
from ortools.sat.python import cp_model

parser=argparse.ArgumentParser()
parser.add_argument('--n',type=int,default=12)
parser.add_argument('--marks',type=int,default=4)
args=parser.parse_args()
n=args.n
model=cp_model.CpModel()
a=[model.new_bool_var(f'a{i}') for i in range(n)]
b=[model.new_bool_var(f'b{i}') for i in range(n)]
c=[model.new_bool_var(f'c{i}') for i in range(n)]
z={(v,u):model.new_bool_var(f'z{v}_{u}') for v in range(n) for u in range(v+1)}
for i in range(n):
    model.add(b[i]+c[i]==a[i])
    model.add(z[i,i]==0).only_enforce_if(b[i])
    model.add(z[i,i]==1).only_enforce_if(c[i])
model.add(sum(b)==args.marks);model.add(sum(c)==args.marks)
model.add(b[0]==1);model.add(a[-1]==1)
corners=[]
for x,y in z:
    for d in range(1,n-x):
        tr=((x,y),(x+d,y),(x+d,y+d))
        req=[a[i].negated() for i in sorted({x,y,x+d,y+d})]
        model.add_bool_or(req+[z[q] for q in tr])
        model.add_bool_or(req+[z[q].negated() for q in tr])
        corners.append(tr)
solver=cp_model.CpSolver()
solver.parameters.max_time_in_seconds=20
solver.parameters.num_search_workers=1
solver.parameters.random_seed=20260911
status=solver.solve(model)
out=dict(hypothesis='joint weak-triangle span compression; bounded construction probe',domain=n,marks_per_color=args.marks,
         status=solver.status_name(status),seconds=solver.wall_time)
if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
    B=[i for i in range(n) if solver.value(b[i])]
    C=[i for i in range(n) if solver.value(c[i])]
    S=set(B+C)
    coloring={q:solver.value(v) for q,v in z.items() if q[0] in S and q[1] in S}
    bad=[tr for tr in corners if all(q in coloring for q in tr) and len({coloring[q] for q in tr})==1]
    if bad:raise RuntimeError('producer returned invalid coloring')
    out.update(B=B,C=C,colors=[[x,y,v] for (x,y),v in coloring.items()],
               actual_corners=sum(all(q in coloring for q in tr) for tr in corners))
Path(__file__).with_name(f'span_compression_n{n}_m{args.marks}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='colors'}))
