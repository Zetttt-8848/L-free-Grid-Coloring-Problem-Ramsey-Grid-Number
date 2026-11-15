"""Verify finite interior-rainbow lower bounds for orders 15 and 16."""
import argparse
import lzma
from itertools import combinations, permutations
from math import comb
from pathlib import Path
from tempfile import TemporaryDirectory

from pysat.card import CardEnc, EncType
from verify_rectangle_lines import check

HERE = Path(__file__).resolve().parent


def formula(n, budget, minima):
    cells = [(x,y) for x in range(1,n) for y in range(x)]
    index = {point: i for i,point in enumerate(cells)}
    rows = []
    for v in range(len(cells)):
        colors = [1+3*v+c for c in range(3)]
        rows.append(colors)
        rows.extend([[-i,-j] for i,j in combinations(colors,2)])
    interior = []
    for x,y in cells:
        for d in range(1,n-x):
            points = ((x,y),(x+d,y),(x+d,y+d))
            corners = [index[p] for p in points]
            rows.extend([[-1-3*v-c for v in corners] for c in range(3)])
            boundary = any(b==0 or b==a-1 or a==n-1 for a,b in points)
            if boundary:
                rows.extend([[-1-3*v-c for v,c in zip(corners,p)] for p in permutations(range(3))])
            else:
                interior.append(((x-y-1,y,n-1-x-d),corners))
    rows.extend([[1], [1+3*index[(n-1,0)]], [2+3*index[(n-1,n-2)]]])
    high = 3*len(cells)
    selectors = []
    for position,corners in interior:
        high += 1
        selectors.append((position,high))
        rows.extend([[-1-3*v-c for v,c in zip(corners,p)]+[high] for p in permutations(range(3))])
    assert len(selectors)==comb(n-3,3)

    def at_most(flags,limit):
        nonlocal high
        if len(flags)<=limit:
            return
        encoding = EncType.pairwise if limit==1 else EncType.seqcounter
        block = CardEnc.atmost(flags,limit,high,encoding=encoding)
        rows.extend(block.clauses)
        high = max(high,block.nv)

    seen = set()
    for m,minimum in minima:
        if m>=n:
            continue
        for a in range(n-m+1):
            for b in range(n-m-a+1):
                c = n-m-a-b
                outside = tuple(flag for (i,j,k),flag in selectors if i<a or j<b or k<c)
                limit = budget-minimum
                if (outside,limit) not in seen:
                    at_most(outside,limit)
                    seen.add((outside,limit))
    at_most([v for _,v in selectors],budget)
    return (f"p cnf {high} {len(rows)}\n" +
            "".join(" ".join(map(str,row))+" 0\n" for row in rows)).encode("ascii")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker",type=Path,help="path to drat-trim")
    parser.add_argument("--improved",action="store_true",help="check the stronger bounds from the order-13-through-12 catalog")
    args = parser.parse_args()
    if args.improved:
        minima=((15,15),(14,14),(13,13),(12,6),(11,3))
        cases=((15,14,"order15_through14.rup.xz"),(16,15,"order16_through15.rup.xz"))
    else:
        minima=((15,14),(14,13),(13,11),(12,6),(11,3))
        cases=((16,14,"order16_interior.rup.xz"),)
    with TemporaryDirectory() as tmp:
        cnf,proof = Path(tmp)/"triangle.cnf",Path(tmp)/"triangle.rup"
        for n,budget,name in cases:
            cnf.write_bytes(formula(n,budget,minima))
            proof.write_bytes(lzma.decompress((HERE/name).read_bytes()))
            check(args.checker.resolve(),cnf,proof)
            print(f"Every proper order-{n} triangle with no boundary rainbow has at least {budget+1} interior rainbows.")



if __name__=="__main__":
    main()
