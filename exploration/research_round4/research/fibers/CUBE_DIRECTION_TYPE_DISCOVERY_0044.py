"""Raw SAT discovery for direction types in one separated Boolean 3-cube.

One call is made for each requested type triple until a SAT triple with
fewer than two P directions is found.  This script is discovery only.
"""
import itertools
import json
import time
from pathlib import Path

from pysat.solvers import Solver

A = [0, 1, 4, 5, 16, 17, 20, 21]
STEPS = [1, 4, 16]
OUT = Path(__file__).with_suffix(".json")
cells = [(v, u) for i, v in enumerate(A) for u in A[:i]]
ix = {cell: i + 1 for i, cell in enumerate(cells)}


def bitvec(x):
    return ((x & 1) > 0, (x & 4) > 0, (x & 16) > 0)


def edge_cells(direction):
    step = STEPS[direction]
    return [(x + step, x) for x in A if not bitvec(x)[direction]]


def patterns(kind):
    # Entries are signs 0/1 in the lexicographic list of the four cube edges.
    if kind == "N":
        return [tuple(int(i == j) for i in range(4)) for j in range(4)] + [
            tuple(int(i != j) for i in range(4)) for j in range(4)
        ]
    if kind == "P":
        # Same color on each of two parallel pairs, with either pair-coloring.
        ans = []
        for coordinate in (0, 1):
            for flip in (0, 1):
                ans.append(tuple(((i >> coordinate) & 1) ^ flip for i in range(4)))
        return ans
    if kind == "Q":
        return [tuple((((i & 1) ^ ((i >> 1) & 1)) ^ flip) for i in range(4))
                for flip in (0, 1)]
    raise ValueError(kind)


corners = []
for u, v in itertools.combinations(A, 2):
    for d in range(1, max(A) + 1):
        if u + d in A and v + d in A:
            corners.append(((u + d, u), (v + d, v), (v + d, u)))


def raw_call(types):
    clauses = []
    # Proper strict source: forbid monochromatic three-cell corners.
    for tri in corners:
        clauses.append([-ix[q] for q in tri])
        clauses.append([ix[q] for q in tri])
    top = len(cells)
    for direction, kind in enumerate(types):
        opts = patterns(kind)
        selectors = list(range(top + 1, top + 1 + len(opts)))
        top += len(opts)
        clauses.append(selectors)
        es = edge_cells(direction)
        for selector, pattern in zip(selectors, opts):
            for q, value in zip(es, pattern):
                clauses.append([-selector, ix[q] if value else -ix[q]])
    start = time.monotonic()
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        ok = solver.solve_limited()
        elapsed = time.monotonic() - start
        row = {
            "types": list(types),
            "status": "SAT" if ok else "UNSAT" if ok is False else "UNKNOWN",
            "seconds": elapsed,
            "cells": len(cells),
            "corners": len(corners),
        }
        if ok:
            positive = set(solver.get_model())
            row["full_28_cell_colors"] = [
                [v, u, int(ix[(v, u)] in positive)] for (v, u) in cells
            ]
            row["direction_edge_colors"] = [
                {
                    "step": STEPS[i],
                    "cells": [[v, u, int(ix[(v, u)] in positive)] for v, u in edge_cells(i)],
                }
                for i in range(3)
            ]
    return row


rows = []
for types in itertools.product(("N", "P", "Q"), repeat=3):
    result = raw_call(types)
    rows.append(result)
    if result["status"] == "SAT" and sum(t == "P" for t in types) < 2:
        break

OUT.write_text(
    json.dumps(
        {
            "scope": "one raw SAT call per visited type triple; no replay or validation",
            "source": A,
            "steps": STEPS,
            "type_convention": {
                "N": "3+1 on the four parallel source-edge cells",
                "P": "two parallel same-color pairs",
                "Q": "two diagonal same-color pairs",
            },
            "rows": rows,
        },
        indent=2,
    ),
    encoding="utf-8",
)
print(json.dumps(rows, indent=2))
