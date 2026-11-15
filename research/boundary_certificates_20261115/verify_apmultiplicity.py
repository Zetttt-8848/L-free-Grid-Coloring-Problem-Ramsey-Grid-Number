"""Check finite obstructions to repeated arithmetic progressions on a binary strict source."""
from pathlib import Path
import json
from itertools import product
from verify_box_shapes import refuted


def source(marks,difference):
    # Each mark is an ordered label. Discover triples by selecting the starting
    # pair and the two target coordinates directly. This does not use grouping
    # by common differences, which was used to produce the certificates.
    cells=[(b,a) for a in marks for b in marks if b>a]
    var={q:i+1 for i,q in enumerate(cells)}
    clauses=[]
    for x,y in cells:
        for u in marks:
            if u<=x:continue
            step=difference(u,x)
            for v in marks:
                if v<=y or (u,v) not in var or difference(v,y)!=step:continue
                vs=[var[x,y],var[u,y],var[u,v]]
                clauses.extend((vs,[-z for z in vs]))
    return clauses,len(cells)


def residual_source(starts,size):
    marks=sorted({(j+t,r) for j,r in starts for t in range(size)})
    def difference(b,a):
        return (b[0]-a[0],() if b[1]==a[1] else (b[1],a[1]))
    return source(marks,difference)


def grid_source(numerator,denominator,special):
    marks=list(product(range(3),repeat=2))
    if special:
        integers=sorted({numerator*i+denominator*j for i,j in marks})
        return source(integers,lambda b,a:b-a)
    # Encode rank separately while keeping the formal vector difference.
    coords=sorted(marks,key=lambda p:numerator*p[0]+denominator*p[1])
    return source(list(range(9)),lambda b,a:tuple(i-j for i,j in zip(coords[b],coords[a])))


def main():
    configurations=[
        ("four-close-four-starts",[(0,i) for i in range(4)],4,False),
        ("four-touch-four-starts",[(0,0),(0,1),(0,2),(1,0)],4,False),
        ("four-close-three-attain",[(0,i) for i in range(3)],4,True),
        ("four-pair-cross-1",[(0,0),(1,1)],4,False),
        ("four-pair-cross-2",[(0,0),(2,1)],4,False),
        ("four-pair-align-2",[(0,0),(2,0)],4,False),
        ("four-pair-align-3",[(0,0),(3,0)],4,False),
        ("five-close-pair",[(0,0),(0,1)],5,False),
        ("five-touch-pair",[(0,0),(1,0)],5,False),
    ]
    records=json.loads((Path(__file__).resolve().parent/"progression_certificates.json").read_text())
    actual={row["case"]:row for row in records}
    tests=[(nm,*residual_source(x,s),v) for nm,x,s,v in configurations]
    tests.extend((k,*grid_source(a,b,s),ok) for k,a,b,s,ok in [
        ("square-interlocked",3,2,False,False),("square-step-double",2,1,True,False),
        ("square-separated",3,1,False,False),("square-equal",1,1,True,True)])
    for name,db,count,expected in tests:
        record=actual[name]
        assert record["colorable"]==expected
        proof=record["certificate"]
        if expected:
            model=set(proof)
            assert len(model)==count and set(map(abs,model))==set(range(1,count+1))
            assert all(any(v in model for v in clause) for clause in db)
        else:
            assert proof and proof[-1]==[]
            for clause in proof:
                assert all(0<abs(v)<=count for v in clause)
                assert refuted(db,[-v for v in clause]),name
                db.append(clause)
        print(name,"colorable" if expected else "excluded")


if __name__=="__main__":main()
