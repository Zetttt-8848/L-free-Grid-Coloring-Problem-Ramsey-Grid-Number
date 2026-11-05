"""Discovery only: falsify a proposed linear source-corner budget."""
from pathlib import Path
from itertools import combinations
from ortools.sat.python import cp_model
import json
import time
import sys

ROOT = Path(__file__).resolve().parent

def attempt(n, seconds, coefficient=1):
    model = cp_model.CpModel()
    chosen = [model.new_bool_var(f"a{i}") for i in range(n)]
    color = {(v,u): model.new_bool_var(f"c{v}_{u}")
             for v in range(n) for u in range(v)}
    pairs = {}
    for u,v in combinations(range(n), 2):
        p = model.new_bool_var(f"p{u}_{v}")
        model.add_min_equality(p, [chosen[u], chosen[v]])
        pairs[v,u] = p
    corners = []
    for u in range(n):
        for v in range(u+1, n):
            for t in range(1, n-v):
                z = model.new_bool_var(f"e{u}_{v}_{t}")
                model.add_min_equality(z, [chosen[x] for x in {u,v,u+t,v+t}])
                cells = [color[v,u], color[v+t,u], color[v+t,u+t]]
                model.add_bool_or(cells).only_enforce_if(z)
                model.add_bool_or([c.Not() for c in cells]).only_enforce_if(z)
                corners.append(z)
    model.add(chosen[0] == 1)
    model.maximize(sum(corners)-coefficient*sum(pairs.values()))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 4
    solver.parameters.random_seed = 2026091209
    start = time.monotonic()
    status = solver.solve(model)
    out = dict(n=n, coefficient=coefficient, status=solver.status_name(status), seconds=time.monotonic()-start,
               scope="Search outcome only; no negative or optimum is a theorem.")
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        A = [i for i in range(n) if solver.value(chosen[i])]
        out.update(marks=A, objective=int(round(solver.objective_value)),
                   best_bound=solver.best_objective_bound,
                   rows={str(v): {str(u): solver.value(color[v,u])
                                 for u in A if u<v} for v in A})
    return out

coefficient = int(sys.argv[1]) if len(sys.argv)>1 else 1
results = []
for n,seconds in ([(14,10),(22,15),(30,20)] if coefficient==1 else [(22,15),(30,20)]):
    result = attempt(n, seconds, coefficient)
    results.append(result)
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}), flush=True)
    if result.get("objective", 0)>0:
        break
suffix = "" if coefficient==1 else f"_{coefficient}"
(ROOT / f"source_energy_probe{suffix}.json").write_text(json.dumps(results, indent=2)+"\n", encoding="utf-8")
