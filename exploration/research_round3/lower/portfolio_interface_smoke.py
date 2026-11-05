#!/usr/bin/env python3
"""Smoke-test the exact API combination used by both portfolio workers."""

from __future__ import annotations

import argparse
import json
import threading
from pathlib import Path

from pysat.examples.genhard import PHP
from pysat.solvers import Solver


def test(name: str) -> dict[str, object]:
    formula = PHP(5)
    try:
        with Solver(name=name, bootstrap_with=formula.clauses, with_proof=True, use_timer=True) as solver:
            solver.set_phases([1, -2, 3])
            timer = threading.Timer(2.0, solver.interrupt)
            timer.start()
            try:
                answer = solver.solve_limited(expect_interrupt=True)
            finally:
                timer.cancel()
                try:
                    solver.clear_interrupt()
                except Exception:
                    pass
            proof = solver.get_proof() if answer is False else None
            return {
                "solver": name,
                "solve_limited_return": answer,
                "proof_lines": len(proof) if proof is not None else None,
                "proof_nonempty": bool(proof),
                "stats": solver.accum_stats(),
                "pass": answer is False and bool(proof),
            }
    except Exception as exc:
        return {"solver": name, "pass": False, "error_type": type(exc).__name__, "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    candidates = ["glucose4", "glucose3", "maplesat", "maplecm", "mergesat3", "minisat22", "lingeling"]
    result = {"schema": "round3_lower_portfolio_interface_smoke_v1", "solvers": [test(name) for name in candidates]}
    # The stage needs at least two workers that pass the exact combined API.
    result["passing_solvers"] = [r["solver"] for r in result["solvers"] if r["pass"]]
    result["pass"] = len(result["passing_solvers"]) >= 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
