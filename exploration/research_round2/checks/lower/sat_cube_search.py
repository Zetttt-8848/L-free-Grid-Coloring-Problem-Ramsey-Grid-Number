#!/usr/bin/env python3
"""Bounded, explicit cube search for Round-2 directed L-free colorings.

The constructor and independent verifier deliberately live in separate files.
This program never labels an interrupted cube UNSAT.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import threading
import time
from pathlib import Path

from pysat.solvers import Solver


def var(n: int, row: int, col: int, color: int) -> int:
    return 3 * (row * n + col) + color + 1


def build_cnf(n: int) -> tuple[list[list[int]], dict[str, int]]:
    clauses: list[list[int]] = []

    # Exactly one of three colors at each cell.
    for row in range(n):
        for col in range(n):
            vs = [var(n, row, col, color) for color in range(3)]
            clauses.append(vs)
            clauses.extend(([-vs[0], -vs[1]], [-vs[0], -vs[2]], [-vs[1], -vs[2]]))

    geometric = 0
    # Mandate orientation: (x,y), (x+d,y), (x+d,y+d).
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                geometric += 1
                for color in range(3):
                    clauses.append(
                        [
                            -var(n, x, y, color),
                            -var(n, x + d, y, color),
                            -var(n, x + d, y + d, color),
                        ]
                    )

    # Sound color-permutation symmetry.  First cell is color 0.  In row-major
    # order color 2 may appear only after color 1 has appeared.
    clauses.append([var(n, 0, 0, 0)])
    for index in range(1, n * n):
        row, col = divmod(index, n)
        earlier_color_1 = [var(n, *divmod(j, n), 1) for j in range(1, index)]
        clauses.append([-var(n, row, col, 2), *earlier_color_1])

    exact_geometric = (n - 1) * n * (2 * n - 1) // 6
    if geometric != exact_geometric:
        raise AssertionError((geometric, exact_geometric))
    exact_total = 5 * n * n + 3 * geometric
    if len(clauses) != exact_total:
        raise AssertionError((len(clauses), exact_total))
    return clauses, {
        "variables": 3 * n * n,
        "geometric_triples": geometric,
        "forbidden_color_clauses": 3 * geometric,
        "cell_clauses": 4 * n * n,
        "symmetry_clauses": n * n,
        "total_clauses": len(clauses),
    }


def read_phase_grid(path: Path, n: int, transpose: bool) -> list[int]:
    rows = [[int(t) - 1 for t in line.split()] for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if not rows or any(len(row) != len(rows) for row in rows):
        raise ValueError("phase matrix must be square")
    if transpose:
        rows = [list(row) for row in zip(*rows)]
    old_n = len(rows)
    rng = random.Random(910_000 + n)
    grid = [rng.randrange(3) for _ in range(n * n)]
    for row in range(min(old_n, n)):
        for col in range(min(old_n, n)):
            grid[row * n + col] = rows[row][col]
    return grid


def phase_literals(n: int, grid: list[int]) -> list[int]:
    result = []
    for index, chosen in enumerate(grid):
        row, col = divmod(index, n)
        for color in range(3):
            v = var(n, row, col, color)
            result.append(v if color == chosen else -v)
    return result


def decode(n: int, model: list[int]) -> list[list[int]]:
    positive = {literal for literal in model if literal > 0}
    grid = []
    for row in range(n):
        out_row = []
        for col in range(n):
            colors = [color for color in range(3) if var(n, row, col, color) in positive]
            if len(colors) != 1:
                raise AssertionError(f"model gives colors {colors} at {(row, col)}")
            out_row.append(colors[0] + 1)
        grid.append(out_row)
    return grid


def write_matrix(path: Path, grid: list[list[int]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(" ".join(map(str, row)) for row in grid) + "\n", encoding="ascii")


def solve_epoch(solver: Solver, assumptions: list[int], seconds: float) -> tuple[bool | None, float]:
    solver.clear_interrupt()
    timer = threading.Timer(seconds, solver.interrupt)
    start = time.perf_counter()
    timer.start()
    try:
        answer = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
    finally:
        timer.cancel()
    elapsed = time.perf_counter() - start
    solver.clear_interrupt()
    return answer, elapsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--epoch-seconds", type=float, required=True)
    parser.add_argument("--cube-seed", type=int, required=True)
    parser.add_argument("--phase-matrix", type=Path)
    parser.add_argument("--transpose-phase", action="store_true")
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if not (0 < args.epoch_seconds <= 60):
        raise ValueError("each solver epoch must be in (0,60] seconds")

    clauses, counts = build_cnf(args.n)
    cube_indices = [1, args.n, args.n + 1, args.n * args.n - 1]
    cube_cells = [list(divmod(index, args.n)) for index in cube_indices]
    cubes = list(itertools.product(range(3), repeat=len(cube_indices)))
    random.Random(args.cube_seed).shuffle(cubes)
    cube_records = []
    witness_grid = None
    started = time.perf_counter()

    with Solver(name=args.solver, bootstrap_with=clauses, use_timer=True) as solver:
        if args.phase_matrix:
            phase = read_phase_grid(args.phase_matrix, args.n, args.transpose_phase)
            solver.set_phases(phase_literals(args.n, phase))

        for order, colors in enumerate(cubes):
            assumptions = [
                var(args.n, *divmod(index, args.n), color)
                for index, color in zip(cube_indices, colors)
            ]
            answer, elapsed = solve_epoch(solver, assumptions, args.epoch_seconds)
            status = "SAT" if answer is True else "UNSAT" if answer is False else "UNDECIDED"
            cube_records.append(
                {
                    "order": order,
                    "cube_colors_0_based": list(colors),
                    "assumption_literals": assumptions,
                    "status": status,
                    "wall_seconds": elapsed,
                }
            )
            if answer is True:
                witness_grid = decode(args.n, solver.get_model())
                write_matrix(args.witness, witness_grid)
                break

    statuses = {status: sum(r["status"] == status for r in cube_records) for status in ("SAT", "UNSAT", "UNDECIDED")}
    result = {
        "schema": "round2_lower_cube_search_v1",
        "mathematical_status": "SAT_WITNESS_PENDING_INDEPENDENT_VERIFICATION" if witness_grid else "UNDECIDED",
        "non_claims": [
            "UNDECIDED cubes are not UNSAT",
            "Even all internal UNSAT answers would require proof artifacts before an UNSAT claim",
        ],
        "n": args.n,
        "colors": 3,
        "orientation": "(x,y),(x+d,y),(x+d,y+d)",
        "solver": args.solver,
        "counts": counts,
        "symmetry_breaking": {
            "cell_0_color": 0,
            "restricted_growth": "color 2 cannot precede color 1 in row-major order",
            "justification": "permute color at cell 0 to 0, then swap residual colors 1 and 2 so their first occurrence is 1",
        },
        "cube_partition": {
            "cells_0_based": cube_cells,
            "all_color_tuples": "{0,1,2}^4",
            "cube_count": 81,
            "order_seed": args.cube_seed,
            "coverage": "Every total coloring assigns exactly one of the 81 tuples to these four cells",
        },
        "epoch_wall_cap_seconds": args.epoch_seconds,
        "phase_matrix": str(args.phase_matrix) if args.phase_matrix else None,
        "phase_matrix_transposed": bool(args.transpose_phase),
        "cubes_attempted": len(cube_records),
        "statuses": statuses,
        "total_wall_seconds": time.perf_counter() - started,
        "witness_path": str(args.witness) if witness_grid else None,
        "cube_records": cube_records,
    }
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("mathematical_status", "n", "counts", "cubes_attempted", "statuses", "total_wall_seconds", "witness_path")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
