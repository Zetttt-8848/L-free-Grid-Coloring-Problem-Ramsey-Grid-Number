"""Standalone standard-library exact verifier for R_4(L) <= 21,947,830.

Independently reconstructs and checks, from first principles with no research
module imports:
  1. Optional exact rational window correlations, table excess, and all 401
     coarse coverage alignments from the pinned upstream matrices (G, H, p).
  2. Ordinary Golomb lower spans through 18,000 marks and binary-source lower
     spans (600 nonuniform seeded + uniform extension through 18,000 marks).
  3. Joint contiguous multi-bin + partial-bin subadditive Farkas dual
     certificates for both inner Golomb discrepancy D_inn and binary-source
     discrepancy D_bin across all 12 oriented window rows and 150 edge bins.
  4. All 201 strengthened inner Golomb span thresholds (4,600 <= k <= 4,800)
     and all 566 staggered binary-source capacity witnesses.
  5. Complete 441-partition histogram-stratified rank-split Lagrangian outer
     matching certificates proving >= 75 missing matches per 35-shift drop
     block (plus the 20-shift recurrence proving >= 41 missing matches on the
     single boundary block), pairwise block disjointness, and the exact
     integer contradiction margin at side 21,947,830.
"""

import argparse
import hashlib
import json
import lzma
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASELINE = HERE.parent / "boundary_certificates_20261115"
WIDTHS = (4, 8, 12, 18, 24, 35, 50, 70, 100, 140, 200, 280, 400, 600, 850, 1200, 1800)
REF = 21_975_000
T = 35_990


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def golomb_bounds(limit=18_000):
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


def extend_and_audit_uniform_spans(prefix_bounds, g, limit):
    spans = list(prefix_bounds)
    Q = lambda x: max(0, bisect_right(g, x) - 1)
    for k in range(len(spans), limit + 1):
        lower = spans[-1] + 1
        total = endpoints = 0
        for rnk in range(1, 81):
            total += spans[rnk]
            endpoints += total
            pairs = rnk * k - rnk * (rnk + 1) // 2
            while True:
                cap = 2 * Q(lower - 1)
                need(cap > 0, "positive uniform Golomb cap")
                full, extra = divmod(pairs, cap)
                cheapest = cap * full * (full + 1) // 2 + extra * (full + 1)
                if 2 * cheapest + 4 * endpoints <= lower * rnk * (rnk + 1):
                    break
                lower += 1
        spans.append(lower)
    need(g[-1] > spans[-1], "extended Golomb sentinel")
    return spans


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


def load_and_verify_window(tables_dir, expected_hashes):
    win = json.loads((BASELINE / "four_window_correlations.json").read_text())
    den = int(win["denominator"])
    r = list(map(int, win["correlations"]))
    alpha = F(win["table_excess"])
    need(len(r) == 200 and min(r) >= 0 and 2 * sum(r) - r[0] == den and alpha > 0, "window normalization")

    if tables_dir is None:
        return den, r, alpha, None, None, None

    tables = tables_dir.resolve()
    mats = {}
    for name in ("G", "H", "p"):
        path = tables / f"{name}.txt"
        raw = path.read_bytes()
        need(hashlib.sha256(raw).hexdigest() == expected_hashes[path.name], f"SHA-256 mismatch on {path.name}")
        mats[name] = [[F(v) for v in line.split(",")] for line in raw.decode("ascii").splitlines()]
    G, H, (pi,) = mats["G"], mats["H"], mats["p"]
    need(len(G) == len(H) == len(pi) == 6 and sum(pi) == 1 and all(x > 0 for x in pi), "row probabilities")
    m = 200
    for j in range(6):
        need(len(G[j]) == m and len(H[j]) == 3 * m and all(x >= 0 for x in G[j]) and all(x >= 0 for x in H[j]), "matrix dimensions")

    # Verify coarse correlations r[0..199] and table_excess alpha from G, H, p
    masses = [sum(row) for row in G]
    for d in range(m):
        exp_corr = sum(pi[j] * sum(G[j][i] * G[j][i + d] for i in range(m - d)) / (masses[j] ** 2) for j in range(6))
        need(exp_corr == F(r[d], den), f"window correlation mismatch at shift {d}")
    exp_alpha = sum(pi[j] * sum(x * x for x in H[j]) for j in range(6)) - 2 * m
    need(exp_alpha == alpha, "window table_excess mismatch")

    # Verify all 401 coarse coverage alignments >= 1
    for shift in range(2 * m + 1):
        cov = sum(pi[j] * sum(G[j][i] * H[j][shift + i] for i in range(m)) / masses[j] for j in range(6))
        need(cov >= 1, f"window coverage failed at alignment {shift}")

    return den, r, alpha, G, H, pi


