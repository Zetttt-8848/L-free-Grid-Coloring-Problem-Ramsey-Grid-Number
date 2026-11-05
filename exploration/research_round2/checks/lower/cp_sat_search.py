#!/usr/bin/env python3
"""Bounded OR-Tools CP-SAT feasibility search for Round-2 directed L colorings."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import ortools
from ortools.sat.python import cp_model


def triples(n: int) -> list[tuple[int, int, int]]:
    out = [
        (x * n + y, (x + d) * n + y, (x + d) * n + y + d)
        for d in range(1, n)
        for x in range(n - d)
        for y in range(n - d)
    ]
    exact = (n - 1) * n * (2 * n - 1) // 6
    if len(out) != exact:
        raise AssertionError((len(out), exact))
    return out


def load_hint(path: Path, transpose: bool) -> np.ndarray:
    if path.suffix.lower() == ".json":
        record = json.loads(path.read_text(encoding="utf-8"))
        n = int(record["n"])
        data = np.asarray(record["best_grid"], dtype=np.int8).reshape((n, n))
        if record.get("schema", "").startswith("task_1_1_checkpoint"):
            data = data - 1
    else:
        rows = [[int(t) - 1 for t in line.split()] for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        if not rows or any(len(row) != len(rows) for row in rows):
            raise ValueError("hint matrix must be square")
        data = np.asarray(rows, dtype=np.int8)
    if np.any((data < 0) | (data > 2)):
        raise ValueError("hint colors must normalize to {0,1,2}")
    return data.T.copy() if transpose else data


def expanded_hint(n: int, source: np.ndarray, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    result = rng.integers(0, 3, size=(n, n), dtype=np.int8)
    m = min(n, source.shape[0])
    result[:m, :m] = source[:m, :m]
    return result


def render(values: list[int], n: int) -> str:
    return "\n".join(" ".join(str(values[r * n + c] + 1) for c in range(n)) for r in range(n)) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--solver-seconds", type=float, required=True)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--hint", type=Path)
    parser.add_argument("--transpose-hint", action="store_true")
    parser.add_argument("--max-changes", type=int)
    parser.add_argument("--no-symmetry", action="store_true")
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if not (0 < args.solver_seconds <= 60):
        raise ValueError("solver epoch must lie in (0,60] seconds")

    ts = triples(args.n)
    model = cp_model.CpModel()
    cells = [model.NewIntVar(0, 2, f"c_{r}_{c}") for r in range(args.n) for c in range(args.n)]
    forbidden = [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
    for a, b, c in ts:
        model.AddForbiddenAssignments([cells[a], cells[b], cells[c]], forbidden)
    if not args.no_symmetry:
        model.Add(cells[0] == 0)
        if len(cells) > 1:
            model.Add(cells[1] <= 1)

    hint_sha256 = None
    change_variables = []
    if args.hint:
        source = load_hint(args.hint, args.transpose_hint)
        hint = expanded_hint(args.n, source, args.seed)
        hint_text = render([int(v) for v in hint.reshape(-1)], args.n)
        hint_sha256 = hashlib.sha256(hint_text.encode("ascii")).hexdigest()
        for cell, value in zip(cells, hint.reshape(-1)):
            model.AddHint(cell, int(value))
        if args.max_changes is not None:
            for index, (cell, value) in enumerate(zip(cells, hint.reshape(-1))):
                changed = model.NewBoolVar(f"changed_{index}")
                model.Add(cell != int(value)).OnlyEnforceIf(changed)
                model.Add(cell == int(value)).OnlyEnforceIf(changed.Not())
                change_variables.append(changed)
            model.Add(sum(change_variables) <= args.max_changes)
    elif args.max_changes is not None:
        raise ValueError("--max-changes requires --hint")

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.solver_seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.cp_model_presolve = True
    started = time.perf_counter()
    status_code = solver.Solve(model)
    elapsed = time.perf_counter() - started
    status_name = solver.StatusName(status_code)
    feasible = status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL)
    witness_path = None
    if feasible:
        values = [solver.Value(cell) for cell in cells]
        if any(value not in (0, 1, 2) for value in values):
            raise AssertionError("CP-SAT returned an out-of-domain value")
        args.witness.parent.mkdir(parents=True, exist_ok=True)
        args.witness.write_text(render(values, args.n), encoding="ascii")
        witness_path = str(args.witness)

    record = {
        "schema": "round2_lower_cp_sat_v1",
        "status": "SAT_WITNESS_PENDING_INDEPENDENT_VERIFICATION" if feasible else "UNDECIDED",
        "raw_solver_status": status_name,
        "non_claims": ["UNKNOWN and unproved INFEASIBLE statuses are not UNSAT certificates"],
        "n": args.n,
        "colors": 3,
        "orientation": "(x,y),(x+d,y),(x+d,y+d)",
        "variables": len(cells),
        "geometric_triples": len(ts),
        "constraints": len(model.Proto().constraints),
        "symmetry_breaking": None if args.no_symmetry else "cell 0 = 0 and cell 1 <= 1; sound residual color permutation",
        "ortools_version": ortools.__version__,
        "random_seed": args.seed,
        "workers": args.workers,
        "solver_wall_cap_seconds": args.solver_seconds,
        "measured_wall_seconds": elapsed,
        "solver_wall_time_seconds": solver.WallTime(),
        "conflicts": solver.NumConflicts(),
        "branches": solver.NumBranches(),
        "hint_path": str(args.hint) if args.hint else None,
        "hint_transposed": bool(args.transpose_hint),
        "canonical_expanded_hint_sha256": hint_sha256,
        "max_changes_from_hint": args.max_changes,
        "change_variables": len(change_variables),
        "witness": witness_path,
    }
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
