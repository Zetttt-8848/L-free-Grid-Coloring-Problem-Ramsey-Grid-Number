"""Verify that boundary-touching rainbow corners are forced at orders 17 and 18."""
import argparse
import lzma
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_rectangle_lines import check

HERE = Path(__file__).resolve().parent


def triples(n):
    cells = [(x,y) for x in range(1,n) for y in range(x)]
    index = {p:i for i,p in enumerate(cells)}
    for x,y in cells:
        for d in range(1,n-x):
            points = ((x,y),(x+d,y),(x+d,y+d))
            boundary = any(b == 0 or b == a-1 or a == n-1 for a,b in points)
            yield [index[p] for p in points], boundary


def formula(n):
    count = n*(n-1)//2
    rows = []
    for v in range(count):
        colors = [1+3*v+c for c in range(3)]
        rows.append(colors)
        rows.extend([[-i,-j] for i,j in combinations(colors,2)])
    for corners,boundary in triples(n):
        rows.extend([[-1-3*v-c for v in corners] for c in range(3)])
        if boundary:
            rows.extend([[-1-3*v-c for v,c in zip(corners,p)] for p in permutations(range(3))])
    last = (n-1)*(n-2)//2
    rows.extend([[1], [1+3*last], [2+3*(count-1)]])
    return (f"p cnf {3*count} {len(rows)}\n" +
            "".join(" ".join(map(str,row))+" 0\n" for row in rows)).encode("ascii")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker", type=Path, help="path to drat-trim")
    args = parser.parse_args()
    word = (HERE/"boundary_free_16.txt").read_text().strip()
    assert len(word)==120 and set(word)==set("012")
    counts = [0,0]
    for corners,boundary in triples(16):
        distinct = len({word[v] for v in corners})
        assert distinct >= 2
        if distinct==3:
            counts[boundary] += 1
    assert counts[1]==0
    print(f"T16 witness has {counts[0]} interior rainbows and zero boundary rainbows.")
    with TemporaryDirectory() as tmp:
        cnf,proof = Path(tmp)/"triangle.cnf",Path(tmp)/"triangle.rup"
        for n in (17,18):
            cnf.write_bytes(formula(n))
            proof.write_bytes(lzma.decompress((HERE/f"boundary_required_{n}.rup.xz").read_bytes()))
            check(args.checker.resolve(),cnf,proof)
            print(f"T{n} requires a boundary rainbow. RUP SHA-256 {sha256(proof.read_bytes()).hexdigest()}.")

if __name__=="__main__":
    main()
