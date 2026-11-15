"""Check the four whole-board row and column palette refutations."""
import argparse
import json
import lzma
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_rectangle_lines import check

HERE = Path(__file__).resolve().parent
SIDE = 21


def formula(words, row_first):
    clauses = []
    last_variable = 3*SIDE*SIDE

    def exactly_one(choices):
        clauses.append(choices)
        clauses.extend([[-a,-b] for a,b in combinations(choices,2)])

    def line_maps():
        nonlocal last_variable
        maps = []
        for unused in range(SIDE):
            image = [[last_variable+3*i+j+1 for j in range(3)] for i in range(3)]
            last_variable += 9
            for row in image:
                exactly_one(row)
            for col in zip(*image):
                exactly_one(list(col))
            maps.append(image)
        for i in range(3):
            clauses.append([maps[0][i][i]])
        return maps

    rows, columns = line_maps(), line_maps()
    for x in range(SIDE):
        for y in range(SIDE):
            v = x*SIDE+y
            colors = [1+3*v+c for c in range(3)]
            exactly_one(colors)
            if x >= len(words):
                continue
            original = int(words[x][y])
            first, second = (rows[x],columns[y]) if row_first else (columns[y],rows[x])
            for i in range(3):
                for c in range(3):
                    clauses.append([-first[original][i],-second[i][c],colors[c]])
    for d in range(1,SIDE):
        for x in range(SIDE-d):
            for y in range(SIDE-d):
                triple = (x*SIDE+y,(x+d)*SIDE+y,(x+d)*SIDE+y+d)
                clauses.extend([[-1-3*v-c for v in triple] for c in range(3)])
    dimacs = f"p cnf {last_variable} {len(clauses)}\n" + "".join(
        " ".join(map(str,row))+" 0\n" for row in clauses
    )
    return clauses, dimacs.encode("ascii")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker",type=Path,help="compiled drat-trim executable")
    parser.add_argument("--cache",type=Path,help="read or store compressed RUP proofs")
    args = parser.parse_args()
    checker = args.checker.resolve()
    rectangle = json.loads((HERE/"rectangle_20_21.json").read_text())
    near = json.loads((HERE.parent/"coupled_budget_20261108/lower/runs/local71.json").read_text())["grid"]
    assert len(rectangle)==20 and len(near)==21
    for tag, template in (("rect", rectangle), ("near", near)):
        assert all(len(row)==SIDE and all(int(c) in (0,1,2) for c in row) for row in template)
        for row_first in (False,True):
            clauses, data = formula(template,row_first)
            name = tag+("reverse" if row_first else "")
            with TemporaryDirectory() as tmp:
                root = Path(tmp)
                cnf, raw, proof = root/"board.cnf",root/"raw.drat",root/"proof.rup"
                cnf.write_bytes(data)
                cache = args.cache/f"palette_proof_{name}_0"/"proof.rup.xz" if args.cache else None
                if cache and cache.is_file():
                    proof.write_bytes(lzma.decompress(cache.read_bytes()))
                else:
                    from pysat.solvers import Solver
                    with Solver(name="glucose4",bootstrap_with=clauses,with_proof=True) as solver:
                        if solver.solve():
                            raise AssertionError("unexpected proper square")
                        raw.write_bytes(("\n".join(solver.get_proof())+"\n").encode("ascii"))
                    check(checker,cnf,raw,"-l",proof)
                check(checker,cnf,proof)
                if cache and not cache.exists():
                    cache.parent.mkdir(parents=True,exist_ok=True)
                    cache.write_bytes(lzma.compress(proof.read_bytes(),preset=2))
            order = "rows then columns" if row_first else "columns then rows"
            print(f"Verified {tag}, {order}, {len(clauses):,} clauses.",flush=True)


if __name__=="__main__":
    main()
