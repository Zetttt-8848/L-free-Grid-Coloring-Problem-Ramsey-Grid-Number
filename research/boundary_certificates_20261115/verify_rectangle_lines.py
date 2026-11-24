"""Rebuild each fixed-line grid formula and verify its RUP refutation."""
import argparse
import json
import lzma
import subprocess
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
SIZE = 21
KEPT = 7
CNF_DIGEST = {
    "rows": "83c9f916befe8c5e298d910977dedfde71998e37d4c13af4676a1546483924ec",
    "columns": "0929492e8268ec1ca89ea35d1cd2be97d2157cec765575b5b62a1e16e9bfc0bd",
}


def formula(rows, mode):
    def color(cell, c):
        return 1+3*cell+c

    clauses = []
    for v in range(SIZE*SIZE):
        choices = [color(v,c) for c in range(3)]
        clauses.append(choices)
        clauses.extend([[-a,-b] for a,b in combinations(choices,2)])
    for d in range(1, SIZE):
        for x in range(SIZE-d):
            for y in range(SIZE-d):
                cells = (x*SIZE+y, (x+d)*SIZE+y, (x+d)*SIZE+y+d)
                for c in range(3):
                    clauses.append([-color(v,c) for v in cells])
    num_lines = len(rows) if mode == "rows" else SIZE
    high = 3*SIZE*SIZE
    keep = [high+1+j for j in range(num_lines)]
    high += num_lines
    for v, c in enumerate("".join(rows)):
        j = v//SIZE if mode == "rows" else v%SIZE
        clauses.append([-keep[j], color(v,int(c))])

    # A true flag at (i,k) certifies at least k selected lines among the first i.
    previous = {}
    for i, selected in enumerate(keep, 1):
        current = {}
        for k in range(1, min(i,KEPT)+1):
            high += 1
            current[k] = high
            skip = [previous[k]] if k in previous else []
            clauses.append([-high]+skip+[selected])
            if k>1:
                clauses.append([-high]+skip+[previous[k-1]])
        previous = current
    clauses.append([previous[KEPT]])
    text = f"p cnf {high} {len(clauses)}\n"+ "".join(
        " ".join(map(str,clause))+" 0\n" for clause in clauses
    )
    return clauses, text.encode("ascii")


def check(checker, cnf, proof, *options):
    result = subprocess.run([checker,str(cnf),str(proof),*map(str,options),"-U"],
                            capture_output=True, text=True)
    if result.returncode or "s VERIFIED" not in result.stdout.splitlines():
        raise RuntimeError(result.stdout[-1000:]+result.stderr[-1000:])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker", help="path to a compiled drat-trim executable")
    parser.add_argument("--mode", choices=("rows", "columns", "both"), default="both")
    parser.add_argument("--cache", type=Path, help="read or save compressed, trimmed RUP proofs")
    args = parser.parse_args()
    checker = str(Path(args.checker).resolve())
    rows = json.loads((HERE/"rectangle_20_21.json").read_text())
    if len(rows)!=20 or any(len(row)!=SIZE or not set(row)<=set("012") for row in rows):
        raise ValueError("rectangle dimensions or palette")
    if args.cache:
        args.cache.mkdir(parents=True, exist_ok=True)
    for mode in (("rows","columns") if args.mode=="both" else [args.mode]):
        clauses, data = formula(rows, mode)
        if sha256(data).hexdigest()!=CNF_DIGEST[mode]:
            raise ValueError("geometric formula digest mismatch")
        stored = args.cache/f"linequota_{mode}_7_glucose4.xz" if args.cache else None
        with TemporaryDirectory() as directory:
            root = Path(directory)
            cnf, raw, proof = root/"grid.cnf", root/"untrimmed.drat", root/"proof.rup"
            cnf.write_bytes(data)
            if stored and stored.is_file():
                proof.write_bytes(lzma.decompress(stored.read_bytes()))
            else:
                from pysat.solvers import Solver
                with Solver(name="glucose4", bootstrap_with=clauses, with_proof=True) as solver:
                    if solver.solve():
                        raise RuntimeError("unexpected satisfying assignment")
                    raw.write_bytes(("\n".join(solver.get_proof())+"\n").encode("ascii"))
                check(checker, cnf, raw, "-l",proof)
            check(checker, cnf, proof)
            if stored and not stored.is_file():
                stored.write_bytes(lzma.compress(proof.read_bytes(), preset=2))
            print(f"Ruled out {KEPT} unchanged {mode}. "
                  f"RUP SHA-256 {sha256(proof.read_bytes()).hexdigest()}.", flush=True)


if __name__ == "__main__":
    main()
