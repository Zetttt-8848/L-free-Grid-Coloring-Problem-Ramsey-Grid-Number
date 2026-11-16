#!/usr/bin/env python3
"""Independently verify line energy using triple-index L coordinates."""

import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "energy_results.json"
OUT = ROOT / "energy_verification.json"


def cells_triple_order(n):
    return [(x, y) for y in range(n) for x in range(y + 1, n)]


def ls_from_coordinate_triples(n):
    result = []
    for u, v, w in itertools.combinations(range(n), 3):
        triple = ((w - v + u, u), (w, u), (w, v))
        x, y = triple[0]
        d = v - u
        assert triple == ((x, y), (x + d, y), (x + d, y + d))
        result.append(tuple(sorted(triple)))
    return result


def direct_lines(n, cells):
    groups = {}
    for x, y in cells:
        groups.setdefault(("row", y), []).append((x, y))
        groups.setdefault(("column", x), []).append((x, y))
        groups.setdefault(("offset", x - y), []).append((x, y))
    return [sorted(group) for group in groups.values()]


def main():
    source = json.loads(SOURCE.read_text(encoding="ascii"))
    words_checked = 0
    for n in (2, 3, 4):
        cells = cells_triple_order(n)
        ls = ls_from_coordinate_triples(n)
        lines = direct_lines(n, cells)
        assert len(ls) == n * (n - 1) * (n - 2) // 6
        pair_counts = Counter(pair for line in lines for pair in itertools.combinations(line, 2))
        l_pair_counts = Counter(pair for triple in ls for pair in itertools.combinations(triple, 2))
        assert pair_counts == l_pair_counts
        assert sum(pair_counts.values()) == 3 * len(ls)
        for word in itertools.product(range(4), repeat=len(cells)):
            color = dict(zip(cells, word))
            equal_pairs = 0
            discrepancy = Fraction(0)
            for line in lines:
                counts = [0, 0, 0, 0]
                for cell in line:
                    counts[color[cell]] += 1
                equal_pairs += sum(c * (c - 1) // 2 for c in counts)
                discrepancy += sum((Fraction(c) - Fraction(len(line), 4)) ** 2 for c in counts)
            mono = sum(len({color[cell] for cell in triple}) == 1 for triple in ls)
            rainbow = sum(len({color[cell] for cell in triple}) == 3 for triple in ls)
            c = len(ls)
            m = len(cells)
            s = sum(len(line) ** 2 for line in lines)
            assert s == n * (n - 1) * (2 * n - 1) // 2
            right = 2 * c - Fraction(s, 4) + 3 * m
            assert equal_pairs == c - rainbow + 2 * mono
            assert discrepancy + 2 * rainbow - 4 * mono == right
            words_checked += 1

    table_checks = 0
    for row in source["exact_table"]:
        n = row["N"]
        c = n * (n - 1) * (n - 2) // 6
        h = Fraction(n * (n - 1) * (2 * n + 23), 24)
        assert Fraction(row["H_N_4"]) == h
        defect = Fraction(0)
        for length in range(1, n):
            base, extra = divmod(length, 4)
            counts = [base] * (4 - extra) + [base + 1] * extra
            defect += 3 * sum((Fraction(value) - Fraction(length, 4)) ** 2 for value in counts)
        ceiling = (h - defect) / 2
        assert Fraction(row["balanced_D_floor"]) == defect
        assert Fraction(row["rainbow_ceiling"]) == ceiling
        assert Fraction(row["equal_pair_floor"]) == c - ceiling
        assert row["pure_energy_forces_impossibility"] is False
        table_checks += 1
    assert all(Fraction(n * (n - 1) * (2 * n + 23), 24) >= 3 * (n - 1)
               for n in range(3, 100))
    assert Fraction(2 * 1 * (2 * 2 + 23), 24) == Fraction(9, 4)
    assert all((2 * (n * (n - 1) * (n - 2) // 6)
                - Fraction(n * (n - 1) * (2 * n - 1) // 2, 3)
                + 3 * (n * (n - 1) // 2)) == n * (n - 1)
               for n in range(1, 100))

    verification = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "independent_coordinates": "Ls indexed by integer triples u<v<w",
        "all_four_color_words_checked": words_checked,
        "formula_rows_recomputed": table_checks,
        "pair_completion_bijections_checked": [2, 3, 4],
        "k3_manuscript_reduction_checked_through_N": 99,
        "pure_energy_contradiction": False,
        "scope": "Internal independent recomputation; not external review or formalization",
    }
    OUT.write_text(json.dumps(verification, indent=2) + "\n", encoding="ascii")
    print(json.dumps(verification, indent=2))


if __name__ == "__main__":
    main()
