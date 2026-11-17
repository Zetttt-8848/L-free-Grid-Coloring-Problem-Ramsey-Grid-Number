#!/usr/bin/env python3
"""Discover finite scale packings and export exact feasible certificates."""

import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent
PAIRS = ((30, 6), (60, 6), (120, 6))
OUT = ROOT / "dual_results.json"
DIAGNOSTICS = ROOT / "solver_diagnostics.json"


def scales(n, m):
    return range(1, (n - 1) // (m - 1) + 1)


def copy_count(n, m, s):
    q = n - 1 - (m - 1) * s
    if q < 0:
        return 0
    t = min(s - 1, q)
    return (q + 1) * (q + 2) // 2 + t * (q + 1) - t * (t + 1) // 2


def incidence_coefficients(m):
    return tuple((m - j) * (m - j - 1) // 2 for j in range(1, m - 1))


def constraint_matrix(n, m):
    ss = tuple(scales(n, m))
    cs = incidence_coefficients(m)
    rows = []
    for h in range(1, n - 1):
        row = [0] * len(ss)
        for j, c in enumerate(cs, start=1):
            if h % j == 0 and h // j in ss:
                row[ss.index(h // j)] = c
        rows.append(row)
    return np.asarray(rows, dtype=float), np.asarray(
        [copy_count(n, m, s) for s in ss], dtype=float)


def rainbow_ceiling(n):
    h = Fraction(n * (n - 1) * (2 * n + 23), 24)
    e = Fraction(0)
    for length in range(1, n):
        r = length % 4
        e += 3 * Fraction(r * (4 - r), 4)
    return (h - e) / 2


def as_exact_vector(values):
    return [Fraction(str(max(0.0, float(value)))).limit_denominator(10 ** 9)
            for value in values]


def exact_primal(n, m, values):
    ss = tuple(scales(n, m))
    cs = incidence_coefficients(m)
    a = as_exact_vector(values)
    largest = Fraction(0)
    for h in range(1, n - 1):
        value = sum((cs[j - 1] * a[h // j - 1]
                     for j in range(1, m - 1)
                     if h % j == 0 and 1 <= h // j <= len(ss)), Fraction(0))
        largest = max(largest, value)
    if largest > 1:
        a = [value / largest for value in a]
    j_value = sum((copy_count(n, m, s) * a[s - 1] for s in ss), Fraction(0))
    return a, j_value


def exact_dual(n, m, values):
    ss = tuple(scales(n, m))
    cs = incidence_coefficients(m)
    y = as_exact_vector(values)
    repair = Fraction(1)
    for s in ss:
        covered = sum((cs[j - 1] * y[j * s - 1]
                       for j in range(1, m - 1) if j * s <= n - 2), Fraction(0))
        required = copy_count(n, m, s)
        if covered < required:
            if covered == 0:
                raise ValueError(f"Dual support has zero coverage at N={n}, s={s}")
            repair = max(repair, Fraction(required) / covered)
    y = [repair * value for value in y]
    return y, sum(y, Fraction(0))


def rational(value):
    return str(Fraction(value))


def exact_vector(values):
    return [rational(value) for value in values]


def run_pair(n, m):
    matrix, objective = constraint_matrix(n, m)
    result = linprog(-objective, A_ub=matrix, b_ub=np.ones(n - 2),
                     bounds=(0, None), method="highs")
    if not result.success:
        return {"N": n, "m": m, "status": "UNDECIDED",
                "solver_message": result.message}, {
            "N": n, "m": m, "success": False, "message": result.message}
    # For minimization with upper inequalities, HiGHS reports nonpositive
    # marginals; their negatives are nonnegative dual variables.
    primal, primal_value = exact_primal(n, m, result.x)
    dual, dual_value = exact_dual(n, m, -result.ineqlin.marginals)
    c_m = m * (m - 1) * (m - 2) // 6
    ceiling = rainbow_ceiling(n)
    uniform = [Fraction(1, c_m)] * len(tuple(scales(n, m)))
    uniform_value = sum((copy_count(n, m, s) * uniform[s - 1]
                         for s in scales(n, m)), Fraction(0))
    row = {
        "N": n,
        "m": m,
        "status": "EXACT_FEASIBLE_CERTIFICATES",
        "C_m": c_m,
        "rainbow_ceiling_U_N": rational(ceiling),
        "uniform_normalized_J": rational(uniform_value),
        "primal_a": exact_vector(primal),
        "primal_J": rational(primal_value),
        "primal_best_case_margin_Cm_J_minus_U": rational(c_m * primal_value - ceiling),
        "dual_y": exact_vector(dual),
        "dual_bound": rational(dual_value),
        "dual_best_case_margin_Cm_bound_minus_U": rational(c_m * dual_value - ceiling),
        "closure_certified_by_dual": c_m * dual_value <= ceiling,
        "positive_best_case_certified_by_primal": c_m * primal_value > ceiling,
    }
    diagnostic = {
        "N": n,
        "m": m,
        "evidence_status": "DISCOVERY_ONLY",
        "solver": "scipy.optimize.linprog(method=highs)",
        "success": True,
        "message": result.message,
        "floating_objective_maximize_J": -float(result.fun),
        "floating_primal_nonzeros": int(np.count_nonzero(result.x > 1e-9)),
        "floating_dual_nonzeros": int(np.count_nonzero(-result.ineqlin.marginals > 1e-9)),
        "floating_primal_x": [float(v) for v in result.x],
        "floating_dual_y": [float(v) for v in -result.ineqlin.marginals],
    }
    return row, diagnostic


def main():
    rows = []
    diagnostics = []
    for n, m in PAIRS:
        row, diagnostic = run_pair(n, m)
        rows.append(row)
        diagnostics.append(diagnostic)
    result = {
        "date": "2026-11-16",
        "python": sys.version.split()[0],
        "scipy": scipy.__version__,
        "pairs": [[n, m] for n, m in PAIRS],
        "normalization": "Lambda_h<=1 for every 1<=h<=N-2",
        "floating_point_status": "discovery only; exact vectors are the evidence",
        "rows": rows,
        "new_Ramsey_bound": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    DIAGNOSTICS.write_text(json.dumps({
        "status": "NON_EVIDENTIARY_DISCOVERY_DIAGNOSTICS",
        "rows": diagnostics,
    }, indent=2) + "\n", encoding="ascii")
    print(json.dumps({
        "status": "PASS" if all(row["status"] == "EXACT_FEASIBLE_CERTIFICATES" for row in rows)
                  else "UNDECIDED",
        "output": str(OUT),
        "summary": [{"N": row["N"], "m": row["m"],
                     "primal_margin": row.get("primal_best_case_margin_Cm_J_minus_U"),
                     "dual_margin": row.get("dual_best_case_margin_Cm_bound_minus_U"),
                     "closure": row.get("closure_certified_by_dual")}
                    for row in rows],
        "new_Ramsey_bound": False,
    }, indent=2))


if __name__ == "__main__":
    main()
