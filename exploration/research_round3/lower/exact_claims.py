#!/usr/bin/env python3
"""Independent exact-integer recomputation of Route-5 headline counts."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    n = 21
    direct_corners = sum((n - d) ** 2 for d in range(1, n))
    formula_corners = (n - 1) * n * (2 * n - 1) // 6
    variables = 3 * n * n
    cell_clauses = 4 * n * n
    forbidden = 3 * direct_corners
    pre_symmetry = cell_clauses + forbidden
    symmetry = n * n
    total = pre_symmetry + symmetry
    affine_pairs = sum(m * m for m in range(2, 51))
    affine_attempted = 18916 + 4198 + 2989
    result = {
        "schema": "round3_lower_exact_claims_v1",
        "arithmetic_type": "Python integers and fractions only",
        "n21": {
            "corners_direct_sum": direct_corners,
            "corners_closed_formula": formula_corners,
            "corner_count_match": direct_corners == formula_corners == 2870,
            "variables": variables,
            "cell_clauses": cell_clauses,
            "forbidden_color_clauses": forbidden,
            "clauses_before_symmetry": pre_symmetry,
            "symmetry_clauses": symmetry,
            "total_clauses": total,
            "cubes": 3 ** 4,
            "stage1_nominal_solver_cap_seconds": 33 * 2 + 48 * 10,
            "hard_cubes": 24 + 5 + 19,
            "certified_easy_plus_unresolved_hard": 33 + 48,
        },
        "difference_circulant_n3": {"corners": sum(m * m for m in range(1, 3))},
        "affine_scan": {
            "parameter_pairs": affine_pairs,
            "attempted": affine_attempted,
            "remaining": affine_pairs - affine_attempted,
        },
        "inherited_gap": {
            "lower_bound": 21,
            "upper_bound": 465,
            "integer_gap": 465 - 21,
            "ratio_numerator": Fraction(465, 21).numerator,
            "ratio_denominator": Fraction(465, 21).denominator,
        },
    }
    checks = [
        direct_corners == formula_corners == 2870,
        (variables, cell_clauses, forbidden, pre_symmetry, symmetry, total) == (1323, 1764, 8610, 10374, 441, 10815),
        3 ** 4 == 81,
        33 * 2 + 48 * 10 == 546,
        24 + 5 + 19 == 48,
        33 + 48 == 81,
        sum(m * m for m in range(1, 3)) == 5,
        affine_pairs == 42924,
        affine_attempted == 26103,
        affine_pairs - affine_attempted == 16821,
        465 - 21 == 444,
        Fraction(465, 21) == Fraction(155, 7),
    ]
    result["all_exact_checks_pass"] = all(checks)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["all_exact_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

