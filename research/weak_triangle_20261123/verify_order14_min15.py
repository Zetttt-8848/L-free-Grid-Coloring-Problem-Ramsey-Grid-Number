"""Verify unconditional r_14 >= 15 (shells 2 and 3) and upgraded local packings through order 32."""

import argparse
import hashlib
import json
import lzma
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import ceil
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_143 import DATA, read_json
from verify_patch_proofs import check

COARSE = [(x, y) for x in range(1, 4) for y in range(x)]
COARSE_EDGES = [
    (COARSE.index((x, y)), COARSE.index((x + d, y)), COARSE.index((x + d, y + d)))
    for x, y in COARSE
    for d in range(1, 4 - x)
]
COARSE_OUTER = [COARSE.index(p) for p in ((1, 0), (3, 0), (3, 2))]


def coarse_orbit_reps(sides):
    def allowed(w):
        a, b, c = [w[i] for i in COARSE_OUTER]
        if sides in (0, 3):
            return (a, b, c) == (0, 0, 1)
        return a == 0 and b != 2 and (b != 0 or c != 2)

    active = set(range(sides))
    keep = {
        w for w in product(range(3), repeat=6)
        if allowed(w) and all(len({w[i] for i in e}) == 2 for e in COARSE_EDGES)
    }
    sym_maps = []
    for perm in permutations(range(3)):
        if {perm[i] for i in active} != active:
            continue
        image = []
        for x, y in COARSE:
            gaps = (x - y - 1, y, 3 - x)
            a, b, _ = [gaps[j] for j in perm]
            image.append(COARSE.index((1 + a + b, b)))
        sym_maps.append(image)
    pool = set(keep)
    reps = []
    while pool:
        w = min(pool)
        orbit = {tuple(pal[w[j]] for j in img) for pal in permutations(range(3)) for img in sym_maps} & keep
        if w != min(orbit) or not orbit <= pool:
            raise ValueError("Invalid symmetry orbit decomposition")
        pool -= orbit
        reps.append("".join(map(str, w)))
    return reps


def order14_shell_formula(sides, coarse_word):
    from pysat.card import CardEnc, EncType

    cells = [(x, y) for x in range(1, 14) for y in range(x)]
    idx = {p: i for i, p in enumerate(cells)}
    clauses = []
    for i in range(len(cells)):
        vals = [1 + 3 * i + c for c in range(3)]
        clauses.append(vals)
        clauses.extend([[-a, -b] for a, b in combinations(vals, 2)])
    outer = [1 + 3 * idx[p] for p in ((1, 0), (13, 0), (13, 12))]
    if sides in (0, 3):
        clauses.extend([[outer[0]], [outer[1]], [outer[2] + 1]])
    else:
        a, b, c = outer
        clauses.extend([[a], [-b - 2], [-b, -c - 2]])

    high = 3 * len(cells)
    flags = []
    faces = [[] for _ in range(sides)]
    for x, y in cells:
        for d in range(1, 14 - x):
            triple = [idx[p] for p in ((x, y), (x + d, y), (x + d, y + d))]
            g = (x - y - 1, y, 13 - x - d)
            touch = [i for i, h in enumerate(g) if h == 0]
            clauses.extend([[-1 - 3 * v - c for v in triple] for c in range(3)])
            allowed = len(touch) == 0 or (len(touch) == 1 and touch[0] < sides)
            flag = 0
            if allowed:
                high += 1
                flag = high
                face = touch[0] if touch else -1
                flags.append((g, flag, face))
                if touch:
                    faces[face].append(flag)
                    for u, v in combinations(triple, 2):
                        clauses.extend([[-flag, -1 - 3 * u - c, -1 - 3 * v - c] for c in range(3)])
            for palette in permutations(range(3)):
                row = [-1 - 3 * v - c for v, c in zip(triple, palette)]
                clauses.append(row + ([flag] if flag else []))

    def atmost(lits, limit):
        nonlocal high
        if limit < 0:
            clauses.append([])
        elif len(lits) <= limit:
            return
        elif limit == 0:
            clauses.extend([[-k] for k in lits])
        else:
            enc = CardEnc.atmost(lits=lits, bound=limit, top_id=high, encoding=EncType.seqcounter)
            clauses.extend(enc.clauses)
            high = max(high, enc.nv)

    for vals in faces:
        clauses.append(vals)
        atmost(vals, 1)
    atmost([v for _, v, f in flags if f < 0], 14 - sides)
    for m, minimum in ((12, 10), (11, 7), (10, 1)):
        for a in range(15 - m):
            for b in range(15 - m - a):
                margins = (a, b, 14 - m - a - b)
                outside_faces = {f for f in range(sides) if margins[f] > 0}
                vs = [v for g, v, f in flags if f not in outside_faces and any(i < j for i, j in zip(g, margins))]
                atmost(vs, 14 - minimum - len(outside_faces))

    clauses.extend([[1 + 3 * idx[(1 + 6 * (x - 1), 6 * y)] + int(ch)] for (x, y), ch in zip(COARSE, coarse_word)])
    return (f"p cnf {high} {len(clauses)}\n" + "".join(" ".join(map(str, r)) + " 0\n" for r in clauses)).encode("ascii")


