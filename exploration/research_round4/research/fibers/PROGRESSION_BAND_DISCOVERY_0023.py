"""Bounded new progression-cluster search for high single-band ratios.

This generates only new stepped-cluster and no-carry AP-product sources, skips
all source arrays saved by SOURCE_SINGLE_BAND_DISCOVERY_0020, and invokes SAT
once only when max_H T_H/M >= 1.  No old coloring is read or checked.
"""

from __future__ import annotations

import json
import threading
import time
from fractions import Fraction
from math import comb
from pathlib import Path

from pysat.solvers import Solver


HERE = Path(__file__).resolve()
OLD = HERE.with_name("SOURCE_SINGLE_BAND_DISCOVERY_0020.json")
OUT = HERE.with_name("PROGRESSION_BAND_DISCOVERY_0023.json")
LIMIT, SAT_SECONDS = 100, 2.0


def band_profile(A: list[int]):
    S, span, M = set(A), A[-1] - A[0], comb(len(A), 2)
    H, bands = 1, []
    while H <= span:
        total, by_h = 0, {}
        for h in range(H, min(2 * H, span + 1)):
            value = sum(x + d in S and x + h in S and x + d + h in S
                        for x in A for d in range(1, span + 1))
            if value:
                by_h[str(h)] = value
                total += value
        bands.append({"H": H, "T_H": total, "by_translation_h": by_h})
        H *= 2
    peak = max(bands, key=lambda x: x["T_H"])
    ratio = Fraction(peak["T_H"], M)
    return bands, peak, ratio


def corners(A: list[int]):
    S, result = set(A), []
    for u in A:
        for d in range(1, A[-1] - u + 1):
            if u + d not in S:
                continue
            for v in A:
                if u < v and v + d in S:
                    result.append(((u + d, u), (v + d, u), (v + d, v)))
    return result


def sat_once(A: list[int]):
    triples = corners(A)
    cells = sorted({cell for triple in triples for cell in triple})
    ix = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for triple in triples:
        row = [ix[x] for x in triple]
        clauses.extend((row, [-x for x in row]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        start = time.monotonic()
        timer.start()
        try:
            answer = solver.solve_limited(expect_interrupt=True)
            elapsed = time.monotonic() - start
            if answer is None:
                return "UNKNOWN", None, len(triples), elapsed
            if not answer:
                return "UNSAT", None, len(triples), elapsed
            model = set(solver.get_model())
            return "SAT", {f"{v},{u}": int(ix[(v, u)] in model) for v, u in cells}, len(triples), elapsed
        finally:
            timer.cancel()
            solver.clear_interrupt()


def old_sources():
    if not OLD.exists():
        return set()
    data = json.loads(OLD.read_text(encoding="utf-8"))
    return {tuple(record["A"]) for record in data.get("records", [])}


def candidates():
    prior, seen, pool = old_sources(), set(), []

    def add(name, blocks, family):
        A = sorted({x for block in blocks for x in block})
        if not (8 <= len(A) <= 24 and A[-1] - A[0] <= 300):
            return
        A = [x - A[0] for x in A]
        key = tuple(A)
        if key not in seen and key not in prior:
            seen.add(key)
            pool.append((name, A, blocks, family))

    # Three to five clusters, each a progression of non-unit step.  The
    # nonuniform centers keep this family separate from prior equal translates.
    for step in (2, 3, 4):
        for length in (3, 4, 5):
            base = [step * t for t in range(length)]
            for H in (13, 17, 21, 29, 37):
                for shifts in ([0, H, 2 * H], [0, H, 3 * H], [0, H, 2 * H, 4 * H],
                               [0, H, 3 * H, 4 * H], [0, H, 2 * H, 4 * H, 5 * H]):
                    if len(pool) >= LIMIT:
                        return pool
                    blocks = [[shift0 + x for x in base] for shift0 in shifts]
                    add(f"stepped_s{step}_l{length}_H{H}_layers{'-'.join(map(str,shifts))}", blocks,
                        "sparse union of 3-5 short progression clusters")

    # No-carry products B+H*G, with B a short AP and G a non-interval layer
    # set.  H exceeds span(B), so the displayed product coordinates are unique.
    for step in (2, 3, 4):
        for length in (3, 4, 5, 6):
            B = [step * t for t in range(length)]
            for H in (17, 23, 31, 43):
                for G in ([0, 1, 3], [0, 2, 3], [0, 1, 4], [0, 2, 5]):
                    if len(pool) >= LIMIT:
                        return pool
                    blocks = [[H * g + b for b in B] for g in G]
                    add(f"nocarry_AP_s{step}_l{length}_H{H}_G{'-'.join(map(str,G))}", blocks,
                        "no-carry product with a short AP factor")
    return pool[:LIMIT]


def main() -> None:
    records, found = [], None
    for name, A, raw_blocks, family in candidates()[:LIMIT]:
        M = comb(len(A), 2)
        bands, peak, ratio = band_profile(A)
        record = {"name": name, "provenance": family, "A": A, "raw_blocks": raw_blocks,
                  "size": len(A), "span": A[-1] - A[0], "M": M, "bands": bands,
                  "peak_H": peak["H"], "peak_T_H": peak["T_H"],
                  "peak_ratio_numerator": ratio.numerator, "peak_ratio_denominator": ratio.denominator,
                  "sat_called": ratio >= 1}
        if ratio >= 1:
            status, array, number, seconds = sat_once(A)
            record.update({"sat_status": status, "color_array": array,
                           "corner_count": number, "sat_seconds": seconds})
            if status == "SAT" and ratio > Fraction(7, 5):
                found = record
                records.append(record)
                break
        records.append(record)
    result = {"purpose": "bounded new progression-band discovery; SAT only for max T_H/M >= 1",
              "candidate_cap": LIMIT, "candidates_examined": len(records), "records": records,
              "first_SAT_ratio_gt_7_over_5": found,
              "scope": "No old literal input was solved or checked. Solver statuses are raw bounded discovery, and negative outcomes prove no universal statement."}
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidates_examined": len(records), "band_ratio_at_least_one": sum(x["sat_called"] for x in records),
                      "first_SAT_ratio_gt_7_over_5": found}))


if __name__ == "__main__":
    main()
