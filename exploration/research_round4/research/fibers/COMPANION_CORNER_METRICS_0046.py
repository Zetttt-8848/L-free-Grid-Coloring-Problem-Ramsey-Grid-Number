"""Companion-corner metrics from saved symbolic proper strict-source rules only."""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__)

def corner_data(values, color):
    values = sorted(values)
    cells = [(v, u) for v in values for u in values if u < v]
    cset = set(cells)
    corners = []
    by_outer = defaultdict(list)
    for x, y in cells:
        for d in range(1, max(values) - x + 1):
            edge = ((x, y), (x + d, y), (x + d, y + d))
            if all(q in cset for q in edge):
                forcing = color(edge[0]) == color(edge[2])
                item = {"edge": edge, "forcing": forcing, "outer_color": color(edge[1])}
                corners.append(item)
                if forcing:
                    by_outer[edge[1]].append(item)

    companion = Counter()
    for u in values:
        for d in range(1, max(values) - u + 1):
            for h in range(d + 1, max(values) - u + 1):
                marks = (u, u + d, u + h, u + d + h)
                if all(a in values for a in marks):
                    e_d = ((u + d, u), (u + d + h, u), (u + d + h, u + h))
                    e_h = ((u + h, u), (u + d + h, u), (u + d + h, u + d))
                    kind = "".join(sorted(("F" if color(e_d[0]) == color(e_d[2]) else "M",
                                           "F" if color(e_h[0]) == color(e_h[2]) else "M")))
                    companion[kind] += 1

    ap3 = Counter()
    for u in values:
        for d in range(1, (max(values) - u) // 2 + 1):
            if u + d in values and u + 2 * d in values:
                edge = ((u + d, u), (u + 2 * d, u), (u + 2 * d, u + d))
                ap3["forcing" if color(edge[0]) == color(edge[2]) else "mixed"] += 1

    anchor = {}
    for sign in (0, 1):
        qs = [q for q in cells if color(q) == sign]
        loads = [len(by_outer[q]) for q in qs]
        anchor[str(sign)] = {
            "anchor_class_size": len(qs),
            "forcing_endpoint_triples": sum(loads),
            "anchors_with_forcing_triple": sum(load > 0 for load in loads),
            "forcing_load_histogram": {str(k): v for k, v in sorted(Counter(loads).items())},
            "anchored_pairs_of_forcing_triples": sum(load * (load - 1) // 2 for load in loads),
        }

    return {
        "source_size": len(values),
        "cells": len(cells),
        "corners": len(corners),
        "forcing_corners": sum(x["forcing"] for x in corners),
        "mixed_corners": sum(not x["forcing"] for x in corners),
        "companion_parallelograms": dict(sorted(companion.items())),
        "ap3_corners": dict(sorted(ap3.items())),
        "forcing_triples_by_outer_color": anchor,
    }

# THREE_CUBE_MIXED_CORNER_MINIMUM_0046.md, Section 2.
w3 = (1, 4, 16)
masks3 = range(8)
vals3 = {mask: sum(w for i, w in enumerate(w3) if mask >> i & 1) for mask in masks3}
def c3(cell):
    a, b = cell
    x = next(k for k, v in vals3.items() if v == a)
    y = next(k for k, v in vals3.items() if v == b)
    sx, sy = x.bit_count(), y.bit_count()
    return int(
        (0 in (x, y) and ({sx, sy} - {0}) <= {1, 2})
        or ({sx, sy} == {1, 3})
        or (sx == 1 and sy == 2 and (x ^ y) == 7)
    )

# FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md, Tables (4)--(6).
w4 = (1, 3, 9, 27)
vals4 = {mask: sum(w for i, w in enumerate(w4) if mask >> i & 1) for mask in range(16)}
L = ["", "1", "10", "100", "1001", "10110", "110101", "0001111"]
U = ["", "0", "01", "111", "0110", "11001", "101010", "1000000"]
X = [
    "10010110", "10111100", "11011010", "00010001",
    "11100110", "00100100", "01101000", "01101010",
]
def c4(cell):
    a, b = cell
    hi = next(k for k, v in vals4.items() if v == a)
    lo = next(k for k, v in vals4.items() if v == b)
    if hi < 8:
        return int(L[hi][lo])
    if lo >= 8:
        return int(U[hi - 8][lo - 8])
    return int(X[hi - 8][lo])

# WEIGHT_TWO_LAYER.md with r=5 and weights 5^i, an explicit family member.
r = 5
w2 = tuple(5 ** i for i in range(r))
masks2 = [sum(1 << i for i in pair) for pair in combinations(range(r), 2)]
vals2 = {mask: sum(w for i, w in enumerate(w2) if mask >> i & 1) for mask in masks2}
def c2(cell):
    a, b = cell
    x = next(k for k, v in vals2.items() if v == a)
    y = next(k for k, v in vals2.items() if v == b)
    return int((x & y) == 0)

records = {
    "three_cube": corner_data(vals3.values(), c3),
    "four_cube": corner_data(vals4.values(), c4),
    "weight_two_r5": corner_data(vals2.values(), c2),
}
out = {
    "scope": "Metrics only from three saved symbolic proper strict-source rules. No solver run and no properness recheck was performed.",
    "provenance": {
        "three_cube": "research/THREE_CUBE_MIXED_CORNER_MINIMUM_0046.md, Section 2",
        "four_cube": "research/fibers/FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md, Tables (4)--(6)",
        "weight_two_r5": "research/fibers/WEIGHT_TWO_LAYER.md, rule (1), with the stated powers-of-five family",
    },
    "records": records,
}
HERE.with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(records, indent=2))

