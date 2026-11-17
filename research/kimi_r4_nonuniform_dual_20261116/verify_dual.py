#!/usr/bin/env python3
"""Independently verify exact primal and dual certificates from definitions."""

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "dual_results.json"
OUT = ROOT / "dual_verification.json"


def copy_count_by_differences(n, m, s):
    q = n - 1 - (m - 1) * s
    if q < 0:
        return 0
    return sum(q + 1 - abs(d) for d in range(-q, q + 1) if d >= 1 - s)


def copy_count_by_origins(n, m, s):
    q = n - 1 - (m - 1) * s
    if q < 0:
        return 0
    return sum(1 for a in range(q + 1) for b in range(q + 1)
               if a - b + s >= 1)


def ceiling_by_line_residues(n):
    h = Fraction(n * (n - 1) * (2 * n + 23), 24)
    e = sum((3 * Fraction((length % 4) * (4 - length % 4), 4)
             for length in range(1, n)), Fraction(0))
    return (h - e) / 2


def parse_vector(values):
    return [Fraction(value) for value in values]


def primal_errors(n, m, a):
    errors = []
    smax = (n - 1) // (m - 1)
    if len(a) != smax:
        errors.append("wrong primal length")
    if any(value < 0 for value in a):
        errors.append("negative primal coordinate")
    if len(a) != smax:
        return errors
    for h in range(1, n - 1):
        incidence = Fraction(0)
        for j in range(1, m - 1):
            if h % j == 0 and 1 <= h // j <= smax:
                incidence += Fraction((m - j) * (m - j - 1), 2) * a[h // j - 1]
        if incidence > 1:
            errors.append(f"primal incidence violation at h={h}: {incidence}")
    return errors


def dual_errors(n, m, y):
    errors = []
    smax = (n - 1) // (m - 1)
    if len(y) != n - 2:
        errors.append("wrong dual length")
    if any(value < 0 for value in y):
        errors.append("negative dual coordinate")
    if len(y) != n - 2:
        return errors
    for s in range(1, smax + 1):
        coverage = Fraction(0)
        for j in range(1, m - 1):
            if j * s <= n - 2:
                coverage += Fraction((m - j) * (m - j - 1), 2) * y[j * s - 1]
        required = copy_count_by_differences(n, m, s)
        if coverage < required:
            errors.append(f"dual coverage violation at s={s}: {coverage} < {required}")
    return errors


def main():
    source = json.loads(SOURCE.read_text(encoding="ascii"))
    assert source["pairs"] == [[30, 6], [60, 6], [120, 6]]
    geometry_checks = 0
    for n, m in ((7, 3), (8, 4), (10, 6), (11, 6)):
        for s in range(1, (n - 1) // (m - 1) + 1):
            assert copy_count_by_differences(n, m, s) == copy_count_by_origins(n, m, s)
            geometry_checks += 1

    # Negative controls must be rejected before any stored row is accepted.
    assert primal_errors(30, 6, [Fraction(1)] * 5)
    assert dual_errors(30, 6, [Fraction(0)] * 28)
    assert not primal_errors(30, 6, [Fraction(0)] * 5)
    # The uniform vector is a known feasible nonzero control.
    assert not primal_errors(30, 6, [Fraction(1, 20)] * 5)

    rows = []
    for stored in source["rows"]:
        n, m = stored["N"], stored["m"]
        c_m = m * (m - 1) * (m - 2) // 6
        assert c_m == stored["C_m"]
        a = parse_vector(stored["primal_a"])
        y = parse_vector(stored["dual_y"])
        p_errors = primal_errors(n, m, a)
        d_errors = dual_errors(n, m, y)
        assert not p_errors, p_errors
        assert not d_errors, d_errors
        primal = sum((copy_count_by_differences(n, m, s) * a[s - 1]
                      for s in range(1, len(a) + 1)), Fraction(0))
        dual = sum(y, Fraction(0))
        ceiling = ceiling_by_line_residues(n)
        assert primal == Fraction(stored["primal_J"])
        assert dual == Fraction(stored["dual_bound"])
        assert ceiling == Fraction(stored["rainbow_ceiling_U_N"])
        assert primal <= dual
        primal_margin = c_m * primal - ceiling
        dual_margin = c_m * dual - ceiling
        assert primal_margin == Fraction(stored["primal_best_case_margin_Cm_J_minus_U"])
        assert dual_margin == Fraction(stored["dual_best_case_margin_Cm_bound_minus_U"])
        assert (dual_margin <= 0) == stored["closure_certified_by_dual"]
        assert (primal_margin > 0) == stored["positive_best_case_certified_by_primal"]
        uniform = sum((Fraction(copy_count_by_differences(n, m, s), c_m)
                       for s in range(1, (n - 1) // (m - 1) + 1)), Fraction(0))
        assert uniform == Fraction(stored["uniform_normalized_J"])
        rows.append({
            "N": n,
            "m": m,
            "primal_constraints_checked": n - 2,
            "dual_constraints_checked": len(a),
            "primal_J": str(primal),
            "dual_bound": str(dual),
            "exact_optimum_certified_by_equal_feasible_values": primal == dual,
            "C_m_times_V_minus_U_N": str(dual_margin) if primal == dual else None,
            "uniform_best_case_margin": str(c_m * uniform - ceiling),
            "status": "PASS",
        })

    result = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "implementation": "standard library only; no import from dual_probe.py",
        "origin_counts_cross_checked": geometry_checks,
        "negative_controls_rejected": 2,
        "known_feasible_controls_accepted": 2,
        "rows": rows,
        "scope": "Three finite weighted uniform-incidence programs only",
        "actual_local_rho_6": "not computed; the positive best-case margins are not Ramsey bounds",
        "new_Ramsey_bound": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
