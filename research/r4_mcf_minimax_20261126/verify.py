#!/usr/bin/env python3
"""Standalone Python standard-library exact verifier for R_4(L) <= 21,947,741
(exact side read from certificate.json.xz).

Independently reconstructs and verifies, from first principles using only exact
integer and rational arithmetic (int, fractions.Fraction) and zero external
research module imports:
  1. Exact rational window correlations r[0..199], table excess alpha, and all
     401 coarse coverage alignments >= 1 from the vendored Carter-O'Bryant-Tao
     matrices window_tables/{G.txt, H.txt, p.txt} (verified by SHA-256).
  2. Optimal small Golomb spans g_2..g_10 from first principles (explicit
     rulers + exhaustive bitwise search), rank-neighbor Golomb lower spans
     through 56,000 marks, finite binary-source lower spans e_2..e_16 from
     rup_manifest.json + 11 RUP proofs (verified in a temporary directory via
     C99 rup_check.c or pure-Python 2-watched-literal RUP fallback), and exact
     nonuniform rank-neighbor binary-source spans through 22,000 marks.
  3. Exact-integer Min-Cost-Flow (MCF) Farkas dual discrepancy bands across all
     12 oriented window rows and all 200 disjoint edge bins, incorporating the
     exact reversed partial-bin span (kr - 1) and direct non-circular test
     scalar lambda* = K_0 / (P_1 + B_1 * alpha - D*).
  4. All 201 strengthened inner Golomb span thresholds (4,600 <= k <= 4,800)
     and all staggered binary-source capacity witnesses under their certified
     exact-B Farkas discrepancy bands.
  5. Three-segment KD-tree histogram-stratified outer matching DP certificates
     (proving >= 99 missing matches per 39-shift drop block across all 39
     sorted first-segment partitions and exhaustive 560x560 simplex coverage of
     all (n_1, n_2) pairs, with exact 36-shift 12+12+12 prefix fallback on 16
     boundary points, plus boundary 2-segment tiers S=32->80, S=28->77,
     S=26->75 and S=20->41), pairwise block disjointness, and strict integer
     margin sign change between side N - 1 (< 0) and side N (> 0).
  6. Explicit proper 4-color square witnesses on S_6..S_10 achieving zero
     rainbow Ls in the strict lower triangle T_m (and zero across all of S_6,
     S_7), formally closing the Kimi Round 5 (1da352c) 4-color rainbow ceiling.
"""

import argparse
import hashlib
import json
import lzma
import os
import shutil
import subprocess
import tempfile
import time
from bisect import bisect_right
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
WIDTHS = (4, 8, 12, 18, 24, 35, 50, 70, 100, 140, 200, 280, 400, 600, 850, 1200, 1800)
REF = 21_975_000
T = 35_990
G_DEN = 20_971_520  # 20 * 2^20


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


# ---------------------------------------------------------------------------
# 1. Window matrices, correlations, table excess, and 401 coverage alignments
# ---------------------------------------------------------------------------

def load_and_verify_window(tables_dir, expected_hashes, den, r, alpha):
    need(len(r) == 200 and min(r) >= 0 and 2 * sum(r) - r[0] == den and alpha > 0, "window normalization")
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
    G_int = []
    for j in range(6):
        need(len(G[j]) == m and len(H[j]) == 3 * m and all(x >= 0 for x in G[j]) and all(x >= 0 for x in H[j]), "matrix dimensions")
        mass = sum(G[j])
        need(mass == 20, f"unexpected row mass {mass}")
        row_int = []
        for x in G[j]:
            xi = (x * 1_048_576).numerator
            need((x * 1_048_576).denominator == 1 and F(xi, G_DEN) == x / mass, "non-dyadic G entry")
            row_int.append(int(xi))
        G_int.append(row_int)

    for d in range(m):
        exp_corr = sum(pi[j] * sum(G[j][i] * G[j][i + d] for i in range(m - d)) / 400 for j in range(6))
        need(exp_corr == F(r[d], den), f"window correlation mismatch at shift {d}")
    exp_alpha = sum(pi[j] * sum(x * x for x in H[j]) for j in range(6)) - 2 * m
    need(exp_alpha == alpha, "window table_excess mismatch")

    for shift in range(2 * m + 1):
        cov = sum(pi[j] * sum(G[j][i] * H[j][shift + i] for i in range(m)) / 20 for j in range(6))
        need(cov >= 1, f"window coverage failed at alignment {shift}")

    return G_int, H, pi


# ---------------------------------------------------------------------------
# 2. First-principles Golomb seeds g_2..g_10, RUP seeds e_2..e_16, and spans
# ---------------------------------------------------------------------------

def verify_small_golomb_seeds(g_seeds):
    rulers = {
        1: [0],
        2: [0, 1],
        3: [0, 1, 3],
        4: [0, 1, 4, 6],
        5: [0, 1, 4, 9, 11],
        6: [0, 1, 4, 10, 12, 17],
        7: [0, 1, 4, 10, 18, 23, 25],
        8: [0, 1, 4, 9, 15, 22, 32, 34],
        9: [0, 1, 5, 12, 25, 27, 35, 41, 44],
        10: [0, 1, 6, 10, 23, 26, 34, 41, 53, 55],
    }
    g_ver = {1: 0}
    for k in range(2, 11):
        R = rulers[k]
        need(len(R) == k and R[0] == 0 and R == sorted(R), f"invalid Golomb witness k={k}")
        diffs = [R[j] - R[i] for i in range(k) for j in range(i + 1, k)]
        need(len(diffs) == len(set(diffs)), f"duplicate difference in Golomb witness k={k}")
        L_opt = R[-1]
        max_L = L_opt - 1

        def has_ruler(idx, last_pos, rev_marks, diffs_mask):
            if idx == k:
                return True
            rem = k - idx
            min_pos = max(last_pos + 1, g_ver.get(idx + 1, 0))
            max_pos = max_L - g_ver[rem]
            for x in range(min_pos, max_pos + 1):
                d_bits = rev_marks >> (max_L - x)
                if d_bits & diffs_mask:
                    continue
                if has_ruler(idx + 1, x, rev_marks | (1 << (max_L - x)), diffs_mask | d_bits):
                    return True
            return False

        need(not has_ruler(1, 0, 1 << max_L, 0), f"smaller Golomb ruler exists for k={k}")
        g_ver[k] = L_opt

    for k_s, v in g_seeds.items():
        need(g_ver[int(k_s)] == v, f"Golomb seed mismatch at k={k_s}")
    return g_ver


def audit_golomb_spans(g_ver, gol_wit_c, limit):
    need(len(gol_wit_c) == limit + 1 and gol_wit_c[:2] == [0, 0], "bad gol_wit_c length")
    gol = [0, 0]
    ep_cache = [0]
    run_sum = 0
    for k in range(2, limit + 1):
        bound = max(gol[k - 1] + 1, g_ver.get(k, 0))
        c = gol_wit_c[k]
        need(type(c) is int and 0 <= c < k, f"bad Golomb witness rank at k={k}")
        if c > 0:
            while len(ep_cache) <= c:
                idx = len(ep_cache)
                run_sum += gol[idx]
                ep_cache.append(ep_cache[-1] + run_sum)
            H_val = c * k - c * (c + 1) // 2
            num = H_val * (H_val + 1) + 4 * ep_cache[c]
            cand = (num + c * (c + 1) - 1) // (c * (c + 1))
            if cand > bound:
                bound = cand
        gol.append(bound)
    return gol


