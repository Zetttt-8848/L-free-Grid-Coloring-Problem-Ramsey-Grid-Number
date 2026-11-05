#!/usr/bin/env python3
"""Independent direct audit of the CNF mapping and the 81-cube partition."""

from __future__ import annotations

import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path


def lit(n: int, x: int, y: int, c: int) -> int:
    if not (0 <= x < n and 0 <= y < n and 0 <= c < 3):
        raise ValueError((n, x, y, c))
    return 3 * (x * n + y) + c + 1


def reconstruct(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for x, y in itertools.product(range(n), repeat=2):
        a, b, c = (lit(n, x, y, q) for q in range(3))
        out.extend(((a, b, c), (-a, -b), (-a, -c), (-b, -c)))
    triples = 0
    for d in range(1, n):
        for x, y in itertools.product(range(n - d), repeat=2):
            triples += 1
            for c in range(3):
                out.append((-lit(n, x, y, c), -lit(n, x + d, y, c), -lit(n, x + d, y + d, c)))
    if triples != sum(m * m for m in range(1, n)):
        raise AssertionError(triples)
    out.append((lit(n, 0, 0, 0),))
    for index in range(1, n * n):
        x, y = divmod(index, n)
        prior = tuple(lit(n, *divmod(j, n), 1) for j in range(1, index))
        out.append((-lit(n, x, y, 2), *prior))
    return out


def parse_dimacs(path: Path) -> tuple[int, int, list[tuple[int, ...]]]:
    nvars = nclauses = None
    clauses: list[tuple[int, ...]] = []
    for raw in path.read_text(encoding="ascii").splitlines():
        line = raw.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p "):
            fields = line.split()
            if len(fields) != 4 or fields[:2] != ["p", "cnf"]:
                raise ValueError("malformed DIMACS header")
            nvars, nclauses = map(int, fields[2:])
            continue
        values = tuple(map(int, line.split()))
        if not values or values[-1] != 0 or 0 in values[:-1]:
            raise ValueError("malformed DIMACS clause")
        clauses.append(values[:-1])
    if nvars is None or nclauses is None or nclauses != len(clauses):
        raise ValueError("missing or inconsistent DIMACS header")
    if max(abs(q) for clause in clauses for q in clause) > nvars:
        raise ValueError("literal exceeds declared variable range")
    return nvars, nclauses, clauses


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=21)
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    nvars, nclauses, actual = parse_dimacs(args.cnf)
    expected = reconstruct(args.n)
    clause_match = collections.Counter(actual) == collections.Counter(expected)
    cubes = json.loads(args.cubes.read_text(encoding="utf-8"))
    cells = [tuple(cell) for cell in cubes["split_cells_0_based"]]
    expected_tuples = set(itertools.product(range(3), repeat=len(cells)))
    found_tuples = [tuple(r["cube_colors_0_based"]) for r in cubes["records"]]
    literal_checks = []
    for record in cubes["records"]:
        colors = record["cube_colors_0_based"]
        want = [lit(args.n, x, y, c) for (x, y), c in zip(cells, colors)]
        literal_checks.append(record["assumption_literals"] == want)
    result = {
        "schema": "round3_lower_independent_instance_audit_v1",
        "n": args.n,
        "cnf_sha256": hashlib.sha256(args.cnf.read_bytes()).hexdigest(),
        "declared_variables": nvars,
        "declared_clauses": nclauses,
        "expected_variables": 3 * args.n * args.n,
        "expected_geometric_triples": sum(m * m for m in range(1, args.n)),
        "expected_clauses": len(expected),
        "clause_multiset_exact_match": clause_match,
        "cube_record_count": len(found_tuples),
        "cube_unique_count": len(set(found_tuples)),
        "cube_tuple_set_exact_match": set(found_tuples) == expected_tuples,
        "all_assumption_literals_exact": all(literal_checks),
        "coverage_argument": "restriction of any total coloring to the four split cells is one tuple in {0,1,2}^4; exact tuple-set equality gives one and only one cube",
    }
    result["audit_pass"] = all((
        nvars == 3 * args.n * args.n,
        nclauses == len(expected),
        clause_match,
        len(found_tuples) == 81,
        len(set(found_tuples)) == 81,
        result["cube_tuple_set_exact_match"],
        result["all_assumption_literals_exact"],
    ))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["audit_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

