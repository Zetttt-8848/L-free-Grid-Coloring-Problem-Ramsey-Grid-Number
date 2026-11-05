"""Bounded discovery for a source missed by the exact independent-line budget.

This is deliberately a discovery script.  It reads at most 100 saved
window-13 minimal-bad supports, computes the three line-graph cut minima by
brute-force sign patterns, and asks SAT only after the relaxed budget passes.
Its raw UNSAT result is recorded as discovery data, not as a certificate.
"""

from __future__ import annotations

import itertools
import json
import time
from collections import defaultdict
from pathlib import Path

from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[3]
CATALOG = ROOT / "research_round3" / "joint" / "window13.json"
OUT = Path(__file__).with_name("ROUTING_DUAL_DISCOVERY_0014.json")
LIMIT = 100
SECONDS = 120.0


def phi(r: int) -> int:
    return (r - 1) ** 2 // 4 if r else 0


def source_geometry(marks: list[int]):
    source = set(marks)
    by_difference: dict[int, list[int]] = {}
    for d in range(1, marks[-1] - marks[0] + 1):
        starts = [u for u in marks if u + d in source]
        if starts:
            by_difference[d] = starts
    corners = []
    for d, starts in by_difference.items():
        for u, v in itertools.combinations(starts, 2):
            corners.append(((u + d, u), (v + d, u), (v + d, v)))
    return by_difference, corners


def graph_tau(edges: set[tuple[tuple[int, int], tuple[int, int]]]) -> tuple[int, int]:
    vertices = sorted({x for edge in edges for x in edge})
    if not edges:
        return 0, 0
    index = {v: i for i, v in enumerate(vertices)}
    encoded = [(index[x], index[y]) for x, y in edges]
    best = len(encoded)
    # Complementing all signs preserves the number of equal-color edges.
    for mask in range(1 << (len(vertices) - 1)):
        equal = sum((((mask >> (i - 1)) if i else 0) & 1)
                    == (((mask >> (j - 1)) if j else 0) & 1)
                    for i, j in encoded)
        best = min(best, equal)
    return best, len(vertices)


def line_budget(marks: list[int], corners):
    row_edges = defaultdict(set)
    column_edges = defaultdict(set)
    for left, middle, right in corners:
        row_edges[middle[0]].add(tuple(sorted((middle, right))))
        column_edges[middle[1]].add(tuple(sorted((left, middle))))
    rows = {str(anchor): graph_tau(edges) for anchor, edges in row_edges.items()}
    columns = {str(anchor): graph_tau(edges) for anchor, edges in column_edges.items()}
    return rows, columns


def sat_status(corners: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]) -> str:
    cells = sorted({cell for corner in corners for cell in corner})
    index = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for corner in corners:
        variables = [index[cell] for cell in corner]
        clauses.extend((variables, [-var for var in variables]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        return "SAT" if solver.solve() else "UNSAT"


def main() -> None:
    started = time.monotonic()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    candidates = sorted(
        (entry["marks"] for entry in catalog["minimal_bad"]
         if len(entry["marks"]) <= 8 and entry["marks"][-1] - entry["marks"][0] <= 13),
        key=lambda marks: (len(marks), marks[-1] - marks[0], marks),
    )
    examined = []
    found = None
    for marks in candidates[:LIMIT]:
        if time.monotonic() - started > SECONDS:
            break
        fibers, corners = source_geometry(marks)
        diagonal = sum(phi(len(starts)) for starts in fibers.values())
        rows, columns = line_budget(marks, corners)
        row_total = sum(value[0] for value in rows.values())
        column_total = sum(value[0] for value in columns.values())
        total = diagonal + row_total + column_total
        entry = {
            "marks": marks,
            "span": marks[-1] - marks[0],
            "cells": len(marks) * (len(marks) - 1) // 2,
            "corners": len(corners),
            "diagonal_tau": diagonal,
            "row_tau": row_total,
            "column_tau": column_total,
            "independent_line_budget": total,
            "budget_minus_corners": total - len(corners),
        }
        examined.append(entry)
        if total <= len(corners):
            entry["sat_status"] = sat_status(corners)
            found = {**entry, "row_lines": rows, "column_lines": columns,
                     "difference_fibers": {str(d): len(f) for d, f in fibers.items()}}
            break
    result = {
        "purpose": "bounded discovery for an ordered-routing dual; raw solver status only",
        "catalog": str(CATALOG),
        "candidate_limit": LIMIT,
        "candidate_pool": len(candidates),
        "candidates_examined": len(examined),
        "seconds": time.monotonic() - started,
        "examined": examined,
        "found": found,
        "scope": "No claim of completeness beyond the listed prefix, and no proof claim from SAT UNSAT.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("candidate_pool", "candidates_examined", "seconds", "found")}))


if __name__ == "__main__":
    main()
