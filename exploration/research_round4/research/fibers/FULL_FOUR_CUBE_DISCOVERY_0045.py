"""One raw unrestricted strict V(A) SAT query for A={subset sums of 1,3,9,27}."""
from itertools import product
from pathlib import Path
from threading import Timer
import json
import time

from pysat.solvers import Solver

GENERATORS = (1, 3, 9, 27)
A = sorted(sum(bit * g for bit, g in zip(bits, GENERATORS)) for bits in product((0, 1), repeat=4))
CELLS = [(v, u) for v in A for u in A if u < v]
INDEX = {cell: i + 1 for i, cell in enumerate(CELLS)}
CELL_SET = set(CELLS)

# Every positive equal-step corner in the full strict source triangle.
corners = []
for x, y in CELLS:
    for d in range(1, max(A) - x + 1):
        edge = ((x, y), (x + d, y), (x + d, y + d))
        if all(q in CELL_SET for q in edge):
            corners.append(edge)

clauses = []
for edge in corners:
    lit = [INDEX[q] for q in edge]
    clauses.extend((lit, [-q for q in lit]))

started = time.monotonic()
with Solver(name="g4", bootstrap_with=clauses) as solver:
    timer = Timer(30, solver.interrupt)
    timer.start()
    try:
        answer = solver.solve_limited(expect_interrupt=True)
    finally:
        timer.cancel()
    elapsed = time.monotonic() - started
    model = set(q for q in solver.get_model() if q > 0) if answer else None

record = {
    "scope": "One raw 30-second SAT observation. All 120 strict cells are independent variables; no type identifications are used. A false or null answer is not a theorem.",
    "source": A,
    "generators": list(GENERATORS),
    "cells": len(CELLS),
    "variables": len(INDEX),
    "positive_equal_step_corners": len(corners),
    "clauses": len(clauses),
    "answer": answer,
    "seconds": elapsed,
}
if answer:
    record["one_colored_cells"] = [list(q) for q in CELLS if INDEX[q] in model]

Path(__file__).with_suffix(".json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in record.items() if k != "one_colored_cells"}))
