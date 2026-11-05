"""R3 joint feasibility: exact occupancy pairs plus redundant ordered ranks."""
from pathlib import Path
import argparse, bisect, hashlib, json, platform, time
import ortools
from ortools.sat.python import cp_model

ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

def specs(n):
    return dict(n=n,size=(n+2)//3,caps=[0]+[2*(bisect.bisect_right(H,n-d)-1) for d in range(1,n)],pair_count=n*(n-1)//2,ap_count=sum(n-5*d for d in range(1,(n-1)//5+1)))

def minsum(num,caps):
    result=0
    for d,k in enumerate(caps):
        take=min(num,k); result+=d*take; num-=take
        if not num:return result
    raise ValueError('insufficient capacity')

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--n',type=int,default=464);pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--seed',type=int,default=20260910);pa.add_argument('--workers',type=int,default=1);pa.add_argument('--no-ranks',action='store_true');pa.add_argument('--hint');pa.add_argument('--tag',default='rank600');args=pa.parse_args()
    for n in (464,463,462):(ROOT/f'spec_{n}.json').write_text(json.dumps(specs(n),indent=2)+'\n')
    sp=specs(args.n); n,s=sp['n'],sp['size']; start=time.time()
    model=cp_model.CpModel(); x=[model.new_bool_var(f'x{i}') for i in range(n)];model.add(sum(x)==s);model.add(x[0]==1)
    pair_count=0
    for d in range(1,n):
        pp=[]
        for i in range(n-d):
            p=model.new_bool_var(f'p{i}_{d}');model.add_bool_or([~x[i],~x[i+d],p]);model.add_implication(p,x[i]);model.add_implication(p,x[i+d]);pp.append(p);pair_count+=1
        model.add(sum(pp)<=sp['caps'][d])
    ap_count=0
    for d in range(1,(n-1)//5+1):
        for i in range(n-5*d):model.add(sum(x[i+j*d] for j in range(6))<=5);ap_count+=1
    assert pair_count==sp['pair_count'] and ap_count==sp['ap_count']
    ranks=[];cuts=[]
    if not args.no_ranks:
        ranks=[model.new_int_var(i+i//5,n-s+i,f'a{i}') for i in range(s)]
        for i,a in enumerate(ranks):
            model.add_element(a,x,1)
            if i:model.add(a>ranks[i-1])
        model.add(ranks[0]==0)
        for i in range(s-5):
            model.add(ranks[i+5]>=ranks[i]+6);bs=[]
            for j in range(1,5):
                b=model.new_bool_var(f'neqgap{i}_{j}')
                expr=(ranks[i+1]-ranks[i])-(ranks[i+j+1]-ranks[i+j])
                model.add(expr!=0).only_enforce_if(b);model.add(expr==0).only_enforce_if(~b);bs.append(b)
            model.add_bool_or(bs)
        for c in range(1,min(25,s)):
            count=c*s-c*(c+1)//2;lb=minsum(count,sp['caps'])
            expr=sum((c-i)*(ranks[s-1-i]-ranks[i]) for i in range(c))
            model.add(expr>=lb);cuts.append(dict(c=c,pairs=count,lower=lb,upper=(n-1)*c*(c+1)//2))
    if args.hint:
        data=json.loads(Path(args.hint).read_text()); marks=set(data['marks'])
        for i,z in enumerate(x):model.add_hint(z,int(i+1 in marks))
        for a,v in zip(ranks,sorted(marks)):model.add_hint(a,v-1)
    model.add_decision_strategy(x,cp_model.CHOOSE_FIRST,cp_model.SELECT_MAX_VALUE)
    base=ROOT/f'cp_{args.n}_{args.tag}'
    model_path=base.with_suffix('.pbtxt');model.export_to_file(str(model_path))
    (base.with_suffix('.setup.json')).write_text(json.dumps(dict(spec=sp,rank_count=len(ranks),neighbor_cuts=cuts,model_sha256=hashlib.sha256(model_path.read_bytes()).hexdigest(),build_seconds=time.time()-start,arguments=vars(args),python=platform.python_version(),ortools=ortools.__version__),indent=2)+'\n')
    print('MODEL_BUILT',n,s,pair_count,ap_count,'ranks',len(ranks),flush=True)
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=args.seconds;solver.parameters.num_search_workers=args.workers;solver.parameters.random_seed=args.seed;solver.parameters.log_search_progress=True
    solver.parameters.cp_model_presolve=True
    tick=time.time();status=solver.solve(model)
    out=dict(n=n,size=s,status=solver.status_name(status),runtime_seconds=time.time()-tick,arguments=vars(args),response_statistics=solver.response_stats(),label='UNDECIDED unless literal witness independently verified')
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):out['marks']=[i+1 for i in range(n) if solver.value(x[i])]
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
