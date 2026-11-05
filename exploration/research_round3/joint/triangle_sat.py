"""Two-color SAT for the actual completion triangle of a literal set."""
from pathlib import Path
import argparse,hashlib,itertools,json,threading,time
from pysat.solvers import Solver
ROOT=Path(__file__).resolve().parent

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--witness',default=str(ROOT/'witness_464.json'));pa.add_argument('--seconds',type=int,default=600);pa.add_argument('--solver',default='glucose4');pa.add_argument('--tag',default='triangle464');args=pa.parse_args()
    obj=json.loads(Path(args.witness).read_text());A=obj['marks'];cell=[(b,a) for a,b in itertools.combinations(A,2)];ids={c:i+1 for i,c in enumerate(cell)};clauses=[];corners=[];AS=set(A)
    for d in range(1,max(A)-min(A)+1):
        starts=[a for a in A if a+d in AS]
        for y,x in itertools.combinations(starts,2):
            q=[ids[x,y],ids[x+d,y],ids[x+d,y+d]];corners.append([x,y,d]);clauses.append(q);clauses.append([-v for v in q])
    # Interchanging the two colors gives a representative with the first cell True.
    clauses.append([1]);base=ROOT/args.tag;cnf=base.with_suffix('.cnf')
    with cnf.open('w') as f:
        f.write(f'p cnf {len(cell)} {len(clauses)}\n')
        for c in clauses:f.write(' '.join(map(str,c))+' 0\n')
    base.with_suffix('.mapping.json').write_text(json.dumps(dict(source=args.witness,source_sha256=hashlib.sha256(Path(args.witness).read_bytes()).hexdigest(),cells=cell,corners=corners),separators=(',',':'))+'\n')
    setup=dict(variables=len(cell),corners=len(corners),clauses=len(clauses),solver=args.solver,seconds=args.seconds,cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),arguments=vars(args));base.with_suffix('.setup.json').write_text(json.dumps(setup,indent=2)+'\n');print(json.dumps(setup),flush=True)
    with Solver(name=args.solver,bootstrap_with=clauses,with_proof=True) as solver:
        timer=threading.Timer(args.seconds,solver.interrupt);timer.start();start=time.time()
        result=solver.solve_limited(expect_interrupt=True);timer.cancel();out=dict(result=result,status='UNDECIDED' if result is None else 'SAT candidate' if result else 'UNSAT unverified',runtime_seconds=time.time()-start,statistics=solver.accum_stats(),setup=setup)
        if result is True:out['colors']=[int(v>0) for v in solver.get_model()[:len(cell)]]
        if result is False:
            proof=solver.get_proof();base.with_suffix('.drat').write_text('\n'.join(proof)+'\n');out['proof_lines']=len(proof);out['proof_sha256']=hashlib.sha256(base.with_suffix('.drat').read_bytes()).hexdigest()
        base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='colors'},indent=2),flush=True)

if __name__=='__main__':main()
