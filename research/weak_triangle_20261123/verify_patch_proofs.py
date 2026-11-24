"""Replay the 539 archived group proofs or regenerate and check missing groups."""

import argparse
import hashlib
import lzma
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_143 import BASELINE, DATA, read_json


def check(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode or "s VERIFIED" not in result.stdout.splitlines():
        detail = (result.stdout + result.stderr)[-1000:]
        raise RuntimeError(f"{command[0]} failed\n{detail}")


def verify_group(baseline, proof_path, patch, words, checkers, generate, expected_formula=None):
    sys.path.insert(0, str(baseline))
    from verify_square_patches import square_formula

    clauses, dimacs = square_formula(patch, words)
    if expected_formula is not None and hashlib.sha256(dimacs).hexdigest() != expected_formula:
        raise ValueError(f"Regenerated formula disagrees with manifest for {proof_path.name}")
    existing = proof_path.is_file()
    if not existing and not generate:
        raise FileNotFoundError(proof_path)
    with TemporaryDirectory(prefix="weak-triangle-rup-") as tmp:
        cnf = Path(tmp) / "formula.cnf"
        proof = Path(tmp) / "proof.rup"
        cnf.write_bytes(dimacs)
        if existing:
            proof.write_bytes(lzma.decompress(proof_path.read_bytes()))
        else:
            from pysat.solvers import Solver

            with Solver(name="glucose4", bootstrap_with=clauses, with_proof=True) as solver:
                if solver.solve():
                    raise ValueError(f"Found a proper extension for {proof_path.name}")
                trace = Path(tmp) / "trace.drat"
                trace.write_text("\n".join(solver.get_proof()) + "\n", encoding="ascii")
            check([checkers[0], cnf, trace, "-l", proof, "-U"])

        for checker in checkers:
            check([checker, cnf, proof, "-U"])
        decoded = proof.read_bytes()
        if not existing:
            proof_path.write_bytes(lzma.compress(decoded, preset=3))
        return existing, proof_path.stat().st_size, hashlib.sha256(decoded).hexdigest()


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
    from verify_square_patches import PATCHES
    from verify_triangle_boundary import cost, orientations

    catalogs = read_json(baseline / "triangle_grid_catalogs.json.xz")
    deep = lzma.decompress((baseline / "triangle_13_through_12.txt.xz").read_bytes())
    if set(deep.decode("ascii").splitlines()) != set(catalogs["13/12"]):
        raise ValueError("The two archived order-13 catalogs disagree")
    expected = {
        (patch, group): (count, size, digest)
        for patch, group, count, size, digest
        in read_json(DATA / "baseline_patch_manifest.json")["groups"]
    }
    args.proof_dir.mkdir(parents=True, exist_ok=True)
    tasks = {}
    for index, patch in enumerate(PATCHES):
        order, budget, side, x, y, group_size, count, stride = patch
        cutoff, words = max(
            (int(key.split("/")[1]), words) for key, words in catalogs.items()
            if key.startswith(f"{order}/")
        )
        if cutoff < budget:
            raise ValueError(f"Missing catalog for order {order}, cutoff {budget}")
        forms = set()
        for word in words:
            encoded = word.encode("ascii")
            if cost(order, encoded) <= budget:
                forms.update(orientations(order, encoded))
        if len(forms) != count:
            raise ValueError(f"Unexpected orbit coverage for patch {index}")
        ordered = sorted(forms)
        for group, start in enumerate(range(0, count, group_size)):
            name = f"p{index:02d}_n{order}_b{budget}_s{side}_x{x}_y{y}_st{stride}_g{group:03d}.rup.xz"
            words = ordered[start:start + group_size]
            tasks[index, group] = (args.proof_dir / name, patch, words)
    if tasks.keys() != expected.keys():
        raise ValueError("Reconstructed groups disagree with the manifest")
    print(f"Checking {len(tasks)} groups across {len(PATCHES)} patches.", flush=True)
    regenerated = 0
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = {
            pool.submit(verify_group, baseline, proof_path, patch, words, checkers, args.generate_missing): key
            for key, (proof_path, patch, words) in tasks.items()
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            key = futures[future]
            existing, size, digest = future.result()
            count, historical_size, historical_digest = expected[key]
            if len(tasks[key][2]) != count:
                raise ValueError(f"Wrong case count for group {key}")
            same_trace = (size, digest) == (historical_size, historical_digest)
            if existing and not same_trace and not args.generate_missing:
                raise ValueError(f"Proof differs from the archived trace for group {key}")
            regenerated += not same_trace
            if completed % 50 == 0 or completed == len(tasks):
                print(f"Verified {completed}/{len(tasks)} groups.", flush=True)
    print(f"Both RUP checkers passed. Traces differing from the archival manifest: {regenerated}.")


if __name__ == "__main__":
    main()
