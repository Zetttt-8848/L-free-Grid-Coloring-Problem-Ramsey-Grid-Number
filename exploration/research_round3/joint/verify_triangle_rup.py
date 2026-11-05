"""Independent geometry and pure Python RUP checker; no producer imports."""
from pathlib import Path
import argparse,collections,hashlib,itertools,json
ROOT=Path(__file__).resolve().parent

def read_cnf(path):
    clauses=[];n=None;expected=None
    for line in path.read_text().splitlines():
        terms=line.split()
        if not terms or terms[0]=='c':continue
        if terms[0]=='p':_,kind,n,expected=terms;n=int(n);expected=int(expected);assert kind=='cnf';continue
        vals=list(map(int,terms));assert vals[-1]==0 and all(v and abs(v)<=n for v in vals[:-1]);clauses.append(vals[:-1])
    assert len(clauses)==expected
    return n,clauses

def rup(clauses,clause,n):
    assignment=[0]*(n+1);queue=collections.deque(-lit for lit in clause)
    # Unit propagation by rebuilding clause residual counts each round.
    while True:
        while queue:
            lit=queue.popleft();v=abs(lit);sign=1 if lit>0 else -1
            if assignment[v]==-sign:return True
            assignment[v]=sign
        for current in clauses:
            if any(assignment[abs(lit)]==(1 if lit>0 else -1) for lit in current):continue
            unknown=[lit for lit in current if assignment[abs(lit)]==0]
            if not unknown:return True
            if len(unknown)==1:queue.append(unknown[0])
        if not queue:return False

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--tag',default='triangle_core');args=pa.parse_args()
    core=json.loads((ROOT/f'{args.tag}.json').read_text());A=core['marks'];assert A==sorted(set(A));cells=core['cells'];expected_cells=[[x,y] for y in A for x in A if y<x];assert cells==expected_cells
    ids={tuple(c):j+1 for j,c in enumerate(cells)};corners=[];expected=[]
    for x,y in cells:
        for u,v in cells:
            if v!=y or u<=x:continue
            d=u-x
            if (u,y+d) in ids:
                lits=[ids[x,y],ids[u,v],ids[u,y+d]];expected.extend([tuple(lits),tuple(-l for l in lits)]);corners.append((x,y,d))
    n,clauses=read_cnf(ROOT/f'{args.tag}.cnf');assert n==len(cells)
    assert collections.Counter(tuple(c) for c in clauses)==collections.Counter(expected+[(1,)])
    assert set(corners)==set(map(tuple,core['corners']))
    checked=0;empty=False
    for line in (ROOT/f'{args.tag}.rup').read_text().splitlines():
        values=list(map(int,line.split()));assert values[-1]==0;clause=values[:-1];assert all(0<abs(l)<=n for l in clause)
        if not rup(clauses,clause,n):raise AssertionError(f'non-RUP addition {checked+1}: {clause}')
        clauses.append(clause);checked+=1;empty=not clause
    assert empty
    aset=set(A);aps=[list(range(first,first+6*d,d)) for first in A for d in range(1,(max(A)-first)//5+1) if all(first+j*d in aset for j in range(6))];assert not aps
    out=dict(verdict='PASS',scope='The two-color completion triangle of the literal mark set is impossible; color-pin is complete by color interchange',marks=A,mark_count=len(A),cells=n,corners=len(corners),base_clauses=len(expected)+1,rup_additions_checked=checked,six_APs_in_pattern=aps,sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in [f'{args.tag}.json',f'{args.tag}.cnf',f'{args.tag}.rup']})
    (ROOT/f'{args.tag}.check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
