#!/usr/bin/env python3
"""Generate exact four-color line-energy formulas and finite identity checks."""

import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).resolve().parent / "energy_results.json"


def triangle_cells(n):
    return [(x, y) for x in range(n) for y in range(x)]


def triangle_ls(n):
    result = []
    for x, y in triangle_cells(n):
        for d in range(1, n - x):
            result.append(((x, y), (x + d, y), (x + d, y + d)))
    return result


def line_families(n):
    lines = []
    for y in range(n - 1):
        lines.append(("H", y, [(x, y) for x in range(y + 1, n)]))
    for x in range(1, n):
        lines.append(("V", x, [(x, y) for y in range(x)]))
    for c in range(1, n):
        lines.append(("D", c, [(y + c, y) for y in range(n - c)]))
    return lines


def completed_l(direction, a, b):
    if direction == "H":
        (x1, y1), (x2, y2) = a, b
        d = x2 - x1
        third = (x2, y1 + d)
    elif direction == "V":
        (x1, y1), (x2, y2) = a, b
        d = y2 - y1
        third = (x1 - d, y1)
    else:
        (x1, y1), (x2, y2) = a, b
        d = x2 - x1
        assert d == y2 - y1
        third = (x2, y1)
        return tuple(sorted((a, third, b)))
    return tuple(sorted((a, b, third)))


def incidence(n):
    pair_map = {}
    for direction, _, cells in line_families(n):
        for a, b in itertools.combinations(cells, 2):
            triple = completed_l(direction, a, b)
            assert all(0 <= y < x < n for x, y in triple)
            assert (a, b) not in pair_map
            pair_map[(a, b)] = triple
    from_ls = Counter()
    for triple in triangle_ls(n):
        for pair in itertools.combinations(sorted(triple), 2):
            from_ls[pair] += 1
    assert from_ls == Counter({pair: 1 for pair in pair_map})
    assert len(pair_map) == 3 * len(triangle_ls(n))
    return len(pair_map)


def metrics(coloring, cells, ls, lines, k):
    at = dict(zip(cells, coloring))
    p = 0
    discrepancy = Fraction(0)
    for _, _, line in lines:
        counts = [0] * k
        for cell in line:
            counts[at[cell]] += 1
        p += sum(c * (c - 1) // 2 for c in counts)
        discrepancy += sum((Fraction(c) - Fraction(len(line), k)) ** 2 for c in counts)
    mono = 0
    rainbow = 0
    for triple in ls:
        used = len({at[cell] for cell in triple})
        mono += used == 1
        rainbow += used == 3
    return p, discrepancy, mono, rainbow


def rhs(n, k):
    m = n * (n - 1) // 2
    c = n * (n - 1) * (n - 2) // 6
    s = n * (n - 1) * (2 * n - 1) // 2
    return 2 * c - Fraction(s, k) + 3 * m


def balanced_defect(length, k):
    q, r = divmod(length, k)
    counts = [q] * (k - r) + [q + 1] * r
    return sum((Fraction(c) - Fraction(length, k)) ** 2 for c in counts)


def main():
    assert sys.version_info >= (3, 9)
    exhaustive = []
    for n in (2, 3, 4):
        cells = triangle_cells(n)
        ls = triangle_ls(n)
        lines = line_families(n)
        assert len(ls) == n * (n - 1) * (n - 2) // 6
        pair_count = incidence(n)
        checked = 0
        proper = 0
        for word in itertools.product(range(4), repeat=len(cells)):
            p, discrepancy, mono, rainbow = metrics(word, cells, ls, lines, 4)
            c = len(ls)
            assert p == c - rainbow + 2 * mono
            assert discrepancy + 2 * rainbow - 4 * mono == rhs(n, 4)
            checked += 1
            proper += mono == 0
        exhaustive.append({
            "N": n,
            "cells": len(cells),
            "Ls": len(ls),
            "line_pairs": pair_count,
            "all_four_color_words_checked": checked,
            "proper_words": proper,
            "identity": "D+2R-4B=2*C(N,3)-S/4+3*C(N,2)",
            "status": "PASS",
        })

    table = []
    for n in range(1, 11):
        c = n * (n - 1) * (n - 2) // 6
        defect_min = 3 * sum((balanced_defect(length, 4) for length in range(1, n)), Fraction(0))
        rainbow_ceiling = (rhs(n, 4) - defect_min) / 2
        equal_pair_floor = c - rainbow_ceiling
        assert rainbow_ceiling.denominator == 1
        assert equal_pair_floor.denominator == 1
        table.append({
            "N": n,
            "C": c,
            "H_N_4": str(rhs(n, 4)),
            "balanced_D_floor": str(defect_min),
            "rainbow_ceiling": str(rainbow_ceiling),
            "equal_pair_floor": str(equal_pair_floor),
            "pure_energy_forces_impossibility": rainbow_ceiling < 0,
        })
        assert rhs(n, 3) == n * (n - 1)

    result = {
        "date": "2026-11-15",
        "branch": "kimi/r4-energy-20261115",
        "python": sys.version.split()[0],
        "coordinates": "T_N={(x,y):0<=y<x<N}; L=(x,y),(x+d,y),(x+d,y+d)",
        "general_identity": "D_k+2R_k-4B_k=2*C(N,3)-S_N/k+3*C(N,2)",
        "proper_identity": "P_k+R_k=C(N,3)",
        "manuscript_k3_reduction": "D_3+2R_3=N(N-1) in every proper three-coloring",
        "four_color_H": "H_N_4=N(N-1)(2N+23)/24",
        "four_color_balanced_defect": "E_N=3*sum_(1<=l<N) r_l*(4-r_l)/4, r_l=l mod 4",
        "asymptotic": {
            "equal_pair_floor_over_C": "3/4",
            "rainbow_ceiling_over_C": "1/4",
            "gap_C_minus_equal_pair_floor": "N^3/24+O(N^2)",
        },
        "pure_energy_consumer": "CLOSED: positive rainbow ceiling; no contradiction at any N",
        "exhaustive_checks": exhaustive,
        "exact_table": table,
        "new_R3_bound": False,
        "new_R4_bound": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"status": "PASS", "output": str(OUT),
                      "words_checked": sum(row["all_four_color_words_checked"] for row in exhaustive),
                      "equal_pair_leading_coefficient": "3/4",
                      "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
