"""Check budget-14 refutations for rainbow Ls meeting multiple outer sides."""

import argparse
import hashlib
import json
import lzma
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
from tempfile import TemporaryDirectory

from pysat.card import CardEnc, EncType
from verify_patch_proofs import check

HERE = Path(__file__).resolve().parent


@lru_cache(maxsize=2)
def triangle_formula(extreme):
    cells = [(x, y) for x in range(1, 14) for y in range(x)]
    index = {p: i for i, p in enumerate(cells)}
    clauses = []
    for i in range(len(cells)):
        colors = [1 + 3 * i + c for c in range(3)]
        clauses.append(colors)
        clauses.extend([[-a, -b] for a, b in combinations(colors, 2)])
    if extreme:
        first, middle, last = [1 + 3 * index[p] for p in ((1, 0), (13, 0), (13, 12))]
        clauses.extend([[first], [-(middle + 2)], [-middle, -(last + 2)]])

    high = 3 * len(cells)
    flags = []
    for x, y in cells:
        for d in range(1, 14 - x):
            triple = [index[p] for p in ((x, y), (x + d, y), (x + d, y + d))]
            clauses.extend([[-(1 + 3 * v + c) for v in triple] for c in range(3)])
            high += 1
            flags.append(((x - y - 1, y, 13 - x - d), high))
            for palette in permutations(range(3)):
                clauses.append([-(1 + 3 * v + c) for v, c in zip(triple, palette)] + [high])

    def at_most(literals, bound):
        nonlocal high
        if len(literals) <= bound:
            return
        encoding = EncType.pairwise if bound <= 1 else EncType.seqcounter
        block = CardEnc.atmost(lits=list(literals), bound=bound, top_id=high, encoding=encoding)
        clauses.extend(block.clauses)
        high = max(high, block.nv)

    at_most([v for _, v in flags], 14)
    minima = ((13, 13), (12, 6), (11, 3), (10, 1)) if extreme else (
        (13, 13), (12, 10), (11, 7), (10, 1))
    used = set()
    for m, minimum in minima:
        for a in range(15 - m):
            for b in range(15 - m - a):
                c = 14 - m - a - b
                outside = tuple(v for (i, j, k), v in flags if i < a or j < b or k < c)
                key = (outside, 14 - minimum)
                if key not in used:
                    at_most(*key)
                    used.add(key)
    return index, tuple(flags), high, clauses


def formula(step):
    if step not in range(1, 13):
        raise ValueError("Invalid boundary step")
    extreme = step == 12
    index, flags, high, base = triangle_formula(extreme)
    clauses = base.copy()
    vertices = ((1, 0), (1 + step, 0), (1 + step, step))
    clauses.extend([[1 + 3 * index[p] + c] for c, p in enumerate(vertices)])
    if extreme:
        clauses.extend([[-v] for gap, v in flags if min(gap) == 0 and max(gap) > 0])
    else:
        chosen = (0, 0, 12 - step)
        clauses.extend([[-v] for gap, v in flags if gap != chosen and (gap[0] == 0 or gap[1] == 0)])
    dimacs = (f"p cnf {high} {len(clauses)}\n"
              + "".join(" ".join(map(str, row)) + " 0\n" for row in clauses)).encode("ascii")
    return clauses, dimacs


def verify(task):
    row, folder, drat, rup, generate = task
    step = row["step"]
    clauses, dimacs = formula(step)
    if hashlib.sha256(dimacs).hexdigest() != row["cnf_sha256"]:
        raise ValueError(f"Formula mismatch at step {step}")
    archive = folder / f"step-{step:02d}.rup.xz"
    with TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        cnf, proof = tmp / "triangle.cnf", tmp / "proof.rup"
        cnf.write_bytes(dimacs)
        if archive.is_file():
            raw = lzma.decompress(archive.read_bytes())
            if not generate and hashlib.sha256(raw).hexdigest() != row["proof_sha256"]:
                raise ValueError(f"Archived proof mismatch at step {step}")
            proof.write_bytes(raw)
        elif generate:
            from pysat.solvers import Solver
            with Solver(name="glucose4", bootstrap_with=clauses, with_proof=True) as solver:
                if solver.solve():
                    raise ValueError(f"Unexpected satisfying assignment at step {step}")
                trace = tmp / "proof.drat"
                trace.write_text("\n".join(solver.get_proof()) + "\n")
            check([drat, cnf, trace, "-l", proof, "-U"])
        else:
            raise FileNotFoundError(archive)
        for checker in (drat, rup):
            check([checker, cnf, proof, "-U"])
        if not archive.exists():
            archive.write_bytes(lzma.compress(proof.read_bytes(), preset=2))
    return step


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--rup-check", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--generate-missing", action="store_true")
    args = parser.parse_args()
    rows = json.loads((HERE / "data/order14_boundary.json").read_bytes())
    if [r["step"] for r in rows] != list(range(1, 13)):
        raise ValueError("Incomplete list of boundary cases")
    args.proof_dir.mkdir(parents=True, exist_ok=True)
    tasks = [(row, args.proof_dir.resolve(), args.drat_trim.resolve(), args.rup_check.resolve(),
              args.generate_missing) for row in rows]
    with ProcessPoolExecutor(args.jobs) as pool:
        for step in pool.map(verify, tasks):
            print(f"Step {step} checked by both verifiers.", flush=True)


if __name__ == "__main__":
    main()
