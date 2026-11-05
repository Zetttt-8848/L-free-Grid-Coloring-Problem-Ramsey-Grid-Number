"""Deterministic multistart search with exact reevaluation of every candidate.

Numerical optimization is only a heuristic search.  Each returned vector is
replaced by an explicitly saved integer vector before its reported exact score
and exact Rayleigh quotient are evaluated.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import minimize
from scipy.linalg import toeplitz


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]
SEED = 2026090901
INTEGER_SCALE = 10**12


def q_from_span(span: int) -> int:
    if not 0 <= span < H[-1]:
        raise ValueError(span)
    return max(m for m, lower in enumerate(H) if lower <= span)


def q_d(n: int, d: int) -> int:
    positions = n - d
    return min(positions, q_from_span(positions - 1))


def matrix(n: int, t: int) -> np.ndarray:
    first = [-float(n)] + [
        (n - d - 18 * q_d(n, d)) / 2.0 for d in range(1, t)
    ]
    return toeplitz(first)


def exact_score(n: int, w: list[int]) -> tuple[int, int, Fraction, list[int]]:
    a = [sum(w[i] * w[i + d] for i in range(len(w) - d))
         for d in range(len(w))]
    score = sum((n - d - 18 * q_d(n, d)) * a[d]
                for d in range(1, len(w))) - n * a[0]
    return score, a[0], Fraction(score, a[0]), a


def analytic_starts(t: int) -> list[tuple[str, np.ndarray]]:
    i = np.arange(1, t + 1, dtype=float)
    starts = [
        ("ones", np.ones(t)),
        ("tent", np.minimum(i, t + 1 - i)),
        ("parabola", i * (t + 1 - i)),
        ("sine", np.sin(np.pi * i / (t + 1))),
    ]
    return [(name, v / np.linalg.norm(v)) for name, v in starts]


def solve_start(B: np.ndarray, x0: np.ndarray) -> object:
    def fun(x: np.ndarray) -> float:
        return -float(x @ B @ x)

    def jac(x: np.ndarray) -> np.ndarray:
        return -2.0 * (B @ x)

    constraint = {
        "type": "eq",
        "fun": lambda x: float(x @ x - 1.0),
        "jac": lambda x: 2.0 * x,
    }
    return minimize(fun, x0, jac=jac, method="SLSQP",
                    bounds=[(0.0, None)] * len(x0),
                    constraints=[constraint],
                    options={"ftol": 1e-12, "maxiter": 2000, "disp": False})


def integerize(x: np.ndarray) -> list[int]:
    x = np.maximum(x, 0.0)
    if not np.any(x > 0):
        raise ValueError("optimizer returned zero vector")
    # Normalize by the largest coordinate, then use one common exact integer
    # denominator.  The Rayleigh quotient is unaffected by this rescaling.
    y = x / np.max(x)
    w = np.rint(INTEGER_SCALE * y).astype(object)
    return [int(max(0, z)) for z in w]


def centered_pad(x: np.ndarray, t: int) -> np.ndarray:
    if len(x) > t:
        raise ValueError("cannot pad to shorter length")
    before = (t - len(x)) // 2
    y = np.zeros(t)
    y[before:before + len(x)] = x
    return y / np.linalg.norm(y)


def run_case(n: int, t: int, previous_best: np.ndarray | None) -> tuple[dict, np.ndarray]:
    B = matrix(n, t)
    rng = np.random.default_rng(SEED + 1000 * n + t)
    starts = analytic_starts(t)
    if previous_best is not None:
        starts.append(("centered_previous_best", centered_pad(previous_best, t)))
    for j in range(16):
        v = rng.exponential(scale=1.0, size=t)
        if j % 2:
            v = (v + v[::-1]) / 2
        starts.append((f"exp_seed_{j:02d}", v / np.linalg.norm(v)))

    candidates = []
    best_key = None
    best_x = None
    for start_index, (start_name, x0) in enumerate(starts):
        res = solve_start(B, x0)
        w = integerize(res.x)
        score, norm2, quotient, a = exact_score(n, w)
        rec = {
            "start_index": start_index,
            "start_name": start_name,
            "solver_success": bool(res.success),
            "solver_status": int(res.status),
            "solver_message": str(res.message),
            "iterations": int(res.nit),
            "floating_objective": float(res.x @ B @ res.x),
            "floating_norm2": float(res.x @ res.x),
            "integer_scale": INTEGER_SCALE,
            "integer_weights": w,
            "exact_score": score,
            "exact_norm2": norm2,
            "exact_quotient_numerator": quotient.numerator,
            "exact_quotient_denominator": quotient.denominator,
            "minimum_autocorrelation": min(a),
        }
        candidates.append(rec)
        key = Fraction(score, norm2)
        if best_key is None or key > best_key:
            best_key = key
            best_x = np.asarray(w, dtype=float)
            best_x /= np.linalg.norm(best_x)

    best_index = max(range(len(candidates)), key=lambda j: Fraction(
        candidates[j]["exact_quotient_numerator"],
        candidates[j]["exact_quotient_denominator"]))
    best = candidates[best_index]
    return {
        "n": n,
        "t": t,
        "candidate_count": len(candidates),
        "best_candidate_index": best_index,
        "best_exact_score": best["exact_score"],
        "best_exact_norm2": best["exact_norm2"],
        "best_exact_quotient_numerator": best["exact_quotient_numerator"],
        "best_exact_quotient_denominator": best["exact_quotient_denominator"],
        "best_floating_objective": best["floating_objective"],
        "candidates": candidates,
    }, best_x


def main() -> None:
    cases = []
    for n in (464, 465):
        previous = None
        previous_q = None
        for t in (68, 93, 120, 150):
            case, previous = run_case(n, t, previous)
            q = Fraction(case["best_exact_quotient_numerator"],
                         case["best_exact_quotient_denominator"])
            if previous_q is not None:
                # The explicitly included zero-padded previous exact vector
                # makes this a finite exact check, not a claim about solver quality.
                assert q >= previous_q
            previous_q = q
            cases.append(case)

    output = {
        "honesty_label": "UNVERIFIED optimizer; exact rational candidate evaluations",
        "mathematical_nonclaim": (
            "Negative candidates do not prove that the nonnegative relaxation "
            "optimum is negative."
        ),
        "coefficient_convention": "c_d=n-d-18*q_d; B_ii=-n; B_ij=c_|i-j|/2",
        "q_convention": "q_d from inherited H_0..H_28 and n-d start positions",
        "normalization": "unit l2 in SLSQP; exact score/exact_norm2 after integerization",
        "seed": SEED,
        "integer_scale": INTEGER_SCALE,
        "software": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "cases": cases,
    }
    path = Path(__file__).with_name("weights_multistart_result.json")
    text = json.dumps(output, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps({
        "result_file": str(path),
        "sha256": digest,
        "cases": [{k: case[k] for k in (
            "n", "t", "candidate_count", "best_candidate_index",
            "best_exact_score", "best_exact_norm2",
            "best_exact_quotient_numerator", "best_exact_quotient_denominator",
            "best_floating_objective")}
                  for case in cases],
    }, indent=2))


if __name__ == "__main__":
    main()
