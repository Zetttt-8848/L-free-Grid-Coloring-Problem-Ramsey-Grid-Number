#!/usr/bin/env python3
"""Build the exact side-21 one-hot CNF and the exhaustive 81-cube split."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from pathlib import Path


def var(n: int, x: int, y: int, color: int) -> int:
    return 3 * (x * n + y) + color + 1


def expected_clauses(n: int) -> tuple[list[list[int]], dict[str, int]]:
    clauses: list[list[int]] = []
    for x in range(n):
        for y in range(n):
            vs = [var(n, x, y, c) for c in range(3)]
            clauses.append(vs)
            clauses.extend(([-vs[0], -vs[1]], [-vs[0], -vs[2]], [-vs[1], -vs[2]]))

    triples = 0
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                triples += 1
                for c in range(3):
                    clauses.append([
                        -var(n, x, y, c),
                        -var(n, x + d, y, c),
                        -var(n, x + d, y + d, c),
                    ])

    # Every color orbit has a representative satisfying these clauses.
    clauses.append([var(n, 0, 0, 0)])
    for index in range(1, n * n):
        x, y = divmod(index, n)
        earlier_color_1 = [var(n, *divmod(j, n), 1) for j in range(1, index)]
        clauses.append([-var(n, x, y, 2), *earlier_color_1])

    formula = (n - 1) * n * (2 * n - 1) // 6
    if triples != formula:
        raise AssertionError((triples, formula))
    counts = {
        "variables": 3 * n * n,
        "geometric_triples": triples,
        "cell_clauses": 4 * n * n,
        "forbidden_color_clauses": 3 * triples,
        "symmetry_clauses": n * n,
        "clauses_before_symmetry": 4 * n * n + 3 * triples,
        "total_clauses": len(clauses),
    }
    if counts["total_clauses"] != 5 * n * n + 3 * triples:
        raise AssertionError(counts)
    return clauses, counts


def dimacs_bytes(nvars: int, clauses: list[list[int]]) -> bytes:
    lines = [f"p cnf {nvars} {len(clauses)}"]
    lines.extend(" ".join(map(str, clause)) + " 0" for clause in clauses)
    return ("\n".join(lines) + "\n").encode("ascii")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=21)
    parser.add_argument("--seed", type=int, default=62101)
    parser.add_argument("--legacy", type=Path, required=True)
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    if args.n != 21:
        raise ValueError("this frozen Round-3 instance builder is pinned to n=21")

    clauses, counts = expected_clauses(args.n)
    rendered = dimacs_bytes(counts["variables"], clauses)
    args.cnf.parent.mkdir(parents=True, exist_ok=True)
    args.cnf.write_bytes(rendered)

    legacy = json.loads(args.legacy.read_text(encoding="utf-8"))
    legacy_by_tuple = {
        tuple(record["cube_colors_0_based"]): record["status"]
        for record in legacy["cube_records"]
    }
    if len(legacy_by_tuple) != 81:
        raise ValueError("legacy split is not a complete 81-tuple map")

    cube_indices = [1, args.n, args.n + 1, args.n * args.n - 1]
    tuples = list(itertools.product(range(3), repeat=4))
    random.Random(args.seed).shuffle(tuples)
    records = []
    for order, colors in enumerate(tuples):
        prior = legacy_by_tuple[tuple(colors)]
        assumptions = [
            var(args.n, *divmod(index, args.n), color)
            for index, color in zip(cube_indices, colors)
        ]
        records.append({
            "order": order,
            "cube_colors_0_based": list(colors),
            "assumption_literals": assumptions,
            "round2_raw_status": prior,
            "stage1_cap_seconds": 10 if prior == "UNDECIDED" else 2,
        })
    cubes = {
        "schema": "round3_lower_cubes_v1",
        "n": args.n,
        "split_cells_0_based": [list(divmod(index, args.n)) for index in cube_indices],
        "seed": args.seed,
        "cube_count": 81,
        "nominal_solver_cap_seconds": sum(r["stage1_cap_seconds"] for r in records),
        "coverage_claim": "all assignments in {0,1,2}^4, exactly once",
        "records": records,
    }
    args.cubes.write_text(json.dumps(cubes, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest = {
        "schema": "round3_lower_instance_manifest_v1",
        "formal_orientation": "(x,y),(x+d,y),(x+d,y+d)",
        "indexing": "zero-based x,y; 1 <= d < min(n-x,n-y); colors 0,1,2 in CNF",
        "n": args.n,
        "colors": 3,
        "counts": counts,
        "symmetry": {
            "fixed_cell": [0, 0],
            "fixed_color": 0,
            "restricted_growth": "color 2 cannot occur before the first occurrence of color 1 in row-major order",
            "soundness": "permute the first-cell color to 0, then swap residual colors 1 and 2 if their first-occurrence order requires it",
        },
        "cube_file": str(args.cubes),
        "cnf_file": str(args.cnf),
        "cnf_sha256": hashlib.sha256(rendered).hexdigest(),
        "legacy_input": str(args.legacy),
        "legacy_sha256": hashlib.sha256(args.legacy.read_bytes()).hexdigest(),
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"counts": counts, "cnf_sha256": manifest["cnf_sha256"], "nominal_solver_cap_seconds": cubes["nominal_solver_cap_seconds"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

