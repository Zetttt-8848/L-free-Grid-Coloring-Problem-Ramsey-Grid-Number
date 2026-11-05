#!/usr/bin/env python3
"""Search the finite modular-affine family chi(x,y)=f(a*x+b*y mod m)."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import pysat
from pysat.solvers import Solver


def var(m: int, residue: int, color: int) -> int:
    return 3 * residue + color + 1


def constraints(n: int, m: int, a: int, b: int) -> tuple[list[list[int]], int]:
    clauses = []
    for r in range(m):
        vs = [var(m, r, c) for c in range(3)]
        clauses.append(vs)
        clauses.extend(([-vs[0], -vs[1]], [-vs[0], -vs[2]], [-vs[1], -vs[2]]))
    triples = set()
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                triple = ((a * x + b * y) % m, (a * (x + d) + b * y) % m, (a * (x + d) + b * (y + d)) % m)
                triples.add(triple)
    for r0, r1, r2 in sorted(triples):
        for c in range(3):
            clauses.append([-var(m, r0, c), -var(m, r1, c), -var(m, r2, c)])
    clauses.append([var(m, 0, 0)])
    return clauses, len(triples)


def decode(model: list[int], m: int) -> list[int]:
    positive = {q for q in model if q > 0}
    out = []
    for r in range(m):
        colors = [c for c in range(3) if var(m, r, c) in positive]
        if len(colors) != 1:
            raise AssertionError((r, colors))
        out.append(colors[0])
    return out


def render_grid(n: int, m: int, a: int, b: int, f: list[int]) -> str:
    return "\n".join(" ".join(str(f[(a * x + b * y) % m] + 1) for y in range(n)) for x in range(n)) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=21)
    parser.add_argument("--min-modulus", type=int, default=2)
    parser.add_argument("--max-modulus", type=int, default=50)
    parser.add_argument("--solver", default="maplechrono")
    parser.add_argument("--start-pair-index", type=int, default=0)
    parser.add_argument("--conflict-budget", type=int, default=100000)
    parser.add_argument("--wall-cap-seconds", type=float, default=180)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if (args.n, args.min_modulus, args.max_modulus) != (21, 2, 50):
        raise ValueError("parameters differ from the frozen first affine scan")
    expected_pairs = sum(m * m for m in range(args.min_modulus, args.max_modulus + 1))
    if expected_pairs != 42924:
        raise AssertionError(expected_pairs)

    started = time.perf_counter()
    raw_unsat = interrupted = attempted = 0
    hardest: list[dict[str, int]] = []
    witness_record = None
    stop = False
    global_pair_index = 0
    for m in range(args.min_modulus, args.max_modulus + 1):
        if stop:
            break
        for a in range(m):
            if stop:
                break
            for b in range(m):
                if global_pair_index < args.start_pair_index:
                    global_pair_index += 1
                    continue
                if time.perf_counter() - started >= args.wall_cap_seconds:
                    stop = True
                    break
                clauses, distinct_triples = constraints(args.n, m, a, b)
                with Solver(name=args.solver, bootstrap_with=clauses, use_timer=True) as solver:
                    solver.conf_budget(args.conflict_budget)
                    answer = solver.solve_limited()
                    stats = solver.accum_stats()
                    model = solver.get_model() if answer is True else None
                attempted += 1
                global_pair_index += 1
                score = int(stats.get("conflicts", 0))
                hardest.append({"m": m, "a": a, "b": b, "conflicts": score, "decisions": int(stats.get("decisions", 0)), "distinct_residue_triples": distinct_triples, "clauses": len(clauses)})
                hardest.sort(key=lambda r: (r["conflicts"], r["decisions"]), reverse=True)
                del hardest[20:]
                if answer is False:
                    raw_unsat += 1
                elif answer is None:
                    interrupted += 1
                else:
                    f = decode(model, m)
                    matrix = render_grid(args.n, m, a, b, f)
                    args.witness.parent.mkdir(parents=True, exist_ok=True)
                    args.witness.write_text(matrix, encoding="ascii")
                    witness_record = {
                        "m": m,
                        "a": a,
                        "b": b,
                        "f_0_based": f,
                        "matrix_sha256": hashlib.sha256(matrix.encode("ascii")).hexdigest(),
                    }
                    stop = True
                    break
    elapsed = time.perf_counter() - started
    result = {
        "schema": "round3_lower_affine_modular_scan_v1",
        "family": "chi(x,y)=f((a*x+b*y) mod m)",
        "n": args.n,
        "modulus_range_inclusive": [args.min_modulus, args.max_modulus],
        "coefficient_range": "all ordered (a,b) in Z_m^2 for each m",
        "expected_parameter_pairs": expected_pairs,
        "start_pair_index": args.start_pair_index,
        "pairs_in_epoch_scope": expected_pairs - args.start_pair_index,
        "pairs_attempted": attempted,
        "next_pair_index": args.start_pair_index + attempted,
        "raw_unsat_unverified": raw_unsat,
        "interrupted_undecided": interrupted,
        "solver": args.solver,
        "python_sat_version": getattr(pysat, "__version__", "unknown"),
        "per_call_conflict_budget": args.conflict_budget,
        "wall_cap_seconds": args.wall_cap_seconds,
        "wall_seconds": elapsed,
        "hardest_by_solver_conflicts": hardest,
        "witness": witness_record,
        "witness_path": str(args.witness) if witness_record else None,
        "mathematical_status": "SAT_WITNESS_PENDING_INDEPENDENT_CHECK" if witness_record else "UNDECIDED_NO_NEGATIVE_PROOFS",
        "non_claim": "raw UNSAT across a finite family is telemetry unless every negative decision receives an independently checked certificate",
    }
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("mathematical_status", "expected_parameter_pairs", "pairs_attempted", "raw_unsat_unverified", "interrupted_undecided", "wall_seconds", "witness")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
