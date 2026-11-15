"""Verify which ordered progression products admit a proper binary strict source."""
from itertools import product
from pathlib import Path
import json

def canonical_source(dimensions):
    marks=list(product(*(range(d) for d in dimensions)))
    coords=[(b,a) for b in marks for a in marks if b>a]
    variables={cell:i+1 for i,cell in enumerate(coords)}
    # Directly enumerate the leftmost cell and its new column. Translate the
    # second coordinate by the same vector; retain a strict cell at the top.
    clauses=[]
    for b,a in coords:
        for v in marks:
            if v<=b:continue
            step=tuple(p-q for p,q in zip(v,b))
            w=tuple(p+d for p,d in zip(a,step))
            if (v,w) not in variables:continue
            row=(variables[b,a],variables[v,a],variables[v,w])
            clauses.extend((row,tuple(-x for x in row)))
    return clauses,len(coords)

def refuted(clauses,assumptions):
    assigned=set(assumptions)
    if any(-lit in assigned for lit in assigned):return True
    while True:
        before=len(assigned)
        for clause in clauses:
            if any(lit in assigned for lit in clause):continue
            free=[lit for lit in clause if -lit not in assigned]
            if not free:return True
            if len(free)==1:assigned.add(free[0])
        if len(assigned)==before:return False

def main():
    data=json.loads((Path(__file__).resolve().parent/"ordered_box_certificates.json").read_text())
    for row in data:
        shape=row["shape"];db,n=canonical_source(shape)
        if row["sat"]:
            m=set(row["data"])
            assert len(m)==n and set(map(abs,m))==set(range(1,n+1))
            assert all(any(x in m for x in clause) for clause in db)
        else:
            proof=row["data"]
            assert proof and not proof[-1]
            for clause in proof:
                assert all(0<abs(v)<=n for v in clause)
                assert refuted(db,[-v for v in clause])
                db.append(clause)
        print(" x ".join(map(str,shape)),n,"cells", "colorable" if row["sat"] else "excluded")
if __name__=="__main__":
    main()
