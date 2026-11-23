"""Check every included order-13 word against the placement evidence for side 18."""
import argparse
import hashlib
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from verify_143 import BASELINE, DATA, read_json
from verify_patch_proofs import verify_group
from verify_placement_witnesses import check


def check_group(task):
    baseline, patch, words, offset, record, proof_root, checkers, generate = task
    from verify_square_patches import square_formula

    start, cnf_hash, proof_hash = record
    if proof_root is None:
        _, dimacs = square_formula(patch, words)
        if hashlib.sha256(dimacs).hexdigest() != cnf_hash:
            raise ValueError(f"The formula at offset {offset}, group {start} disagrees with the manifest")
    else:
        directory = proof_root / f"{offset[0]}-{offset[1]}"
        directory.mkdir(parents=True, exist_ok=True)
        proof = directory / f"{start:06d}.rup.xz"
        existing, _, digest = verify_group(baseline, proof, patch, words, checkers, generate)
        if existing and not generate and digest != proof_hash:
            raise ValueError(f"Unexpected archived proof at {proof}")
    return len(words)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof-dir", type=Path, help="replay traces extracted from the placement archive")
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--rup-check", type=Path)
    parser.add_argument("--generate-missing", action="store_true")
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()
    if args.proof_dir and not (args.drat_trim and args.rup_check):
        parser.error("supply both RUP checkers with --proof-dir")
    if args.generate_missing and not args.proof_dir:
        parser.error("--generate-missing requires --proof-dir")
    sys.path.insert(0, str(BASELINE))
    from verify_square_patches import PATCHES, Patch
    from verify_triangle_boundary import cost, orientations

    data = read_json(DATA / "order13_side18_profiles.json.xz")
    if tuple(data[k] for k in ("side", "order", "cutoff", "stride", "group_size")) != (18, 13, 12, 1, 96):
        raise ValueError("Unexpected host or source parameters")
    catalog = read_json(BASELINE / "triangle_grid_catalogs.json.xz")["13/12"]
    words = sorted({word for canonical in catalog for word in orientations(13, canonical.encode("ascii"))})
    if len(words) != data["oriented_cases"] or len(words) != 2928:
        raise ValueError("Incomplete source catalog")
    baseline_offsets = {(p.x, p.y) for p in PATCHES if (p.order, p.cutoff, p.side, p.stride) == (13, 12, 18, 1)}
    offsets = set()
    successes = {}
    tasks = []
    checkers = (args.drat_trim.resolve(), args.rup_check.resolve()) if args.proof_dir else None
    for placement in data["placements"]:
        x, y = offset = tuple(placement["offset"])
        if min(x, y) < 0 or x + y > 6 or offset in offsets or offset in baseline_offsets:
            raise ValueError("Repeated placement or invalid reflection representative")
        offsets.add(offset)
        survivors = set()
        for row in placement["survivors"]:
            i = row["index"]
            grid = row["square"]
            if not 0 <= i < len(words) or i in survivors:
                raise ValueError("Invalid survivor index")
            projection = "".join(grid[x + a][y + b] for a in range(12) for b in range(a + 1))
            if projection.encode("ascii") != words[i]:
                raise ValueError("The square does not carry the named catalog word")
            check(dict(spec=[13, 12, 18, x, y, 1], square=grid, rainbows=cost(13, words[i])))
            survivors.add(i)
        if survivors:
            successes[offset] = sorted(survivors)
        patch = Patch(13, 12, 18, x, y, 96, len(words), 1)
        expected = [(start, [w for i, w in enumerate(words[start:start + 96], start) if i not in survivors])
                    for start in range(0, len(words), 96)]
        expected = [(start, group) for start, group in expected if group]
        if [start for start, group in expected] != [row[0] for row in placement["groups"]]:
            raise ValueError("Missing group in the complement of the witnesses")
        for (_, group), record in zip(expected, placement["groups"]):
            tasks.append((BASELINE, patch, group, offset, record, args.proof_dir, checkers, args.generate_missing))
    all_offsets = {(x, y) for x in range(7) for y in range(7 - x)}
    if all_offsets - offsets - baseline_offsets != {(0, 6)} or successes != {(3, 2): [2103, 2300, 2337]}:
        raise ValueError("The complete placement table disagrees with the stated coverage")
    with ProcessPoolExecutor(args.jobs) as pool:
        total = sum(pool.map(check_group, tasks, chunksize=3))
    evidence = "checked by both RUP checkers" if args.proof_dir else "matched to reconstructed formula hashes"
    print(f"{len(tasks)} groups and {total:,} excluded orientations {evidence}.")
    print(f"{len(offsets) - len(successes) + len(baseline_offsets)} excluded orbits; survivors {successes}; open (0, 6).")


if __name__ == "__main__":
    main()
