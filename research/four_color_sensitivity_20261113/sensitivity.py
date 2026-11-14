"""Exact sensitivity of the four-color upper bound to a binary-source span coefficient.

Hypothesis H(q, Lmax): every finite integer set A with span L(A) <= Lmax whose
strict source V(A) admits a proper two-coloring satisfies M(A) <= q * L(A),
where M(A) = |A| * (|A| - 1) / 2.

Under H(q, n - 2), a proper four-coloring of the n by n square is impossible
whenever, for some integer t >= 1,

    a^2 t^2 > (l + t) * [a t + 6 * sum_{h=1}^{t-1} (t - h) * S_q(l - h)],

with a = ceil(n / 4), l = n - 1, and S_q(L) the largest integer s such that
s (s - 1) <= 2 q L.  See README.md for the derivation.  All arithmetic below is
exact integer arithmetic.  A positive margin is a certificate for one side n;
the searches that locate n and q are heuristics and claim no optimality.

The unconditional section replaces H by elementary capacity bounds obtained
from the same shift-count inequality.  It is a deliberately simple recomputation
used as a cross-check of scale, not a replacement for the stronger archived
certificate in exploration/research_round3/four/.
"""
import json
import sys
from math import isqrt
from pathlib import Path

ARCHIVED_UNCONDITIONAL = 21991300  # exploration/research_round3/four/R3_R4_REPORT.md


def cap_from_span(q, span):
    """Largest s with s(s-1) <= 2*q*span; span >= 0."""
    s = (1 + isqrt(1 + 8 * q * span)) // 2
    while s * (s - 1) > 2 * q * span:
        s -= 1
    while (s + 1) * s <= 2 * q * span:
        s += 1
    return s


def best_margin(n, q, t_max=None):
    """Return (margin, t) maximizing margin/t^2-free exact margin over 1 <= t <= t_max."""
    a = -(-n // 4)
    l = n - 1
    if t_max is None:
        t_max = max(2, n // 40)
    t_max = min(t_max, l + 1)
    p1 = 0  # sum_{h<t} S(l-h)
    p2 = 0  # sum_{h<t} h*S(l-h)
    best = None
    for t in range(1, t_max + 1):
        if t >= 2:
            h = t - 1
            s = cap_from_span(q, l - h)
            p1 += s
            p2 += h * s
        weighted = t * p1 - p2
        margin = a * a * t * t - (l + t) * (a * t + 6 * weighted)
        # compare margins normalized by t^2 without floats: keep the first positive
        # and the largest value of margin * best_t^2 versus best_margin * t^2
        if best is None or margin * best[1] * best[1] > best[0] * t * t:
            best = (margin, t)
    return best


def margin_at(n, q, t):
    a = -(-n // 4)
    l = n - 1
    weighted = sum((t - h) * cap_from_span(q, l - h) for h in range(1, t))
    return a * a * t * t - (l + t) * (a * t + 6 * weighted)


def least_tested_side(q, lo, hi):
    """Bisection on n assuming (unproved) monotonic sign; result is re-certified."""
    while lo < hi:
        mid = (lo + hi) // 2
        if best_margin(mid, q)[0] > 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def shift_cap(span, w):
    """Largest s with s^2 t <= (span+t)(s + w(t-1)) for every integer t in a scan.

    Any single t gives a valid necessary condition, so the minimum over a finite
    scan of t is a valid upper bound on the cardinality of a set of the given
    span whose difference multiplicities are all at most w.
    """
    best = None
    t = 1
    while t <= max(2, 4 * span):
        # largest s with s^2 t - (span+t) s - (span+t) w (t-1) <= 0
        b = span + t
        c = b * w * (t - 1)
        s = (b + isqrt(b * b + 4 * t * c)) // (2 * t)
        while s * s * t > b * (s + w * (t - 1)):
            s -= 1
        while (s + 1) * (s + 1) * t <= b * (s + 1 + w * (t - 1)):
            s += 1
        if best is None or s < best[0]:
            best = (s, t)
        t = t + 1 if t < 64 else t + max(1, t // 64)
    return best


def unconditional_chain(n):
    """Elementary three-level capacity chain at side n with uniform caps."""
    l = n - 1
    golomb, tg = shift_cap(l, 1)            # one Golomb class of span <= l
    binary, tb = shift_cap(l, 2 * golomb)   # set with properly 2-colored strict source
    ternary, tt = shift_cap(l, 3 * binary)  # set with properly 3-colored strict source
    a = -(-n // 4)
    return {"n": n, "golomb_cap": golomb, "binary_cap": binary,
            "ternary_cap": ternary, "needed": a, "excluded": ternary < a,
            "t": [tg, tb, tt]}


def main():
    out = {"hypothesis": "H(q, n-2): M(A) <= q*L(A) for properly 2-colorable strict sources of span <= n-2",
           "conditional_table": [], "notes": []}

    # 1. conditional table
    for q in (10, 21, 25, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 4500):
        guess = 4608 * q
        n = least_tested_side(q, max(8, guess // 2), 2 * guess + 4000)
        margin, t = best_margin(n, q)
        assert margin > 0 and margin == margin_at(n, q, t)
        below = best_margin(n - 1, q)[0]
        out["conditional_table"].append({
            "q": q, "certified_side": n, "t": t, "margin": margin,
            "span_range_needed": n - 2, "ratio_side_over_q": round(n / q, 3),
            "side_minus_one_scanned_margin_positive": below > 0})
        print(q, n, t, margin > 0, below > 0, flush=True)

    # 2. largest q in a bisection that still beats the archived unconditional bound
    target = ARCHIVED_UNCONDITIONAL - 1
    lo, hi = 1000, 6000
    assert best_margin(target, lo)[0] > 0 and best_margin(target, hi)[0] <= 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if best_margin(target, mid)[0] > 0:
            lo = mid
        else:
            hi = mid
    margin, t = best_margin(target, lo)
    assert margin == margin_at(target, lo, t) and margin > 0
    out["threshold"] = {"side": target, "largest_q_with_positive_margin": lo, "t": t,
                        "margin": margin, "first_q_without_scanned_certificate": hi}
    print("threshold", lo, t, flush=True)

    # 3. elementary unconditional cross-check of scale
    lo, hi = 10**6, 10**9
    assert unconditional_chain(hi)["excluded"] and not unconditional_chain(lo)["excluded"]
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if unconditional_chain(mid)["excluded"]:
            hi = mid
        else:
            lo = mid
    out["elementary_unconditional"] = unconditional_chain(hi)
    out["elementary_unconditional"]["archived_bound_for_comparison"] = ARCHIVED_UNCONDITIONAL
    print("elementary", out["elementary_unconditional"], flush=True)

    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
