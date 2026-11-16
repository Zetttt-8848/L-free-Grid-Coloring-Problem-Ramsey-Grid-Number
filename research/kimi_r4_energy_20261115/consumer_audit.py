#!/usr/bin/env python3
"""Audit valid full-square embeddings into the host strict triangle."""

import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "consumer_results.json"


def q_value(n, m, s):
    return n - 1 - (m - 1) * s


def valid_origin_count(n, m, s):
    q = q_value(n, m, s)
    if q < 0:
        return 0
    t = min(s - 1, q)
    return (q + 1) * (q + 2) // 2 + t * (q + 1) - t * (t + 1) // 2


def valid_origins_literal(n, m, s):
    q = q_value(n, m, s)
    if q < 0:
        return []
    result = []
    for a in range(q + 1):
        for b in range(q + 1):
            if all(a + s * i > b + s * j
                   for i in range(1, m) for j in range(i)):
                result.append((a, b))
    return result


def local_ls(m):
    result = []
    for x in range(m):
        for y in range(x):
            for step in range(1, m - x):
                result.append(((x, y), (x + step, y), (x + step, y + step)))
    return result


def host_ls(n):
    result = []
    for x in range(n):
        for y in range(x):
            for step in range(1, n - x):
                result.append(((x, y), (x + step, y), (x + step, y + step)))
    return result


def audit_scenario(n, m):
    locals_ = local_ls(m)
    assert len(locals_) == m * (m - 1) * (m - 2) // 6
    direct = Counter()
    copy_count = 0
    scale_rows = []
    for s in range(1, (n - 1) // (m - 1) + 1):
        origins = valid_origins_literal(n, m, s)
        formula = valid_origin_count(n, m, s)
        assert len(origins) == formula
        copy_count += formula
        scale_rows.append({"s": s, "valid_origins": formula})
        for a, b in origins:
            for local in locals_:
                host = tuple((a + s * x, b + s * y) for x, y in local)
                direct[host] += 1
    formula_incidence = Counter()
    for host in host_ls(n):
        (x, y), (_, _), _ = host
        h = host[2][1] - y
        for j in range(1, m - 1):
            if h % j:
                continue
            s = h // j
            q = q_value(n, m, s)
            if q < 0:
                continue
            for local in locals_:
                step = local[2][1] - local[1][1]
                if step != j:
                    continue
                lx, ly = local[0]
                a, b = x - s * lx, y - s * ly
                if 0 <= a <= q and 0 <= b <= q and a - b + s >= 1:
                    formula_incidence[host] += 1
    assert direct == formula_incidence
    assert sum(direct.values()) == len(locals_) * copy_count
    universal_cap = len(locals_)
    assert all(value <= universal_cap for value in direct.values())
    return {
        "N": n,
        "m": m,
        "scale_rows": scale_rows,
        "J_uniform": copy_count,
        "host_Ls": len(host_ls(n)),
        "incidence_entries": len(direct),
        "total_incidences": sum(direct.values()),
        "maximum_actual_incidence": max(direct.values(), default=0),
        "universal_Lambda_cap_C_m": universal_cap,
        "literal_copy_and_formula_agreement": True,
    }


def main():
    scenarios = [audit_scenario(n, m) for n, m in
                 ((4, 3), (5, 3), (6, 4), (7, 4), (8, 5))]
    kernels = json.loads((ROOT / "kernel_results.json").read_text(encoding="ascii"))
    rho = {row["m"]: row.get("rho_m") for row in kernels["orders"]}
    thresholds = []
    for m in range(3, 9):
        c = m * (m - 1) * (m - 2) // 6
        j_coefficient = Fraction(m + 1, 6 * m * (m - 1))
        required_fraction = Fraction(1, 24) / j_coefficient
        strict_rho_threshold = c * required_fraction
        possible = required_fraction < 1
        row = {
            "m": m,
            "C_m": c,
            "J_over_N_cubed_limit": str(j_coefficient),
            "rainbow_ceiling_over_N_cubed_limit": "1/24",
            "required_rho_over_C_m_strictly_above": str(required_fraction),
            "required_rho_strictly_above": str(strict_rho_threshold),
            "asymptotic_uniform_consumer_possible": possible,
            "tested_rho": rho.get(m, "not tested"),
        }
        if possible:
            assert m in (3, 4, 5)
            assert rho[m] == 0
        else:
            assert m >= 6
        row["consumer_closed"] = True
        thresholds.append(row)

    # The contracted unrestricted origin count is already wrong at N=4,m=3,s=1.
    assert q_value(4, 3, 1) == 1
    assert valid_origin_count(4, 3, 1) == 3
    assert (q_value(4, 3, 1) + 1) ** 2 == 4

    result = {
        "date": "2026-11-15",
        "python": sys.version.split()[0],
        "validity_condition": "a-b+s>=1; equivalently every local strict-triangle cell lies in host T_N",
        "origin_formula": "q=N-1-(m-1)s; t=min(s-1,q); A=C(q+2,2)+t(q+1)-C(t+1,2)",
        "corrected_J": "sum_s a_s*A(N,m,s)",
        "Lambda_upper": "sum_(j|h,1<=j<=m-2) a_(h/j)*C(m-j,2)",
        "uniform_J_leading_coefficient": "(m+1)/(6*m*(m-1))",
        "uniform_K": "C(m,3)",
        "asymptotic_closure": "m=3,4,5 have rho=0; for m>=6 even rho=C(m,3) cannot beat the uniform-K ceiling",
        "scenarios": scenarios,
        "thresholds": thresholds,
        "new_R4_bound": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"status": "PASS", "output": str(OUT),
                      "scenarios": len(scenarios),
                      "uniform_asymptotic_consumer_closed_for_all_m": True,
                      "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
