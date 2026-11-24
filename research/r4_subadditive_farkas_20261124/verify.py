"""Independent exact standard-library verifier for R_4(L) <= 21,947,834.

Imports no third-party libraries and no project research modules. Reconstructs
the rational window correlations, coverage checks, Golomb bounds, nonuniform
and uniform binary-source span bounds, subadditive multi-bin Farkas dual
discrepancies (for both ordinary Golomb sets and proper binary strict sources),
inner Golomb thresholds, all 566 binary-source interval witnesses, the 26-shift
rank-weighted Lagrangian outer matching deficit (loss = 57), and the final
exact integer outer margin at side 21,947,834.
"""

import argparse
import hashlib
import json
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, groupby
from math import comb, isqrt
from pathlib import Path

WIDTHS = (4, 8, 12, 18, 24, 35, 50, 70, 100, 140, 200, 280, 400, 600, 850, 1200, 1800)
REF = 21_975_000


def need(ok, why):
    if not ok:
        raise ValueError(why)


def load_pinned_window(tables: Path, expected_hashes: dict):
    mats = {}
    for name in ("G.txt", "H.txt", "p.txt"):
        raw = (tables / name).read_bytes()
        need(hashlib.sha256(raw).hexdigest() == expected_hashes[name], f"SHA-256 mismatch for {name}")
        mats[name] = [[F(v) for v in line.split(",")] for line in raw.decode("ascii").splitlines()]
    G, H, (pi,) = mats["G.txt"], mats["H.txt"], mats["p.txt"]
    need(len(G) == 6 and len(H) == 6 and len(pi) == 6, "six window rows")
    need(sum(pi) == 1 and all(v > 0 for v in pi), "probability normalization")
    masses = [sum(row) for row in G]
    need(len(set(masses)) == 1 and masses[0] > 0, "equal row masses")
    m = len(G[0])
    need(m == 200 and all(len(row) == m for row in G) and all(len(row) == 3 * m for row in H), "window dimensions")
    # Verify all 401 coarse coverage alignments (shifts 0..2m):
    for shift in range(2 * m + 1):
        cov = F(0)
        for row_idx in range(6):
            cov += pi[row_idx] * sum(G[row_idx][i] * H[row_idx][shift + i] for i in range(m)) / masses[row_idx]
        need(cov >= 1, f"coarse coverage failed at shift {shift}")
    # Reconstruct exact rational correlations r_0..r_{m-1} and table excess alpha:
    r_frac = []
    for j in range(m):
        acc = F(0)
        for row_idx in range(6):
            acc += pi[row_idx] * sum(G[row_idx][i] * G[row_idx][i + j] for i in range(m - j)) / (masses[row_idx] ** 2)
        r_frac.append(acc)
    den = 1
    for v in r_frac:
        den = den * v.denominator // isqrt(1)  # compute exact LCM below
    from math import lcm
    den = lcm(*(v.denominator for v in r_frac))
    r = [int(v * den) for v in r_frac]
    need(min(r) >= 0 and 2 * sum(r) - r[0] == den, "correlation normalization")
    alpha = sum(pi[row_idx] * sum(v * v for v in H[row_idx]) for row_idx in range(6)) - 2 * m
    need(alpha > 0, "positive table excess")
    return G, H, pi, den, r, alpha


