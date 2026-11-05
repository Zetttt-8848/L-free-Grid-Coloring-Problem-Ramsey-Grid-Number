#!/usr/bin/env python3
"""Bounded 81-cube telemetry run for the exact side-21 CNF."""

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


def bounded_solve(solver: Solver, assumptions: list[int], seconds: float) -> tuple[bool | None, float]:
    solver.clear_interrupt()
    timer = threading.Timer(seconds, solver.interrupt)
    started = time.perf_counter()
    timer.start()
    try:
        answer = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
    finally:
        timer.cancel()
        solver.clear_interrupt()
    return answer, time.perf_counter() - started


def stats_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    return {key: int(after.get(key, 0) - before.get(key, 0)) for key in sorted(set(before) | set(after))}


def load_phases(path: Path, n: int) -> list[int]:
    record = json.loads(path.read_text(encoding="utf-8"))
    values = record["best_grid"]
    if record.get("n") != n or len(values) != n * n or any(c not in (0, 1, 2) for c in values):
        raise ValueError("phase checkpoint is not an n-by-n zero-based three-color grid")
    phases = []
    for index, chosen in enumerate(values):
        x, y = divmod(index, n)
        for color in range(3):
            v = var(n, x, y, color)
            phases.append(v if color == chosen else -v)
    return phases


def decode_model(model: list[int], n: int) -> list[list[int]]:
    positive = {q for q in model if q > 0}
    grid = []
    for x in range(n):
        row = []
        for y in range(n):
            chosen = [c for c in range(3) if var(n, x, y, c) in positive]
            if len(chosen) != 1:
                raise AssertionError((x, y, chosen))
            row.append(chosen[0] + 1)
        grid.append(row)
    return grid


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--phase-checkpoint", type=Path, required=True)
    parser.add_argument("--solver", default="maplechrono")
    parser.add_argument("--overall-cap-seconds", type=float, default=600.0)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if not (0 < args.overall_cap_seconds <= 600):
        raise ValueError("overall cap must lie in (0,600]")

    formula = CNF(from_file=str(args.cnf))
    cube_data = json.loads(args.cubes.read_text(encoding="utf-8"))
    n = int(cube_data["n"])
    if n != 21 or len(cube_data["records"]) != 81:
        raise ValueError("expected the frozen side-21 81-cube manifest")
    phases = load_phases(args.phase_checkpoint, n)
    started = time.perf_counter()
    records = []
    witness_grid = None
    result = {
        "schema": "round3_lower_cube_telemetry_v1",
        "mathematical_status": "RUNNING",
        "n": n,
        "solver": args.solver,
        "python_sat_version": getattr(pysat, "__version__", "unknown"),
        "cnf_sha256": hashlib.sha256(args.cnf.read_bytes()).hexdigest(),
        "cube_manifest_sha256": hashlib.sha256(args.cubes.read_bytes()).hexdigest(),
        "phase_checkpoint_sha256": hashlib.sha256(args.phase_checkpoint.read_bytes()).hexdigest(),
        "overall_cap_seconds": args.overall_cap_seconds,
        "records": records,
        "non_claims": [
            "raw internal UNSAT without an independently checked proof is not mathematical UNSAT",
            "interrupted cubes are UNDECIDED",
            "solver counters are telemetry rather than proof",
        ],
    }
    with Solver(name=args.solver, bootstrap_with=formula.clauses, use_timer=True) as solver:
        solver.set_phases(phases)
        for cube in cube_data["records"]:
            elapsed_total = time.perf_counter() - started
            remaining = args.overall_cap_seconds - elapsed_total
            if remaining <= 0:
                break
            cap = min(float(cube["stage1_cap_seconds"]), remaining)
            before = solver.accum_stats()
            answer, elapsed = bounded_solve(solver, cube["assumption_literals"], cap)
            after = solver.accum_stats()
            status = "SAT" if answer is True else "RAW_UNSAT_UNVERIFIED" if answer is False else "INTERRUPTED_UNDECIDED"
            record = {
                "order": cube["order"],
                "cube_colors_0_based": cube["cube_colors_0_based"],
                "assumption_literals": cube["assumption_literals"],
                "round2_raw_status": cube["round2_raw_status"],
                "wall_cap_seconds": cap,
                "wall_seconds": elapsed,
                "status": status,
                "stats_delta": stats_delta(before, after),
            }
            records.append(record)
            result["records"] = records
            result["cubes_attempted"] = len(records)
            result["total_wall_seconds_so_far"] = time.perf_counter() - started
            save_json(args.result, result)
            if answer is True:
                witness_grid = decode_model(solver.get_model(), n)
                args.witness.parent.mkdir(parents=True, exist_ok=True)
                args.witness.write_text("\n".join(" ".join(map(str, row)) for row in witness_grid) + "\n", encoding="ascii")
                break

    counts = {status: sum(r["status"] == status for r in records) for status in ("SAT", "RAW_UNSAT_UNVERIFIED", "INTERRUPTED_UNDECIDED")}
    if witness_grid is not None:
        mathematical = "SAT_WITNESS_PENDING_INDEPENDENT_CHECK"
    else:
        mathematical = "UNDECIDED"
    result.update({
        "mathematical_status": mathematical,
        "cubes_attempted": len(records),
        "all_81_attempted": len(records) == 81,
        "statuses": counts,
        "total_wall_seconds": time.perf_counter() - started,
        "witness_path": str(args.witness) if witness_grid is not None else None,
    })
    save_json(args.result, result)
    print(json.dumps({key: result[key] for key in ("mathematical_status", "cubes_attempted", "all_81_attempted", "statuses", "total_wall_seconds", "witness_path")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

