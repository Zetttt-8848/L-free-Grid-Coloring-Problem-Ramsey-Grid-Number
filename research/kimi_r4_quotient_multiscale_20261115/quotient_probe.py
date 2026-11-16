#!/usr/bin/env python3
"""Deterministic probe for four-color quotient signatures on a 5-square."""

import argparse
import itertools
import json
import random
from collections import Counter
from pathlib import Path

PALETTE = frozenset(range(4))
# Each side contains color 0. The seven masks enumerate all proper nonempty
# sides up to complement, without the empty or full palette.
SIDES = tuple(
    frozenset({0} | {c for c in (1, 2, 3) if mask & (1 << (c - 1))})
    for mask in range(7)
)


def geometric_ls(n):
    """Generate every forward equal-leg L exactly once."""
    for d in range(1, n):
        for x in range(n - d):
            for y in range(n - d):
                yield ((x, y), (x + d, y), (x + d, y + d))


def signature(colors):
    """Bits of quotient bipartitions making this three-cell pattern mono."""
    used = frozenset(colors)
    return sum(
        1 << i for i, side in enumerate(SIDES)
        if used <= side or used <= PALETTE - side
    )


def proper(rows):
    n = len(rows)
    return all(len({rows[x][y] for x, y in L}) > 1 for L in geometric_ls(n))


def minimum_cover(rows):
    """Return the exact minimum number of Ls covering all quotient bits."""
    n = len(rows)
    entries = []
    union = 0
    for L in geometric_ls(n):
        sig = signature(rows[x][y] for x, y in L)
        if sig:
            entries.append((L, sig))
            union |= sig
    if union != 0x7F:
        raise AssertionError("The seven quotient signatures do not cover")
    for size in range(4):
        for chosen in itertools.combinations(entries, size):
            covered = 0
            for _, sig in chosen:
                covered |= sig
            if covered == 0x7F:
                return size, [[list(p) for p in L] for L, _ in chosen]
    return None, None


def random_proper(n, rng):
    attempts = 0
    while True:
        attempts += 1
        rows = [[rng.randrange(4) for _ in range(n)] for _ in range(n)]
        if proper(rows):
            return rows, attempts


def self_tests():
    assert len(SIDES) == 7
    assert all(side and side != PALETTE for side in SIDES)
    assert len({min(side, PALETTE - side, key=lambda s: sorted(s))
                for side in SIDES}) == 7
    assert len(list(geometric_ls(2))) == 1
    assert len(list(geometric_ls(5))) == 30
    for colors in itertools.product(range(4), repeat=3):
        expected = {1: 7, 2: 3, 3: 1, 4: 0}[len(set(colors))]
        assert signature(colors).bit_count() == expected
    assert not proper([[0] * 2 for _ in range(2)])
    # Exhaust all binary 4-squares and independently recover R_2 > 4.
    found_proper_binary = False
    for bits in range(1 << 16):
        rows = [[(bits >> (4 * x + y)) & 1 for y in range(4)]
                for x in range(4)]
        if proper(rows):
            found_proper_binary = True
            break
    assert found_proper_binary
    # Binary 5-squares must contain a monochromatic L; this is a test sample,
    # while the proof of Q1 cites the established theorem R_2=5.
    rng = random.Random(205)
    for _ in range(100):
        rows = [[rng.randrange(2) for _ in range(5)] for _ in range(5)]
        assert not proper(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20261115)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.samples < 1:
        parser.error("--samples must be positive")
    self_tests()
    rng = random.Random(args.seed)
    distribution = Counter()
    max_example = None
    total_attempts = 0
    for _ in range(args.samples):
        rows, attempts = random_proper(5, rng)
        total_attempts += attempts
        minimum, witness = minimum_cover(rows)
        if minimum is None:
            distribution[">=4"] += 1
            max_example = {"rows": rows, "minimum_cover": ">=4",
                           "witness": None}
            break
        distribution[str(minimum)] += 1
        if max_example is None or str(minimum) > max_example["minimum_cover"]:
            max_example = {"rows": rows, "minimum_cover": str(minimum),
                           "witness": witness}
        if minimum >= 4:
            break
    result = {
        "status": "FINITE-CHECKED samples; not exhaustive over all colorings",
        "self_tests": "PASS",
        "n": 5,
        "requested_samples": args.samples,
        "completed_samples": sum(distribution.values()),
        "seed": args.seed,
        "geometric_L_count": len(list(geometric_ls(5))),
        "random_generation_attempts": total_attempts,
        "minimum_cover_distribution": dict(sorted(distribution.items())),
        "example": max_example,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