def verify_case(task):
    entry, proof_dir, drat, rup = task
    dimacs = order14_shell_formula(entry["sides"], entry["coarse_word"])
    name = entry["name"]
    if hashlib.sha256(dimacs).hexdigest() != entry["cnf_sha256"]:
        raise ValueError(f"CNF SHA-256 mismatch for {name}")
    if proof_dir is not None:
        proof = lzma.decompress((proof_dir / f"{name}.rup.xz").read_bytes())
        if hashlib.sha256(proof).hexdigest() != entry["proof_sha256"]:
            raise ValueError(f"Proof SHA-256 mismatch for {name}")
        with TemporaryDirectory() as tmp:
            cnf = Path(tmp) / "in.cnf"
            tr = Path(tmp) / "pr.rup"
            cnf.write_bytes(dimacs)
            tr.write_bytes(proof)
            for checker in (drat, rup):
                check([checker, cnf, tr, "-U"])
    return name


@lru_cache(maxsize=None)
def weighted_corners_15(m, rule):
    if rule == "uniform":
        bound = None
    elif rule == "single" and 14 <= m <= 18:
        bound = 2 * m + 2
    elif rule == "multiple" and 14 <= m <= 18:
        bound = 3 * m + 1 if m >= 15 else 3 * m
    elif rule == "boundary" and m in (17, 18):
        bound = m + 2
    elif m == 14 and rule in ("11", "11a", "11b", "12", "13", "13b"):
        params = {
            "11": (10, 1, 220, 11),
            "11a": (10, 1, 220, 11),
            "11b": (20, 3, 490, 11),
            "12": (6, 1, 150, 12),
            "13": (3, 2, 123, 13),
            "13b": (3, 2, 123, 13),
        }
        base, extra, bound, s = params[rule]
        offsets = [(u + v, v) for u in range(m - s + 1) for v in range(m - s + 1 - u)]
    else:
        raise ValueError(f"Uncertified order-{m} weight rule {rule}")
    corners = []
    for x in range(m - 1):
        for y in range(x + 1):
            for j in range(1, m - 1 - x):
                faces = (y == 0) + (x == y) + (x + j == m - 2)
                if rule == "uniform":
                    weight = 1
                elif rule == "single":
                    weight = 2 + (faces == 1)
                elif rule == "multiple":
                    weight = 3 - max(0, faces - 1)
                elif rule == "boundary":
                    weight = 1 + (faces > 0)
                else:
                    containing = sum(0 <= y - oy <= x - ox and x - ox + j <= s - 2 for ox, oy in offsets)
                    weight = base + extra * containing
                corners.append((x, y, j, weight))
    return bound, corners


