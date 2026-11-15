"""Bounded witness search; solver infeasibility is not a proof export."""
import itertools, json, time
from pathlib import Path
from pysat.solvers import Solver

ROOT=Path(__file__).parent

def golomb_partition(H):
    H=sorted(H)
    for mask in range(1 << max(0,len(H)-1)):
        buckets=[set(),set()]; good=True
        for j,b in enumerate(H):
            color=(mask>>j)&1 if j<len(H)-1 else 0
            for i,a in enumerate(H[:j]):
                other=(mask>>i)&1
                if color==other:
                    if b-a in buckets[color]:good=False;break
                    buckets[color].add(b-a)
            if not good:break
        if good:return mask
    return None

def search(H,T):
    A=sorted({0,T}|set(H)|{T-h for h in H})
    if min(H)<=0 or max(H)>=T:return None
    cells=[(x,y) for x in A for y in A if x>y]
    ids={p:i+1 for i,p in enumerate(cells)}
    clauses=[]; marks=set(A)
    for x,y in cells:
        for v in A:
            d=v-x
            if d>0 and y+d in marks:
                c=[ids[x,y],ids[v,y],ids[v,y+d]]
                clauses.extend([c,[-i for i in c]])
    clauses.append([ids[T,0]])
    for h in H:
        clauses.extend([[-ids[h,0]],[-ids[T,T-h]]])
    with Solver(name='g3',bootstrap_with=clauses) as solver:
        solver.conf_budget(20000)
        if solver.solve_limited() is not True:return None
        pos={x for x in solver.get_model() if x>0}
    colors=[[x,y,int(ids[x,y] in pos)] for x,y in cells]
    return dict(A=A,T=T,H=sorted(H),colors=colors)

def main():
    start=time.monotonic(); tried=0; candidates=0
    # All subsets of 1..12 with 7..10 marks, then one 3-cube.
    for k in range(7,11):
        for H in itertools.combinations(range(1,13),k):
            if time.monotonic()-start>90:
                print('Pilot time ceiling; no completeness claim.');return
            if golomb_partition(H) is not None:continue
            candidates+=1
            for T in (max(H)+1,2*max(H)+1,5*max(H)):
                tried+=1
                hit=search(H,T)
                if hit:
                    hit.update(candidate='R2-C1',attempts=tried,nonpartition_candidates=candidates)
                    (ROOT/'counterexample.json').write_text(json.dumps(hit,indent=2)+'\n')
                    print('COUNTEREXAMPLE',H,T,'attempts',tried);return
    print('NO WITNESS',tried,candidates,'elapsed',time.monotonic()-start)

if __name__=='__main__':main()
