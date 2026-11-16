#!/usr/bin/env python3
"""Independent exact checks for contiguous-block averaging results."""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    for row in data["rows"]:
        n = row["n"]
        assert row["contiguous_5_blocks"] == (n - 4) ** 2
        assert row["step_multiplicities"] == {
            str(d): (5 - d) ** 2 for d in range(1, 5)
        }
        if n <= 10:
            for d in range(1, 5):
                direct = 0
                for a in range(n - 4):
                    for b in range(n - 4):
                        # Count the block's Ls of step d from definitions.
                        direct += sum(
                            1 for x in range(a, a + 5) for y in range(b, b + 5)
                            if x + d < a + 5 and y + d < b + 5
                        )
                # Aggregate incidence uses the same multiplicity per fixed L.
                assert direct == (n - 4) ** 2 * (5 - d) ** 2
        total = n * (n - 1) * (2 * n - 1) // 6
        assert row["all_geometric_Ls"] == total
        if n <= 10:
            direct_total = sum(
                1 for x in range(n) for y in range(n) for d in range(1, n)
                if x + d < n and y + d < n
            )
            assert direct_total == total
        density = Fraction(row["density_lower_bound_numerator"],
                           row["density_lower_bound_denominator"])
        assert density == Fraction(3 * (n - 4) ** 2, total)
        assert density == Fraction(18 * (n - 4) ** 2,
                                   n * (n - 1) * (2 * n - 1))
    print(json.dumps({"status": "PASS", "checked_sides": [r["n"] for r in data["rows"]],
                      "scope": "contiguous-block incidence and exact arithmetic only"},
                     indent=2))


if __name__ == "__main__":
    main()
