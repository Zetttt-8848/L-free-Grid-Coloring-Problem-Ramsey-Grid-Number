"""B0, second pass: hypothetical outer sensitivity with capacities RE-CERTIFIED
at the spans each target side actually needs (elementary chain only).

Status: HYPOTHETICAL. Nothing here is a bound on R_4. The only new
certificates are the binary-source caps K(L) at the listed spans. Each one is
proved by the same elementary rank-neighbor inequality as the PR 11 verifier
(FOUR_COLOR.md, "Large binary sources"), with exact integer arithmetic. The
Golomb table g and the small-set spans e_j are imported read-only from
verify_four_rank.py at commit 726998b9.

For a set with a properly two-colored strict source occupying L+1 consecutive
positions (span L), at internal distance h the multiplicity is at most
Q(L-h) + Q(L-h-1), where Q(x) = max{s : g_s <= x}. Size s is excluded if, for
some rank 1 <= c < s, with H = c s - c(c+1)/2,

    2 P(H; v) + 4 sum_{i<c} (c-i) e_{i+1}  >  L c (c+1).

Every larger size is then excluded too, by restriction. The cap K(L) = s-1 also
applies to every smaller span.

Outer use. Side n, shift d, completion class of rank j (0..11): it occupies at
most n-d-j consecutive positions, so its span is at most n-d-j-1. Shifts are
grouped in blocks of BLOCK. Every class in the block [d0, d0+BLOCK) is capped
by K(n-d0-1). This is valid but slightly weaker than the per-index profile.
"""
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
CERT = HERE.parents[1] / "boundary_certificates_20261115"
sys.path.insert(0, str(CERT))
import verify_four_rank as vr                        # noqa: E402  (read-only import)

G = vr.golomb_spans()
RANK_LO, RANK_HI = 300, 1400
E = vr.binary_spans(G, RANK_HI + 1)
T = 35_000
BLOCK = 500


def Q(x):
    return bisect_right(G, x) - 1


def corr(d, t=T):
    m = t + 1 - d
    return m * (m * m - 1) * (m * m + 1 + 5 * d * (t + 1)) // 30


A = [corr(d) for d in range(T)]
# Endpoint corrections C(c) = sum_{i<c} (c-i) e_{i+1}.
CORR = [0]
_run = 0
for c in range(1, RANK_HI + 1):
    _run += E[c]
    CORR.append(CORR[-1] + _run)


class Profile:
    def __init__(self, span, hmax=80_000):
        self.span = span
        cnt, mom = [0], [0]
        for h in range(1, hmax + 1):
            v = Q(span - h) + Q(span - h - 1)
            cnt.append(cnt[-1] + v)
            mom.append(mom[-1] + h * v)
        self.cnt, self.mom = cnt, mom

    def cheapest(self, H):
        f = bisect_right(self.cnt, H - 1)      # least f with cnt[f] >= H
        if f >= len(self.cnt):
            raise ValueError("profile too short")
        return self.mom[f - 1] + f * (H - self.cnt[f - 1])

    def excluded_rank(self, s):
        L = self.span
        for c in range(RANK_LO, min(RANK_HI, s - 1) + 1):
            H = c * s - c * (c + 1) // 2
            if 2 * self.cheapest(H) + 4 * CORR[c] > L * c * (c + 1):
                return c
        return None


def prove_cap(span, hint):
    """Return (K, rank) with size K+1 excluded at this span (rank verified)."""
    prof = Profile(span)
    lo, hi = hint - 3000, hint + 3000       # lo: not excluded (checked), hi: excluded
    assert prof.excluded_rank(hi) is not None
    while prof.excluded_rank(lo) is not None:
        lo -= 3000
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if prof.excluded_rank(mid) is not None:
            hi = mid
        else:
            lo = mid
    rank = prof.excluded_rank(hi)
    assert rank is not None
    return hi - 1, rank


_cache = {}


def cap(span, hint):
    if span not in _cache:
        _cache[span] = prove_cap(span, hint)
    return _cache[span]


def sums(n):
    raw = -3 * n * A[0]
    weighted = 0
    hint = 458_000
    block_caps = {}
    for d0 in range(1, T, BLOCK):
        k, _ = cap(n - d0 - 1, hint)
        hint = k
        block_caps[d0] = k
    for d in range(1, T):
        d0 = 1 + ((d - 1) // BLOCK) * BLOCK
        u = 12 * block_caps[d0]
        raw += 2 * (n - d - 4 * u) * A[d]
        weighted += u * A[d]
    return raw, weighted, block_caps


def main():
    # Sanity: reproduce the certified table caps at three indices (cap may be
    # larger here only by the rank-window restriction; it must never be smaller
    # than a valid profile would allow, and it is itself independently proved).
    rows = json.loads((CERT / "four_capacity_runs.json").read_text(encoding="utf-8"))
    checks = []
    for start, bound, _ in (rows[0], rows[300], rows[-1]):
        span = vr.REFERENCE_SIDE - start - 1
        k, r = cap(span, bound)
        checks.append({"index": start, "span": span, "table_cap": bound, "recertified_cap": k, "rank": r})
    sides = [21_987_409, 21_900_000, 21_800_000, 21_700_000, 21_600_000, 21_500_000,
             21_250_000, 21_000_000, 20_500_000, 20_000_000, 19_500_000]
    table = []
    for n in sides:
        raw, w, bc = sums(n)
        dstar = Fraction(max(0, -raw), 8 * w)
        table.append({"side": n, "raw_margin": raw, "delta_star": str(dstar),
                      "delta_star_float": float(dstar),
                      "relative_side_reduction": (21_987_409 - n) / 21_987_409,
                      "cap_at_largest_span": bc[1], "cap_at_smallest_block": bc[max(bc)]})
        print(f"side {n:>10}: raw {'+' if raw > 0 else '-'} delta* {float(dstar):.6g}  "
              f"rel. reduction {(21_987_409 - n) / 21_987_409:.5f}  K(n-2) {bc[1]}")
    caps = {str(s): {"cap": k, "rank": r} for s, (k, r) in sorted(_cache.items())}
    out = {"status": "HYPOTHETICAL sensitivity; only the listed caps are certified statements",
           "outer_window": {"t": T, "weights": "i(t+1-i)"}, "block": BLOCK,
           "table_reproduction": checks, "targets": table, "certified_caps": caps}
    (HERE / "b0_recertified_results.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    for c in checks:
        print("reproduction", c)


if __name__ == "__main__":
    main()