def reconstruct_binary_source_cnf(k, L, prev_e):
    nv = 0
    clauses = []

    def nv_next():
        nonlocal nv
        nv += 1
        return nv

    m = [nv_next() for _ in range(L + 1)]
    clauses.append([m[0]])
    clauses.append([m[L]])

    cells = {}
    for x in range(1, L + 1):
        for y in range(x):
            cells[(x, y)] = nv_next()
    clauses.append([-cells[(L, 0)]])

    for y in range(L + 1):
        for x in range(y + 1, L + 1):
            c1 = cells[(x, y)]
            for d in range(1, L - x + 1):
                c2 = cells[(x + d, y)]
                c3 = cells[(x + d, y + d)]
                guard = [-m[idx] for idx in sorted({y, x, y + d, x + d})]
                clauses.append(guard + [c1, c2, c3])
                clauses.append(guard + [-c1, -c2, -c3])

    S = {}
    for x in range(L + 1):
        for j in range(1, min(x + 1, k) + 1):
            z = nv_next()
            S[(x, j)] = z
            p = S.get((x - 1, j), None)
            q = True if j == 1 else S.get((x - 1, j - 1), None)
            if p is not None:
                clauses.append([-p, z])
            if q is True:
                clauses.append([-m[x], z])
            elif q is not None:
                clauses.append([-m[x], -q, z])
            if p is None:
                clauses.append([-z, m[x]])
                if type(q) is int:
                    clauses.append([-z, q])
                elif q is not True:
                    clauses.append([-z])
            else:
                clauses.append([-z, p, m[x]])
                if q is None:
                    clauses.append([-z, p])
                elif q is not True:
                    clauses.append([-z, p, q])
        if x >= k:
            clauses.append([-S[(x - 1, k)], -m[x]])
    clauses.append([S[(L, k)]])

    def s_lit(x, j):
        if j <= 0:
            return True
        if x < j - 1:
            return False
        return S[(x, j)]

    for a in range(k):
        for b in range(a + 1, k):
            r = b - a + 1
            if r >= k or r not in prev_e:
                continue
            er = prev_e[r]
            if er <= 1:
                continue
            for x in range(0, L - er + 2):
                y = x + er - 1
                lhs = s_lit(x - 1, a + 1)
                rhs = s_lit(y, b + 1)
                if lhs is True or rhs is False:
                    continue
                cl = [] if lhs is False else [lhs]
                cl.append(-rhs)
                clauses.append(cl)

    half = L // 2
    eq_prev = None
    for i in range(1, half + 1):
        u, v = m[i], m[L - i]
        if u == v:
            continue
        clauses.append([u, -v] if eq_prev is None else [-eq_prev, u, -v])
        if i < half:
            eq_next = nv_next()
            if eq_prev is None:
                clauses.extend([[u, v, eq_next], [-u, -v, eq_next], [-eq_next, -u, v], [-eq_next, u, -v]])
            else:
                clauses.extend([[-eq_prev, u, v, eq_next], [-eq_prev, -u, -v, eq_next], [-eq_next, eq_prev], [-eq_next, -u, v], [-eq_next, u, -v]])
            eq_prev = eq_next

    raw = (f"p cnf {nv} {len(clauses)}\n" + "".join(" ".join(map(str, cl)) + " 0\n" for cl in clauses)).encode("ascii")
    return nv, clauses, raw


def verify_pure_python_rup(nv, cnf_clauses, rup_bytes):
    # Standalone pure-Python 2-watched-literal forward RUP checker (used when --pure-python or no C compiler)
    assign = [0] * (nv + 2)  # 0=unassigned, 1=true, -1=false; indexed by var
    trail = []
    watches = [[] for _ in range(2 * (nv + 2) + 2)]
    clauses = []
    active = []
    buckets = {}

    def lit_idx(l):
        return (2 * l) if l > 0 else (2 * (-l) + 1)

    def ensure_v(v):
        while len(assign) <= v + 1:
            assign.append(0)
            watches.extend([[], []])

    def is_true(l):
        a = assign[l if l > 0 else -l]
        return a == 1 if l > 0 else a == -1

    def is_false(l):
        a = assign[l if l > 0 else -l]
        return a == -1 if l > 0 else a == 1

    def enqueue(l):
        if is_false(l):
            return False
        if is_true(l):
            return True
        v = l if l > 0 else -l
        assign[v] = 1 if l > 0 else -1
        trail.append(v)
        return True

    def propagate(qhead):
        while qhead < len(trail):
            v = trail[qhead]
            qhead += 1
            flit = -v if assign[v] == 1 else v
            li = lit_idx(flit)
            wlist = watches[li]
            i = 0
            while i < len(wlist):
                wnode = wlist[i]
                cid = wnode >> 1
                side = wnode & 1
                if not active[cid]:
                    wlist[i] = wlist[-1]
                    wlist.pop()
                    continue
                cl = clauses[cid]
                if cl[side] != flit:
                    cl[0], cl[1] = cl[1], cl[0]
                other = cl[1 - side]
                if is_true(other):
                    i += 1
                    continue
                moved = False
                for k_i in range(2, len(cl)):
                    if not is_false(cl[k_i]):
                        nl = cl[k_i]
                        cl[k_i] = flit
                        cl[side] = nl
                        wlist[i] = wlist[-1]
                        wlist.pop()
                        watches[lit_idx(nl)].append(wnode)
                        moved = True
                        break
                if not moved:
                    if not enqueue(other):
                        return False
                    i += 1
        return True

    def add_cl(lits):
        arr = []
        seen = set()
        for l in lits:
            v = l if l > 0 else -l
            ensure_v(v)
            if -l in seen:
                return True
            if l not in seen:
                seen.add(l)
                arr.append(l)
        if not arr:
            return False
        if len(arr) == 1:
            qh = len(trail)
            return enqueue(arr[0]) and propagate(qh)
        placed = 0
        for idx_i in range(len(arr)):
            if not is_false(arr[idx_i]):
                arr[placed], arr[idx_i] = arr[idx_i], arr[placed]
                placed += 1
                if placed == 2:
                    break
        cid = len(clauses)
        clauses.append(arr)
        active.append(True)
        key = tuple(sorted(arr))
        buckets.setdefault(key, []).append(cid)
        watches[lit_idx(arr[0])].append(2 * cid)
        watches[lit_idx(arr[1])].append(2 * cid + 1)
        if placed == 0:
            return False
        if placed == 1:
            qh = len(trail)
            return enqueue(arr[0]) and propagate(qh)
        return True

    for cl in cnf_clauses:
        if not add_cl(cl):
            return True

    for raw_line in rup_bytes.decode("ascii").splitlines():
        line = raw_line.strip()
        if not line or line[0] == "c":
            continue
        if line[0] == "d":
            toks = [int(x) for x in line[1:].split() if x != "0"]
            if len(toks) >= 2:
                lst = buckets.get(tuple(sorted(toks)))
                if lst:
                    active[lst.pop()] = False
            continue
        lits = [int(x) for x in line.split()]
        need(lits and lits[-1] == 0, "unterminated RUP line")
        lits.pop()
        saved = len(trail)
        conflict = False
        for l in lits:
            ensure_v(abs(l))
            if not enqueue(-l):
                conflict = True
                break
        if not conflict and not propagate(saved):
            conflict = True
        while len(trail) > saved:
            assign[trail.pop()] = 0
        need(conflict, "RUP step failed in pure-Python checker")
        if not lits:
            return True
        if not add_cl(lits):
            return True
    raise ValueError("RUP proof ended without deriving empty clause")