def golomb_bounds(limit=18000):
    g = [0, 0]
    for k in range(2, limit + 1):
        bound = g[k - 1] + 1
        endpoint = 0
        running = 0
        for c in range(1, min(130, k - 1) + 1):
            running += g[c]
            endpoint += running
            H = c * k - c * (c + 1) // 2
            num = H * (H + 1) + 4 * endpoint
            bound = max(bound, (num + c * (c + 1) - 1) // (c * (c + 1)))
        g.append(bound)
    return g


def audit_nonuniform_spans(bounds, g, seeds):
    need(bounds[:2] == [0, 0], "span initialization")
    need(g[-1] > bounds[-1], "Golomb sentinel")
    Q = lambda x: max(0, bisect_right(g, x) - 1)
    for k in range(2, len(bounds)):
        need(bounds[k] >= bounds[k - 1] + 1, "span monotonicity")
        start = max(bounds[k - 1] + 1, seeds.get(k, 0))
        need(bounds[k] >= start, "seed preservation")
        endpoint = [0]
        accum = 0
        for c in range(1, min(80, k - 1) + 1):
            accum += bounds[c]
            endpoint.append(endpoint[-1] + accum)
        for L in range(start, bounds[k]):
            totals = [0]
            costs = [0]
            for h in range(1, L + 1):
                v = Q(L - h) + Q(L - h - 1)
                totals.append(totals[-1] + v)
                costs.append(costs[-1] + h * v)
            rejected = False
            for c in range(1, len(endpoint)):
                H = c * k - c * (c + 1) // 2
                h = bisect_left(totals, H)
                if h == len(totals):
                    rejected = True
                    break
                price = costs[h - 1] + h * (H - totals[h - 1])
                if 2 * price + 4 * endpoint[c] > L * c * (c + 1):
                    rejected = True
                    break
            need(rejected, f"unjustified nonuniform span: size {k}, span {L}")


def extend_uniform_spans(bounds_prefix, g, limit):
    b = list(bounds_prefix)
    for size in range(len(b), limit + 1):
        lower = b[-1] + 1
        total = endpoints = 0
        for c in range(1, 81):
            total += b[c]
            endpoints += total
            H = c * size - c * (c + 1) // 2
            while True:
                cap = 2 * (bisect_right(g, lower - 1) - 1)
                q, rem = divmod(H, cap)
                cheapest = cap * q * (q + 1) // 2 + rem * (q + 1)
                if 2 * cheapest + 4 * endpoints <= lower * c * (c + 1):
                    break
                lower += 1
        b.append(lower)
    return b


@lru_cache(None)
def old_cap(n, binary):
    if n <= 0:
        return 0
    cap = n if binary else (1 + isqrt(8 * n - 7)) // 2
    gamma = 2 * old_cap(n, False) if binary else 1
    for w in WIDTHS:
        a = n + w - 1
        cap = min(cap, (a + isqrt(a * a + 4 * w * a * gamma * (w - 1))) // (2 * w))
    return cap


def verify_farkas_discrepancy(samples, G, H, pi, alpha, B0, B1, P1, K0, cap_fn, expected_D):
    lam_inv = F(P1 + B1 * alpha, K0 * B0)
    seen_row_side = set()
    total_nanos = 0
    for rec in samples:
        row_idx = rec["row"]
        side = int(bool(rec["reverse"]))
        need((row_idx, side) not in seen_row_side and 0 <= row_idx < 6, "duplicate or invalid row/side")
        seen_row_side.add((row_idx, side))
        mass = sum(G[row_idx])
        L_row = len(G[row_idx])
        seen_bins = set()
        row_nanos = 0
        for brec in rec["bins"]:
            j = brec["bin"]
            need(0 <= j < 150 and j not in seen_bins, "invalid or duplicate bin")
            seen_bins.add(j)
            if side == 0:
                g_vec = [G[row_idx][r] / mass for r in range(j + 1)]
                target = H[row_idx][j]
            else:
                g_vec = [G[row_idx][L_row - 1 - r] / mass for r in range(j + 1)]
                target = H[row_idx][-1 - j]
            # Verify Farkas dual certificate on prior bins 0..j-1:
            cov = [F(0)] * j
            prior_ub = F(0)
            for a, b, y_str in brec["prior_farkas"]:
                yv = F(y_str)
                need(0 <= a <= b < j and yv >= 0, "invalid Farkas interval or negative multiplier")
                for r in range(a, b + 1):
                    cov[r] += yv
                prior_ub += yv * cap_fn((b - a + 1) * B1)
            for r in range(j):
                need(cov[r] >= g_vec[r], f"Farkas coverage shortfall at row {row_idx} side {side} bin {j} r {r}")
            max_g = max(g_vec)
            bin_var = F(0)
            for q_k, grp in groupby(range(1, B0 + 1), key=cap_fn):
                grp_list = list(grp)
                kl, kr = grp_list[0], grp_list[-1]
                cnt = kr - kl + 1
                ub_val = min(prior_ub + g_vec[j] * q_k, max_g * cap_fn(j * B1 + kr))
                shortfall = target - lam_inv * ub_val
                if shortfall <= 0:
                    break
                bin_var += cnt * (shortfall ** 2)
            bin_nanos = (bin_var * pi[row_idx] * 10**9).__floor__()
            need(bin_nanos == brec["variance_floor_nanos"], "bin variance floor mismatch")
            row_nanos += bin_nanos
        need(row_nanos == rec["variance_floor_nanos"], "row variance floor mismatch")
        total_nanos += row_nanos
    need(F(total_nanos, 10**9) == expected_D, "total discrepancy mismatch")
    return F(total_nanos, 10**9)


def verify_inner_thresholds(thresholds, D_inn, den, r, alpha):
    need(len(thresholds) == 201, "201 inner Golomb thresholds")
    need(all(a < b for a, b in zip(thresholds, thresholds[1:])), "threshold strict monotonicity")
    for idx, k in enumerate(range(4600, 4801)):
        length = thresholds[idx]
        p = length - 1
        c = F((k - 1) * r[0], den)
        z = k * k * c / alpha
        center = isqrt(z.numerator // z.denominator) - c.numerator // c.denominator
        certified = False
        for B in range(max(15000, center - 4), min(16600, center + 4) + 1):
            if D_inn < p <= 22_500_000 and p - 1 >= 400 * B:
                if k * k > (p + B * alpha - D_inn) * (1 + c / B):
                    certified = True
                    break
        need(certified, f"unjustified inner threshold for k={k}, L={length}")


def verify_binary_rows(rows, D_bin, thresholds, den, r, alpha):
    need(all(a[0] < b[0] and a[1] >= b[1] for a, b in zip(rows, rows[1:])), "row ordering")
    Q = lambda p: 4599 + bisect_right(thresholds, p)
    rr = r + [0]
    for offset, cap, B in rows:
        p, k = REF - offset, cap + 1
        need(1720 <= B <= 1820 and D_bin < p <= 21_975_000 and k >= 455_000 and p - 1 >= 400 * B, "binary domain")
        need(thresholds[0] <= p - 200 * B and p < thresholds[-1], "Golomb table domain")
        blocks = [0]
        for j in range(200):
            blocks.append(blocks[-1] + B * (B + 1) // 2 * rr[j] + B * (B - 1) // 2 * rr[j + 1])

        def prefix(h):
            if h < 0:
                return 0
            j, t = divmod(h, B)
            if j >= 200:
                return blocks[-1]
            q = t + 1
            return blocks[j] + q * B * rr[j] + q * (q - 1) // 2 * (rr[j + 1] - rr[j])

        breaks = sorted({1, 200 * B} | {h for x in thresholds for h in (p - x, p - x + 1) if 1 < h < 200 * B})
        energy = k * B * r[0]
        for a, b in zip(breaks, breaks[1:]):
            v = Q(p - a) + Q(p - a - 1)
            need(v == Q(p - b + 1) + Q(p - b), "profile constant on interval")
            energy += 2 * v * (prefix(b - 1) - prefix(a - 1))
        need(k * k * den * B * B > (p + B * alpha - D_bin) * energy, f"binary witness failed at offset {offset}")


def quartic_correlations(T):
    a = [0, 5 * (T + 1) ** 3, (T + 1) ** 2, -12 * (T + 1), 6]
    out = []
    for d in range(T):
        n = T - d
        powers = [n]
        for j in range(1, 9):
            num = (n + 1) ** (j + 1) - 1 - sum(comb(j + 1, k) * powers[k] for k in range(j))
            need(num % (j + 1) == 0, "power sum divisibility")
            powers.append(num // (j + 1))
        shifted = [sum(a[j] * comb(j, k) * d ** (j - k) for j in range(k, 5)) for k in range(5)]
        out.append(sum(a[j] * shifted[k] * powers[j + k] for j in range(1, 5) for k in range(5)))
    need(all(x > y > 0 for x, y in zip(out, out[1:])), "decreasing positive correlation")
    return out


def verify_rank_weighted_outer_loss(S_blk, weights_prefix, weight_den):
    b = list(weights_prefix) + [weight_den] * max(0, S_blk - len(weights_prefix))
    need(len(b) >= S_blk, "weight length")
    b = b[:S_blk]
    need(0 <= b[0] and b[-1] <= weight_den and all(x <= y for x, y in zip(b, b[1:])), "monotone rank weights in [0, D]")
    rc = [0] + [sum(b[max(0, x - 3):x]) for x in range(1, S_blk + 1)]
    cc = [0] + [sum(weight_den - b[r] for r in range(x)) for x in range(1, S_blk + 1)]
    prev = {(0, 0, 0, 0): 0}
    for size in range(1, S_blk + 1):
        cur = {}
        for u in combinations_with_replacement(range(size + 1), 4):
            if sum(u) != size:
                continue
            bp = max(prev[tuple(sorted(u[:i] + (u[i] - 1,) + u[i + 1:]))] for i in range(4) if u[i])
            cur[u] = bp + rc[u[0]] + rc[u[1]] + rc[u[2]] + rc[u[3]] + max(cc[u[0]], cc[u[1]], cc[u[2]], cc[u[3]])
        prev = cur
    score_ub = max(prev.values()) // weight_den
    ordinary = sum(min(s, 12) for s in range(1, S_blk + 1))
    return ordinary - score_ub


def outer_margin(rows, n, T, weights, S_blk, loss_val):
    offset = REF - n
    need(rows[0][0] <= offset + 1 and rows[-1][0] >= offset + T + 10, "outer coverage")
    prefix = [0]
    for x in weights:
        prefix.append(prefix[-1] + x)
    raw = -3 * n * weights[0] + 2 * sum((n - d) * weights[d] for d in range(1, T))
    for i, (a, cap, _) in enumerate(rows):
        b = rows[i + 1][0] - 1 if i + 1 < len(rows) else offset + T + 11
        for j in range(12):
            lo = max(1, a - offset - j)
            hi = min(T - 1, b - offset - j)
            if lo <= hi:
                raw -= 8 * cap * (prefix[hi + 1] - prefix[lo])
    blocks = []
    bonus = 0
    for i in range(1, len(rows) - 1):
        a, cap, _ = rows[i]
        center = a - offset
        if (rows[i - 1][1] == cap + 1 and a - rows[i - 1][0] >= S_blk and rows[i + 1][0] - a >= 12
                and center - S_blk >= 1 and center - 1 < T):
            blocks.append(center)
            bonus += 8 * loss_val * min(weights[center - s] for s in range(1, S_blk + 1))
    need(all(b - a >= S_blk for a, b in zip(blocks, blocks[1:])), "disjoint outer blocks")
    return {"blocks": len(blocks), "raw": raw, "bonus": bonus, "loss": loss_val, "margin": raw + bonus}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--window", type=Path, required=True, help="path to pinned upstream asymptotic directory")
    args = parser.parse_args()
    cert = json.loads(Path(__file__).with_name("certificate.json").read_bytes())

    G, H, pi, den, r, alpha = load_pinned_window(args.window.resolve(), cert["rational_window_inputs"])
    print("PASS: Pinned rational window matrices, 401 coarse coverage alignments, and correlations.", flush=True)

    gol = golomb_bounds(cert["uniform_span_limit"])
    seeds = {int(k): v for k, v in cert["seeds"].items()}
    audit_nonuniform_spans(cert["binary_spans_600"], gol[:601], seeds)
    b_spans = extend_uniform_spans(cert["binary_spans_600"], gol, cert["uniform_span_limit"])
    need(b_spans[-1] == cert["binary_span_18000"], "extended binary span sentinel mismatch")
    print(f"PASS: Audited 600 nonuniform and {len(b_spans) - 601:,} uniform binary-source spans (max span {b_spans[-1]:,}).", flush=True)

    def cap_bin(u):
        v = old_cap(u, True)
        return min(v, bisect_right(b_spans, u - 1) - 1) if u <= b_spans[-1] else v

    def cap_inn(u):
        v = old_cap(u, False)
        return min(v, bisect_right(gol, u - 1) - 1) if u <= gol[-1] else v

    D_inn = verify_farkas_discrepancy(
        cert["inner_farkas_samples"], G, H, pi, alpha, 15000, 16600, 22_500_000, 4600,
        cap_inn, F(cert["inner_discrepancy_lower_bound"]),
    )
    D_bin = verify_farkas_discrepancy(
        cert["binary_farkas_samples"], G, H, pi, alpha, 1720, 1820, 21_975_000, 455_000,
        cap_bin, F(cert["binary_discrepancy_lower_bound"]),
    )
    print(f"PASS: Subadditive Farkas discrepancies D_inn = {D_inn} ({float(D_inn):.9f}), D_bin = {D_bin} ({float(D_bin):.9f}).", flush=True)

    verify_inner_thresholds(cert["inner_thresholds"], D_inn, den, r, alpha)
    verify_binary_rows(cert["rows"], D_bin, cert["inner_thresholds"], den, r, alpha)
    print(f"PASS: Verified 201 inner Golomb thresholds and {len(cert['rows'])} binary-source interval witnesses.", flush=True)

    loss_val = verify_rank_weighted_outer_loss(
        cert["outer_shift_block"], cert["outer_rank_weights_num"], cert["outer_rank_weights_den"]
    )
    need(loss_val == cert["outer_block_loss"], "outer block loss mismatch")
    weights = quartic_correlations(cert["width"])
    res_hi = outer_margin(cert["rows"], cert["side"], cert["width"], weights, cert["outer_shift_block"], loss_val)
    res_lo = outer_margin(cert["rows"], cert["side"] - 1, cert["width"], weights, cert["outer_shift_block"], loss_val)
    need(res_hi == cert["result"] and res_hi["margin"] > 0, "final positive margin mismatch")
    need(res_lo == cert["preceding_side_result"] and res_lo["margin"] < 0, "preceding side margin mismatch")
    print(f"PASS: 26-shift rank-weighted loss = {loss_val}; CERTIFIED R_4(L) <= {cert['side']:,} (margin = +{res_hi['margin']:,}).", flush=True)


if __name__ == "__main__":
    main()
