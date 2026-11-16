#!/usr/bin/env python3
"""Exhaustively search prescribed cells for an O1 counterexample."""

import itertools
import json
from pathlib import Path

N = 3
FIXED = {(0, 0): 0, (1, 1): 0, (1, 0): 1, (2, 1): 1}
FREE = [(x, y) for x in range(N) for y in range(N) if (x, y) not in FIXED]


def geometric_ls():
    for d in range(1, N):
        for x in range(N - d):
            for y in range(N - d):
                yield ((x, y), (x + d, y), (x + d, y + d))


def proper(rows):
    return all(len({rows[x][y] for x, y in L}) > 1 for L in geometric_ls())


def main():
    output = Path(__file__).with_name("counterexample.json")
    tested = 0
    witness = None
    for values in itertools.product(range(4), repeat=len(FREE)):
        tested += 1
        rows = [[0] * N for _ in range(N)]
        for (x, y), color in FIXED.items():
            rows[x][y] = color
        for (x, y), color in zip(FREE, values):
            rows[x][y] = color
        if proper(rows):
            witness = rows
            break
    result = {
        "status": "COUNTEREXAMPLE" if witness else "UNDECIDED",
        "search_domain": "all 4^5 assignments to unprescribed cells, stopping at first witness",
        "tested_assignments": tested,
        "free_cells": FREE,
        "fixed_cells": {str(cell): color for cell, color in FIXED.items()},
        "witness": witness,
        "O1_violation": "W_0[0]=W_0[1]=0, W_1[0]=W_1[1]=1, but chi(1,0)=1"
    }
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
