#!/usr/bin/env python3
"""Independent parser and direct corner verifier for a complete matrix."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [[int(t) for t in line.split()] for line in args.matrix.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(rows) != args.n or any(len(row) != args.n for row in rows):
        raise ValueError("matrix must contain exactly n rows of exactly n entries")
    if any(v not in (1, 2, 3) for row in rows for v in row):
        raise ValueError("every matrix entry must be one of the three symbols 1,2,3")
    violations = []
    inspected = 0
    for x in range(args.n):
        for y in range(args.n):
            for d in range(1, min(args.n - x, args.n - y)):
                inspected += 1
                if rows[x][y] == rows[x + d][y] == rows[x + d][y + d]:
                    violations.append({"x": x, "y": y, "d": d, "color": rows[x][y]})
    exact = (args.n - 1) * args.n * (2 * args.n - 1) // 6
    if inspected != exact:
        raise AssertionError((inspected, exact))
    canonical = "\n".join(" ".join(map(str, row)) for row in rows) + "\n"
    result = {
        "schema": "round3_lower_direct_coloring_check_v1",
        "n": args.n,
        "symbols": [1, 2, 3],
        "orientation": "(x,y),(x+d,y),(x+d,y+d)",
        "corners_inspected": inspected,
        "color_counts": {str(c): sum(v == c for row in rows for v in row) for c in (1, 2, 3)},
        "violations": len(violations),
        "first_violations": violations[:20],
        "canonical_sha256": hashlib.sha256(canonical.encode("ascii")).hexdigest(),
        "verified_corner_free": not violations,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())

