"""One-shot greedy deletion discovery from the raw 0031 cube-free lead.

This intentionally does not rerun the parent source.  Each proper subset is
visited at most once and receives one bounded full strict-source SAT call.
"""

from __future__ import annotations

import json
import threading
import time
from collections import defaultdict
from pathlib import Path

from pysat.solvers import Solver


HERE = Path(__file__).resolve().parent
INPUT = HERE / "CUBE_FREE_COLOR_DISCOVERY_0031.json"
OUT = HERE / "CUBE_FREE_OBSTRUCTION_REDUCTION_0032.json"
CALL_CAP = 50
SAT_SECONDS = 2.0


def fibres(A):
    F = defaultdict(list)
    for i, u in enumerate(A):
        for v in A[i + 1:]:
            F[v - u].append(u)
    return F


def corners(A):
    result = []
    for d, starts in fibres(A).items():
        for i, u in enumerate(starts):
            for v in starts[i + 1:]:
                result.append(((u + d, u), (v + d, u), (v + d, v)))
    return result


def sat_once(A):
    triple_list = corners(A)
    cell_list = sorted({cell for triple in triple_list for cell in triple})
    index = {cell: i + 1 for i, cell in enumerate(cell_list)}
    clauses = []
    for triple in triple_list:
        literals = [index[cell] for cell in triple]
        clauses.extend((literals, [-literal for literal in literals]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        began = time.monotonic()
        timer.start()
        try:
            answer = solver.solve_limited(expect_interrupt=True)
            elapsed = time.monotonic() - began
            if answer is None:
                return "UNKNOWN", elapsed, triple_list, cell_list
            return ("SAT" if answer else "UNSAT"), elapsed, triple_list, cell_list
        finally:
            timer.cancel()
            solver.clear_interrupt()


def json_cells(items):
    return [[v, u] for v, u in items]


def json_corners(items):
    return [[list(a), list(b), list(c)] for a, b, c in items]


def main():
    parent = json.loads(INPUT.read_text(encoding="utf-8"))["first_raw_UNSAT_lead"]
    original = parent["A"]
    current = list(original)
    visited, attempts, reductions = {tuple(original)}, [], []
    reduction_found_in_sweep = True
    while len(attempts) < CALL_CAP and reduction_found_in_sweep:
        reduction_found_in_sweep = False
        # A new sweep starts only after retaining a strictly smaller raw-UNSAT
        # subset.  At the first retained deletion we restart from that source.
        for deleted in list(current):
            if len(attempts) >= CALL_CAP:
                break
            trial = [x for x in current if x != deleted]
            key = tuple(trial)
            if key in visited:
                continue
            visited.add(key)
            status, seconds, triple_list, cell_list = sat_once(trial)
            attempt = {
                "deleted_mark": deleted, "A": trial, "size": len(trial),
                "corner_count": len(triple_list), "cell_count": len(cell_list),
                "sat_status": status, "sat_seconds": seconds,
            }
            attempts.append(attempt)
            if status == "UNSAT":
                current = trial
                reductions.append(attempt)
                reduction_found_in_sweep = True
                break
    final_corners = corners(current)
    final_cells = sorted({cell for triple in final_corners for cell in triple})
    result = {
        "purpose": "raw greedy proper-subset obstruction reduction from CUBE_FREE_COLOR_DISCOVERY_0031",
        "original_claim_provenance": {
            "path": str(INPUT),
            "parent_source": original,
            "parent_raw_status": parent["sat_status"],
            "parent_call_was_not_rerun": True,
        },
        "per_subset_call_limit_seconds": SAT_SECONDS,
        "call_cap": CALL_CAP,
        "visited_sources_including_parent": [list(x) for x in visited],
        "attempts": attempts,
        "retained_raw_UNSAT_reductions": reductions,
        "final_raw_subset": current,
        "final_cell_list": json_cells(final_cells),
        "final_corner_list": json_corners(final_corners),
        "final_counts": {"marks": len(current), "corners": len(final_corners), "cells": len(final_cells)},
        "stopping_reason": ("call_cap" if len(attempts) >= CALL_CAP else "complete_deletion_sweep_with_no_reduction"),
        "scope": "Every attempted proper subset is distinct and was solved once. All SAT/UNSAT/UNKNOWN entries are raw discovery statuses; this is not a proof or a validation of the parent result.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"calls": len(attempts), "reductions": len(reductions),
                      "final_counts": result["final_counts"], "stopping_reason": result["stopping_reason"],
                      "statuses": [x["sat_status"] for x in attempts]}))


if __name__ == "__main__":
    main()
