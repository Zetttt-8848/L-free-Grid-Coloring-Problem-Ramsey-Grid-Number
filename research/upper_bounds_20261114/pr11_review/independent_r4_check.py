"""Independent re-implementation of the PR 11 four-color certificate (R_4 <= 21,987,409).

Written for the review of PR 11 (head b3941b3ad1d669bad7d3f849a28aebb486b178c2).
It shares no code with verify_four_rank.py.  Differences from that verifier:

* each rank witness is re-checked by a direct loop over internal differences h
  (no prefix sums, no bisection on the cumulative profile);
* the autocorrelation a_d of w_i = i(t+1-i) is computed by literal summation at
  twelve lags and the degree-5 polynomial in d through those values is used
  (a_d is a polynomial of degree <= 5 in d on 0 <= d <= t, so twelve literal
  values over-determine it; the closed form is then checked against it);
* every inequality is evaluated in exact integer arithmetic.

Usage:  python independent_r4_check.py path/to/four_capacity_runs.json
"""
import json
import sys
from fractions import Fraction

N_REF = 21_991_300      # indexing origin used by the witness file
SIDE = 21_987_409       # side of the square to be excluded
T = 35_000              # weight support
CLASSES = 12            # (diagonal color, completion color) pairs for four colors


def golomb_lower_spans(max_size, max_rank):
    """g[s] = proved lower bound on the span of an s-mark Golomb set."""
    g = [0, 0]
    for s in range(2, max_size + 1):
        best = g[s - 1] + 1                        # delete the largest mark
        for c in range(1, min(s - 1, max_rank) + 1):
            H = c * s - c * (c + 1) // 2           # differences of rank <= c
            ends = sum((c - i) * g[i + 1] for i in range(c))
            # 2 * (1 + 2 + ... + H) + 4 * ends <= L * c(c+1)
            num = H * (H + 1) + 4 * ends
            den = c * (c + 1)
            best = max(best, -(-num // den))
        g.append(best)
    return g


def make_Q(g):
    """Q(S) = largest s with g[s] <= S (g strictly increasing from index 1)."""
    import bisect
    def Q(S):
        if S < 0:
            raise ValueError("negative span requested")
        return bisect.bisect_right(g, S) - 1
    return Q


def binary_lower_spans(Q, max_size, max_rank):
    """e[s] = proved lower bound on the span of an s-mark binary-source set."""
    e = [0, 0]
    for s in range(2, max_size + 1):
        L = e[s - 1] + 1
        for c in range(1, min(s - 1, max_rank) + 1):
            H = c * s - c * (c + 1) // 2
            ends = sum((c - i) * e[i + 1] for i in range(c))
            while True:
                M = 2 * Q(L - 1)                   # uniform cap: two Golomb classes
                full, extra = divmod(H, M)
                P = M * full * (full + 1) // 2 + extra * (full + 1)
                if 2 * P + 4 * ends <= L * c * (c + 1):
                    break                          # span L not excluded at this rank
                L += 1
        e.append(L)
    return e


def check_run(Q, e, start, bound, rank):
    """Prove: a binary-source set of span <= N_REF-start-1 has at most `bound` marks."""
    L = N_REF - start - 1
    s = bound + 1
    c = rank
    assert 1 <= c < s
    H = c * s - c * (c + 1) // 2
    P = 0
    left = H
    h = 1
    while left > 0:
        assert L - h - 1 >= 0
        m = Q(L - h) + Q(L - h - 1)                # two Golomb classes, distinct minima
        take = min(m, left)
        P += take * h
        left -= take
        h += 1
    ends = sum((c - i) * e[i + 1] for i in range(c))
    return 2 * P + 4 * ends > L * c * (c + 1)


def autocorrelation_polynomial():
    def literal(d):
        return sum(i * (T + 1 - i) * (i + d) * (T + 1 - i - d) for i in range(1, T - d + 1))
    pts = [0, 1, 2, 3, 7, 100, 999, 5000, 12345, 20000, 30000, 34999]
    vals = [literal(d) for d in pts]
    # Lagrange interpolation through the first six points, check the other six.
    base = list(zip(pts[:6], vals[:6]))
    def interp(x):
        tot = Fraction(0)
        for i, (xi, yi) in enumerate(base):
            term = Fraction(yi)
            for j, (xj, _) in enumerate(base):
                if j != i:
                    term *= Fraction(x - xj, xi - xj)
            tot += term
        return tot
    for x, y in zip(pts[6:], vals[6:]):
        assert interp(x) == y, "a_d is not the degree-5 interpolant"
    def closed(d):
        m = T + 1 - d
        return Fraction(m * (m * m - 1) * (m * m + 1 + 5 * d * (T + 1)), 30)
    for x in pts:
        assert closed(x) == interp(x)
    # closed() and interp() are polynomials of degree <= 5 agreeing at 12 points,
    # hence identical; and interp() equals the literal a_d at 12 points, so the
    # degree-5 literal polynomial equals closed() on all of 0..T.
    return lambda d: int(closed(d))


def main(path):
    runs = json.load(open(path, encoding="utf-8"))
    g = golomb_lower_spans(4900, 130)
    assert g[4900] > N_REF
    Q = make_Q(g)
    e = binary_lower_spans(Q, max(r[2] for r in runs), 80)
    last = N_REF - SIDE + (T - 1) + (CLASSES - 1)
    caps = {}
    for k, (start, bound, rank) in enumerate(runs):
        end = runs[k + 1][0] - 1 if k + 1 < len(runs) else last
        assert check_run(Q, e, start, bound, rank), f"run at {start} not proved"
        for v in range(start, end + 1):
            caps[v] = bound
    assert runs[0][0] == 1 and all(v in caps for v in range(1, last + 1))
    a = autocorrelation_polynomial()
    off = N_REF - SIDE
    margin = -3 * SIDE * a(0)
    for d in range(1, T):
        U = sum(caps[off + d + j] for j in range(CLASSES))
        margin += 2 * (SIDE - d - 4 * U) * a(d)
    print(f"runs proved: {len(runs)}; lags: {T-1}; margin = {margin}")
    print("POSITIVE: square excluded" if margin > 0 else "NOT POSITIVE")
    return margin


if __name__ == "__main__":
    main(sys.argv[1])
