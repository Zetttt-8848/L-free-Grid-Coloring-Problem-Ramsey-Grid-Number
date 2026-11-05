"""One-call-per-rank discovery on signed two-atom root sources.

Differences and corners are built from source pairs, never by scanning the
large ambient span.  Each requested r receives at most one 10-second SAT call.
"""

from __future__ import annotations

import itertools
import json
import threading
import time
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

from pysat.solvers import Solver


OUT = Path(__file__).with_name("SIGNED_ROOT_SOURCE_DISCOVERY_0024.json")
SAT_SECONDS = 10.0


def source(r: int):
    S = sum(9 ** i for i in range(1, r + 1))
    H = 1
    while H <= 8 * S:
        H *= 2
    D = 3 * H // 4
    w = [D + 9 ** i for i in range(1, r + 1)]
    A = sorted({si * w[i] + sj * w[j]
                for i, j in itertools.combinations(range(r), 2)
                for si in (-1, 1) for sj in (-1, 1)})
    return S, H, D, w, A


def fibers(A):
    out = defaultdict(list)
    for u, v in itertools.combinations(A, 2):
        out[v - u].append(u)
    return out


def geometry(A, H):
    F = fibers(A)
    T_H, per_difference, corners = 0, {}, []
    for d, starts in F.items():
        count = 0
        for u, v in itertools.combinations(starts, 2):
            h = v - u
            corners.append(((u + d, u), (v + d, u), (v + d, v)))
            if H <= h < 2 * H:
                count += 1
        if count:
            per_difference[str(d)] = count
            T_H += count
    return F, T_H, per_difference, corners


def sat_once(corners):
    cells = sorted({cell for triple in corners for cell in triple})
    ix = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for triple in corners:
        values = [ix[cell] for cell in triple]
        clauses.extend((values, [-x for x in values]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        started = time.monotonic()
        timer.start()
        try:
            answer = solver.solve_limited(expect_interrupt=True)
            elapsed = time.monotonic() - started
            if answer is None:
                return "UNKNOWN", None, elapsed, len(cells)
            if not answer:
                return "UNSAT", None, elapsed, len(cells)
            model = set(solver.get_model())
            colors = {f"{v},{u}": int(ix[(v, u)] in model) for v, u in cells}
            return "SAT", colors, elapsed, len(cells)
        finally:
            timer.cancel()
            solver.clear_interrupt()


def main() -> None:
    records, witness = [], None
    for r in (3, 4, 5, 6):
        S, H, D, w, A = source(r)
        F, T_H, per_difference, corners = geometry(A, H)
        M = comb(len(A), 2)
        ratio = Fraction(T_H, M)
        status, colors, seconds, used_cells = sat_once(corners)
        record = {
            "r": r, "S": S, "H": H, "D": D, "weights": w, "A": A,
            "size": len(A), "span": A[-1] - A[0], "M": M,
            "T_H": T_H, "T_H_over_M_numerator": ratio.numerator,
            "T_H_over_M_denominator": ratio.denominator,
            "fiber_count": len(F), "band_per_difference": per_difference,
            "corner_count": len(corners), "cell_count_used": used_cells,
            "sat_status": status, "sat_seconds": seconds, "color_array": colors,
        }
        records.append(record)
        if status == "SAT" and ratio > Fraction(7, 5):
            witness = record
            break
    result = {
        "purpose": "signed two-atom root-source discovery; exactly one bounded SAT call per attempted rank",
        "definition": "A_r={+-w_i+-w_j: i<j}, w_i=D+9^i, H is the least power of two above 8S, D=3H/4",
        "records": records, "first_SAT_ratio_gt_7_over_5": witness,
        "scope": "Raw solver statuses only; no coloring replay or verification is performed, and negatives prove no general statement.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ranks_attempted": [x["r"] for x in records],
                      "summary": [{"r": x["r"], "m": x["size"], "T_H": x["T_H"], "M": x["M"], "ratio": f'{x["T_H_over_M_numerator"]}/{x["T_H_over_M_denominator"]}', "status": x["sat_status"]} for x in records],
                      "witness": witness is not None}))


if __name__ == "__main__":
    main()
