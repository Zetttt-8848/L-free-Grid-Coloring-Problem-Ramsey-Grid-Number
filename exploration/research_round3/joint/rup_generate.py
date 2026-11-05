"""Small exact DPLL refutation producer; outputs a DRAT-compatible RUP trace."""
from pathlib import Path
import argparse,json,time
ROOT=Path(__file__).resolve().parent

def parse(path):
    result=[]
    for line in path.read_text().splitlines():
        if line and line[0] not in 'cp':result.append(tuple(map(int,line.split()[:-1])))
    return result

def propagate(clauses,assumptions):
    assigned=set(assumptions)
    while True:
        changed=False
        for clause in clauses:
            if any(lit in assigned for lit in clause):continue
            left=[lit for lit in clause if -lit not in assigned]
            if not left:return None
            if len(left)==1:
                if -left[0] in assigned:return None
                if left[0] not in assigned:assigned.add(left[0]);changed=True
        if not changed:return assigned

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--tag',default='triangle_core');args=pa.parse_args()
    clauses=parse(ROOT/f'{args.tag}.cnf');proof=[];nodes=0;started=time.time()
    def search(path):
        nonlocal nodes
        nodes+=1
        if nodes>1000000 or time.time()-started>60:raise RuntimeError('bounded proof generation exhausted')
        assignment=propagate(clauses,path)
        if assignment is None:
            learned=tuple(-lit for lit in path);clauses.append(learned);proof.append(learned);return
        active=[tuple(l for l in c if -l not in assignment) for c in clauses if not any(l in assignment for l in c)]
        if not active:raise RuntimeError('SAT assignment in claimed core')
        var=abs(min(active,key=len)[0]);search(path+(var,));search(path+(-var,))
        learned=tuple(-lit for lit in path);clauses.append(learned);proof.append(learned)
    search(())
    (ROOT/f'{args.tag}.rup').write_text('\n'.join(' '.join(map(str,c))+(' ' if c else '')+'0' for c in proof)+'\n')
    out=dict(nodes=nodes,proof_lines=len(proof),runtime_seconds=time.time()-started,claim='candidate RUP refutation; independent check required');(ROOT/f'{args.tag}.producer.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