def expand_packing_15(record, generic, with_clearance=None):
    n = record["n"]
    load = Counter()
    score = 0
    for column in record["columns"]:
        m, step, a, b, c, rule, coefficient = column
        if min(a, b, c) < 0 or min(coefficient, step) <= 0 or a + b + c + (m - 2) * step != n - 2:
            raise ValueError("Invalid intermediate copy placement")
        if m >= n or m not in generic:
            raise ValueError("Induction requires smaller certified source")
        floor, corners = weighted_corners_15(m, rule)
        if floor is None:
            floor = with_clearance[m] if with_clearance and step == 1 else generic[m]
        for left, bottom, right in permutations((a, b, c)):
            ox, oy = left + bottom, bottom
            for x, y, j, weight in corners:
                xy = (ox + step * x, oy + step * y, step * j)
                if not 0 <= xy[1] <= xy[0] < xy[0] + xy[2] <= n - 2:
                    raise ValueError("Charged physical corner escapes host")
                load[xy] += coefficient * weight
            score += coefficient * floor
    value = Fraction(score, max(load.values()))
    if list(record["exact"]) != [value.numerator, value.denominator]:
        raise ValueError(f"Packing quotient mismatch at order {n}: {value} vs {record['exact']}")
    return max(ceil(value), generic.get(n, 0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof-dir", type=Path, help="directory containing extracted 2-*.rup.xz and 3-*.rup.xz traces")
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--rup-check", type=Path)
    parser.add_argument("--skip-cnf", action="store_true", help="skip python-sat CNF hash reconstruction")
    parser.add_argument("--jobs", type=int, default=2)
    args = parser.parse_args()
    if args.proof_dir and not (args.drat_trim and args.rup_check):
        parser.error("supply both --drat-trim and --rup-check with --proof-dir")

    manifest = read_json(DATA / "order14_min15.json")
    expected = [(s, w) for s in (2, 3) for w in coarse_orbit_reps(s)]
    actual = [(c["sides"], c["coarse_word"]) for c in manifest["cases"]]
    if actual != expected:
        raise ValueError("Incomplete orbit coverage for shells 2 and 3")

    if not args.skip_cnf:
        proof_dir = args.proof_dir.resolve() if args.proof_dir else None
        drat = args.drat_trim.resolve() if args.drat_trim else None
        rup = args.rup_check.resolve() if args.rup_check else None
        tasks = [(entry, proof_dir, drat, rup) for entry in manifest["cases"]]
        with ProcessPoolExecutor(args.jobs) as pool:
            checked_names = list(pool.map(verify_case, tasks))
        mode = "dual-checked RUP traces" if proof_dir else "reconstructed DIMACS formula hashes"
        print(f"PASS: Verified all {len(checked_names)} shell-2 and shell-3 orbits ({mode}); unconditional r_14 >= 15.")

    records = read_json(DATA / "local_boundary_packings_15.json")
    generic = {10: 1, 11: 3, 12: 6, 13: 11, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19}
    clearance = {10: 1, 11: 3, 12: 10, 13: 13}
    for field, dest in (("generic", generic), ("with_clearance", clearance)):
        for n, row in zip(range(14, 33), records[field], strict=True):
            ext = clearance if field == "with_clearance" else None
            got = expand_packing_15(row, generic, ext)
            if row["n"] != n or got != row["floor"]:
                raise ValueError(f"Mismatch in {field} packing at order {n}: got {got}, expected {row['floor']}")
            dest[n] = row["floor"]
    print("PASS: Upgraded local boundary packings under r_14 >= 15 verified for orders 14..32:")
    print("  Generic       (19..32):", *(generic[n] for n in range(19, 33)))
    print("  With clearance(19..32):", *(clearance[n] for n in range(19, 33)))


if __name__ == "__main__":
    main()
