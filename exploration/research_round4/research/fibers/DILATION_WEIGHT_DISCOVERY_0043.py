"""Raw dilation-weight LP discovery for N=464, m=10,...,18.

This is intentionally a one-pass floating-point discovery calculation.
It does not certify an optimum, a rational inequality, or any local
rainbow lower bound.
"""
import json
from math import comb
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

N = 464
M_HOST = comb(N, 2)
OUT = Path(__file__).with_suffix(".json")


def run(m):
    D = (N - 2) // (m - 2)
    ds = list(range(1, D + 1))
    C = np.array([comb(N - d * (m - 2), 2) for d in ds], dtype=float)
    A = np.array(
        [
            [
                comb(m - h // d, 2)
                if h % d == 0 and 1 <= h // d <= m - 2
                else 0
                for d in ds
            ]
            for h in range(1, N - 1)
        ],
        dtype=float,
    )
    result = linprog(
        c=-C,
        A_ub=A,
        b_ub=np.ones(N - 2),
        bounds=[(0, None)] * D,
        method="highs",
    )
    if not result.success:
        return {
            "m": m, "D": D, "status": result.message,
            "dilations": ds, "C_d": [int(x) for x in C],
        }
    w = result.x
    value = float(C @ w)
    row_loads = A @ w
    row_sums = A.sum(axis=1)
    uniform_scale = 1.0 / float(row_sums.max())
    uniform_value = float(C.sum() * uniform_scale)
    support = [
        {"d": d, "weight": float(x), "C_d": int(C[i])}
        for i, (d, x) in enumerate(zip(ds, w))
        if x > 1e-9
    ]
    return {
        "m": m,
        "D": D,
        "status": result.message,
        "objective_raw": value,
        "conditional_rho_threshold_raw": M_HOST / value,
        "candidate_support": support,
        "max_row_load_raw": float(row_loads.max()),
        "active_host_steps": [h + 1 for h, x in enumerate(row_loads) if abs(x - 1) < 1e-7],
        "uniform_safe_scale_raw": uniform_scale,
        "uniform_objective_raw": uniform_value,
        "gain_over_uniform_raw": value / uniform_value,
        "dilations": ds,
        "C_d": [int(x) for x in C],
    }


rows = [run(m) for m in range(10, 19)]
OUT.write_text(
    json.dumps(
        {
            "scope": "raw float LP discovery only; no exact certification",
            "N": N,
            "M_host": M_HOST,
            "constraints": (
                "A[h,d]=binom(m-h/d,2) if d divides h and "
                "1<=h/d<=m-2, otherwise 0; A w <= 1; w >= 0"
            ),
            "objective": "maximize sum_d C_d w_d",
            "rows": rows,
        },
        indent=2,
    ),
    encoding="utf-8",
)
print(json.dumps(rows, indent=2))