def verify_farkas_discrepancy(samples, G, H, pi, B0, B1, P1, K0, alpha, cap_fn):
    lam_inv = F(P1 + B1 * alpha, K0 * B0)
    need(len(samples) == 12, "expected 12 oriented window rows")
    seen_rows = set()
    total_nanos = 0

    for entry in samples:
        row_idx = entry["row"]
        rev = bool(entry["reverse"])
        need(0 <= row_idx < 6 and (row_idx, rev) not in seen_rows, "duplicate row sample")
        seen_rows.add((row_idx, rev))
        mass = sum(G[row_idx])
        L_row = len(G[row_idx])

        row_nanos = 0
        seen_bins = set()
        for b_entry in entry["bins"]:
            j = b_entry["bin"]
            need(0 <= j < 150 and j not in seen_bins, "invalid or duplicate bin")
            seen_bins.add(j)
            if not rev:
                g_vec = [G[row_idx][r] / mass for r in range(j + 1)]
                target = H[row_idx][j]
            else:
                g_vec = [G[row_idx][L_row - 1 - r] / mass for r in range(j + 1)]
                target = H[row_idx][-1 - j]

            bin_var = F(0)
            prev_kr = 0
            for kl, kr, mults in b_entry["blocks"]:
                need(type(kl) is int and type(kr) is int and prev_kr < kl <= kr <= B0, "non-disjoint or out-of-range k block")
                prev_kr = kr
                cov = [F(0)] * (j + 1)
                ub_val = F(0)
                for a, b, y_str in mults:
                    need(type(a) is int and type(b) is int and 0 <= a <= b <= j, "bad Farkas interval")
                    yv = F(y_str)
                    need(yv >= 0, "negative Farkas multiplier")
                    for r_pos in range(a, b + 1):
                        cov[r_pos] += yv
                    span_len = (b - a + 1) * B1 if b < j else (j - a) * B1 + kr
                    ub_val += yv * cap_fn(span_len)
                for r_pos in range(j + 1):
                    need(cov[r_pos] >= g_vec[r_pos], f"Farkas dual under-covers position {r_pos} at row {row_idx} bin {j}")
                shortfall = target - lam_inv * ub_val
                if shortfall > 0:
                    bin_var += (kr - kl + 1) * (shortfall ** 2)
            row_nanos += (bin_var * pi[row_idx] * 10**9).__floor__()

        need(row_nanos == entry["variance_floor_nanos"], f"row nanos mismatch on {(row_idx, rev)}")
        total_nanos += row_nanos

    return F(total_nanos, 10**9)


