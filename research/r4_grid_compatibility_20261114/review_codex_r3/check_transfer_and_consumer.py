"""Independent replay of Codex round 3, sections 2-4 (R4 <= 21,947,865).

Written separately from Codex's transfer.py and verify_numeric.py. It recomputes:

1. The hereditary binary-source lower spans e_s for s = 2..600. It uses the nonuniform
   multiplicity profile v_h(L) = Q(L-h) + Q(L-h-1), ranks c <= min(s-1, 80), and the
   finite seeds e_8>=8, e_10>=12, e_12>=16, e_15>=20. The spans are recomputed from
   the recursion, not audited from a stored list. The seeds are checked independently
   by check_finite_caps.py.
2. The improved local cap: min(old elementary cap, max{s : e_s <= n-1}).
3. The binary endpoint discrepancy, as an exact rational, and the check D >= 1097/5.
4. The 566 interval rows with saving 1097/5, using the inherited verify_profile, plus
   the full-square margin at n = 21,947,865, using the inherited outer_twenty and
   quartic correlations.

Inherited, already reviewed, read-only: research/boundary_certificates_20261115
(verify_four_rank.golomb_spans, verify_four_edges.local_cap / read_samples /
quartic_correlations, verify_four_window.load_window / verify_profile,
verify_four_double.sidon_length, verify_four_twenty.outer_twenty).

Usage: python check_transfer_and_consumer.py <codex_worktree_root>
"""
import json
import sys
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(sys.argv[1])
CERT = ROOT / "research" / "boundary_certificates_20261115"
CODEX = ROOT / "research" / "r4_local_capacity_round3_20261114"
sys.path.insert(0, str(CERT))
import verify_four_rank as vr          # noqa: E402
import verify_four_edges as ve         # noqa: E402
import verify_four_window as vw        # noqa: E402
import verify_four_double as vd        # noqa: E402
import verify_four_twenty as vt        # noqa: E402

SEEDS = {8: 8, 10: 12, 12: 16, 15: 20}
SMAX = 600
CMAX = 80


def lower_spans(g):
    Q = lambda x: 0 if x < 0 else bisect_right(g, x) - 1
    e = [0, 0]
    for s in range(2, SMAX + 1):
        L = max(e[-1] + 1, SEEDS.get(s, 0))
        # endpoint corrections C(c) = sum_{i<c} (c-i) e_{i+1}
        corr, run = [0], 0
        for c in range(1, min(s - 1, CMAX) + 1):
            run += e[c]
            corr.append(corr[-1] + run)
        while True:
            # cheapest-H prefix structure for span L
            cum, mom = [0], [0]
            excluded = False
            for c in range(1, len(corr)):
                H = c * s - c * (c + 1) // 2
                while cum[-1] < H and len(cum) <= L:
                    h = len(cum)
                    v = Q(L - h) + Q(L - h - 1)
                    cum.append(cum[-1] + v)
                    mom.append(mom[-1] + h * v)
                if cum[-1] < H:          # fewer than H available differences
                    excluded = True
                    break
                f = bisect_left(cum, H)
                price = mom[f - 1] + f * (H - cum[f - 1])
                if 2 * price + 4 * corr[c] > L * c * (c + 1):
                    excluded = True
                    break
            if not excluded:
                break
            L += 1
        e.append(L)
    return e


def main():
    g = vr.golomb_spans()
    e = lower_spans(g)
    rec = {"e_tail": e[-5:], "e_seeds": {s: e[s] for s in SEEDS}}
    # Compare with Codex's stored spans (consistency only, not a premise).
    tr = json.loads((CODEX / "transfer_results.json").read_text())
    stored = tr["variants"]["nonuniform_with_finite"]["binary_spans"]
    rec["spans_equal_codex"] = (stored[:len(e)] == e)
    rec["first_difference"] = next((s for s in range(min(len(e), len(stored))) if e[s] != stored[s]), None)

    def cap(n):
        return min(ve.local_cap(n, True), bisect_right(e, n - 1) - 1)

    den, r, alpha = vw.load_window(None)
    samples = ve.read_samples(None)
    b0, b1, p1, k0, step, _ = ve.BINARY
    rate = F(k0, 1) / (p1 + b1 * alpha)
    total = F(0)
    for end, i, j, *raw in samples:
        pr, gg, prior, h = map(F, raw)
        for lo in range(0, b0, step):
            hi = min(b0, lo + step)
            short = h - (prior * cap(b1) + gg * cap(hi)) / (b0 * rate)
            if short > 0:
                total += pr * (hi - lo) * short ** 2
    D = F(1097, 5)
    rec["D_float"] = float(total)
    rec["D_ge_1097_5"] = total >= D

    # Inner Golomb thresholds as in the inherited edge verifier.
    def inner_domain(k, p, b):
        ve.domain_check(ve.INNER, k, p, b)
    ve.variance_certificate(samples, alpha, ve.INNER, False)
    thresholds = [vd.sidon_length(k, den, r, alpha, ve.INNER[-1], inner_domain) for k in range(4600, 4801)]
    cr = json.loads((CODEX / "consumer_results.json").read_text())["finite_seeded"]
    rows = cr["rows"]
    for v, capv, b in rows:
        ve.domain_check(ve.BINARY, capv + 1, vw.REFERENCE - v, b)
    vw.verify_profile(rows, den, r, alpha, thresholds, D)
    rec["rows_verified"] = len(rows)
    a = ve.quartic_correlations(ve.WIDTH)
    n = 21_947_865
    count, raw, bonus, loss = vt.outer_twenty(rows, n, ve.WIDTH, lambda t, d: a[d])
    rec.update({"side": n, "blocks": count, "loss": loss, "margin": raw + bonus,
                "margin_positive": raw + bonus > 0,
                "margin_equals_codex": raw + bonus == int(cr["margin"])})
    print(json.dumps(rec, indent=1, default=str))
    Path(__file__).with_name("transfer_consumer_check.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
