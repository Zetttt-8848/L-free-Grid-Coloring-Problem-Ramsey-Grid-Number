#!/usr/bin/env python3
"""Smoke-test bounded solving and proof emission without extrapolating claims."""

from __future__ import annotations

import argparse
import json
import threading
import time
from pathlib import Path

import pysat
from pysat.examples.genhard import PHP
from pysat.solvers import Solver


def bounded_smoke(name: str) -> dict[str, object]:
    record: dict[str, object] = {"solver": name}
    try:
        with Solver(name=name, bootstrap_with=[[1], [-1]], use_timer=True) as solver:
            timer = threading.Timer(1.0, solver.interrupt)
            timer.start()
            started = time.perf_counter()
            try:
                answer = solver.solve_limited(expect_interrupt=True)
            finally:
                timer.cancel()
                solver.clear_interrupt()
            record.update({
                "constructed": True,
                "solve_limited_return": answer,
                "expected_unsat_observed": answer is False,
                "wall_seconds": time.perf_counter() - started,
                "stats": solver.accum_stats(),
            })
    except Exception as exc:  # interface audit records failures literally
        record.update({"constructed": False, "error_type": type(exc).__name__, "error": str(exc)})
    return record


def proof_smoke(name: str) -> dict[str, object]:
    record: dict[str, object] = {"solver": name}
    try:
        # Pigeonhole PHP(5): 6 pigeons into 5 holes.  This avoids solver
        # preprocessing reducing the formula to an empty trace.
        nontrivial_unsat = PHP(5)
        with Solver(name=name, bootstrap_with=nontrivial_unsat.clauses, with_proof=True) as solver:
            answer = solver.solve()
            proof = solver.get_proof()
            record.update({
                "constructed_with_proof": True,
                "solve_return": answer,
                "proof_object_type": type(proof).__name__,
                "proof_line_count": len(proof) if proof is not None else None,
                "proof_nonempty": bool(proof),
                "input_variables": nontrivial_unsat.nv,
                "input_clauses": len(nontrivial_unsat.clauses),
                "first_proof_lines": proof[:3] if proof else [],
            })
    except Exception as exc:
        record.update({"constructed_with_proof": False, "error_type": type(exc).__name__, "error": str(exc)})
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    proof_solvers = ["cadical195", "cadical300", "glucose3", "glucose4", "lingeling"]
    result = {
        "schema": "round3_lower_solver_tooling_smoke_v1",
        "python_sat_version": getattr(pysat, "__version__", "unknown"),
        "bounded_interface": bounded_smoke("maplechrono"),
        "proof_emission": [proof_smoke(name) for name in proof_solvers],
        "interpretation": "A nontrivial tiny proof object establishes only interface availability. It is not a proof of the n=21 instance and has not been independently checked.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["bounded_interface"].get("expected_unsat_observed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
