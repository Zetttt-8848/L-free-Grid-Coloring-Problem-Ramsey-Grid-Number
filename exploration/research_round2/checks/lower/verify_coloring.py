#!/usr/bin/env python3
"""Independent verifier for directed equal-arm L-free grid colorings.

Input is an n-line whitespace matrix with entries 1, 2, 3.  This verifier does
not import or share code with the construction search.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def read_grid(path: Path) -> list[list[int]]:
    rows = [
        [int(token) for token in line.split()]
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    if not rows:
        raise ValueError("matrix is empty")
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError(f"matrix is not square: {n} rows, row lengths {[len(r) for r in rows]}")
    if any(value not in (1, 2, 3) for row in rows for value in row):
        raise ValueError("matrix entries must all lie in {1,2,3}")
    return rows


def verify(grid: list[list[int]]) -> dict[str, object]:
    n = len(grid)
    bad: list[dict[str, object]] = []
    triples = 0
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                triples += 1
                color = grid[x][y]
                if color == grid[x + d][y] == grid[x + d][y + d]:
                    bad.append(
                        {
                            "points_1_based": [[x + 1, y + 1], [x + d + 1, y + 1], [x + d + 1, y + d + 1]],
                            "color": color,
                        }
                    )
    expected = sum(m * m for m in range(1, n))
    if triples != expected:
        raise AssertionError(f"enumerated {triples} triples but exact formula gives {expected}")
    canonical = "\n".join(" ".join(map(str, row)) for row in grid) + "\n"
    counts = {str(color): sum(value == color for row in grid for value in row) for color in (1, 2, 3)}
    return {
        "n": n,
        "geometric_triples": triples,
        "color_specific_forbidden_clauses": 3 * triples,
        "expected_geometric_triples_formula": f"sum_{{m=1}}^{{{n-1}}} m^2 = {(n-1)*n*(2*n-1)//6}",
        "color_counts": counts,
        "violations": len(bad),
        "first_violations": bad[:10],
        "canonical_matrix_sha256": hashlib.sha256(canonical.encode("ascii")).hexdigest(),
        "verified_corner_free": not bad,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--transpose-input",
        action="store_true",
        help="interpret source rows as the second Round-2 coordinate",
    )
    args = parser.parse_args()
    grid = read_grid(args.matrix)
    if args.transpose_input:
        grid = [list(row) for row in zip(*grid)]
    result = verify(grid)
    result["input_transposed"] = args.transpose_input
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["verified_corner_free"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
