"""B0: exact, explicitly HYPOTHETICAL sensitivity of the outer four-color count.

Nothing computed here is a bound on R_4. Every figure is conditional on the
hypothesis H(delta) stated below. The original certificates are not modified:
the PR 11 verifiers are imported read-only from
research/boundary_certificates_20261115 at commit 726998b9.

Outer inequality (FOUR_COLOR.md, FOUR_COLOR_WINDOW.md). For an outer window
with nonnegative correlations a_d (0 <= d < t), and for any certified upper
bound X_d on the number of equal-colored main-diagonal pairs at shift d
(summed over the four colors), every four-coloring of the n x n square satisfies

    -3 n a_0 + 2 sum_{d=1}^{t-1} (n - d - 4 X_d) a_d <= 0.

A positive left side therefore excludes the side n.

Baseline: X_d = U_d(n) = sum_{j=0}^{11} K(n - d - j) (distinct-minima staggering
of the twelve completion classes).

Hypothesis H(delta), 0 <= delta < 1 rational: for every shift d in the window,
the twelve classes satisfy  sum_{c,e} |S_{c,e}(d)| <= (1 - delta) U_d(n).
The margin is then linear in delta:

    M(n, delta) = raw(n) + 8 delta sum_d U_d(n) a_d.

The equivalent per-shift additive form H'(Delta), X_d = U_d - Delta, gives
M = raw(n) + 8 Delta sum_d a_d.

Capacity tables. K is read from the certified rows. A row of the elementary
table at index i bounds every binary-source set in at most REF - i - 1
positions (and all shorter ones). The rows also apply beyond the last tabulated
index (shorter spans), because the capacity is monotone in the span. This
overstates K for sides well below the certified side, so delta* computed there
is an upper estimate of the delta actually needed. We report how far each
target lies outside the tabulated index range.

The twenty-shift correction of the window chain also reduces X_d. It and H(delta)
charge the same starts, so they are NOT added. We report the existing
correction as an equivalent delta for comparison, and we evaluate H(delta)
against the raw distinct-minima baseline only.
"""
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CERT = HERE.parents[1] / "boundary_certificates_20261115"
sys.path.insert(0, str(CERT))

import verify_four_edges as edges          # noqa: E402  (read-only import)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Chain:
    def __init__(self, name, ref, starts, caps, kernel, width, certified, certified_margin):
        self.name, self.ref, self.starts, self.caps = name, ref, starts, caps
        self.a, self.t = kernel, width
        self.certified, self.certified_margin = certified, certified_margin

    def cap(self, index):
        if index < self.starts[0]:
            raise ValueError(f"{self.name}: index {index} precedes the certified table")
        return self.caps[bisect_right(self.starts, index) - 1]

    def last_index_needed(self, n):
        return self.ref - n + (self.t - 1) + 11

    def sums(self, n):
        """Return raw(n) and W(n) = sum_d U_d(n) a_d, exactly."""
        off = self.ref - n
        lo, hi = off + 1, off + self.t - 1 + 11
        k = [self.cap(i) for i in range(lo, hi + 1)]
        pref = [0]
        for x in k:
            pref.append(pref[-1] + x)
        raw = -3 * n * self.a[0]
        weighted = 0
        for d in range(1, self.t):
            u = pref[d + 11] - pref[d - 1]   # caps at indices off+d .. off+d+11
            raw += 2 * (n - d - 4 * u) * self.a[d]
            weighted += u * self.a[d]
        return raw, weighted

    def delta_star(self, n):
        raw, w = self.sums(n)
        return Fraction(max(0, -raw), 8 * w), raw, w

    def delta_additive_star(self, n):
        raw, _ = self.sums(n)
        s = sum(self.a[1:self.t])
        return Fraction(max(0, -raw), 8 * s)

    def margin(self, n, delta):
        raw, w = self.sums(n)
        return raw + 8 * delta * w

    def hypothetical_bound(self, delta, lo):
        """Least n in (lo, certified] found by bisection with M(n,delta) > 0."""
        hi = self.certified
        if self.margin(hi, delta) <= 0:
            return None
        if self.margin(lo, delta) > 0:
            return ("<=", lo)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.margin(mid, delta) > 0:
                hi = mid
            else:
                lo = mid
        assert self.margin(hi, delta) > 0 and self.margin(hi - 1, delta) <= 0
        return ("=", hi)


