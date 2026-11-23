"""Reconstruct and check every additional local proof group used at side 141."""

import argparse
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from verify_143 import BASELINE, DATA, read_json
from verify_patch_proofs import verify_group


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--rup-check", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--generate-missing", action="store_true")
    args = parser.parse_args()
    baseline = args.baseline.resolve()
    checkers = (args.drat_trim.resolve(), args.rup_check.resolve())
    sys.path.insert(0, str(baseline))
    from verify_square_patches import Patch
    from verify_triangle_boundary import cost, orientations

    catalogs = read_json(baseline / "triangle_grid_catalogs.json.xz")
    manifest = read_json(DATA / "side_141_patch_manifest.json.xz")
    specs = read_json(DATA / "side_141_patches.json")
    if [entry["patch"] for entry in manifest] != specs:
        raise ValueError("Manifest is missing a patch used in the arithmetic")
    tasks = []
    for entry in manifest:
        order, budget, side, x, y, stride = spec = entry["patch"]
        words = sorted({
            orientation for word in catalogs[f"{order}/{budget}"]
            if cost(order, word.encode("ascii")) <= budget
            for orientation in orientations(order, word.encode("ascii"))
        })
        starts = list(range(0, len(words), 96))
        records = entry["proof_records"]
        if len(words) != entry["oriented_cases"] or [r["start"] for r in records] != starts:
            raise ValueError(f"Incomplete proof coverage for patch {spec}")
        patch = Patch(order, budget, side, x, y, 96, len(words), stride)
        directory = args.proof_dir / "-".join(map(str, spec))
        directory.mkdir(parents=True, exist_ok=True)
        for start, record in zip(starts, records):
            group = words[start:start + 96]
            if record["spec"] != spec or record["count"] != len(group):
                raise ValueError(f"Incorrect group coverage for patch {spec}")
            tasks.append((directory / f"{start:06d}.rup.xz", patch, group, record["proof_sha256"]))

    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {
            pool.submit(verify_group, baseline, path, patch, words, checkers, args.generate_missing): digest
            for path, patch, words, digest in tasks
        }
        for count, future in enumerate(as_completed(futures), start=1):
            existing, _, digest = future.result()
            if existing and not args.generate_missing and digest != futures[future]:
                raise ValueError("An existing trace differs from the archive")
            if count % 50 == 0 or count == len(tasks):
                print(f"Verified {count}/{len(tasks)} proofs with both checkers.", flush=True)


if __name__ == "__main__":
    main()