def _rup_worker(args):
    k, L, prev_e, cnf_sha, rup_sha, rup_xz_path, bin_path = args
    nv, cnf_clauses, raw_cnf = reconstruct_binary_source_cnf(k, L, prev_e)
    need(hashlib.sha256(raw_cnf).hexdigest() == cnf_sha, f"CNF SHA-256 mismatch at k={k}, L={L}")
    rup_bytes = lzma.decompress(Path(rup_xz_path).read_bytes())
    need(hashlib.sha256(rup_bytes).hexdigest() == rup_sha, f"RUP SHA-256 mismatch at k={k}, L={L}")
    if bin_path is not None:
        with tempfile.TemporaryDirectory() as td:
            fc = Path(td) / "f.cnf"
            fp = Path(td) / "p.rup"
            fc.write_bytes(raw_cnf)
            fp.write_bytes(rup_bytes)
            res = subprocess.run([bin_path, str(fc), str(fp)], capture_output=True, text=True, timeout=240)
            need(res.returncode == 0 and "s VERIFIED" in res.stdout, f"rup_check failed on k={k}, L={L}")
    else:
        need(verify_pure_python_rup(nv, cnf_clauses, rup_bytes), f"pure-Python RUP failed on k={k}, L={L}")
    return k, L


def verify_rup_manifest_and_binary_spans(manifest_path, rup_dir, rup_c_path, expected_seeds, b_spans, b_wit_rnk, gol, pure_python=False):
    manifest = json.loads(manifest_path.read_text())
    prev_e = {1: 0}
    cur_k = 2
    exp_L = 1
    rup_jobs = []

    for entry in manifest["entries"]:
        k, L, st = entry["k"], entry["L"], entry["status"]
        if k != cur_k:
            need(k == cur_k + 1 and cur_k in prev_e, f"out-of-sequence k={k} in rup_manifest")
            cur_k = k
            exp_L = prev_e[k - 1] + 1
        need(L == exp_L, f"skipped span L={L} vs {exp_L} at k={k}")
        if st == "SAT":
            A = entry["witness_A"]
            need(len(A) == k and A == sorted(set(A)) and A[0] == 0 and A[-1] == L, f"bad witness marks k={k}")
            chi = {(x, y): c for x, y, c in entry["witness_coloring"]}
            need(set(chi.keys()) == {(v, u) for u in A for v in A if u < v} and set(chi.values()) <= {0, 1}, f"bad witness domain k={k}")
            S_set = set(A)
            for u in A:
                for v in A:
                    if v > u:
                        for t in range(1, L - v + 1):
                            if (u + t) in S_set and (v + t) in S_set:
                                need(not (chi[(v, u)] == chi[(v + t, u)] == chi[(v + t, u + t)]), f"monochromatic L in SAT witness k={k}")
            prev_e[k] = L
        elif st == "UNSAT-VERIFIED":
            rup_jobs.append((k, L, dict(prev_e), entry["cnf_sha256"], entry["rup_sha256"], str(rup_dir / entry["rup_xz_file"])))
            exp_L = L + 1
            prev_e[k] = exp_L
        else:
            raise ValueError(f"unknown status {st}")

    for k_s, v in expected_seeds.items():
        need(prev_e[int(k_s)] == v, f"binary seed mismatch at k={k_s}")

    cc_bin = None
    if not pure_python:
        for cand in ("cc", "clang", "gcc"):
            if shutil.which(cand):
                cc_bin = cand
                break

    with tempfile.TemporaryDirectory() as td:
        bin_path = None
        if cc_bin is not None:
            bin_path = str(Path(td) / "rup_check_bin")
            comp = subprocess.run([cc_bin, "-O3", "-std=c99", str(rup_c_path), "-o", bin_path], capture_output=True, text=True)
            need(comp.returncode == 0, f"failed to compile rup_check.c: {comp.stderr}")
        jobs_with_bin = [jb + (bin_path,) for jb in rup_jobs]
        workers = min(8, os.cpu_count() or 1)
        with ProcessPoolExecutor(max_workers=workers) as ex:
            for _ in ex.map(_rup_worker, jobs_with_bin):
                pass

    # Audit all 22,000 nonuniform binary-source spans in O(log M) exact integer ops per mark
    limit = len(b_spans) - 1
    need(b_spans[:2] == [0, 0] and len(b_wit_rnk) == limit + 1, "bad binary span array")
    need(gol[-1] > b_spans[-1], "Golomb table does not cover binary spans")
    g_small = gol[:1200]
    need(g_small[-1] > b_spans[-1], "g_small sentinel failed")
    pref_g = [0]
    pref_g2 = [0]
    for x in g_small[1:]:
        pref_g.append(pref_g[-1] + x)
        pref_g2.append(pref_g2[-1] + x * x)

    def count_and_cost_at_h(L_val, h):
        if h <= 0:
            return 0, 0
        tot_cnt = tot_cst = 0
        for X in (L_val, L_val - 1):
            if X <= 0:
                continue
            m_hi = bisect_right(g_small, X - 1) - 1
            if m_hi <= 0:
                continue
            m_lo = max(0, bisect_right(g_small, X - h) - 1)
            if m_lo > 0:
                tot_cnt += m_lo * h
                tot_cst += m_lo * (h * (h + 1) // 2)
            if m_hi > m_lo:
                n_m = m_hi - m_lo
                sg = pref_g[m_hi] - pref_g[m_lo]
                sg2 = pref_g2[m_hi] - pref_g2[m_lo]
                sum_u = n_m * X - sg
                sum_u2 = n_m * X * X - 2 * X * sg + sg2
                tot_cnt += sum_u
                tot_cst += (sum_u2 + sum_u) // 2
        return tot_cnt, tot_cst

    def min_price_nonuniform(L_val, pairs):
        max_cnt, _ = count_and_cost_at_h(L_val, L_val)
        if max_cnt < pairs:
            return None
        lo, hi = 1, L_val
        while lo < hi:
            mid = (lo + hi) // 2
            if count_and_cost_at_h(L_val, mid)[0] >= pairs:
                hi = mid
            else:
                lo = mid + 1
        c_prev, cst_prev = count_and_cost_at_h(L_val, lo - 1)
        return cst_prev + lo * (pairs - c_prev)

    ep_b = [0]
    run_b = 0
    for k in range(2, limit + 1):
        base_lb = max(b_spans[k - 1] + 1, prev_e.get(k, 0))
        need(type(b_spans[k]) is int and b_spans[k] >= base_lb, f"binary span monotonicity failed at k={k}")
        if b_spans[k] > base_lb:
            rnk = b_wit_rnk[k]
            need(type(rnk) is int and 1 <= rnk < k, f"bad binary witness rank at k={k}")
            while len(ep_b) <= rnk:
                idx = len(ep_b)
                run_b += b_spans[idx]
                ep_b.append(ep_b[-1] + run_b)
            L0 = b_spans[k] - 1
            pairs = rnk * k - rnk * (rnk + 1) // 2
            pr = min_price_nonuniform(L0, pairs)
            # By multiset monotonicity v_{L'}(h) <= v_{L0}(h) for all L' <= L0,
            # rejecting L0 at rank rnk simultaneously rejects every 0 <= L' <= L0.
            need(pr is None or 2 * pr + 4 * ep_b[rnk] > L0 * rnk * (rnk + 1), f"unjustified binary span {b_spans[k]} at k={k}")


# ---------------------------------------------------------------------------
# 3. Exact integer MCF Farkas discrepancy bands & threshold/row audits
# ---------------------------------------------------------------------------

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


def verify_farkas_bands(bands, G_int, H, pi, alpha, cap_fn, max_span_covered):
    for idx_b, band in enumerate(bands):
        need(band["band_id"] == idx_b, "band_id sequence mismatch")
        B0, B1, P1, K0 = band["B0"], band["B1"], band["P1"], band["K0"]
        D_star = F(band["D"])
        need(1 <= B0 <= B1 and K0 >= 1 and D_star > 0, "invalid band bounds")
        need(200 * B1 <= max_span_covered, "band span exceeds recursive span table")
        need(F(P1) + B0 * alpha - D_star > 0, "non-positive denominator in test scalar lambda*")

        lam_inv = (F(P1) + B1 * alpha - D_star) / (K0 * B0)
        samples = band["samples"]
        need(len(samples) == 12, "expected 12 oriented window rows")
        seen_rows = set()
        total_nanos = 0

        for entry in samples:
            r_idx = entry["row"]
            rev = bool(entry["reverse"])
            need(0 <= r_idx < 6 and (r_idx, rev) not in seen_rows, "duplicate row sample")
            seen_rows.add((r_idx, rev))

            row_nanos = 0
            seen_bins = set()
            for b_entry in entry["bins"]:
                j = b_entry["bin"]
                need(type(j) is int and 0 <= j < 200 and j not in seen_bins, "invalid or duplicate bin")
                seen_bins.add(j)
                target = H[r_idx][-1 - j] if rev else H[r_idx][j]
                g_req = [G_int[r_idx][199 - r] if rev else G_int[r_idx][r] for r in range(j + 1)]

                const_ub = []
                bnd_arcs = []
                for mults in b_entry["duals"]:
                    cov = [0] * (j + 1)
                    cub = 0
                    barcs = []
                    for a, b, y_int in mults:
                        need(type(a) is int and type(b) is int and type(y_int) is int and 0 <= a <= b <= j and y_int > 0, "bad Farkas dual arc")
                        for r_pos in range(a, b + 1):
                            cov[r_pos] += y_int
                        if b < j:
                            cub += y_int * cap_fn((b - a + 1) * B1)
                        else:
                            barcs.append(((j - a) * B1, y_int))
                    for r_pos in range(j + 1):
                        need(cov[r_pos] >= g_req[r_pos], f"Farkas dual under-covers pos {r_pos} on band {idx_b}")
                    const_ub.append(cub)
                    bnd_arcs.append(barcs)

                tn, td = target.numerator, target.denominator
                ln, ld = lam_inv.numerator, lam_inv.denominator
                m_den = td * ld * G_DEN
                a_int = tn * ld * G_DEN
                b_int = td * ln
                bin_num_sq = 0
                prev_kr = 0
                for kl, kr, d_idx in b_entry["blocks"]:
                    need(type(kl) is int and type(kr) is int and type(d_idx) is int, "non-int block entry")
                    need(prev_kr < kl <= kr <= B0 and 0 <= d_idx < len(const_ub), "invalid k block")
                    prev_kr = kr
                    span_part = (kr - 1) if rev else kr
                    ub_num = const_ub[d_idx] + sum(y_int * cap_fn(base_sp + span_part) for base_sp, y_int in bnd_arcs[d_idx])
                    sf_num = a_int - b_int * ub_num
                    if sf_num > 0:
                        bin_num_sq += (kr - kl + 1) * (sf_num * sf_num)
                row_nanos += (F(bin_num_sq, m_den * m_den) * pi[r_idx] * 10**9).__floor__()

            need(row_nanos == entry["variance_floor_nanos"], f"row nanos mismatch on band {idx_b}")
            total_nanos += row_nanos

        need(F(total_nanos, 10**9) >= D_star, f"band {idx_b} verified discrepancy below claimed D*")


def verify_inner_thresholds(lengths, wit_B_band, inner_bands, den, r, alpha):
    need(len(lengths) == 201 and len(wit_B_band) == 201, "bad inner threshold count")
    need(all(type(a) is int and a < b for a, b in zip(lengths, lengths[1:])), "inner threshold monotonicity")
    for idx, k in enumerate(range(4600, 4801)):
        length = lengths[idx]
        B, b_id = wit_B_band[idx]
        band = inner_bands[b_id]
        D_inn = F(band["D"])
        p = length - 1
        c = F((k - 1) * r[0], den)
        need(band["B0"] <= B <= band["B1"] and D_inn < p <= band["P1"] and k >= band["K0"] and p - 1 >= 400 * B, f"inner domain fail at k={k}")
        need(k * k > (p + B * alpha - D_inn) * (1 + c / B), f"inner threshold inequality failed at k={k}")


def audit_rows(rows, binary_bands, lengths, den, r, alpha):
    need(all(a[0] < b[0] and a[1] >= b[1] for a, b in zip(rows, rows[1:])), "row order")
    Q = lambda p_val: 4599 + bisect_right(lengths, p_val)
    rr = r + [0]
    blocks_by_B = {}
    for offset, cap, B, b_id in rows:
        band = binary_bands[b_id]
        D_bin = F(band["D"])
        p, k = REF - offset, cap + 1
        need(band["B0"] <= B <= band["B1"] and D_bin < p <= band["P1"] and k >= band["K0"] and p - 1 >= 400 * B, f"binary domain fail at offset {offset}")
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
            need(v == Q(p - b + 1) + Q(p - b), "profile not constant on interval")
            energy += 2 * v * (prefix(b - 1) - prefix(a - 1))
        need(k * k * den * B * B > (p + B * alpha - D_bin) * energy, f"binary witness failed at offset {offset}")


# ---------------------------------------------------------------------------
# 4. Two-segment KD-tree outer matching DP & multiscale contradiction check
# ---------------------------------------------------------------------------

def _eval_3seg_exact_box(M_loc, n0_loc, lo1, hi1, lo2, hi2, D, w_list):
    need(len(w_list) == 6, "expected 6 weight arrays for 3-seg")
    b00, b01, b02, b11, b12, b22 = w_list
    for arr, h_req in ((b00, n0_loc), (b01, n0_loc), (b02, n0_loc), (b11, hi1), (b12, hi1), (b22, hi2)):
        need(len(arr) == 4 and [len(arr[c]) for c in range(4)] == h_req, "bad 3-seg weight lengths")
        for c in range(4):
            need(all(type(v) is int and 0 <= v <= D for v in arr[c]), "weight out of [0, D]")
            need(all(x <= y for x, y in zip(arr[c], arr[c][1:])), "weights not nondecreasing")

    T00 = [[max(b00[c][r], b01[c][r]) for r in range(n0_loc[c])] for c in range(4)]
    T01 = [[max(b01[c][r], b02[c][r]) for r in range(n0_loc[c])] for c in range(4)]
    T11 = [[max(b11[c][r], b12[c][r]) for r in range(hi1[c])] for c in range(4)]

    s0_1, s0_2, s0_3 = n0_loc[1] + 1, n0_loc[2] + 1, n0_loc[3] + 1
    st0_0, st0_1, st0_2 = s0_1 * s0_2 * s0_3, s0_2 * s0_3, s0_3
    rc0 = [[0] + [sum(b02[c][max(0, h - 3) : h]) for h in range(1, n0_loc[c] + 1)] for c in range(4)]
    cc0 = [[0] + [sum(D - b00[c][r] for r in range(h)) for h in range(1, n0_loc[c] + 1)] for c in range(4)]
    dp0 = [0] * ((n0_loc[0] + 1) * st0_0)
    for h0 in range(n0_loc[0] + 1):
        r0, c0 = rc0[0][h0], cc0[0][h0]
        base0 = h0 * st0_0
        for h1 in range(n0_loc[1] + 1):
            r01 = r0 + rc0[1][h1]
            c01 = c0 if c0 >= cc0[1][h1] else cc0[1][h1]
            base1 = base0 + h1 * st0_1
            for h2 in range(n0_loc[2] + 1):
                r012 = r01 + rc0[2][h2]
                c012 = c01 if c01 >= cc0[2][h2] else cc0[2][h2]
                base2 = base1 + h2 * st0_2
                for h3 in range(n0_loc[3] + 1):
                    if (h0 | h1 | h2 | h3) == 0:
                        continue
                    idx = base2 + h3
                    bp = -1
                    if h0 and dp0[idx - st0_0] > bp: bp = dp0[idx - st0_0]
                    if h1 and dp0[idx - st0_1] > bp: bp = dp0[idx - st0_1]
                    if h2 and dp0[idx - st0_2] > bp: bp = dp0[idx - st0_2]
                    if h3 and dp0[idx - 1]     > bp: bp = dp0[idx - 1]
                    c_all = c012 if c012 >= cc0[3][h3] else cc0[3][h3]
                    dp0[idx] = bp + r012 + rc0[3][h3] + c_all
    val0 = dp0[-1]

    NEG = -10**18
    vals_12 = []
    for u, lo, hi in ((1, lo1, hi1), (2, lo2, hi2)):
        rc = []
        cc = []
        for c in range(4):
            L0 = n0_loc[c]
            if u == 1:
                top_fixed = T01[c][max(0, L0 - 3) : L0]
                base_cc = sum(D - b01[c][r] for r in range(L0))
                b_r, b_c = b12[c], b11[c]
            else:
                L1 = hi1[c]
                top_fixed = T00[c][max(0, L0 - 3) : L0] + T11[c][max(0, L1 - 3) : L1]
                base_cc = sum(D - b02[c][r] for r in range(L0)) + sum(D - b12[c][r] for r in range(L1))
                b_r, b_c = b22[c], b22[c]
            r_arr = []
            c_arr = []
            for h in range(hi[c] + 1):
                pool = sorted(top_fixed + b_r[max(0, h - 3) : h], reverse=True)
                r_arr.append(sum(pool[:3]))
                c_arr.append(base_cc + sum(D - b_c[r] for r in range(h)))
            rc.append(r_arr)
            cc.append(c_arr)

        d1, d2, d3 = hi[1] + 1, hi[2] + 1, hi[3] + 1
        q0, q1, q2 = d1 * d2 * d3, d2 * d3, d3
        dp = [NEG] * ((hi[0] + 1) * q0)
        dp[0] = 0
        best_u = NEG
        lo0, lo1_c, lo2_c, lo3_c = lo
        hi0, hi1_c, hi2_c, hi3_c = hi
        for h0 in range(hi0 + 1):
            nd0 = lo0 - h0 if lo0 > h0 else 0
            r0, c0 = rc[0][h0], cc[0][h0]
            b0 = h0 * q0
            for h1 in range(min(hi1_c, M_loc - h0) + 1):
                nd01 = nd0 + (lo1_c - h1 if lo1_c > h1 else 0)
                r01 = r0 + rc[1][h1]
                c01 = c0 if c0 >= cc[1][h1] else cc[1][h1]
                b1 = b0 + h1 * q1
                for h2 in range(min(hi2_c, M_loc - h0 - h1) + 1):
                    nd012 = nd01 + (lo2_c - h2 if lo2_c > h2 else 0)
                    r012 = r01 + rc[2][h2]
                    c012 = c01 if c01 >= cc[2][h2] else cc[2][h2]
                    b2 = b1 + h2 * q2
                    rem2 = M_loc - h0 - h1 - h2
                    for h3 in range(min(hi3_c, rem2) + 1):
                        if (h0 | h1 | h2 | h3) == 0:
                            continue
                        rem_s = rem2 - h3
                        if nd012 + (lo3_c - h3 if lo3_c > h3 else 0) > rem_s:
                            continue
                        idx = b2 + h3
                        bp = NEG
                        if h0 and dp[idx - q0] > bp: bp = dp[idx - q0]
                        if h1 and dp[idx - q1] > bp: bp = dp[idx - q1]
                        if h2 and dp[idx - q2] > bp: bp = dp[idx - q2]
                        if h3 and dp[idx - 1]  > bp: bp = dp[idx - 1]
                        if bp == NEG:
                            continue
                        c_all = c012 if c012 >= cc[3][h3] else cc[3][h3]
                        v = bp + r012 + rc[3][h3] + c_all
                        dp[idx] = v
                        if rem_s == 0 and v > best_u:
                            best_u = v
        need(best_u > NEG, f"empty valid terminal state in 3-seg band {u}")
        vals_12.append(best_u)

    allow_loc = sum(min(s, 12) for s in range(1, 3 * M_loc + 1))
    return allow_loc - (val0 + vals_12[0] + vals_12[1]) // D

def verify_3seg_kdtree_tier(tier):
    K = tier["K"]
    S = tier["S"]
    M = tier["M"]
    D = tier["den"]
    target_loss = tier["loss"]
    need(K == 3 and type(S) is int and type(M) is int and S == 3 * M and M >= 3 and type(D) is int and D >= 1, "bad 3-seg tier metadata")

    expected_parts = [
        [n0, n1, n2, M - n0 - n1 - n2]
        for n0 in range(M // 4 + 1)
        for n1 in range(n0, (M - n0) // 3 + 1)
        for n2 in range(n1, (M - n0 - n1) // 2 + 1)
    ]
    part_certs = tier["partitions"]
    need([entry["n0"] for entry in part_certs] == expected_parts, f"incomplete n0 partition coverage at S={S}")

    simplex_pts = [
        (x0, x1, x2, M - x0 - x1 - x2)
        for x0 in range(M + 1)
        for x1 in range(M - x0 + 1)
        for x2 in range(M - x0 - x1 + 1)
    ]
    n_simp = len(simplex_pts)
    full_mask = (1 << n_simp) - 1

    for entry in part_certs:
        n0_vec = entry["n0"]
        boxes = entry["boxes"]
        need(len(boxes) >= 1, "empty box list")

        masks_1 = []
        masks_2 = []
        for bx in boxes:
            l10, l11, l12, l13 = bx["lo1"]
            u10, u11, u12, u13 = bx["hi1"]
            l20, l21, l22, l23 = bx["lo2"]
            u20, u21, u22, u23 = bx["hi2"]
            m1 = 0
            m2 = 0
            for idx_p, (x0, x1, x2, x3) in enumerate(simplex_pts):
                if l10 <= x0 <= u10 and l11 <= x1 <= u11 and l12 <= x2 <= u12 and l13 <= x3 <= u13:
                    m1 |= (1 << idx_p)
                if l20 <= x0 <= u20 and l21 <= x1 <= u21 and l22 <= x2 <= u22 and l23 <= x3 <= u23:
                    m2 |= (1 << idx_p)
            masks_1.append(m1)
            masks_2.append(m2)

        for idx_p1 in range(n_simp):
            bit1 = 1 << idx_p1
            cov2 = 0
            for m1, m2 in zip(masks_1, masks_2):
                if m1 & bit1:
                    cov2 |= m2
            need(cov2 == full_mask, f"incomplete (n1, n2) simplex coverage on n0={n0_vec} at n1={simplex_pts[idx_p1]}")

        for bx in boxes:
            lo1, hi1 = bx["lo1"], bx["hi1"]
            lo2, hi2 = bx["lo2"], bx["hi2"]
            need(len(lo1) == 4 and len(hi1) == 4 and all(0 <= lo1[c] <= hi1[c] <= M for c in range(4)), "bad box1 bounds")
            need(len(lo2) == 4 and len(hi2) == 4 and all(0 <= lo2[c] <= hi2[c] <= M for c in range(4)), "bad box2 bounds")

            if "prefix_12x3" in bx:
                need(M == 13 and lo1 == hi1 and lo2 == hi2 and sum(lo1) == 13 and sum(lo2) == 13, "prefix_12x3 requires exact M=13 point")
                req_triples = set()
                d1_list = [[1 if c == c0 else 0 for c in range(4)] for c0 in range(4) if n0_vec[c0] >= 1]
                d2_list = [[x0, x1, x2, 2 - x0 - x1 - x2] for x0 in range(min(2, lo1[0])+1) for x1 in range(min(2-x0, lo1[1])+1) for x2 in range(min(2-x0-x1, lo1[2])+1) if 2 - x0 - x1 - x2 <= lo1[3]]
                d3_list = [[x0, x1, x2, 3 - x0 - x1 - x2] for x0 in range(min(3, lo2[0])+1) for x1 in range(min(3-x0, lo2[1])+1) for x2 in range(min(3-x0-x1, lo2[2])+1) if 3 - x0 - x1 - x2 <= lo2[3]]
                for d1 in d1_list:
                    m0 = tuple(n0_vec[c] - d1[c] for c in range(4))
                    for d2 in d2_list:
                        m1 = tuple(d1[c] + lo1[c] - d2[c] for c in range(4))
                        for d3 in d3_list:
                            m2 = tuple(d2[c] + lo2[c] - d3[c] for c in range(4))
                            req_triples.add((m0, m1, m2))
                covered_sub = set()
                for sc in bx["prefix_12x3"]:
                    m0_l, m1_l, m2_l = sc["m0"], sc["m1"], sc["m2"]
                    need(sum(m0_l) == 12 and sum(m1_l) == 12 and sum(m2_l) == 12, "bad 12x3 sub-histogram sum")
                    proved_sub = _eval_3seg_exact_box(12, m0_l, m1_l, m1_l, m2_l, m2_l, D, sc["w"])
                    need(proved_sub == sc["loss"] and proved_sub >= target_loss, "12x3 prefix sub-certificate failed")
                    covered_sub.add((tuple(m0_l), tuple(m1_l), tuple(m2_l)))
                need(req_triples <= covered_sub, f"missing 12x3 prefix sub-split on {(n0_vec, lo1, lo2)}")
            else:
                proved = _eval_3seg_exact_box(M, n0_vec, lo1, hi1, lo2, hi2, D, bx["w"])
                need(proved == bx["loss"] and proved >= target_loss, f"3-seg DP loss mismatch on n0={n0_vec}")


def verify_2seg_kdtree_tier(tier):
    S = tier["S"]
    M = tier["M"]
    D = tier["den"]
    target_loss = tier["loss"]
    need(type(S) is int and type(M) is int and S == 2 * M and M >= 3 and type(D) is int and D >= 1, "bad 2-seg tier metadata")

    expected_parts = [
        [n0, n1, n2, M - n0 - n1 - n2]
        for n0 in range(M // 4 + 1)
        for n1 in range(n0, (M - n0) // 3 + 1)
        for n2 in range(n1, (M - n0 - n1) // 2 + 1)
    ]
    part_certs = tier["partitions"]
    need([entry["n0"] for entry in part_certs] == expected_parts, f"incomplete n0 partition coverage at S={S}")

    all_simplex_pts = [
        (x0, x1, x2, M - x0 - x1 - x2)
        for x0 in range(M + 1)
        for x1 in range(M - x0 + 1)
        for x2 in range(M - x0 - x1 + 1)
    ]
    allow = sum(min(s, 12) for s in range(1, S + 1))
    NEG = -10**18

    for entry in part_certs:
        n0_vec = entry["n0"]
        boxes = entry["boxes"]
        need(len(boxes) >= 1, "empty box list")

        # Exhaustive point-by-point simplex coverage check on {h1 in Z_>=0^4 : sum(h1) == M}
        box_bounds = [(tuple(b["lo"]), tuple(b["hi"])) for b in boxes]
        for x0, x1, x2, x3 in all_simplex_pts:
            covered = False
            for (l0, l1, l2, l3), (u0, u1, u2, u3) in box_bounds:
                if l0 <= x0 <= u0 and l1 <= x1 <= u1 and l2 <= x2 <= u2 and l3 <= x3 <= u3:
                    covered = True
                    break
            need(covered, f"uncovered second-half histogram {(x0,x1,x2,x3)} on n0={n0_vec}")

        s1, s2, s3 = n0_vec[1] + 1, n0_vec[2] + 1, n0_vec[3] + 1
        st0, st1, st2 = s1 * s2 * s3, s2 * s3, s3

        for bx in boxes:
            lo, hi = bx["lo"], bx["hi"]
            need(len(lo) == 4 and len(hi) == 4 and all(0 <= lo[c] <= hi[c] <= M for c in range(4)), "invalid box bounds")
            b_LL, b_LR, b_RR = bx["b_LL"], bx["b_LR"], bx["b_RR"]
            need(len(b_LL) == 4 and len(b_LR) == 4 and len(b_RR) == 4, "bad weight color count")
            for c in range(4):
                need(len(b_LL[c]) == n0_vec[c] and len(b_LR[c]) == n0_vec[c] and len(b_RR[c]) == hi[c], "bad weight vector lengths")
                for arr in (b_LL[c], b_LR[c], b_RR[c]):
                    need(all(type(v) is int and 0 <= v <= D for v in arr), "weight out of [0, D]")
                    need(all(x <= y for x, y in zip(arr, arr[1:])), "weights not nondecreasing")

            b_TOP = [[max(b_LL[c][r], b_LR[c][r]) for r in range(n0_vec[c])] for c in range(4)]

            # Half 0 DP (1 <= s <= M)
            rc0 = [[0] + [sum(b_LR[c][max(0, h - 3) : h]) for h in range(1, n0_vec[c] + 1)] for c in range(4)]
            cc0 = [[0] + [sum(D - b_LL[c][r] for r in range(h)) for h in range(1, n0_vec[c] + 1)] for c in range(4)]
            dp0 = [0] * ((n0_vec[0] + 1) * st0)
            for h0 in range(n0_vec[0] + 1):
                r0, c0 = rc0[0][h0], cc0[0][h0]
                base0 = h0 * st0
                for h1 in range(n0_vec[1] + 1):
                    r01 = r0 + rc0[1][h1]
                    c01 = c0 if c0 >= cc0[1][h1] else cc0[1][h1]
                    base1 = base0 + h1 * st1
                    for h2 in range(n0_vec[2] + 1):
                        r012 = r01 + rc0[2][h2]
                        c012 = c01 if c01 >= cc0[2][h2] else cc0[2][h2]
                        base2 = base1 + h2 * st2
                        for h3 in range(n0_vec[3] + 1):
                            if (h0 | h1 | h2 | h3) == 0:
                                continue
                            idx = base2 + h3
                            bp = -1
                            if h0 and dp0[idx - st0] > bp: bp = dp0[idx - st0]
                            if h1 and dp0[idx - st1] > bp: bp = dp0[idx - st1]
                            if h2 and dp0[idx - st2] > bp: bp = dp0[idx - st2]
                            if h3 and dp0[idx - 1]   > bp: bp = dp0[idx - 1]
                            c_all = c012 if c012 >= cc0[3][h3] else cc0[3][h3]
                            dp0[idx] = bp + r012 + rc0[3][h3] + c_all
            val0 = dp0[-1]

            # Half 1 DP (M + 1 <= s <= 2M) restricted to lo <= n1 <= hi, sum(n1) == M
            rc1 = []
            cc1 = []
            for c in range(4):
                base_cc = sum(D - b_LR[c][r] for r in range(n0_vec[c]))
                top_fixed = b_TOP[c][max(0, n0_vec[c] - 3) : n0_vec[c]]
                r_arr = []
                c_arr = []
                for h in range(hi[c] + 1):
                    pool = sorted(top_fixed + b_RR[c][max(0, h - 3) : h], reverse=True)
                    r_arr.append(sum(pool[:3]))
                    c_arr.append(base_cc + sum(D - b_RR[c][r] for r in range(h)))
                rc1.append(r_arr)
                cc1.append(c_arr)

            d1, d2, d3 = hi[1] + 1, hi[2] + 1, hi[3] + 1
            q0, q1, q2 = d1 * d2 * d3, d2 * d3, d3
            dp1 = [NEG] * ((hi[0] + 1) * q0)
            dp1[0] = 0
            best_val1 = NEG
            lo0, lo1, lo2, lo3 = lo
            hi0, hi1, hi2, hi3 = hi

            for h0 in range(hi0 + 1):
                need0 = lo0 - h0 if lo0 > h0 else 0
                r0, c0 = rc1[0][h0], cc1[0][h0]
                b0 = h0 * q0
                max_h1 = min(hi1, M - h0)
                for h1 in range(max_h1 + 1):
                    need01 = need0 + (lo1 - h1 if lo1 > h1 else 0)
                    r01 = r0 + rc1[1][h1]
                    c01 = c0 if c0 >= cc1[1][h1] else cc1[1][h1]
                    b1 = b0 + h1 * q1
                    max_h2 = min(hi2, M - h0 - h1)
                    for h2 in range(max_h2 + 1):
                        need012 = need01 + (lo2 - h2 if lo2 > h2 else 0)
                        r012 = r01 + rc1[2][h2]
                        c012 = c01 if c01 >= cc1[2][h2] else cc1[2][h2]
                        b2 = b1 + h2 * q2
                        rem_after_2 = M - h0 - h1 - h2
                        max_h3 = min(hi3, rem_after_2)
                        for h3 in range(max_h3 + 1):
                            if (h0 | h1 | h2 | h3) == 0:
                                continue
                            rem_steps = rem_after_2 - h3
                            need_all = need012 + (lo3 - h3 if lo3 > h3 else 0)
                            if need_all > rem_steps:
                                continue
                            idx = b2 + h3
                            bp = NEG
                            if h0 and dp1[idx - q0] > bp: bp = dp1[idx - q0]
                            if h1 and dp1[idx - q1] > bp: bp = dp1[idx - q1]
                            if h2 and dp1[idx - q2] > bp: bp = dp1[idx - q2]
                            if h3 and dp1[idx - 1]  > bp: bp = dp1[idx - 1]
                            if bp == NEG:
                                continue
                            c_all = c012 if c012 >= cc1[3][h3] else cc1[3][h3]
                            v = bp + r012 + rc1[3][h3] + c_all
                            dp1[idx] = v
                            if rem_steps == 0 and v > best_val1:
                                best_val1 = v

            need(best_val1 > NEG, f"empty valid terminal set in box {lo}..{hi} on n0={n0_vec}")
            proved = allow - (val0 + best_val1) // D
            need(proved == bx["loss"] and proved >= target_loss, f"2-seg DP loss failed on n0={n0_vec} box {lo}..{hi}")


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

    # Independent direct-summation cross-check at 5 sample lags
    w_vec = [0] + [(i * (T + 1 - i)) * (5 * (T + 1) ** 2 + 6 * i * (T + 1 - i)) for i in range(1, T + 1)]
    for test_d in (0, 1, 17, 18000, T - 1):
        direct = sum(w_vec[i] * w_vec[i + test_d] for i in range(1, T - test_d + 1))
        need(direct == out[test_d], f"correlation direct-sum mismatch at d={test_d}")
    return out


def outer_multiscale(rows, n, weights, tiers):
    offset = REF - n
    need(rows[0][0] <= offset + 1 and rows[-1][0] >= offset + T + 10, "outer coverage")
    prefix = [0]
    for x in weights:
        prefix.append(prefix[-1] + x)
    raw = -3 * n * weights[0] + 2 * sum((n - d) * weights[d] for d in range(1, T))
    for i, r_it in enumerate(rows):
        a, cap = r_it[0], r_it[1]
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
        a, cap = rows[i][0], rows[i][1]
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


# ---------------------------------------------------------------------------
# 5. Zero-rainbow proper 4-color square witnesses S_6..S_10 (Route A closure)
# ---------------------------------------------------------------------------

def verify_zero_rainbow_witnesses(wit_path):
    wits = json.loads(wit_path.read_text())
    for m in (6, 7, 8, 9, 10):
        entry = wits[str(m)]
        grid = entry["rows"]
        need(entry["domain"] == "square" and entry["k"] == 4 and entry["n"] == m and len(grid) == m and all(len(row) == m for row in grid), f"bad witness shape m={m}")
        need(all(type(c) is int and 0 <= c < 4 for row in grid for c in row), f"invalid color in m={m}")
        mono_sq = 0
        rain_sq = 0
        rain_T = 0
        for x in range(m):
            for y in range(m):
                for d in range(1, m):
                    if x + d < m and y + d < m:
                        s = {grid[x][y], grid[x + d][y], grid[x + d][y + d]}
                        if len(s) == 1:
                            mono_sq += 1
                        elif len(s) == 3:
                            rain_sq += 1
                            if y < x:
                                rain_T += 1
        need(mono_sq == 0, f"monochromatic L in S_{m} witness")
        need(rain_T == 0 and entry["rainbows_in_T_m"] == 0, f"nonzero rainbow L in T_{m}")
        need(rain_sq == entry["rainbows_in_S_m"], f"S_{m} rainbow count mismatch")
        if entry["zero_rainbows_in_full_square"]:
            need(rain_sq == 0, f"expected 0 rainbows in full S_{m}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--window", type=Path, default=HERE / "window_tables", help="path to pinned window matrices (default: ./window_tables)")
    parser.add_argument("--pure-python", action="store_true", help="verify RUP traces using the embedded pure-Python checker without C compilation")
    args = parser.parse_args()

    t0 = time.monotonic()
    data = json.loads(lzma.decompress((HERE / "certificate.json.xz").read_bytes()))
    need(data["width"] == T, "unexpected outer width")

    den = int(data["window_denominator"])
    r = list(map(int, data["window_correlations"]))
    alpha = F(data["window_table_excess"])
    G_int, H, pi = load_and_verify_window(args.window, data["rational_window_inputs"], den, r, alpha)
    print(f"[1] Verified window_tables/{{G,H,p}}.txt SHA-256, correlations, excess, and 401 coverages ({time.monotonic()-t0:.2f}s).", flush=True)

    t1 = time.monotonic()
    g_ver = verify_small_golomb_seeds(data["gol_seeds"])
    gol = audit_golomb_spans(g_ver, data["gol_wit_c"], data["gol_limit"])
    verify_rup_manifest_and_binary_spans(
        HERE / "rup_manifest.json",
        HERE / "rup_proofs",
        HERE / "rup_check.c",
        data["b_seeds"],
        data["b_spans"],
        data["b_wit_rnk"],
        gol,
        pure_python=args.pure_python,
    )
    b_spans = data["b_spans"]
    print(f"[2] Verified g_2..g_10, e_2..e_16 RUP proofs, Golomb ({len(gol)-1:,}) & nonuniform binary ({len(b_spans)-1:,}, max={b_spans[-1]:,}) spans ({time.monotonic()-t1:.2f}s).", flush=True)

    t2 = time.monotonic()
    cap_inn = lambda u: 0 if u <= 0 else min(old_cap(u, False), bisect_right(gol, u - 1) - 1)
    cap_bin = lambda u: 0 if u <= 0 else min(old_cap(u, True), bisect_right(b_spans, u - 1) - 1)
    verify_farkas_bands(data["inner_bands"], G_int, H, pi, alpha, cap_inn, gol[-1])
    verify_farkas_bands(data["binary_bands"], G_int, H, pi, alpha, cap_bin, b_spans[-1])
    verify_inner_thresholds(data["inner_thresholds"], data["inner_witness_B_band"], data["inner_bands"], den, r, alpha)
    audit_rows(data["rows"], data["binary_bands"], data["inner_thresholds"], den, r, alpha)
    print(f"[3] Verified {len(data['inner_bands'])} inner + {len(data['binary_bands'])} exact-B binary MCF Farkas bands, 201 Golomb thresholds, and {len(data['rows'])} binary rows ({time.monotonic()-t2:.2f}s).", flush=True)

    t3 = time.monotonic()
    tiers = []
    tot_boxes = 0
    for tier in data.get("outer_tiers_3seg", []):
        verify_3seg_kdtree_tier(tier)
        tiers.append((tier["S"], tier["loss"]))
        tot_boxes += sum(len(p["boxes"]) for p in tier["partitions"])
    for tier in data["outer_tiers_2seg"]:
        verify_2seg_kdtree_tier(tier)
        tiers.append((tier["S"], tier["loss"]))
        tot_boxes += sum(len(p["boxes"]) for p in tier["partitions"])
    fb20 = data["outer_fallback_20"]
    need(fb20["S"] == 20 and twenty_loss() == fb20["loss"], "twenty-shift fallback mismatch")
    tiers.append((20, fb20["loss"]))
    print(f"[4] Verified outer KD-tree DP tiers ({tot_boxes} boxes, main S={tiers[0][0]}->loss>={tiers[0][1]}) ({time.monotonic()-t3:.2f}s).", flush=True)

    weights = correlations()
    for side, key in ((data["side"], "result"), (data["side"] - 1, "preceding_side_result")):
        res = outer_multiscale(data["rows"], side, weights, tiers)
        need(res == data[key], f"outer result mismatch at side {side}")
        print(f"[5] Side {side:,}: blocks={res['blocks']} ({res['tier_counts']}), exact margin = {res['margin']:,}", flush=True)
    need(data["result"]["margin"] > 0 and data["preceding_side_result"]["margin"] < 0, "expected strict sign change at certified side")

    verify_zero_rainbow_witnesses(HERE / "zero_rainbow_witnesses.json")
    print(f"[6] Verified zero-rainbow proper 4-color square witnesses S_6..S_10 (rho_6^(4)=...=rho_10^(4)=0).", flush=True)
    print(f"VERIFIED: R_4(L) <= {data['side']:,} (total time {time.monotonic()-t0:.2f}s).", flush=True)


if __name__ == "__main__":
    main()
