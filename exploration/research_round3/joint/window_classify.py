"""Complete local support classification, with positive and RUP certificates."""
from pathlib import Path
import argparse,itertools,json,time
from pysat.solvers import Solver
ROOT=Path(__file__).resolve().parent

def encode(A):
    cells=[(x,y) for y in A for x in A if y<x];ids={c:i+1 for i,c in enumerate(cells)};clauses=[]
    for d in range(1,max(A,default=0)-min(A,default=0)+1):
        starts=[a for a in A if a+d in A]
        for y,x in itertools.combinations(starts,2):
            q=[ids[x,y],ids[x+d,y],ids[x+d,y+d]];clauses.extend([q,[-v for v in q]])
    if cells:clauses.append([1])
    return cells,clauses

def refute(base,deadline):
    clauses=[tuple(c) for c in base];proof=[]
    def propagate(path):
        assigned=set(path)
        while True:
            changed=False
            for c in clauses:
                if any(t in assigned for t in c):continue
                rem=[t for t in c if -t not in assigned]
                if not rem:return None
                if len(rem)==1 and rem[0] not in assigned:assigned.add(rem[0]);changed=True
            if not changed:return assigned
    def visit(path):
        if time.time()>deadline:raise TimeoutError('window proof deadline')
        assigned=propagate(path)
        if assigned is not None:
            active=[tuple(t for t in c if -t not in assigned) for c in clauses if not any(t in assigned for t in c)]
            if not active:raise AssertionError('SAT in negative core')
            v=abs(min(active,key=len)[0]);visit(path+(v,));visit(path+(-v,))
        c=tuple(-t for t in path);proof.append(c);clauses.append(c)
    visit(());return proof

def classify(width,seconds,save=True):
    start=time.time();deadline=start+seconds;bad=[];good={};status=[None]*(1<<width);pruned=0;queried=0;prooflines=0
    for mask in sorted(range(1<<width),key=lambda m:(m.bit_count(),m)):
        if time.time()>deadline:raise TimeoutError('classification deadline')
        if any(mask&b['mask']==b['mask'] for b in bad):status[mask]=False;pruned+=1;continue
        A=[i for i in range(width) if mask>>i&1];cells,clauses=encode(A);queried+=1
        with Solver(name='minisat22',bootstrap_with=clauses) as solver:
            sat=solver.solve();status[mask]=sat
            if sat:
                model={abs(t):t>0 for t in (solver.get_model() or [])};good[mask]=[int(model.get(i+1,False)) for i in range(len(cells))]
            else:
                proof=refute(clauses,deadline);prooflines+=len(proof);bad.append(dict(mask=mask,marks=A,proof=proof));print(json.dumps(dict(event='minimal_bad',width=width,mask=mask,marks=A,rup_lines=len(proof))),flush=True)
    maximal=[dict(mask=m,marks=[i for i in range(width) if m>>i&1],colors=colors) for m,colors in good.items() if all(m>>i&1 or not status[m|1<<i] for i in range(width))]
    capacities={w:max(m.bit_count() for m in range(1<<w) if status[m]) for w in range(1,width+1)}
    out=dict(width=width,raw_count=1<<width,good_count=sum(status),bad_count=len(status)-sum(status),queried=queried,pruned_by_bad_subset=pruned,minimal_bad_count=len(bad),maximal_good_count=len(maximal),rup_lines=prooflines,capacities=capacities,minimal_bad=bad,maximal_good=maximal,status=status,runtime_seconds=time.time()-start,label='UNVERIFIED pending independent full coverage and proof check')
    if save:
        folder=ROOT/f'window{width}';folder.mkdir(exist_ok=True)
        for b in bad:
            cells,clauses=encode(b['marks']);base=folder/f"bad_{b['mask']}"
            base.with_suffix('.cnf').write_text(f'p cnf {len(cells)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses));base.with_suffix('.rup').write_text(''.join(' '.join(map(str,c))+(' ' if c else '')+'0\n' for c in b['proof']))
        (ROOT/f'window{width}.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    return out

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--width',type=int,default=13);pa.add_argument('--seconds',type=int,default=600);args=pa.parse_args()
    sanity=[]
    for w in (1,2,3):
        result=classify(w,30,False);assert result['good_count']==1<<w;sanity.append(dict(width=w,expected_good=1<<w,observed_good=result['good_count'],verdict='PASS'))
    result=classify(args.width,args.seconds);print(json.dumps(dict(sanity=sanity,**{k:v for k,v in result.items() if k not in ('minimal_bad','maximal_good','status')}),indent=2),flush=True)
    (ROOT/f'window{args.width}.sanity.json').write_text(json.dumps(sanity,indent=2)+'\n')

if __name__=='__main__':main()
