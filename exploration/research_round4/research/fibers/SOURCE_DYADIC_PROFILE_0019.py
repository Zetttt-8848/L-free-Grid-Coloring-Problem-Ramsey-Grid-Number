"""Raw dyadic corner-band profiles from stored proper-source candidates.

No SAT or coloring check is performed.  The only new statistic is
T_H=sum_d sum_{H<=h<2H}|F_d intersect (F_d-h)| for dyadic H, where h is the
translation step between starts in one difference fiber, not the fiber offset d.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
WINDOW = ROOT / "research_round3" / "joint" / "window13.json"
WEIGHTS = ROOT / "research_round4" / "research" / "constant_weight_probe.json"
OUT = HERE.with_name("SOURCE_DYADIC_PROFILE_0019.json")
LIMIT = 100


def band_counts(A: list[int]):
    S = set(A)
    span = A[-1] - A[0]
    bands = []
    H = 1
    while H <= span:
        total = 0
        by_h = {}
        for h in range(H, min(2 * H, span + 1)):
            count = 0
            for d in range(1, span + 1):
                count += sum(x + d in S and x + h in S and x + d + h in S for x in A)
            if count:
                by_h[str(h)] = count
                total += count
        value = Fraction(total, comb(len(A), 2))
        bands.append({"H": H, "T_H": total, "T_H_over_M_numerator": value.numerator,
                      "T_H_over_M_denominator": value.denominator, "by_translation_h": by_h})
        H *= 2
    return bands


def saved_sources():
    pool = []
    weights = json.loads(WEIGHTS.read_text(encoding="utf-8"))
    for i, case in enumerate(weights["cases"]):
        if case.get("answer") is True and case.get("colors"):
            pool.append((case["marks"], {"file": str(WEIGHTS), "case_index": i,
                                          "stored_status": "answer=true with color array"}))
    window = json.loads(WINDOW.read_text(encoding="utf-8"))
    for entry in sorted(window["maximal_good"], key=lambda x: (-len(x["marks"]), x["marks"])):
        if entry.get("colors"):
            pool.append((entry["marks"], {"file": str(WINDOW), "mask": entry["mask"],
                                           "stored_status": "maximal_good with color array"}))
    result, seen = [], set()
    for A, provenance in pool:
        A0 = [x - A[0] for x in A]
        if tuple(A0) not in seen:
            seen.add(tuple(A0))
            result.append((A0, provenance))
    return result


def main() -> None:
    records, counterexample = [], None
    for A, provenance in saved_sources()[:LIMIT]:
        M = comb(len(A), 2)
        bands = band_counts(A)
        peak = max(bands, key=lambda b: b["T_H"])
        record = {"A": A, "size": len(A), "span": A[-1] - A[0], "M": M,
                  "provenance": provenance, "bands": bands,
                  "peak_H": peak["H"], "peak_T_H": peak["T_H"],
                  "peak_ratio_numerator": peak["T_H_over_M_numerator"],
                  "peak_ratio_denominator": peak["T_H_over_M_denominator"],
                  "candidate_T_H_gt_M": peak["T_H"] > M}
        records.append(record)
        if record["candidate_T_H_gt_M"]:
            counterexample = record
            break
    result = {
        "purpose": "bounded dyadic-band discovery on stored proper-source candidates; no color solving or verification",
        "definition": "T_H=sum_d sum_{H<=h<2H}|F_d intersect (F_d-h)|; h is translation step between starts",
        "source_cap": LIMIT, "examined_count": len(records), "records": records,
        "counterexample_candidate_T_H_gt_M": counterexample,
        "inherited_analytic_calibration": {"source": "A_H={0,H,2H,3H,4H} from DYADIC_CHARGING_0016.md section 5", "T_H": 6, "M": 10, "ratio_numerator": 3, "ratio_denominator": 5, "note": "recorded from the existing derivation; its coloring was not checked here"},
        "scope": "A bounded absence cannot establish a universal per-band constant. Stored statuses are provenance only.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"examined_count": len(records), "counterexample_candidate_T_H_gt_M": counterexample}))


if __name__ == "__main__":
    main()
