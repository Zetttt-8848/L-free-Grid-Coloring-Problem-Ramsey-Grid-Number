#!/usr/bin/env python3
"""One shard of the two-solver, 60-second hard-cube portfolio."""

from __future__ import annotations

import argparse
import hashlib
import json
import threading
import time
from pathlib import Path

import pysat
from pysat.formula import CNF
from pysat.solvers import Solver


def var(n: int, x: int, y: int, color: int) -> int:
    return 3 * (x * n + y) + color + 1


def phases_from_checkpoint(path: Path, n: int) -> list[int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    values = data["best_grid"]
    if data.get("n") != n or len(values) != n * n or any(c not in (0, 1, 2) for c in values):
        raise ValueError("invalid phase checkpoint")
    out = []
    for index, chosen in enumerate(values):
        x, y = divmod(index, n)
        for c in range(3):
            q = var(n, x, y, c)
            out.append(q if c == chosen else -q)
    return out


def limited(solver: Solver, seconds: float) -> tuple[bool | None, float]:
    solver.clear_interrupt()
    timer = threading.Timer(seconds, solver.interrupt)
    timer.start()
    started = time.perf_counter()
    try:
        answer = solver.solve_limited(expect_interrupt=True)
    finally:
        timer.cancel()
        solver.clear_interrupt()
    return answer, time.perf_counter() - started


def decode(model: list[int], n: int) -> str:
    positive = {q for q in model if q > 0}
    rows = []
    for x in range(n):
        row = []
        for y in range(n):
            chosen = [c for c in range(3) if var(n, x, y, c) in positive]
            if len(chosen) != 1:
                raise AssertionError((x, y, chosen))
            row.append(chosen[0] + 1)
        rows.append(row)
    return "\n".join(" ".join(map(str, row)) for row in rows) + "\n"


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--phase-checkpoint", type=Path, required=True)
    parser.add_argument("--solver", choices=("glucose4", "glucose3", "maplesat", "maplecm", "mergesat3", "minisat22"), required=True)
    parser.add_argument("--shard-index", type=int, choices=(0, 1), required=True)
    parser.add_argument("--start-target-index", type=int, default=0)
    parser.add_argument("--per-cube-seconds", type=float, default=60)
    parser.add_argument("--worker-wall-cap-seconds", type=float, default=1800)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if args.per_cube_seconds != 60 or args.worker_wall_cap_seconds != 1800:
        raise ValueError("portfolio caps differ from the directed checkpoint")

    formula = CNF(from_file=str(args.cnf))
    cube_data = json.loads(args.cubes.read_text(encoding="utf-8"))
    n = int(cube_data["n"])
    hard = [r for r in cube_data["records"] if r["round2_raw_status"] == "UNDECIDED"]
    if len(hard) != 48:
        raise ValueError(f"expected 48 hard cubes, found {len(hard)}")
    full_targets = [cube for position, cube in enumerate(hard) if position % 2 == args.shard_index]
    if len(full_targets) != 24 or not (0 <= args.start_target_index <= 24):
        raise AssertionError((len(full_targets), args.start_target_index))
    targets = full_targets[args.start_target_index:]
    phases = phases_from_checkpoint(args.phase_checkpoint, n)
    args.proof_dir.mkdir(parents=True, exist_ok=True)
    records = []
    started = time.perf_counter()
    result = {
        "schema": "round3_lower_hard_cube_worker_v1",
        "solver": args.solver,
        "python_sat_version": getattr(pysat, "__version__", "unknown"),
        "shard_index": args.shard_index,
        "shard_count": 2,
        "hard_cube_count_global": 48,
        "full_shard_target_count": 24,
        "start_target_index": args.start_target_index,
        "target_count": len(targets),
        "per_cube_cap_seconds": 60,
        "worker_wall_cap_seconds": 1800,
        "cnf_sha256": hashlib.sha256(args.cnf.read_bytes()).hexdigest(),
        "cube_manifest_sha256": hashlib.sha256(args.cubes.read_bytes()).hexdigest(),
        "phase_checkpoint_sha256": hashlib.sha256(args.phase_checkpoint.read_bytes()).hexdigest(),
        "cube_semantics": "base CNF conjoined with the four logged assumption literals as unit clauses",
        "records": records,
        "mathematical_status": "RUNNING",
    }
    for cube in targets:
        remaining = args.worker_wall_cap_seconds - (time.perf_counter() - started)
        if remaining <= 0:
            break
        cap = min(args.per_cube_seconds, remaining)
        augmented = list(formula.clauses) + [[q] for q in cube["assumption_literals"]]
        with Solver(name=args.solver, bootstrap_with=augmented, with_proof=True, use_timer=True) as solver:
            solver.set_phases(phases)
            answer, elapsed = limited(solver, cap)
            stats = solver.accum_stats()
            proof = solver.get_proof() if answer is False else None
            model = solver.get_model() if answer is True else None
        proof_path = None
        proof_hash = None
        if proof:
            proof_path = args.proof_dir / f"cube_{cube['order']:02d}.drat"
            proof_bytes = ("\n".join(proof) + "\n").encode("ascii")
            proof_path.write_bytes(proof_bytes)
            proof_hash = hashlib.sha256(proof_bytes).hexdigest()
        status = "SAT" if answer is True else "RAW_UNSAT_WITH_TRACE_UNCHECKED" if answer is False and proof else "RAW_UNSAT_EMPTY_TRACE" if answer is False else "INTERRUPTED_UNDECIDED"
        records.append({
            "order": cube["order"],
            "cube_colors_0_based": cube["cube_colors_0_based"],
            "assumption_literals": cube["assumption_literals"],
            "status": status,
            "wall_cap_seconds": cap,
            "wall_seconds": elapsed,
            "stats": stats,
            "proof_path": str(proof_path) if proof_path else None,
            "proof_lines": len(proof) if proof is not None else None,
            "proof_sha256": proof_hash,
        })
        result["records"] = records
        result["attempted"] = len(records)
        result["wall_seconds_so_far"] = time.perf_counter() - started
        save(args.result, result)
        if model is not None:
            matrix = decode(model, n)
            args.witness.parent.mkdir(parents=True, exist_ok=True)
            args.witness.write_text(matrix, encoding="ascii")
            result["witness_path"] = str(args.witness)
            result["witness_sha256"] = hashlib.sha256(matrix.encode("ascii")).hexdigest()
            break
    statuses = {s: sum(r["status"] == s for r in records) for s in sorted({r["status"] for r in records})}
    result.update({
        "attempted": len(records),
        "all_shard_targets_attempted": len(records) == len(targets),
        "statuses": statuses,
        "wall_seconds": time.perf_counter() - started,
        "mathematical_status": "SAT_WITNESS_PENDING_INDEPENDENT_CHECK" if any(r["status"] == "SAT" for r in records) else "UNDECIDED",
    })
    save(args.result, result)
    print(json.dumps({key: result[key] for key in ("solver", "shard_index", "attempted", "all_shard_targets_attempted", "statuses", "wall_seconds", "mathematical_status")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
