"""Complete finite-source encoding and proof-producing bounded discovery."""
import ctypes,json,lzma,subprocess,sys,time
from pathlib import Path
from pysat.solvers import Solver

ROOT=Path(__file__).parent

def encode(n,k):
    marks=list(range(1,n+1));v=n;cells={};clauses=[]
    for x in range(n):
        for y in range(x):v+=1;cells[x,y]=v
    for x,y in cells:
        for d in range(1,n-x):
            guard=[-marks[i] for i in sorted({x,y,x+d,y+d})]
            c=[cells[x,y],cells[x+d,y],cells[x+d,y+d]]
            clauses.extend([guard+c,guard+[-i for i in c]])
    def add(*xs):
        if True in [x for x in xs if type(x) is bool]:return
        clauses.append([x for x in xs if type(x) is not bool])
    def neg(x):return not x if type(x) is bool else -x
    state={}
    def s(i,j):return True if j==0 else False if i<j else state[i,j]
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            v+=1;state[i,j]=v;z=v;p=s(i-1,j);q=s(i-1,j-1);a=marks[i-1]
            add(neg(p),z);add(-a,neg(q),z);add(-z,p,a);add(-z,p,q)
    add(s(n,k))
    return v,clauses,cells

def solve(n,k,checker):
    begin=time.monotonic();v,clauses,cells=encode(n,k)
    name=f'n{n}_k{k}';folder=ROOT/'proofs';folder.mkdir(exist_ok=True)
    cnf=folder/(name+'.cnf');proof=folder/(name+'.drat')
    with Solver(name='g4',bootstrap_with=clauses,with_proof=True) as solver:
        solver.conf_budget(100000)
        answer=solver.solve_limited()
        if sys.platform=='win32':
            ctypes.CDLL('ucrtbase').fflush(None);ctypes.CDLL('msvcrt').fflush(None)
        if answer is True:
            pos={x for x in solver.get_model() if x>0};A=[i for i in range(n) if i+1 in pos]
            witness=dict(n=n,k=k,A=A,colors=[[x,y,int(v in pos)] for (x,y),v in cells.items() if x in A and y in A])
            (folder/(name+'.witness.json')).write_text(json.dumps(witness,indent=2)+'\n')
            return dict(n=n,k=k,status='SAT',seconds=time.monotonic()-begin)
        if answer is None:return dict(n=n,k=k,status='UNDECIDED',seconds=time.monotonic()-begin)
        trace=solver.get_proof()
    cnf.write_text(f'p cnf {v} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses))
    proof.write_text('\n'.join(trace)+'\n')
    done=subprocess.run([str(checker),str(cnf),str(proof),'-t','120'],capture_output=True,text=True,timeout=130)
    log='\n'.join(line.rstrip() for line in (done.stdout+'\n'+done.stderr).splitlines()).strip()+'\n'
    (folder/(name+'.check.txt')).write_text(log)
    assert done.returncode==0 and 's VERIFIED' in done.stdout,(name,done.stdout[-1000:],done.stderr)
    proof.with_suffix('.drat.xz').write_bytes(lzma.compress(proof.read_bytes(),preset=6))
    proof.unlink()
    return dict(n=n,k=k,status='UNSAT-CHECKED',seconds=time.monotonic()-begin,proof_lines=len(trace))

def main():
    checker=Path(sys.argv[1]).resolve();rows=[];caps=[]
    for n in map(int,sys.argv[2:]):
        lo=0;hi=n+1
        while hi-lo>1:
            k=(lo+hi)//2;row=solve(n,k,checker);rows.append(row);print(row,flush=True)
            if row['status']=='SAT':lo=k
            elif row['status']=='UNSAT-CHECKED':hi=k
            else:break
        caps.append(dict(n=n,witness_lower=lo,certified_upper=hi-1,exact=hi==lo+1))
    target=ROOT/('finite_results_'+'_'.join(sys.argv[2:])+'.json')
    target.write_text(json.dumps(dict(runs=rows,caps=caps),indent=2)+'\n')

if __name__=='__main__':main()
