"""Discriminating check: Fejer single-class cap (proof.md Cor. 4.3, sharper form with
the full profile v_l) against Codex's certified binary caps (round 3 consumer rows).

Both use the same certified Golomb lower spans g_s (verify_four_rank.golomb_spans),
Q(L) = max{s : g_s <= L}, v_l(S) = Q(S-l) + Q(S-l-1). For a binary source of span <= S:
  s^2 Lambda^2 / N <= s Lambda + 2 sum_{l<=lam} (Lambda-l) v_l,  Lambda = lam+1, N = S+Lambda
(Lemma 4.2 with r(l) <= v_l). The bound is the positive root, minimised over lam.
A row (i, K, b) of consumer_results.json bounds sets in REFERENCE - i - 1 positions,
i.e. span <= REFERENCE - i - 2.
Usage: python fejer_vs_rank.py <path to consumer_results.json>
"""
import json, math, sys
from bisect import bisect_right
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "boundary_certificates_20261115"))
import verify_four_rank as vr  # noqa: E402

REFERENCE = 21_975_000
g = vr.golomb_spans()

def Q(L):
    return 0 if L < 0 else bisect_right(g, L) - 1

def fejer(S, lam_grid):
    best = None
    for lam in lam_grid:
        Lam = lam + 1
        N = S + Lam
        # Q is a step function; evaluate sum exactly in O(lam)
        tot = sum((Lam - l) * (Q(S - l) + Q(S - l - 1)) for l in range(1, lam + 1))
        a = Lam * Lam / N
        s = (Lam + math.sqrt(Lam * Lam + 8 * a * tot)) / (2 * a)
        if best is None or s < best[0]:
            best = (s, lam)
    return best

rows = json.loads(Path(sys.argv[1]).read_text())["finite_seeded"]["rows"]
out = []
for i, K, b in (rows[0], rows[len(rows) // 2], rows[-1]):
    S = REFERENCE - i - 2
    coarse = fejer(S, range(10000, 120001, 5000))
    lo = max(1000, coarse[1] - 5000)
    fine = fejer(S, range(lo, coarse[1] + 5001, 250))
    out.append({"index": i, "span": S, "Q(S)": Q(S), "v_1": Q(S - 1) + Q(S - 2),
                "codex_cap_K": K, "fejer_cap": round(fine[0], 1), "best_lambda": fine[1],
                "fejer_minus_K_rel": round(fine[0] / K - 1, 5)})
    print(out[-1], flush=True)
(HERE / "fejer_vs_rank.json").write_text(json.dumps(out, indent=1) + "\n")
