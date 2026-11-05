"""One-shot joint weak-triangle span search for four balanced sizes.

For each r this makes a single SAT call selecting r diagonal marks of each
of two colors and coloring every selected-cell weak triangle.  Results are
raw discovery statuses, with no replay or post-solve validation.
"""

from __future__ import annotations

import json
import threading
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.solvers import Solver


OUT = Path(__file__).with_name("WEAK_PRODUCT_SPAN_DISCOVERY_0035.json")
SAT_SECONDS = 3.0
RANKS = (4, 5, 6, 7)


def solve_once(r: int):
    L = (r - 1) ** 2 - 1
    next_var = 0

    def fresh():
        nonlocal next_var
        next_var += 1
        return next_var

    # Membership variables are diagonal colors: B and C are disjoint and
    # their union is the selected source S.  Cell signs are independent
    # variables except for the selected diagonal implications below.
    B = [fresh() for _ in range(L + 1)]
    C = [fresh() for _ in range(L + 1)]
    Z = {(v, u): fresh() for v in range(L + 1) for u in range(v + 1)}
    clauses = []
    for x in range(L + 1):
        clauses.append([-B[x], -C[x]])
        # B is sign 0, C is sign 1 on selected diagonal cells.
        clauses.append([-B[x], -Z[(x, x)]])
        clauses.append([-C[x], Z[(x, x)]])

    for membership in (B, C):
        enc = CardEnc.equals(lits=membership, bound=r, top_id=next_var,
                             encoding=EncType.seqcounter)
        clauses.extend(enc.clauses)
        next_var = enc.nv

    # For every numerical positive corner in W([0,L]), enforce NAE only
    # when every source coordinate used by its three cells is selected.
    # Its source-coordinate set may have two, three, or four marks.
    corner_count = 0
    for u in range(L + 1):
        for v in range(u, L + 1):
            for h in range(1, L - v + 1):
                p = (v, u)
                q = (v + h, u)
                t = (v + h, u + h)
                marks = {u, v, u + h, v + h}
                selected_neg = []
                for x in marks:
                    # x selected iff B[x] or C[x]; distribute the condition
                    # over its two membership literals in the clauses below.
                    selected_neg.append((B[x], C[x]))
                # Expand "not all marks selected or NAE" into one clause for
                # every choice of a membership literal at each mark.
                choices = [[]]
                for pair in selected_neg:
                    choices = [prior + [pick] for prior in choices for pick in pair]
                for selected_lits in choices:
                    guard = [-lit for lit in selected_lits]
                    clauses.append(guard + [Z[p], Z[q], Z[t]])
                    clauses.append(guard + [-Z[p], -Z[q], -Z[t]])
                corner_count += 1

    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        began = time.monotonic()
        timer.start()
        try:
            result = solver.solve_limited(expect_interrupt=True)
            seconds = time.monotonic() - began
            if result is None:
                return {"r": r, "L": L, "sat_status": "UNKNOWN", "sat_seconds": seconds,
                        "candidate_corner_templates": corner_count, "clauses": len(clauses)}
            if not result:
                return {"r": r, "L": L, "sat_status": "UNSAT", "sat_seconds": seconds,
                        "candidate_corner_templates": corner_count, "clauses": len(clauses)}
            model = set(solver.get_model())
            b = [x for x in range(L + 1) if B[x] in model]
            c = [x for x in range(L + 1) if C[x] in model]
            S = sorted(b + c)
            colors = {f"{v},{u}": int(Z[(v, u)] in model)
                      for v in S for u in S if u <= v}
            return {"r": r, "L": L, "sat_status": "SAT", "sat_seconds": seconds,
                    "candidate_corner_templates": corner_count, "clauses": len(clauses),
                    "S": S, "diagonal_B": b, "diagonal_C": c, "cell_colors": colors}
        finally:
            timer.cancel()
            solver.clear_interrupt()


def main() -> None:
    began, records, witness = time.monotonic(), [], None
    for r in RANKS:
        record = solve_once(r)
        records.append(record)
        if record["sat_status"] == "SAT":
            witness = record
            break
    result = {
        "purpose": "new bounded joint weak-product span counterexample discovery",
        "statement_tested": "proper two-color W(S), diagonal class sizes b=c=r, should have span(S) >= (r-1)^2",
        "encoding_scope": "all selected weak-source cells and every original positive corner whose source coordinates are selected; diagonal B/C memberships are selected jointly",
        "per_call_limit_seconds": SAT_SECONDS, "records": records,
        "first_raw_SAT_counterexample_candidate": witness,
        "elapsed_seconds": time.monotonic() - began,
        "scope": "One fresh SAT call per attempted r, no parallel process, replay, or validation. UNSAT and UNKNOWN are raw bounded discovery statuses only.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"attempted_r": [x["r"] for x in records],
                      "statuses": [x["sat_status"] for x in records],
                      "witness": witness is not None, "elapsed": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