def verify_inner_thresholds(lengths, D_inn, den, r, alpha):
    need(len(lengths) == 201 and all(a < b for a, b in zip(lengths, lengths[1:])), "inner threshold monotonicity")
    for idx, k in enumerate(range(4600, 4801)):
        length = lengths[idx]
        p = length - 1
        c = F((k - 1) * r[0], den)
        z = k * k * c / alpha
        center = isqrt(z.numerator // z.denominator) - c.numerator // c.denominator
        certified = False
        for B in range(max(15000, center - 6), min(16600, center + 6) + 1):
            if D_inn < p <= 22_500_000 and p - 1 >= 400 * B and k * k > (p + B * alpha - D_inn) * (1 + c / B):
                certified = True
                break
        need(certified, f"inner threshold unverified at k={k}, length={length}")


def audit_rows(rows, D_bin, lengths, den, r, alpha):
    need(all(a[0] < b[0] and a[1] >= b[1] for a, b in zip(rows, rows[1:])), "row order")
    Q = lambda p: 4599 + bisect_right(lengths, p)
    rr = r + [0]
    blocks_by_B = {}
    for offset, cap, B in rows:
        p, k = REF - offset, cap + 1
        need(1720 <= B <= 1820 and D_bin < p <= 21_975_000 and k >= 455_000 and p - 1 >= 400 * B, "binary domain")
        need(lengths[0] <= p - 200 * B and p < lengths[-1], "Golomb table domain")
        if B not in blocks_by_B:
            bl = [0]
            for j in range(200):
                bl.append(bl[-1] + B * (B + 1) // 2 * rr[j] + B * (B - 1) // 2 * rr[j + 1])
            blocks_by_B[B] = bl
        blocks = blocks_by_B[B]

        def prefix(h):
            if h < 0:
                return 0
            j, t = divmod(h, B)
            if j >= 200:
                return blocks[-1]
            q = t + 1
            return blocks[j] + q * B * rr[j] + q * (q - 1) // 2 * (rr[j + 1] - rr[j])

        breaks = sorted({1, 200 * B} | {h for x in lengths for h in (p - x, p - x + 1) if 1 < h < 200 * B})
        energy = k * B * r[0]
        for a, b in zip(breaks, breaks[1:]):
            v = Q(p - a) + Q(p - a - 1)
            need(v == Q(p - b + 1) + Q(p - b), "profile constant on interval")
            energy += 2 * v * (prefix(b - 1) - prefix(a - 1))
        need(k * k * den * B * B > (p + B * alpha - D_bin) * energy, f"binary witness failed at offset {offset}")


def verify_stratified_outer_loss(S, D, target_loss, part_certs):
    expected_parts = [
        [n0, n1, n2, S - n0 - n1 - n2]
        for n0 in range(S // 4 + 1)
        for n1 in range(n0, (S - n0) // 3 + 1)
        for n2 in range(n1, (S - n0 - n1) // 2 + 1)
    ]
    need([entry["partition"] for entry in part_certs] == expected_parts, "incomplete 4-partition coverage")
    allow = sum(min(s, 12) for s in range(1, S + 1))

    for entry in part_certs:
        n0, n1, n2, n3 = n_tup = entry["partition"]
        b_int = entry["weights"]
        need(len(b_int) == 4 and [len(v) for v in b_int] == n_tup, "bad weight lengths")
        for v in b_int:
            need(all(type(x) is int and 0 <= x <= D for x in v), "weight out of [0, D]")
            need(all(x <= y for x, y in zip(v, v[1:])), "weights not nondecreasing")

        rc = [[0] + [sum(b_int[c][max(0, x - 3) : x]) for x in range(1, n_tup[c] + 1)] for c in range(4)]
        cc = [[0] + [sum(D - b_int[c][r] for r in range(x)) for x in range(1, n_tup[c] + 1)] for c in range(4)]
        s1, s2, s3 = n1 + 1, n2 + 1, n3 + 1
        stride0 = s1 * s2 * s3
        stride1 = s2 * s3
        stride2 = s3
        dp = [0] * ((n0 + 1) * stride0)
        for h0 in range(n0 + 1):
            r0, c0 = rc[0][h0], cc[0][h0]
            base0 = h0 * stride0
            for h1 in range(n1 + 1):
                r01 = r0 + rc[1][h1]
                c01 = c0 if c0 >= cc[1][h1] else cc[1][h1]
                base1 = base0 + h1 * stride1
                for h2 in range(n2 + 1):
                    r012 = r01 + rc[2][h2]
                    c012 = c01 if c01 >= cc[2][h2] else cc[2][h2]
                    base2 = base1 + h2 * stride2
                    for h3 in range(n3 + 1):
                        if (h0 | h1 | h2 | h3) == 0:
                            continue
                        idx = base2 + h3
                        bp = -1
                        if h0 and dp[idx - stride0] > bp: bp = dp[idx - stride0]
                        if h1 and dp[idx - stride1] > bp: bp = dp[idx - stride1]
                        if h2 and dp[idx - stride2] > bp: bp = dp[idx - stride2]
                        if h3 and dp[idx - 1] > bp: bp = dp[idx - 1]
                        c_all = c012 if c012 >= cc[3][h3] else cc[3][h3]
                        dp[idx] = bp + r012 + rc[3][h3] + c_all
        proved = allow - dp[-1] // D
        need(proved == entry["loss"] and proved >= target_loss, f"stratified loss failed on {n_tup}")


def verify_uniform_rank_loss(S, D, prefix_w, target_loss):
    b_int = list(prefix_w) + [D] * (S - len(prefix_w))
    need(len(b_int) == S and all(0 <= x <= y <= D for x, y in zip(b_int, b_int[1:])), "bad uniform rank weights")
    rc = [0] + [sum(b_int[max(0, x - 3) : x]) for x in range(1, S + 1)]
    cc = [0] + [sum(D - b_int[r] for r in range(x)) for x in range(1, S + 1)]
    prev = {(0, 0, 0, 0): 0}
    for size in range(1, S + 1):
        cur = {}
        for u in combinations_with_replacement(range(size + 1), 4):
            if sum(u) != size:
                continue
            bp = max(prev[tuple(sorted(u[:i] + (u[i] - 1,) + u[i + 1 :]))] for i in range(4) if u[i])
            cur[u] = bp + rc[u[0]] + rc[u[1]] + rc[u[2]] + rc[u[3]] + max(cc[u[0]], cc[u[1]], cc[u[2]], cc[u[3]])
        prev = cur
    loss = sum(min(s, 12) for s in range(1, S + 1)) - max(prev.values()) // D
    need(loss == target_loss, f"uniform rank loss mismatch: {loss} vs {target_loss}")


def twenty_loss():
    prev = {(0, 0, 0, 0): 0}
    for size in range(1, 21):
        cur = {}
        for u in combinations_with_replacement(range(size + 1), 4):
            if sum(u) != size:
                continue
            bp = max(prev[tuple(sorted(u[:i] + (u[i] - 1,) + u[i + 1 :]))] for i in range(4) if u[i])
            cur[u] = bp + max(u) + sum(min(3, x) for x in u)
        prev = cur
    need(max(prev.values()) == 267, "twenty-step maximum")
    return sum(min(s, 12) for s in range(1, 21)) - 267 // 2


def correlations():
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


def outer_multiscale(rows, n, weights, tiers):
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
    intervals = []
    bonus = 0
    tier_counts = {str(s): 0 for s, _ in tiers}
    for i in range(1, len(rows) - 1):
        a, cap, _ = rows[i]
        center = a - offset
        if rows[i - 1][1] != cap + 1 or rows[i + 1][0] - a < 12 or center - 1 >= T:
            continue
        gap_prev = a - rows[i - 1][0]
        for s_len, l_val in tiers:
            if gap_prev >= s_len and center - s_len >= 1:
                if not intervals or center - s_len > intervals[-1][1]:
                    intervals.append((center - s_len, center - 1))
                    bonus += 8 * l_val * min(weights[center - s] for s in range(1, s_len + 1))
                    tier_counts[str(s_len)] += 1
                    break
    need(all(x[1] < y[0] for x, y in zip(intervals, intervals[1:])), "disjoint outer blocks")
    return {"blocks": len(intervals), "tier_counts": tier_counts, "raw": raw, "bonus": bonus, "margin": raw + bonus}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--window", type=Path, help="path to pinned upstream asymptotic window matrices (G.txt, H.txt, p.txt)")
    args = parser.parse_args()

    cert_path = HERE / "certificate.json.xz"
    data = json.loads(lzma.decompress(cert_path.read_bytes()))
    need(data["width"] == T, "unexpected outer width")

    den, r, alpha, G, H, pi = load_and_verify_window(args.window, data["rational_window_inputs"])

    gol = golomb_bounds(data["uniform_span_limit"])
    seeds = {int(k): v for k, v in data["seeds"].items()}
    need(len(data["binary_spans_600"]) == data["nonuniform_span_limit"] + 1, "nonuniform span table length")
    audit_nonuniform_spans(data["binary_spans_600"], golomb_bounds(600), seeds)
    b_spans = extend_and_audit_uniform_spans(data["binary_spans_600"], gol, data["uniform_span_limit"])
    need(b_spans[-1] == data["binary_span_last"], "extended binary span endpoint mismatch")
    print(f"[1] Audited Golomb & binary span bounds through {len(b_spans)-1:,} marks (max span {b_spans[-1]:,}).", flush=True)

    D_inn = F(data["inner_discrepancy_lower_bound"])
    D_bin = F(data["binary_discrepancy_lower_bound"])
    if G is not None:
        cap_inn = lambda u: min(old_cap(u, False), bisect_right(gol, u - 1) - 1) if u <= gol[-1] else old_cap(u, False)
        cap_bin = lambda u: min(old_cap(u, True), bisect_right(b_spans, u - 1) - 1) if u <= b_spans[-1] else old_cap(u, True)
        need(verify_farkas_discrepancy(data["inner_farkas_samples"], G, H, pi, 15000, 16600, 22_500_000, 4600, alpha, cap_inn) == D_inn, "D_inn mismatch")
        need(verify_farkas_discrepancy(data["binary_farkas_samples"], G, H, pi, 1720, 1820, 21_975_000, 455_000, alpha, cap_bin) == D_bin, "D_bin mismatch")
        print(f"[2] Verified Farkas multi-bin discrepancies from pinned matrices: D_inn={D_inn}, D_bin={D_bin}.", flush=True)
    else:
        print(f"[2] Window matrix path omitted; using recorded discrepancies D_inn={D_inn}, D_bin={D_bin} (pass --window to verify from G, H, p).", flush=True)

    verify_inner_thresholds(data["inner_thresholds"], D_inn, den, r, alpha)
    audit_rows(data["rows"], D_bin, data["inner_thresholds"], den, r, alpha)
    print(f"[3] Verified 201 inner Golomb thresholds and {len(data['rows'])} binary capacity witnesses.", flush=True)

    S_main = data["outer_stratified_block"]
    L_main = data["outer_stratified_loss"]
    verify_stratified_outer_loss(S_main, data["outer_stratified_den"], L_main, data["outer_stratified_partitions"])
    fb26 = data["outer_fallback_26"]
    verify_uniform_rank_loss(fb26["block"], fb26["den"], fb26["weights"], fb26["loss"])
    fb20 = data["outer_fallback_20"]
    need(fb20["block"] == 20 and twenty_loss() == fb20["loss"], "twenty-shift fallback mismatch")
    print(f"[4] Verified all {len(data['outer_stratified_partitions'])} histogram-stratified rank-split certificates (S={S_main}, loss={L_main}).", flush=True)

    weights = correlations()
    tiers = [(S_main, L_main), (fb26["block"], fb26["loss"]), (fb20["block"], fb20["loss"])]
    for side, key in ((data["side"], "result"), (data["side"] - 1, "preceding_side_result")):
        res = outer_multiscale(data["rows"], side, weights, tiers)
        need(res == data[key], f"outer result mismatch at side {side}")
        print(f"[5] Side {side:,}: blocks={res['blocks']} ({res['tier_counts']}), exact margin = {res['margin']:,}", flush=True)
    need(data["result"]["margin"] > 0 and data["preceding_side_result"]["margin"] < 0, "expected strict sign change at certified side")
    print(f"VERIFIED: R_4(L) <= {data['side']:,}.", flush=True)


if __name__ == "__main__":
    main()
