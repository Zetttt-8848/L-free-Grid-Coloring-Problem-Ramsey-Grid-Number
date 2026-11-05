#!/usr/bin/env python3
"""Attempt proof-logging solves only on the 33 formerly immediate cubes."""

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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--solver", default="glucose4")
    parser.add_argument("--per-cube-seconds", type=float, default=5.0)
    parser.add_argument("--proof-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (0 < args.per_cube_seconds <= 10):
        raise ValueError("proof cap must lie in (0,10]")
    formula = CNF(from_file=str(args.cnf))
    cubes = json.loads(args.cubes.read_text(encoding="utf-8"))
    targets = [r for r in cubes["records"] if r["round2_raw_status"] == "UNSAT"]
    if len(targets) != 33:
        raise ValueError(f"expected 33 legacy-quick targets, found {len(targets)}")
    args.proof_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for cube in targets:
        augmented = list(formula.clauses) + [[q] for q in cube["assumption_literals"]]
        with Solver(name=args.solver, bootstrap_with=augmented, with_proof=True, use_timer=True) as solver:
            answer, elapsed = limited(solver, args.per_cube_seconds)
            proof = solver.get_proof() if answer is False else None
            stats = solver.accum_stats()
        proof_path = None
        proof_hash = None
        if proof:
            proof_path = args.proof_dir / f"cube_{cube['order']:02d}.drat"
            proof_bytes = ("\n".join(proof) + "\n").encode("ascii")
            proof_path.write_bytes(proof_bytes)
            proof_hash = hashlib.sha256(proof_bytes).hexdigest()
        status = "RAW_UNSAT_WITH_TRACE_UNCHECKED" if answer is False and proof else "RAW_UNSAT_EMPTY_TRACE" if answer is False else "INTERRUPTED_UNDECIDED" if answer is None else "SAT_UNEXPECTED"
        records.append({
            "order": cube["order"],
            "cube_colors_0_based": cube["cube_colors_0_based"],
            "assumption_literals": cube["assumption_literals"],
            "status": status,
            "wall_seconds": elapsed,
            "stats": stats,
            "proof_path": str(proof_path) if proof_path else None,
            "proof_lines": len(proof) if proof is not None else None,
            "proof_sha256": proof_hash,
        })
    counts = {status: sum(r["status"] == status for r in records) for status in sorted({r["status"] for r in records})}
    result = {
        "schema": "round3_lower_quick_cube_proofs_v1",
        "solver": args.solver,
        "python_sat_version": getattr(pysat, "__version__", "unknown"),
        "input_cnf": str(args.cnf),
        "input_cnf_sha256": hashlib.sha256(args.cnf.read_bytes()).hexdigest(),
        "cube_manifest": str(args.cubes),
        "cube_manifest_sha256": hashlib.sha256(args.cubes.read_bytes()).hexdigest(),
        "target_rule": "exactly the 33 cubes with Round-2 raw status UNSAT",
        "per_cube_cap_seconds": args.per_cube_seconds,
        "counts": counts,
        "records": records,
        "mathematical_status": "UNDECIDED_PENDING_INDEPENDENT_PROOF_CHECK_AND_48_OTHER_CUBES",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"targets": len(targets), "counts": counts, "proof_line_total": sum(r["proof_lines"] or 0 for r in records)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

