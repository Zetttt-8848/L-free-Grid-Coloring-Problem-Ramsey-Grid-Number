"""Reconstruct and check groups of additional ambient-square refutations."""

import argparse
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from verify_143 import BASELINE, DATA, read_json
from verify_patch_proofs import verify_group


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--proof-dir", type=Path)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--rup-check", type=Path)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument(
        "--collection",
        choices=("side-141", "order12-side18", "side-140"),
        default="side-141",
    )
    parser.add_argument("--generate-missing", action="store_true")
    args = parser.parse_args()
    if args.proof_dir and not (args.drat_trim and args.rup_check):
        parser.error("supply both RUP checkers with --proof-dir")
    if args.generate_missing and not args.proof_dir:
        parser.error("--generate-missing requires --proof-dir")
    baseline = args.baseline.resolve()
    checkers = (args.drat_trim.resolve(), args.rup_check.resolve()) if args.proof_dir else None
    sys.path.insert(0, str(baseline))
    from verify_square_patches import Patch, square_formula
    from verify_triangle_boundary import cost, orientations

    catalogs = read_json(baseline / "triangle_grid_catalogs.json.xz")
    if args.collection == "side-141":
        manifest = read_json(DATA / "side_141_patch_manifest.json.xz")
        specs = read_json(DATA / "side_141_patches.json")
    elif args.collection == "order12-side18":
        manifest = read_json(DATA / "order12_side18_0_1.json.xz")
        specs = [[12, 9, 18, 0, 1, 1]]
    else:
        manifest = read_json(DATA / "side_140_patch_manifest.json.xz")
        specs = read_json(DATA / "side_140_patches.json")
    if [entry["patch"] for entry in manifest] != specs:
        raise ValueError("The patches in the manifest differ from the requested collection")
    deepest_by_order = {11: 6, 12: 9, 13: 12}
    tasks = []
    for entry in manifest:
        order, budget, side, x, y, stride = spec = entry["patch"]
        deepest = deepest_by_order[order]
        words = sorted({
            orientation for word in catalogs[f"{order}/{deepest}"]
            if cost(order, word.encode("ascii")) <= budget
            for orientation in orientations(order, word.encode("ascii"))
        })
        starts = list(range(0, len(words), 96))
        records = entry["proof_records"]
        if len(words) != entry["oriented_cases"] or [r["start"] for r in records] != starts:
            raise ValueError(f"Incomplete proof coverage for patch {spec}")
        patch = Patch(order, budget, side, x, y, 96, len(words), stride)
        directory = (args.proof_dir / "-".join(map(str, spec))) if args.proof_dir else None
        if directory is not None:
            directory.mkdir(parents=True, exist_ok=True)
        for start, record in zip(starts, records):
            group = words[start:start + 96]
            if record["spec"] != spec or record["count"] != len(group):
                raise ValueError(f"Incorrect group coverage for patch {spec}")
            if directory is None:
                import hashlib
                _, cnf = square_formula(patch, group)
                if hashlib.sha256(cnf).hexdigest() != record["cnf_sha256"]:
                    raise ValueError(f"Formula hash mismatch for {spec} at {start}")
            else:
                tasks.append((directory / f"{start:06d}.rup.xz", patch, group, record))

    if not args.proof_dir:
        total_groups = sum(len(e["proof_records"]) for e in manifest)
        print(f"Verified {total_groups} reconstructed formula hashes for collection {args.collection}.", flush=True)
        return

    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {
            pool.submit(verify_group, baseline, path, patch, words, checkers,
                        args.generate_missing, record["cnf_sha256"]): record["proof_sha256"]
            for path, patch, words, record in tasks
        }
        for count, future in enumerate(as_completed(futures), start=1):
            existing, _, digest = future.result()
            if existing and not args.generate_missing and digest != futures[future]:
                raise ValueError("An existing trace differs from the archive")
            if count % 50 == 0 or count == len(tasks):
                print(f"Verified {count}/{len(tasks)} proofs with both checkers.", flush=True)


if __name__ == "__main__":
    main()
