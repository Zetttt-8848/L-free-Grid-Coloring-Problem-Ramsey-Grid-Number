#!/usr/bin/env python3
"""Independently check origin counts and asymptotic consumer thresholds."""

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "consumer_results.json"
OUT = ROOT / "consumer_verification.json"


def difference_enumeration(n, m, s):
    q = n - 1 - (m - 1) * s
    if q < 0:
        return 0
    return sum(q + 1 - abs(d) for d in range(-q, q + 1) if d >= 1 - s)


def cubic_leading_by_exact_sums(m):
    # Reconstruct the leading coefficient on the exact-divisibility subsequence
    # L | N, L=m*(m-1), using five points and finite differences in j=N/L.
    L = m * (m - 1)

    def exact_j(j):
        n = j * L
        total = 0
        for s in range(1, (n - 1) // (m - 1) + 1):
            total += difference_enumeration(n, m, s)
        return total

    values = [exact_j(j) for j in range(1, 6)]
    for order in range(3):
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    third_difference = values[0]
    assert len(values) == 2 and values[1] == third_difference
    # A cubic in j has constant third finite difference 6*a_3.
    coefficient_in_j = Fraction(third_difference, 6)
    return coefficient_in_j / (L ** 3)


def main():
    source = json.loads(SOURCE.read_text(encoding="ascii"))
    origins_checked = 0
    for scenario in source["scenarios"]:
        n, m = scenario["N"], scenario["m"]
        total = 0
        for row in scenario["scale_rows"]:
            s = row["s"]
            count = difference_enumeration(n, m, s)
            assert count == row["valid_origins"]
            total += count
            origins_checked += 1
        assert total == scenario["J_uniform"]
        assert scenario["total_incidences"] == total * (m * (m - 1) * (m - 2) // 6)

    asymptotic = []
    for m in range(3, 9):
        coefficient = cubic_leading_by_exact_sums(m)
        expected = Fraction(m + 1, 6 * m * (m - 1))
        assert coefficient == expected, (m, coefficient, expected)
        required = Fraction(1, 24) / coefficient
        c = m * (m - 1) * (m - 2) // 6
        assert (required < 1) == (m <= 5)
        row = next(row for row in source["thresholds"] if row["m"] == m)
        assert Fraction(row["required_rho_over_C_m_strictly_above"]) == required
        assert Fraction(row["required_rho_strictly_above"]) == c * required
        if m <= 5:
            assert row["tested_rho"] == 0
        asymptotic.append({"m": m, "J_coefficient": str(coefficient),
                           "required_fraction": str(required), "status": "PASS"})

    result = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "origin_rows_recomputed_by_difference_enumeration": origins_checked,
        "cubic_coefficients_reconstructed_by_exact_finite_sums": asymptotic,
        "uniform_asymptotic_consumer_closed_for_all_m": True,
        "nonuniform_weights_or_other_consumers": "not refuted",
        "new_R4_bound": False,
        "scope": "Internal independent arithmetic and geometry checks",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
