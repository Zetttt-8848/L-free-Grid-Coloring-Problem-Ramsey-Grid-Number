"""Extract a small literal candidate core; solver status alone is not proof."""
from pathlib import Path
import argparse,itertools,json
from pysat.solvers import Solver
ROOT=Path(__file__).resolve().parent

def encode(A):
    cells=[(b,a) for a,b in itertools.combinations(A,2)];ids={c:i+1 for i,c in enumerate(cells)};clauses=[];corners=[];aset=set(A)
    for d in range(1,max(A)-min(A)+1):
        st=[a for a in A if a+d in aset]
        for y,x in itertools.combinations(st,2):
            q=[ids[x,y],ids[x+d,y],ids[x+d,y+d]];clauses.extend([q,[-v for v in q]]);corners.append([x,y,d])
    clauses.append([1]);return cells,corners,clauses

def unsat(A):
    if len(A)<2:return False
    _,corners,clauses=encode(A)
    with Solver(name='minisat22',bootstrap_with=clauses) as solver:return not solver.solve()

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--witness',default=str(ROOT/'witness_464.json'));pa.add_argument('--tag',default='triangle_core');args=pa.parse_args()
    A=json.loads(Path(args.witness).read_text())['marks'];log=[]
    for k in range(6,len(A)+1):
        neg=unsat(A[:k]);log.append(dict(kind='prefix',size=k,negative=neg))
        if neg:A=A[:k];break
    else:
        cells,corners,clauses=encode(A)
        with Solver(name='minisat22',bootstrap_with=clauses) as solver:
            assert solver.solve();model={abs(t):int(t>0) for t in solver.get_model()}
        out=dict(marks=A,cells=cells,corners=corners,colors=[model.get(i+1,0) for i in range(len(cells))],status='SAT candidate pending independent check',log=log)
        (ROOT/f'{args.tag}.sat.json').write_text(json.dumps(out,indent=2)+'\n');print('FULL TRIANGLE SAT CANDIDATE');return
    changed=True
    while changed:
        changed=False
        for a in A[:]:
            trial=[b for b in A if b!=a];neg=unsat(trial);log.append(dict(kind='delete',mark=a,negative=neg))
            if neg:A=trial;changed=True
    cells,corners,clauses=encode(A);out=dict(marks=A,mark_count=len(A),cells=cells,corners=corners,variables=len(cells),clause_count=len(clauses),log=log,label='UNVERIFIED candidate until independent proof check')
    (ROOT/f'{args.tag}.json').write_text(json.dumps(out,indent=2)+'\n')
    with (ROOT/f'{args.tag}.cnf').open('w') as f:
        f.write(f'p cnf {len(cells)} {len(clauses)}\n')
        for c in clauses:f.write(' '.join(map(str,c))+' 0\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('cells','corners','log')},indent=2))

if __name__=='__main__':main()
