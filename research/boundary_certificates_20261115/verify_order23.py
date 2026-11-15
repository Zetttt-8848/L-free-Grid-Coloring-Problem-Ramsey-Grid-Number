"""Check the order-23 completion shape at side 460 with the standard library."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json

Q=(0,3,7,17,61,66,91,99,114,159,171,199,200,226,235,246,277,316,329,348,350,366,372)
N=460


def triples_from_starts(group,h):
    for y,x in combinations(sorted(group),2):
        yield ((x,y),(x+h,y),(x+h,y+h))


def extend(values,edges,old,new):
    """Run all newly activated binary triple implications to their closure."""
    work=[]
    def inspect(tri):
        for i in range(3):
            a,b,c=tri[i],tri[(i+1)%3],tri[(i+2)%3]
            if a in values and values[a]==values.get(b):
                if values.get(c)!=1-values[a]:
                    work.append((c,1-values[a]))
    for tri in new:inspect(tri)
    while work:
        point,v=work.pop()
        if point in values:
            if values[point]!=v:return True
            continue
        values[point]=v
        for tri in edges.get(point,()):inspect(tri)
        for tri in old.get(point,()):inspect(tri)
    return False


def incidences(triples):
    nb=defaultdict(list)
    for tri in triples:
        for p in tri:nb[p].append(tri)
    return nb


def base_source(d):
    marks=set(Q)|{v+d for v in Q}
    by=defaultdict(set)
    for a,b in combinations(sorted(marks),2):by[b-a].add(a)
    triples=[t for h,g in by.items() for t in triples_from_starts(g,h)]
    edges=incidences(triples)
    val={(v+d,v):1 for v in Q}
    if extend(val,edges,{},triples):raise ValueError("base contradiction")
    return marks,by,edges,val


def excludes(u,marks,by,edges,val):
    # Only the steps from the new mark to a base mark can add a triple.
    add=defaultdict(set)
    for a in marks:add[abs(u-a)].add(min(u,a))
    new=set()
    for h,starts in add.items():
        for a in starts:
            for b in starts|by.get(h,set()):
                if a!=b:
                    x,y=max(a,b),min(a,b)
                    new.add(((x,y),(x+h,y),(x+h,y+h)))
    return extend(val.copy(),incidences(new),edges,new)


def proof_db(d,u):
    marks=sorted(set(Q)|{v+d for v in Q}|{u})
    ix={(b,a):j+1 for j,(a,b) in enumerate(combinations(marks,2))}
    out=[[ix[x+d,x]] for x in Q]
    for x,y in ix:
        for u1 in marks:
            if u1<=x:continue
            v1=y+u1-x
            if (u1,v1) not in ix:continue
            clause=[ix[x,y],ix[u1,y],ix[u1,v1]]
            out.extend((clause,[-q for q in clause]))
    return out


def check_proofs(data):
    from verify_box_shapes import refuted
    out=defaultdict(set)
    for d,u,trace in data:
        cs=proof_db(d,u)
        if not trace or trace[-1]:raise ValueError("missing empty clause")
        for row in trace:
            if not refuted(cs,[-v for v in row]):raise ValueError("invalid propagation proof")
            cs.append(row)
        out[d].add(u)
    return out


def main():
    extra=check_proofs(json.loads((Path(__file__).resolve().parent/"order23_short_proofs.json").read_text()))
    w=[i*(86-i) for i in range(1,86)]
    a=[sum(x*y for x,y in zip(w,w[h:])) for h in range(85)]
    caps=[48 if N-h>=426 else 46 for h in range(1,85)]
    e=2*sum(x*y for x,y in zip(caps,a[1:]))
    high=max(k for k in range(N+1) if k*k*sum(w)**2<=(N+84)*(k*a[0]+e))
    low=N-2*high
    max_count=0
    for d in range(1,N-Q[-1]):
        mandatory,by,grid,values=base_source(d)
        width=N-Q[-1]-1-d
        excluded={u for u in range(-width,N) if u not in mandatory and excludes(u,mandatory,by,grid,values)}
        excluded.update(extra[d])
        largest=max(N-sum(-s<=u<N-s for u in excluded) for s in range(width+1))
        if largest>=low:raise ValueError((d,largest))
        max_count=max(max_count,largest)
    if (max_count,low)!=(133,134):raise ValueError((max_count,low))
    print(f"All 87 shifts, {sum(map(len,extra.values()))} additional proofs, at most {max_count} positions, need {low}.")


if __name__=="__main__":main()
