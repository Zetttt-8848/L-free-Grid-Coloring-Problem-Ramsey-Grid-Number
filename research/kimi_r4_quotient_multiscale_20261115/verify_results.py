#!/usr/bin/env python3
"""Standalone verification of quotient_probe output, without importing it."""

import argparse
import itertools
import json
from pathlib import Path


def ls_from_definition(n):
    return [
        ((x, y), (x + d, y), (x + d, y + d))
        for x in range(n) for y in range(n) for d in range(1, n)
        if x + d < n and y + d < n
    ]


def quotient_sides():
    # Independent construction: enumerate all 16 subsets, retain nonempty
    # proper subsets, and quotient by complement using color 0 as anchor.
    sides = []
    for mask in range(16):
        side = frozenset(c for c in range(4) if mask & (1 << c))
        if side and 0 in side and side != frozenset(range(4)):
            sides.append(side)
    assert len(sides) == 7
    return sides


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    rows = data["example"]["rows"]
    n = data["n"]
    assert len(rows) == n and all(len(row) == n for row in rows)
    assert all(c in range(4) for row in rows for c in row)
    ls = ls_from_definition(n)
    assert len(ls) == data["geometric_L_count"] == 30
    for L in ls:
        assert len({rows[x][y] for x, y in L}) > 1
    sides = quotient_sides()
    signatures = []
    for L in ls:
        used = frozenset(rows[x][y] for x, y in L)
        sig = frozenset(i for i, side in enumerate(sides)
                        if used <= side or used <= frozenset(range(4)) - side)
        signatures.append(sig)
    assert set().union(*signatures) == set(range(7))
    witness = data["example"]["witness"]
    if witness is None:
        assert data["example"]["minimum_cover"] == ">=4"
        for size in range(4):
            assert not any(
                set().union(*(signatures[ls.index(L)] for L in chosen))
                == set(range(7))
                for chosen in itertools.combinations(ls, size)
            )
    else:
        covered = set()
        for L in witness:
            L_tuple = tuple(tuple(p) for p in L)
            covered |= signatures[ls.index(L_tuple)]
        assert covered == set(range(7))
        target = int(data["example"]["minimum_cover"])
        assert len(witness) == target
        for size in range(target):
            assert not any(
                set().union(*(signatures[ls.index(L)] for L in chosen))
                == set(range(7))
                for chosen in itertools.combinations(ls, size)
            )
    print(json.dumps({
        "status": "PASS",
        "checked_rows": n * n,
        "checked_geometric_Ls": len(ls),
        "quotient_sides": len(sides),
        "example_minimum_cover": data["example"]["minimum_cover"],
        "scope": "stored example only; not a universal sharpness proof"
    }, indent=2))


if __name__ == "__main__":
    main()