def elementary_chain():
    rows = json.loads((CERT / "four_capacity_runs.json").read_text(encoding="utf-8"))
    t = 35_000

    def corr(d):
        m = t + 1 - d
        return m * (m * m - 1) * (m * m + 1 + 5 * d * (t + 1)) // 30
    a = [corr(d) for d in range(t)]
    return Chain("elementary (FOUR_COLOR.md)", 21_991_300,
                 [r[0] for r in rows], [r[1] for r in rows], a, t,
                 21_987_409, 2_727_455_661_705_377_936_113_840)


def window_chain():
    rows = json.loads((CERT / "four_edge_runs.json").read_text(encoding="utf-8"))
    t = edges.WIDTH
    a = edges.quartic_correlations(t)
    return Chain("window (FOUR_COLOR_EDGE_VARIANCE.md)", edges.REFERENCE,
                 [r[0] for r in rows], [r[1] for r in rows], a, t,
                 edges.SIDE,
                 903_981_917_166_788_568_505_391_154_986_854_794_983_918_064)


def fmt(fr, digits=6):
    return f"{float(fr):.{digits}g}"


def report():
    out = {"status": "HYPOTHETICAL sensitivity; not a bound", "inputs": {}, "chains": []}
    for f in ("four_capacity_runs.json", "four_edge_runs.json",
              "verify_four_rank.py", "verify_four_edges.py"):
        out["inputs"][f] = sha256(CERT / f)
    deltas = [Fraction(1, 10000), Fraction(1, 1000), Fraction(1, 200), Fraction(1, 100),
              Fraction(1, 50), Fraction(1, 20), Fraction(1, 10)]
    for chain in (elementary_chain(), window_chain()):
        rec = {"chain": chain.name, "certified_side": chain.certified, "width": chain.t,
               "table_last_index": chain.starts[-1]}
        raw0, w0 = chain.sums(chain.certified)
        rec["raw_margin_at_certified_side"] = raw0
        if chain.name.startswith("window"):
            assert raw0 == -8994733962487986521984660222886550382497049520, \
                "window raw baseline reproduction"
            bonus = chain.certified_margin - raw0
            rec["existing_twenty_shift_correction"] = bonus
            rec["existing_correction_as_equivalent_delta"] = str(Fraction(bonus, 8 * w0))
            rec["existing_correction_as_equivalent_delta_float"] = fmt(Fraction(bonus, 8 * w0))
        else:
            assert raw0 == chain.certified_margin, "elementary margin reproduction"
        targets = [chain.certified - 1, chain.certified - 1000, 21_900_000,
                   21_800_000, 21_500_000, 21_000_000]
        rows = []
        for n in targets:
            ds, raw, w = chain.delta_star(n)
            rows.append({"side": n, "raw_margin": raw,
                         "delta_star": str(ds), "delta_star_float": fmt(ds),
                         "additive_starts_per_shift_star": fmt(chain.delta_additive_star(n)),
                         "mean_U_d": fmt(Fraction(w, sum(chain.a[1:chain.t]))),
                         "indices_beyond_table": max(0, chain.last_index_needed(n) - chain.starts[-1])})
        rec["targets"] = rows
        bounds = []
        for dl in deltas:
            b = chain.hypothetical_bound(dl, lo=15_000_000)
            bounds.append({"delta": str(dl), "least_side_with_positive_margin": b,
                           "gain": None if b is None or b[0] != "=" else chain.certified - b[1]})
        rec["hypothetical_bounds"] = bounds
        out["chains"].append(rec)
    return out


if __name__ == "__main__":
    result = report()
    (HERE / "b0_results.json").write_text(json.dumps(result, indent=1, default=str) + "\n",
                                           encoding="utf-8")
    for rec in result["chains"]:
        print(rec["chain"], "certified side", rec["certified_side"])
        if "existing_correction_as_equivalent_delta_float" in rec:
            print("  existing twenty-shift correction as equivalent delta:",
                  rec["existing_correction_as_equivalent_delta_float"])
        for r in rec["targets"]:
            print(f"  side {r['side']:>10}: delta* {r['delta_star_float']:>10}  "
                  f"additive* {r['additive_starts_per_shift_star']:>10}  "
                  f"mean U_d {r['mean_U_d']}  beyond table {r['indices_beyond_table']}")
        for b in rec["hypothetical_bounds"]:
            print(f"  H(delta={b['delta']}): least side {b['least_side_with_positive_margin']}, gain {b['gain']}")
