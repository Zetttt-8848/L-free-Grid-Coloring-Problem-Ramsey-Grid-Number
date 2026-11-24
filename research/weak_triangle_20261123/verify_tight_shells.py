"""Replay the boundary obstructions for triangles with as many rainbows as their order."""

import argparse
import hashlib
import json
import lzma
import sys
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations, permutations, product
from pathlib import Path
from tempfile import TemporaryDirectory

from pysat.card import CardEnc, EncType
from verify_143 import BASELINE
from verify_patch_proofs import check

sys.path.insert(0, str(BASELINE))
from verify_order16_interior import formula as interior_formula

HERE = Path(__file__).resolve().parent
COARSE = [(x, y) for x in range(1, 4) for y in range(x)]
MINIMA = ((15, 15), (14, 14), (13, 13), (12, 10), (11, 7), (10, 1))


def coarse_representatives():
    triples = [(COARSE.index((x, y)), COARSE.index((x + d, y)), COARSE.index((x + d, y + d)))
               for x, y in COARSE for d in range(1, 4 - x)]
    candidates = {w for w in product(range(3), repeat=6)
                  if (w[0], w[3], w[5]) == (0, 0, 1)
                  and all(len({w[i] for i in triple}) == 2 for triple in triples)}
    maps = []
    for perm in permutations(range(3)):
        image = []
        for x, y in COARSE:
            gaps = (x - y - 1, y, 3 - x)
            a, b, _ = [gaps[j] for j in perm]
            image.append(COARSE.index((1 + a + b, b)))
        maps.append(image)
    representatives = []
    while candidates:
        w = min(candidates)
        orbit = {tuple(palette[w[j]] for j in image)
                 for palette in permutations(range(3)) for image in maps}
        representatives.append("".join(map(str, w)))
        candidates -= orbit
    return representatives


def order14_formula(sides, coarse_word):
    if sides not in (0, 1):
        raise ValueError("This certificate covers zero or one touched side")
    cells = [(x, y) for x in range(1, 14) for y in range(x)]
    idx = {p: i for i, p in enumerate(cells)}
    rows = []
    for k in range(len(cells)):
        colors = [1 + 3 * k + c for c in range(3)]
        rows.append(colors)
        rows.extend([[-a, -b] for a, b in combinations(colors, 2)])
    a, b, c = [1 + 3 * idx[p] for p in ((1, 0), (13, 0), (13, 12))]
    if sides == 0:
        rows.extend([[a], [b], [c + 1]])
    else:
        rows.extend([[a], [-b - 2], [-b, -c - 2]])

    high = 3 * len(cells)
    flags = []
    boundary_flags = []
    for x, y in cells:
        for d in range(1, 14 - x):
            triple = [idx[p] for p in ((x, y), (x + d, y), (x + d, y + d))]
            gaps = (x - y - 1, y, 13 - x - d)
            touched = [i for i, gap in enumerate(gaps) if gap == 0]
            rows.extend([[-1 - 3 * v - color for v in triple] for color in range(3)])
            flag = 0
            if not touched or (sides == 1 and touched == [0]):
                high += 1
                flag = high
                face = 0 if touched else -1
                flags.append((gaps, flag, face))
                if touched:
                    boundary_flags.append(flag)
                    for u, v in combinations(triple, 2):
                        rows.extend([[-flag, -1 - 3 * u - color, -1 - 3 * v - color]
                                     for color in range(3)])
            for palette in permutations(range(3)):
                row = [-1 - 3 * v - color for v, color in zip(triple, palette)]
                rows.append(row + ([flag] if flag else []))

    def at_most(lits, limit):
        nonlocal high
        if limit < 0:
            rows.append([])
        elif len(lits) <= limit:
            return
        elif limit == 0:
            rows.extend([[-v] for v in lits])
        else:
            block = CardEnc.atmost(lits=lits, bound=limit, top_id=high, encoding=EncType.seqcounter)
            rows.extend(block.clauses)
            high = max(high, block.nv)

    if sides == 1:
        rows.append(boundary_flags)
        at_most(boundary_flags, 1)
    at_most([v for _, v, face in flags if face < 0], 14 - sides)
    for m, floor in ((12, 10), (11, 7), (10, 1)):
        for a in range(15 - m):
            for b in range(15 - m - a):
                margins = (a, b, 14 - m - a - b)
                whole_side_outside = sides == 1 and a > 0
                outside = [v for g, v, face in flags
                           if not (whole_side_outside and face == 0)
                           and any(gap < margin for gap, margin in zip(g, margins))]
                at_most(outside, 14 - floor - int(whole_side_outside))
    if coarse_word is not None:
        rows.extend([[1 + 3 * idx[1 + 6 * (x - 1), 6 * y] + int(color)]
                     for (x, y), color in zip(COARSE, coarse_word)])
    return (f"p cnf {high} {len(rows)}\n"
            + "".join(" ".join(map(str, row)) + " 0\n" for row in rows)).encode("ascii")


def verify(task):
    entry, folder, drat, rup = task
    n = entry["order"]
    if n == 14:
        dimacs = order14_formula(entry["sides"], entry.get("coarse_word"))
    else:
        dimacs = interior_formula(n, n, MINIMA)
    name = entry["name"]
    if hashlib.sha256(dimacs).hexdigest() != entry["cnf_sha256"]:
        raise ValueError(f"Formula mismatch for {name}")
    proof = lzma.decompress((folder / f"{name}.rup.xz").read_bytes())
    if hashlib.sha256(proof).hexdigest() != entry["proof_sha256"]:
        raise ValueError(f"Proof mismatch for {name}")
    with TemporaryDirectory() as tmp:
        cnf, trace = Path(tmp) / "triangle.cnf", Path(tmp) / "checked.rup"
        cnf.write_bytes(dimacs)
        trace.write_bytes(proof)
        for checker in (drat, rup):
            check([checker, cnf, trace, "-U"])
    return name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--rup-check", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()
    rows = json.loads((HERE / "data/tight_shells.json").read_bytes())
    expected = [(14, 0, w, f"order14-zero-{w}") for w in coarse_representatives()]
    expected.extend([(14, 1, None, "order14-one"), (15, 0, None, "order15-interior"),
                     (16, 0, None, "order16-interior")])
    if [(r["order"], r["sides"], r.get("coarse_word"), r["name"]) for r in rows] != expected:
        raise ValueError("Incomplete boundary-case coverage")
    tasks = [(row, args.proof_dir.resolve(), args.drat_trim.resolve(), args.rup_check.resolve())
             for row in rows]
    with ProcessPoolExecutor(args.jobs) as pool:
        for name in pool.map(verify, tasks):
            print(f"{name} passed both proof checks.", flush=True)


if __name__ == "__main__":
    main()
