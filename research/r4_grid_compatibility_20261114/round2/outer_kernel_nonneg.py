"""Pilot (lane B, outer aggregation), part 2: best NONNEGATIVE outer kernel.

The unconstrained top eigenvector of M(n) (outer_kernel_pilot.py) oscillates: about half
of its entries are negative, and some correlations b_d are negative. That makes it
inadmissible. Here w >= 0 is enforced, which gives b_d >= 0.
- The kernel is found by projected power iteration, w <- max(0, (M + sigma I) w),
  starting from the quadratic profile i(W+1-i).
- M includes the linearised twenty-shift bonus, 328 * b_{D-1} per block. That equals
  the exact bonus 328 * min_s b_{D-s} because b is nonincreasing.
- The float kernel is rounded to integers. The margin is then evaluated EXACTLY with the
  inherited verifier (verify_four_twenty.outer_twenty) and Codex's certified rows.

It bisects for the smallest side n in [n0 - 20000, n0] with a positive exact margin.
Usage (from this directory): python outer_kernel_nonneg.py <consumer_results.json> [width]
"""
import sys
import time

import numpy as np

CONS = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 35990
sys.argv = ["outer_kernel_pilot.py", CONS]
sys.path.insert(0, ".")
import outer_kernel_pilot as P      # noqa: E402
import verify_four_twenty as vt     # noqa: E402

N0 = 21_947_865
BLOCK = vt.BLOCK


def centers(n):
    rows, starts, off, cs = P.ROWS, P.STARTS, P.REF - n, []
    for i in range(1, len(rows) - 1):
        v, cap, _ = rows[i]
        D = v - off
        if (rows[i - 1][1] == cap + 1 and v - starts[i - 1] >= BLOCK
                and starts[i + 1] - v >= 12 and D - BLOCK >= 1 and D - 1 < W):
            cs.append(D)
    return cs


def operator(n):
    T = np.array([-3.0 * n] + [n - d - 4.0 * P.U(n, d) for d in range(1, W)])
    for D in centers(n):
        T[D - 1] += 8 * 41 / 2.0
    c = np.concatenate([T, [0.0], T[:0:-1]])
    fc, L = np.fft.rfft(c), len(c)
    return lambda x: np.fft.irfft(fc * np.fft.rfft(np.concatenate([x, np.zeros(L - W)])), L)[:W]


def test(n, iters=4000):
    mv = operator(n)
    w = np.array([i * (W + 1 - i) for i in range(1, W + 1)], float)
    w /= np.linalg.norm(w)
    sig = 3.0 * n + 1e5
    for _ in range(iters):
        w = np.clip(mv(w) + sig * w, 0, None)
        nr = np.linalg.norm(w)
        if nr == 0:
            return False, float("-inf"), 0
        w /= nr
    rq = float(w @ mv(w))
    _, b = P.integer_kernel(w)
    m, _ = P.exact_margin(n, W, b)
    return m > 0, rq, m


def main():
    t0 = time.time()
    lo, hi = N0 - 20000, N0
    g, rq, m = test(hi)
    print("width", W, "n0", N0, "positive", g, "rayleigh", round(rq, 1), "exact margin", m, flush=True)
    if g:
        while hi - lo > 1 and time.time() - t0 < 780:
            mid = (lo + hi) // 2
            gm, rqm, _ = test(mid)
            print(mid, gm, round(rqm, 1), flush=True)
            if gm:
                hi = mid
            else:
                lo = mid
    print("bracket", [lo, hi])


if __name__ == "__main__":
    main()
