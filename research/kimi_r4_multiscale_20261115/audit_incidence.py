#!/usr/bin/env python3
"""Definition-level audit of quotient signatures and multiscale incidence."""

import argparse
import hashlib
import itertools
import json
import platform
from collections import Counter
from fractions import Fraction
from pathlib import Path


def quotient_sides():
    return [frozenset(c for c in range(4) if mask & (1 << c))
            for mask in range(16)
            if mask & 1 and mask != 15]


def signature(word, sides):
    used = frozenset(word)
    return frozenset(i for i, side in enumerate(sides)
                     if used <= side or used <= frozenset(range(4)) - side)


def all_ls(n):
    return [(x, y, d) for x in range(n) for y in range(n)
            for d in range(1, n) if x + d < n and y + d < n]


def vertices(L):
    x, y, d = L
    return ((x, y), (x + d, y), (x + d, y + d))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    witness = json.loads(args.witness.read_text(encoding="utf-8"))
    rows = witness["rows"]
    assert witness["n"] == 6 and witness["k"] == 4
    sides = quotient_sides()
    assert len(sides) == 7

    word_counts = Counter()
    for word in itertools.product(range(4), repeat=3):
        sig = signature(word, sides)
        used = len(set(word))
        assert len(sig) == {1: 7, 2: 3, 3: 1}[used]
        word_counts[f"{used}_colors_signature_{len(sig)}"] += 1
    assert sum(word_counts.values()) == 64

    ls6 = all_ls(6)
    assert len(ls6) == 55
    signatures6 = []
    for L in ls6:
        word = tuple(rows[x][y] for x, y in vertices(L))
        assert len(set(word)) > 1
        sig = signature(word, sides)
        assert sig
        signatures6.append(sig)
    p6 = {d: sum(1 for x, y, lag in ls6 if lag == d)
          for d in range(1, 5)}
    assert p6 == {d: (6 - d) ** 2 for d in range(1, 5)}
    old_lhs = sum((Fraction(p6[d], (5 - d) ** 2) for d in range(1, 5)),
                  Fraction(0))
    old_rhs = 3 * (6 - 4) ** 2
    assert old_lhs == Fraction(1381, 144)
    assert old_lhs < old_rhs

    monochrome_rows = [[0] * 6 for _ in range(6)]
    monochrome_p = Counter()
    for x, y, d in ls6:
        word = tuple(monochrome_rows[a][b] for a, b in vertices((x, y, d)))
        assert len(signature(word, sides)) == 7
        if d <= 4:
            monochrome_p[d] += 1
    assert dict(monochrome_p) == p6

    scale_rows = []
    for n in (5, 6, 9, 10):
        host_ls = all_ls(n)
        for s in range(1, (n - 1) // 4 + 1):
            origins = [(a, b) for a in range(n - 4 * s)
                       for b in range(n - 4 * s)]
            copies = []
            for a, b in origins:
                points = frozenset((a + s * i, b + s * j)
                                   for i in range(5) for j in range(5))
                copies.append(points)
            entries = []
            for L in host_ls:
                x, y, d = L
                vs = vertices(L)
                multiplicity = sum(all(v in copy for v in vs)
                                   for copy in copies)
                if d % s == 0 and d // s <= 4:
                    r = d // s
                    assert multiplicity <= (5 - r) ** 2
                else:
                    assert multiplicity == 0
                entries.append((x, y, d, multiplicity))
            copy_count = (n - 4 * s) ** 2
            incidence = sum(entry[3] for entry in entries)
            assert incidence == 30 * copy_count
            digest = hashlib.sha256(json.dumps(
                sorted(entries), separators=(",", ":")).encode("ascii")).hexdigest()
            scale_rows.append({
                "n": n,
                "scale": s,
                "copies": copy_count,
                "host_Ls": len(host_ls),
                "total_copy_L_incidences": incidence,
                "identity": "30*copies",
                "multiplicity_sha256": digest,
            })

    boundary_entries = []
    for n in (5, 6):
        copies = [frozenset((a + i, b + j) for i in range(5) for j in range(5))
                  for a in range(n - 4) for b in range(n - 4)]
        multiplicity = sum(all(v in copy for v in vertices((0, 0, 1)))
                           for copy in copies)
        assert multiplicity == 1
        boundary_entries.append({"n": n, "L": [0, 0, 1],
                                 "actual_multiplicity": multiplicity,
                                 "old_claimed_multiplicity": 16})

    proper_block_counts = []
    monochrome_block_counts = []
    for a in range(2):
        for b in range(2):
            block_ls = [(x, y, d) for x, y, d in ls6
                        if a <= x and x + d < a + 5
                        and b <= y and y + d < b + 5]
            assert len(block_ls) == 30
            proper_block_counts.append(sum(
                bool(signature(tuple(rows[x][y] for x, y in vertices(L)), sides))
                for L in block_ls))
            monochrome_block_counts.append(sum(
                bool(signature(tuple(monochrome_rows[x][y]
                                     for x, y in vertices(L)), sides))
                for L in block_ls))
    assert proper_block_counts == monochrome_block_counts == [30] * 4

    copy_count = 4
    quotient_incidence = 0
    rainbow_incidence = 0
    for L, sig in zip(ls6, signatures6):
        x, y, d = L
        multiplicity = sum(
            1 for a in range(2) for b in range(2)
            if a <= x and x + d < a + 5 and b <= y and y + d < b + 5)
        quotient_incidence += len(sig) * multiplicity
        word = tuple(rows[x][y] for x, y in vertices(L))
        rainbow_incidence += multiplicity * (len(set(word)) == 3)
    assert quotient_incidence == 90 * copy_count - 2 * rainbow_incidence
    assert quotient_incidence >= 30 * copy_count
    trivial_rainbow_upper = 30 * copy_count
    seven_quotient_rainbow_upper = Fraction(83, 2) * copy_count
    assert seven_quotient_rainbow_upper > trivial_rainbow_upper

    result = {
        "status": "PASS; old Q3a is refuted and multiscale pair-tight counts are geometric identities",
        "python": platform.python_version(),
        "signature_word_counts": dict(sorted(word_counts.items())),
        "proper_witness": {
            "n": 6,
            "cells": 36,
            "geometric_Ls": 55,
            "P_d": p6,
            "old_Q3a_lhs": str(old_lhs),
            "old_Q3a_rhs": old_rhs,
            "shortfall": str(Fraction(old_rhs) - old_lhs),
            "unweighted_pair_tight_Ls": sum(p6.values()),
            "old_unweighted_lower_bound": old_rhs,
        },
        "improper_monochrome_square_has_same_P_d": True,
        "position_independent_multiplicity_counterexamples": boundary_entries,
        "scale_identities": scale_rows,
        "proper_6_block_pair_tight_counts": proper_block_counts,
        "improper_6_block_pair_tight_counts": monochrome_block_counts,
        "quotient_incidence_6_scale_1": {
            "actual": quotient_incidence,
            "rainbow_incidence": rainbow_incidence,
            "identity": "Q=90*C-2*R",
            "copies": copy_count,
            "trivial_lower_from_nonempty_signatures": 30 * copy_count,
            "seven_applications_of_R2_equals_5": 7 * copy_count,
            "trivial_rainbow_upper": trivial_rainbow_upper,
            "seven_quotient_rainbow_upper": str(seven_quotient_rainbow_upper),
            "consumer": "none; the seven-quotient lower bound is weaker",
        },
        "scope": "Finite checks and exact general identities; no numerical Ramsey bound",
    }
    encoded = json.dumps(result, indent=2) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
