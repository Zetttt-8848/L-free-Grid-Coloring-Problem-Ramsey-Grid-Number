"""Check that the central order-13 triangle of a proper order-22 triangle has at least 12 rainbows."""
import argparse
import json
import lzma
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_rectangle_lines import check
from verify_triangle_boundary import cost, orbit

HERE = Path(__file__).resolve().parent


def index(x, y):
    return x*(x-1)//2+y


def clauses_for_center(words):
    side = 22
    cells = index(side, 0)
    clauses = []
    for v in range(cells):
        choices = [1+3*v+c for c in range(3)]
        clauses.append(choices)
        clauses.extend([[-choices[i], -choices[j]] for i in range(3) for j in range(i)])
    for x in range(1, side):
        for y in range(x):
            for d in range(1, side-x):
                triple = (index(x, y), index(x+d, y), index(x+d, y+d))
                clauses.extend([[-1-3*v-c for v in triple] for c in range(3)])
    center = [index(x+6, y+3) for x in range(1, 13) for y in range(x)]
    select = [3*cells+i+1 for i in range(len(words))]
    clauses.append(select)
    for flag, word in zip(select, words):
        clauses.extend([[-flag, 1+3*v+int(c)] for v, c in zip(center, word)])
    return select[-1], clauses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker", type=Path, help="compiled drat-trim executable")
    args = parser.parse_args()
    words = json.loads((HERE/"triangle_13_minimizers.json").read_text())
    assert len(set(words)) == len(words) == 21
    for word in words:
        encoded = word.encode("ascii")
        assert cost(13, encoded) == 11 and orbit(13, encoded) == 6
    variables, clauses = clauses_for_center(words)
    header = f"p cnf {variables} {len(clauses)}\n"
    with TemporaryDirectory() as directory:
        cnf = Path(directory)/"center.cnf"
        proof = Path(directory)/"center.rup"
        cnf.write_bytes((header + "".join(" ".join(map(str,c))+" 0\n" for c in clauses)).encode("ascii"))
        proof.write_bytes(lzma.decompress((HERE/"triangle_center_22.rup.xz").read_bytes()))
        check(str(args.checker.resolve()), cnf, proof)
    print(f"Verified all 21 center exclusions in a single {len(clauses):,}-clause formula.")


if __name__ == "__main__":
    main()
