"""Bounded one-color joint six-AP/difference-cap necessary-condition model."""
from ortools.sat.python import cp_model
from pathlib import Path
from bisect import bisect_right
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[1]
N,SIZE=464,155
TABLE=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]

def main():
    model=cp_model.CpModel()
    x=[model.NewBoolVar(f'x{i}') for i in range(N)]
    model.Add(sum(x)==SIZE)
    # Translate the smallest occupied index to zero: preserves all properties.
    model.Add(x[0]==1)
    pairs=0
    for d in range(1,N):
        cap=2*(bisect_right(TABLE,N-d)-1)
        indicators=[]
        for i in range(N-d):
            p=model.NewBoolVar(f'p{i}_{d}')
            # Only the lower implication is required for an upper pair cap.
            model.AddBoolOr([x[i].Not(),x[i+d].Not(),p])
            indicators.append(p)
            pairs+=1
        model.Add(sum(indicators)<=cap)
    aps=0
    for d in range(1,(N-1)//5+1):
        for i in range(N-5*d):
            model.Add(sum(x[i+j*d] for j in range(6))<=5)
            aps+=1
    model_path=ROOT/'certificates'/'four_multi_joint_model.pbtxt'
    model.ExportToFile(str(model_path))
    solver=cp_model.CpSolver()
    solver.parameters.max_time_in_seconds=60
    solver.parameters.num_search_workers=1
    solver.parameters.random_seed=20260909
    solver.parameters.cp_model_presolve=True
    start=time.perf_counter()
    status=solver.Solve(model)
    out=dict(n=N,size=SIZE,pair_indicators=pairs,six_AP_constraints=aps,
             status=solver.StatusName(status),runtime_seconds=time.perf_counter()-start,
             time_limit_seconds=60,workers=1,seed=20260909,
             model_sha256=hashlib.sha256(model_path.read_bytes()).hexdigest(),
             response_statistics=solver.ResponseStats(),
             scope='One-color necessary-condition surrogate, not a partition or a grid')
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        out['marks']=[i+1 for i in range(N) if solver.Value(x[i])]
        out['label']='UNVERIFIED witness until separate checker passes'
    else:
        out['label']='UNDECIDED; no proof of infeasibility claimed'
    (ROOT/'certificates'/'four_multi_joint_sat.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
