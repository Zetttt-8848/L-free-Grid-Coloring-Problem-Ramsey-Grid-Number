"""Bounded one-band counterexample search for D1.

The candidate family is newly generated from short clusters and rank-layer
modifications.  A proper-coloring SAT call is made only after a candidate has
some dyadic band T_H>M.  Stored colorings are never reread or checked.
"""

from __future__ import annotations

import json
import threading
import time
from math import comb
from pathlib import Path

from pysat.solvers import Solver


OUT = Path(__file__).with_name("SOURCE_SINGLE_BAND_DISCOVERY_0020.json")
LIMIT = 120
SAT_SECONDS = 2.0


def bands(A: list[int]):
    S, span = set(A), A[-1] - A[0]
    H, output = 1, []
    while H <= span:
        total, by_h = 0, {}
        for h in range(H, min(2 * H, span + 1)):
            amount = sum(x + d in S and x + h in S and x + d + h in S
                         for d in range(1, span + 1) for x in A)
            if amount:
                by_h[str(h)] = amount
                total += amount
        output.append({"H": H, "T_H": total, "by_translation_h": by_h})
        H *= 2
    return output


def strict_corners(A: list[int]):
    S, result = set(A), []
    for u in A:
        for d in range(1, A[-1] - u + 1):
            if u + d not in S:
                continue
            for v in A:
                if v <= u or v + d not in S:
                    continue
                # The ordered source triangle uses distinct starts u<v.
                result.append(((u + d, u), (v + d, u), (v + d, v)))
    return result


def sat_once(A: list[int]):
    triples = strict_corners(A)
    cells = sorted({cell for triple in triples for cell in triple})
    index = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for triple in triples:
        lits = [index[x] for x in triple]
        clauses.extend((lits, [-x for x in lits]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        timer.start()
        try:
            answer = solver.solve_limited(expect_interrupt=True)
            elapsed = SAT_SECONDS if answer is None else None
            if answer is None:
                return "UNKNOWN", None, len(triples), elapsed
            if not answer:
                return "UNSAT", None, len(triples), elapsed
            positive = set(solver.get_model())
            colors = {f"{v},{u}": int(index[(v, u)] in positive) for v, u in cells}
            return "SAT", colors, len(triples), elapsed
        finally:
            timer.cancel()
            solver.clear_interrupt()


def candidate_pool():
    pool, seen = [], set()

    def add(name, blocks):
        A = sorted({x for block in blocks for x in block})
        if not (8 <= len(A) <= 28 and A[-1] - A[0] <= 400):
            return
        A = [x - A[0] for x in A]
        key = tuple(A)
        if key not in seen:
            seen.add(key)
            pool.append((name, A, blocks))

    # Two and three short clusters; shifts are chosen so their repeated
    # differences lie inside a selected dyadic start-gap band.
    bases = [list(range(q)) for q in range(4, 10)]
    bases += [[0, 1, 2, 4, 5], [0, 1, 3, 4, 6], [0, 2, 3, 5, 6, 8],
              [0, 1, 2, 5, 6, 7], [0, 1, 3, 4, 6, 7, 8]]
    for H in [8, 12, 16, 20, 24, 32, 40, 48]:
        for b in bases:
            if len(pool) >= LIMIT:
                return pool
            add(f"two_clusters_H{H}_b{','.join(map(str,b))}", [b, [H + x for x in b]])
            add(f"three_clusters_H{H}_b{','.join(map(str,b))}", [b, [H + x for x in b], [2 * H + x for x in b]])

    # Near-window rank-layer perturbations, deliberately excluding the prior
    # inherited 29/36 source itself.
    seeds = [[0, 1, 2, 5, 6, 7, 8, 11, 12], [0, 1, 3, 4, 6, 7, 8, 10, 11, 13]]
    for seed in seeds:
        for shift in [2, 3, 4, 5, 7, 9, 12, 16, 20, 24]:
            for index in range(1, len(seed) - 1):
                if len(pool) >= LIMIT:
                    return pool
                modified = seed[:index] + [seed[index] + shift] + seed[index + 1:]
                if len(set(modified)) == len(modified):
                    add(f"rank_layer_seed{len(seed)}_i{index}_s{shift}", [modified])
    return pool[:LIMIT]


def main() -> None:
    records, found = [], None
    for name, A, raw_blocks in candidate_pool()[:LIMIT]:
        M = comb(len(A), 2)
        profile = bands(A)
        peak = max(profile, key=lambda item: item["T_H"])
        record = {"name": name, "A": A, "raw_cluster_blocks": raw_blocks,
                  "size": len(A), "span": A[-1] - A[0], "M": M,
                  "bands": profile, "peak_H": peak["H"], "peak_T_H": peak["T_H"],
                  "band_exceeds_M": peak["T_H"] > M}
        if record["band_exceeds_M"]:
            began = time.monotonic()
            status, colors, corners, recorded = sat_once(A)
            record.update({"sat_status": status, "corner_count": corners,
                           "sat_seconds": (time.monotonic() - began if recorded is None else recorded),
                           "color_array": colors})
            if status == "SAT":
                found = record
                records.append(record)
                break
        records.append(record)
    result = {
        "purpose": "new bounded single-dyadic-band discovery; SAT only after T_H>M",
        "D1_test": "T_H <= M for every dyadic H",
        "candidate_cap": LIMIT, "candidates_examined": len(records), "records": records,
        "first_SAT_counterexample_candidate": found,
        "scope": "No stored coloring was checked. UNSAT and UNKNOWN are raw bounded solver statuses, not proof claims; lack of a SAT witness is not a universal result.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidates_examined": len(records), "first_SAT_counterexample_candidate": found,
                      "band_exceeders": sum(r["band_exceeds_M"] for r in records)}))


if __name__ == "__main__":
    main()
