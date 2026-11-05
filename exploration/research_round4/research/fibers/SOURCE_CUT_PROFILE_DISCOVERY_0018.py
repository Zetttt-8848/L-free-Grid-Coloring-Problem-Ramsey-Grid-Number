"""Balanced-cut discovery profile on saved literal proper-source records.

This reads existing records only and never solves or checks their stored
colorings.  For each retained source it computes U and V at the balanced
source-rank cut, seeking raw candidates against U<=bc or 2U+V<=5bc.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
WINDOW = ROOT / "research_round3" / "joint" / "window13.json"
WEIGHTS = ROOT / "research_round4" / "research" / "constant_weight_probe.json"
OUT = HERE.with_name("SOURCE_CUT_PROFILE_DISCOVERY_0018.json")
LIMIT = 100


def reps(A: list[int]) -> dict[int, int]:
    S = set(A)
    return {h: sum(x + h in S for x in A)
            for h in range(1, A[-1] - A[0] + 1)
            if any(x + h in S for x in A)}


def profile(A: list[int]):
    split = len(A) // 2
    B, C = A[:split], A[split:]
    rB, rC = reps(B), reps(C)
    q = {}
    for b in B:
        for c in C:
            h = c - b
            if h > 0:
                q[h] = q.get(h, 0) + 1
    U = sum(rB.get(h, 0) * rC.get(h, 0) for h in set(rB) | set(rC))
    V = sum((rB.get(h, 0) + rC.get(h, 0)) * count for h, count in q.items())
    bc = len(B) * len(C)
    return B, C, rB, rC, q, U, V, bc


def saved_sources():
    """Return sources with stored-color provenance, without interpreting it."""
    pool = []
    weights = json.loads(WEIGHTS.read_text(encoding="utf-8"))
    for index, case in enumerate(weights["cases"]):
        if case.get("answer") is True and case.get("colors"):
            pool.append((case["marks"], {"file": str(WEIGHTS), "case_index": index,
                                          "stored_status": "answer=true with color array"}))
    window = json.loads(WINDOW.read_text(encoding="utf-8"))
    candidates = sorted(window["maximal_good"], key=lambda x: (-len(x["marks"]), x["marks"]))
    for entry in candidates:
        if entry.get("colors"):
            pool.append((entry["marks"], {"file": str(WINDOW), "mask": entry["mask"],
                                           "stored_status": "maximal_good with color array"}))
    unique, seen = [], set()
    for A, provenance in pool:
        normalized = tuple(x - A[0] for x in A)
        if normalized not in seen:
            seen.add(normalized)
            unique.append((list(normalized), provenance))
    return unique


def main() -> None:
    records = []
    counterexample = None
    for A, provenance in saved_sources()[:LIMIT]:
        B, C, rB, rC, q, U, V, bc = profile(A)
        two_u_v = 2 * U + V
        record = {
            "A": A, "size": len(A), "balanced_rank_split": len(B), "B": B, "C": C,
            "provenance": provenance, "r_B": rB, "r_C": rC, "q_cross_difference": q,
            "U": U, "V": V, "bc": bc,
            "U_over_bc_numerator": Fraction(U, bc).numerator,
            "U_over_bc_denominator": Fraction(U, bc).denominator,
            "two_U_plus_V": two_u_v,
            "two_U_plus_V_over_bc_numerator": Fraction(two_u_v, bc).numerator,
            "two_U_plus_V_over_bc_denominator": Fraction(two_u_v, bc).denominator,
            "candidate_U_gt_bc": U > bc,
            "candidate_2U_plus_V_gt_5bc": two_u_v > 5 * bc,
        }
        records.append(record)
        if record["candidate_U_gt_bc"] or record["candidate_2U_plus_V_gt_5bc"]:
            counterexample = record
            break
    result = {
        "purpose": "bounded cut-quantity discovery using saved literal proper-source records only",
        "source_cap": LIMIT, "examined_count": len(records),
        "balanced_cut": "B is the first floor(|A|/2) source ranks and C is the remainder",
        "definitions": {"U": "sum_h r_B(h)r_C(h)", "V": "sum_h (r_B(h)+r_C(h))q(h)", "q": "#{(b,c) in BxC:c-b=h}"},
        "records": records, "counterexample_candidate": counterexample,
        "scope": "No coloring was solved or checked. Stored properness labels are reused as provenance; negative absence is bounded discovery only.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"examined_count": len(records), "counterexample_candidate": counterexample}))


if __name__ == "__main__":
    main()
