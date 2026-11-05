"""Bounded SAT discovery for Cartesian midpoint cuts.

For each listed finite B,C, cells are B x C and a positive equal-step corner
is ((b,c),(b+h,c),(b+h,c+h)).  The one SAT solve per listed pair tests whether
the resulting 3-uniform NAE constraints have a two-coloring.  This is raw
discovery data only, bounded to the hard-coded modest family below.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from pysat.solvers import Solver


OUT = Path(__file__).with_name("CARTESIAN_CUT_DISCOVERY_0016.json")


def interval(n: int) -> list[int]:
    return list(range(n))


def punctured(n: int, holes: set[int]) -> list[int]:
    return [x for x in range(n) if x not in holes]


# Intervals, punctured intervals, and two-scale separated products.  Every
# product has at most 100 cells; the list has exactly 30 distinct pairs.
CANDIDATES = [
    ("I7xI7", interval(7), interval(7)),
    ("I8xI8", interval(8), interval(8)),
    ("I9xI9", interval(9), interval(9)),
    ("I10xI10", interval(10), interval(10)),
    ("I6xI10", interval(6), interval(10)),
    ("I7xI10", interval(7), interval(10)),
    ("I8xI10", interval(8), interval(10)),
    ("I9xI10", interval(9), interval(10)),
    ("I5xI10", interval(5), interval(10)),
    ("I6xI9", interval(6), interval(9)),
    ("P8{3}xI7", punctured(8, {3}), interval(7)),
    ("P9{4}xI8", punctured(9, {4}), interval(8)),
    ("P10{4}xI9", punctured(10, {4}), interval(9)),
    ("P10{3,6}xI8", punctured(10, {3, 6}), interval(8)),
    ("P11{5}xI9", punctured(11, {5}), interval(9)),
    ("I8xP9{4}", interval(8), punctured(9, {4})),
    ("I9xP10{5}", interval(9), punctured(10, {5})),
    ("P9{2,6}xP9{4}", punctured(9, {2, 6}), punctured(9, {4})),
    ("P10{2,7}xP10{4,6}", punctured(10, {2, 7}), punctured(10, {4, 6})),
    ("P12{3,8}xP10{5}", punctured(12, {3, 8}), punctured(10, {5})),
    ("2I4x2I4", [2 * x for x in range(4)], [2 * x for x in range(4)]),
    ("2I5x2I5", [2 * x for x in range(5)], [2 * x for x in range(5)]),
    ("3I4x3I4", [3 * x for x in range(4)], [3 * x for x in range(4)]),
    ("I3+10I3 x I3+10I3", [a + 10 * q for q in range(3) for a in range(3)], [a + 10 * q for q in range(3) for a in range(3)]),
    ("I3+8I3 x I3+8I3", [a + 8 * q for q in range(3) for a in range(3)], [a + 8 * q for q in range(3) for a in range(3)]),
    ("I3+9I3 x I4+9I2", [a + 9 * q for q in range(3) for a in range(3)], [a + 9 * q for q in range(2) for a in range(4)]),
    ("I4+11I2 x I4+11I2", [a + 11 * q for q in range(2) for a in range(4)], [a + 11 * q for q in range(2) for a in range(4)]),
    ("I3+7I3 x I3+7I3", [a + 7 * q for q in range(3) for a in range(3)], [a + 7 * q for q in range(3) for a in range(3)]),
    ("I2+6I4 x I2+6I4", [a + 6 * q for q in range(4) for a in range(2)], [a + 6 * q for q in range(4) for a in range(2)]),
    ("I5+13I2 x I4+13I2", [a + 13 * q for q in range(2) for a in range(5)], [a + 13 * q for q in range(2) for a in range(4)]),
]


def reps(values: list[int]) -> dict[int, int]:
    value_set = set(values)
    return {h: sum(x + h in value_set for x in values) for h in range(1, max(values) - min(values) + 1) if any(x + h in value_set for x in values)}


def corners(B: list[int], C: list[int]):
    Bset, Cset = set(B), set(C)
    found = []
    for b in B:
        for c in C:
            for h in range(1, min(max(B) - b, max(C) - c) + 1):
                if b + h in Bset and c + h in Cset:
                    found.append(((b, c), (b + h, c), (b + h, c + h)))
    return found


def solve(B: list[int], C: list[int], triples):
    cells = [(b, c) for b in B for c in C]
    index = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for triple in triples:
        literals = [index[cell] for cell in triple]
        clauses.extend((literals, [-literal for literal in literals]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        if not solver.solve():
            return "UNSAT", None
        positive = set(solver.get_model())
    return "SAT", [[int(index[(b, c)] in positive) for c in C] for b in B]


def main() -> None:
    started = time.monotonic()
    records = []
    for name, B, C in CANDIDATES:
        triples = corners(B, C)
        rB, rC = reps(B), reps(C)
        U = sum(rB.get(h, 0) * rC.get(h, 0) for h in set(rB) | set(rC))
        status, colors = solve(B, C, triples)
        records.append({
            "name": name, "B": B, "C": C, "cells": len(B) * len(C),
            "r_B": rB, "r_C": rC, "U": U,
            "U_over_cells": U / (len(B) * len(C)),
            "exceeds_2_cells": U > 2 * len(B) * len(C),
            "solver_status": status, "color_array_rows_B_columns_C": colors,
        })
    result = {
        "purpose": "bounded Cartesian-cut SAT discovery; each listed pair received one solve",
        "definition": "U(B,C)=sum_{h>0} r_B(h) r_C(h), with triples ((b,c),(b+h,c),(b+h,c+h))",
        "candidate_count": len(records), "seconds": time.monotonic() - started,
        "records": records,
        "scope": "No universal conclusion follows from this bounded family or solver status; no certificate or verification pass is claimed.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{"name": x["name"], "cells": x["cells"], "U": x["U"], "ratio": x["U_over_cells"], "status": x["solver_status"]} for x in records]))


if __name__ == "__main__":
    main()
