"""Pilot (lane B, outer aggregation): is the quartic outer kernel far from optimal?

The outer inequality (FOUR_COLOR.md; THEOREM.md section 4 of Codex round 3) is
  raw(w) = -3 n b_0 + 2 sum_{d=1}^{W-1} (n - d - 4 U_d) b_d,   b_d = sum_i w_i w_{i+d},
plus the twenty-shift bonus 8*41*min_s b_{D-s} over disjoint blocks. It is valid for any
real weights w whose correlations b_d are >= 0 for d >= 1. That sign condition is what
allows X_d <= U_d to be substituted and the bonus to be credited.
raw(w) = w^T M w with M Toeplitz, M_0 = -3n, M_d = n-d-4U_d.
So the best kernel without the bonus is a top eigenvector of M.

This script:
 1. reproduces the certified quartic margin at n = 21,947,865 with the inherited exact
    verifier (verify_four_twenty.outer_twenty) and Codex's certified rows;
 2. for each tested n, computes a top eigenvector of M(n) (float, Lanczos, FFT matvec),
    rounds it to integers, checks b_d >= 0 exactly, and evaluates the EXACT margin with
    the same inherited verifier and the same certified rows;
 3. reports the smallest tested n with a positive exact margin, per width.
Rows are Codex's certified finite_seeded rows. For indices beyond the last row, the last
row's cap is reused. That is valid because the capacity is monotone in the number of
positions, but it is weaker than a recomputed row. All float computations are for
discovery only; the reported margins are exact integer evaluations. Nothing here is a
bound until it is re-verified and reviewed.
Usage: python outer_kernel_pilot.py <consumer_results.json> [seconds]
"""
import json
import sys
import time
from bisect import bisect_right
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "boundary_certificates_20261115"))
import verify_four_twenty as vt   # noqa: E402
import verify_four_edges as ve    # noqa: E402

REF = vt.REFERENCE
rows = json.loads(Path(sys.argv[1]).read_text())["finite_seeded"]["rows"]
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 780
PAD = [rows[-1][0] + 100000, rows[-1][1], rows[-1][2]]   # same cap, further index
ROWS = [list(r) for r in rows] + [PAD]
STARTS = [a for a, _, _ in ROWS]


def U(n, d):
    off = REF - n
    return sum(ROWS[bisect_right(STARTS, off + d + j) - 1][1] for j in range(12))


def exact_margin(n, W, b):
    cnt, raw, bonus, _ = vt.outer_twenty(ROWS, n, W, lambda t, d: b[d])
    return raw + bonus, cnt


def top_vector(n, W):
    T = np.array([-3.0 * n] + [n - d - 4.0 * U(n, d) for d in range(1, W)])
    c = np.concatenate([T, [0.0], T[:0:-1]])        # circulant embedding
    fc = np.fft.rfft(c)
    L = len(c)

    def mv(x):
        x = np.asarray(x).ravel()
        y = np.fft.irfft(fc * np.fft.rfft(np.concatenate([x, np.zeros(L - W)])), L)
        return y[:W]
    op = LinearOperator((W, W), matvec=mv, dtype=float)
    val, vec = eigsh(op, k=1, which="LA", tol=1e-10, maxiter=20000)
    v = vec[:, 0]
    if v.sum() < 0:
        v = -v
    return float(val[0]), v


def integer_kernel(v, scale=10**6):
    w = np.rint(v / np.abs(v).max() * scale).astype(np.int64)
    b = np.correlate(w, w, mode="full")[len(w) - 1:]
    return w, [int(x) for x in b]


def main():
    t0 = time.time()
    n0 = 21_947_865
    a = ve.quartic_correlations(ve.WIDTH)
    cnt, raw, bonus, _ = vt.outer_twenty(rows, n0, ve.WIDTH, lambda t, d: a[d])
    out = {"quartic": {"n": n0, "margin": raw + bonus, "positive": raw + bonus > 0,
                       "blocks": cnt}, "eigen": []}
    print("quartic", out["quartic"], flush=True)

    def test(n, W):
        lam, v = top_vector(n, W)
        w, b = integer_kernel(v)
        if min(b[1:]) < 0:
            return False, {"n": n, "lambda": lam, "negative_correlation": True}
        m, blocks = exact_margin(n, W, b)
        return m > 0, {"n": n, "lambda": lam, "margin": m, "blocks": blocks,
                       "w_min": int(w.min())}

    for W in (35990, 30000):
        good, info = test(n0, W)
        rec = {"width": W, "at_n0": info, "positive_at_n0": good}
        if good:
            lo, hi, best = n0 - 50000, n0, info
            while hi - lo > 1 and time.time() - t0 < BUDGET:
                mid = (lo + hi) // 2
                g, inf = test(mid, W)
                if g:
                    hi, best = mid, inf
                else:
                    lo = mid
            rec.update({"bracket": [lo, hi], "best": best,
                        "bisection_complete": hi - lo == 1})
        out["eigen"].append(rec)
        print(json.dumps(rec, default=str), round(time.time() - t0), "s", flush=True)
        if time.time() - t0 > BUDGET:
            break
    (HERE / "outer_kernel_pilot.json").write_text(json.dumps(out, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
