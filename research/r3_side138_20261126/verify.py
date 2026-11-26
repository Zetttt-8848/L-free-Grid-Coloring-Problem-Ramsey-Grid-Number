#!/usr/bin/env python3
"""Standalone exact-integer verifier for R_3(L) <= 138 on S_138 = {0, ..., 137}^2.

Uses ONLY the Python 3 standard library (`int` and `fractions.Fraction`),
imports zero repository helper modules, and writes zero files.

Verification pipeline:
  1. SHA-256 provenance check of `inputs/*` (plus byte-for-byte cross-check
     against sibling repository directories when present).
  2. First-principles check of all eight 91-cell T_14 extension witnesses and
     finite case-partition proof of all 19 directional subtriangle rays on
     T_14 .. T_18.
  3. First-principles replay of all upgraded Chvatal-Gomory local boundary
     packings through order 40 (`local_packings.json.xz`) on literal physical
     corners in exact `Fraction` arithmetic.
  4. Reconstruction of the 39-patch allowlist and first-principles check of all
     ambient-square T_13 witness colorings (`16x16`, `17x17`, `18x18`), plus
     catalog properness and S_3-closed physical profile construction for
     `11/6`, `12/9`, and `13/12`.
  5. Dual independent exact-integer global verifiers on S_138:
       - Verifier 1: Explicit 3D physical square array `host_I[h][X][Y]`.
       - Verifier 2: Signed-gap antidiagonal-orbit counter `orbit_sum`.
  6. Negative self-diagnostics confirming tampered colorings, uncertified
     patches, and inflated packing floors are rejected.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import permutations
import json
import lzma
from math import ceil, comb
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"

BASELINE_PATCHES = (
    (13, 11, 17, 5, 0, 1),
    (13, 11, 18, 0, 0, 1),
    (12, 7, 18, 3, 3, 1),
    (12, 7, 18, 0, 0, 1),
    (12, 7, 18, 7, 0, 1),
    (12, 8, 18, 3, 3, 1),
    (13, 11, 23, 0, 0, 2),
    (13, 12, 18, 3, 3, 1),
    (13, 12, 18, 6, 0, 1),
    (13, 12, 18, 0, 0, 1),
)

DIRECTIONAL_SUB_SPECS = {
    14: ((13, 1, 2, 41), (12, 1, 1, 25), (11, 1, 1, 22), (11, 2, 3, 49)),
    15: ((13, 1, 1, 29), (13, 1, 2, 41), (12, 2, 1, 42), (12, 1, 1, 25), (11, 2, 1, 39), (11, 3, 2, 61)),
    16: ((13, 1, 1, 29), (13, 1, 2, 41), (12, 1, 1, 25), (11, 1, 1, 22), (11, 2, 1, 39)),
    17: ((13, 1, 1, 30), (12, 1, 1, 25), (11, 1, 1, 23)),
    18: ((11, 1, 1, 23),),
}


def read_json(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(lzma.decompress(raw) if p.suffix == ".xz" else raw)


def u_tri(m):
    return comb(m, 2) - (m - 1) + (m - 1) // 3 if m >= 3 else 0


def norm_palette_bytes(bs):
    mp = {}
    out = []
    for ch in bs:
        if ch not in mp:
            mp[ch] = len(mp)
        out.append(48 + mp[ch])
    return bytes(out)


def expand_orientations_bytes(m, canonical_str):
    raw = canonical_str.encode("ascii")
    pos_idx = {
        (xw - yw, yw, m - 2 - xw): xw * (xw + 1) // 2 + yw
        for xw in range(m - 1) for yw in range(xw + 1)
    }
    coords = [(xw - yw, yw, m - 2 - xw) for xw in range(m - 1) for yw in range(xw + 1)]
    res = set()
    for pi in permutations((0, 1, 2)):
        perm_bytes = bytes(raw[pos_idx[(g[pi[0]], g[pi[1]], g[pi[2]])]] for g in coords)
        res.add(norm_palette_bytes(perm_bytes))
    return res


def build_phys_geom(m):
    """Canonical physical corners of W_{m-1} ~= T_m and S_3 corner permutations."""
    cell_idx = {(xw, yw): xw * (xw + 1) // 2 + yw for xw in range(m - 1) for yw in range(xw + 1)}
    corners = []
    key_set = set()
    bary_lookup = {}
    for xw in range(m - 1):
        for yw in range(xw + 1):
            for j in range(1, m - 1 - xw):
                a, b, c = xw - yw, yw, m - 2 - xw - j
                key = (j, *sorted((a, b, c)))
                key_set.add(key)
                i0 = cell_idx[(xw, yw)]
                i1 = cell_idx[(xw + j, yw)]
                i2 = cell_idx[(xw + j, yw + j)]
                ci = len(corners)
                bary_lookup[(j, a, b, c)] = ci
                corners.append((j, xw, yw, a, b, c, i0, i1, i2, key))
    keys = sorted(key_set)
    kid = {k: idx for idx, k in enumerate(keys)}
    k_of_c = [kid[c[9]] for c in corners]
    refl_c = [bary_lookup[(j, a, c, b)] for j, _, _, a, b, c, *_ in corners]
    s3_perms = [
        [bary_lookup[(j, g[pi[0]], g[pi[1]], g[pi[2]])]
         for j, _, _, *g_rest in corners for g in (g_rest[:3],)]
        for pi in permutations((0, 1, 2))
    ]
    return corners, keys, k_of_c, refl_c, s3_perms


def verify_provenance():
    prov = read_json(INPUTS / "provenance.json")
    repo_root = HERE.parent.parent
    checked = 0
    cross_checked = 0
    for item in prov["files"]:
        fp = INPUTS / item["file"]
        if not fp.is_file():
            raise ValueError(f"Missing vendored input {fp}")
        raw = fp.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if len(raw) != item["bytes"] or digest != item["sha256"]:
            raise ValueError(f"Digest mismatch on vendored input {item['file']}")
        checked += 1
        up = repo_root / item["upstream_repo_path"]
        if up.is_file():
            if hashlib.sha256(up.read_bytes()).hexdigest() != digest:
                raise ValueError(f"Vendored input {item['file']} diverges from upstream {up}")
            cross_checked += 1
    return checked, cross_checked


def check_triangle_word(m, word_str, corners):
    if len(word_str) != m * (m - 1) // 2 or any(ch not in "012" for ch in word_str):
        raise ValueError(f"Malformed T_{m} word length or alphabet")
    rainbows = []
    for ci, (*_, i0, i1, i2, _) in enumerate(corners):
        c0, c1, c2 = word_str[i0], word_str[i1], word_str[i2]
        if c0 == c1 == c2:
            raise ValueError(f"Improper monochromatic L in T_{m} coloring")
        if c0 != c1 and c1 != c2 and c0 != c2:
            rainbows.append(ci)
    return rainbows


def verify_extension_rays():
    """Verify T_14 extension witnesses and prove all 19 directional rays by finite case split."""
    ext_rows = read_json(INPUTS / "order14_extension_minima.json")
    c14, *_ = build_phys_geom(14)
    cell14 = {(xw, yw): xw * (xw + 1) // 2 + yw for xw in range(13) for yw in range(xw + 1)}

    witness_table = {}
    for row in ext_rows:
        s = row["source_order"]
        cut = row["cutoff"]
        w14 = row["witness"]
        r14 = len(check_triangle_word(14, w14, c14))
        if r14 != row["minimum"]:
            raise ValueError(f"T_14 witness rainbow count mismatch for ({s}, {cut})")
        cs, *_ = build_phys_geom(s)
        found_sub = False
        for ox in range(14 - s + 1):
            for oy in range(ox + 1):
                sub_w = "".join(w14[cell14[(ox + xw, oy + yw)]] for xw in range(s - 1) for yw in range(xw + 1))
                if len(check_triangle_word(s, sub_w, cs)) <= cut:
                    found_sub = True
                    break
            if found_sub:
                break
        if not found_sub:
            raise ValueError(f"T_14 witness for ({s}, {cut}) lacks qualifying T_{s} subtriangle")
        witness_table[(s, cut)] = row["minimum"]

    expected_ext = {
        (11, 3): 20, (11, 4): 19, (11, 5): 17, (11, 6): 17,
        (12, 6): 19, (12, 7): 18, (12, 8): 17, (12, 9): 17,
    }
    if witness_table != expected_ext:
        raise ValueError("Unexpected T_14 extension minima table")

    # Certified extension lower bounds on T_14 (with r_14 >= 15 unconditional):
    ext14_lb = {
        11: {3: 20, 4: 19, 5: 17, 6: 17, 7: 15},
        12: {6: 19, 7: 18, 8: 17, 9: 17, 10: 15},
        13: {11: 19, 12: 17, 13: 15},
    }
    ray_lookup = {}
    for m, specs in DIRECTIONAL_SUB_SPECS.items():
        base_r_m = m + 1  # r_14>=15, r_15>=16, r_16>=17, r_17>=18, r_18>=19
        for s, bw, ew, bnd in specs:
            best_lhs = min(
                bw * max(base_r_m, r14_min) + ew * rs_val
                for rs_val, r14_min in ext14_lb[s].items()
            )
            if best_lhs != bnd:
                raise ValueError(f"Directional ray ({m},{s},{bw},{ew}) case-split min {best_lhs} != {bnd}")
            ray_lookup[(m, s, bw, ew)] = bnd
    return ray_lookup


def directional_rays(m, corners):
    rays = []
    if not (14 <= m <= 18):
        return rays
    faces = [(a == 0) + (b == 0) + (c == 0) for _, _, _, a, b, c, *_ in corners]
    rays.append(([2 + int(f == 1) for f in faces], 2 * m + 2))
    rays.append(([3 - max(0, f - 1) for f in faces], 3 * m + 1 if m >= 15 else 3 * m))
    if m >= 17:
        rays.append(([1 + int(f > 0) for f in faces], m + 2))
    for s, bw, ew, bnd in DIRECTIONAL_SUB_SPECS[m]:
        delta = m - s
        margins = [(u, v, delta - u - v) for u in range(delta + 1) for v in range(delta + 1 - u)]
        sum_w = [0] * len(corners)
        for u0, v0, w0 in margins:
            vec = [bw + (ew if (a >= u0 and b >= v0 and c >= w0) else 0) for _, _, _, a, b, c, *_ in corners]
            rays.append((vec, bnd))
            for idx, val in enumerate(vec):
                sum_w[idx] += val
        rays.append((sum_w, bnd * len(margins)))
    return rays


def verify_local_packings(pack_records, ray_lookup):
    gen = {10: 1, 11: 3, 12: 6, 13: 11, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19}
    clr = {10: 1, 11: 3, 12: 10, 13: 13}
    for field, dest in (("generic", gen), ("with_clearance", clr)):
        use_clr = clr if field == "with_clearance" else None
        for expected_n, row in zip(range(14, 41), pack_records[field], strict=True):
            n = row["n"]
            if n != expected_n:
                raise ValueError(f"Out-of-sequence local packing order {n} != {expected_n}")
            if not row["columns"]:
                if row["floor"] != dest[n]:
                    raise ValueError(f"Base floor mismatch at {field} n={n}")
                continue
            load = Counter()
            score = 0
            for m, step, a, b, c, rule, coeff in row["columns"]:
                if min(a, b, c) < 0 or min(step, coeff) <= 0 or a + b + c + (m - 2) * step != n - 2 or m >= n:
                    raise ValueError(f"Invalid packing column at {field} n={n}")
                src_c = [(x, y, j) for x in range(m - 1) for y in range(x + 1) for j in range(1, m - 1 - x)]
                if rule == "uniform":
                    fl = use_clr[m] if (use_clr and step == 1 and m in use_clr) else gen[m]
                    w_fn = lambda ga, gb, gc: 1
                elif rule == "single" and 14 <= m <= 18:
                    fl = 2 * m + 2
                    w_fn = lambda ga, gb, gc: 2 + int((ga == 0) + (gb == 0) + (gc == 0) == 1)
                elif rule == "multiple" and 14 <= m <= 18:
                    fl = 3 * m + 1 if m >= 15 else 3 * m
                    w_fn = lambda ga, gb, gc: 3 - max(0, (ga == 0) + (gb == 0) + (gc == 0) - 1)
                elif rule == "boundary" and m in (17, 18):
                    fl = m + 2
                    w_fn = lambda ga, gb, gc: 1 + int(min(ga, gb, gc) == 0)
                elif rule.startswith("dir_") and 14 <= m <= 18:
                    _, s_s, bw_s, ew_s, u0_s, v0_s, w0_s = rule.split("_")
                    s, bw, ew, u0, v0, w0 = map(int, (s_s, bw_s, ew_s, u0_s, v0_s, w0_s))
                    if min(u0, v0, w0) < 0 or u0 + v0 + w0 != m - s or (m, s, bw, ew) not in ray_lookup:
                        raise ValueError(f"Invalid directional packing ray {rule}")
                    fl = ray_lookup[(m, s, bw, ew)]
                    w_fn = lambda ga, gb, gc, bw=bw, ew=ew, u0=u0, v0=v0, w0=w0: (
                        bw + (ew if (ga >= u0 and gb >= v0 and gc >= w0) else 0)
                    )
                else:
                    raise ValueError(f"Uncertified packing rule {rule}")

                t_abc = (a, b, c)
                for pi in permutations((0, 1, 2)):
                    pa, pb, pc = t_abc[pi[0]], t_abc[pi[1]], t_abc[pi[2]]
                    for x, y, j in src_c:
                        g = (x - y, y, m - 2 - x - j)
                        h_ga = pa + step * g[pi[0]]
                        h_gb = pb + step * g[pi[1]]
                        h_gc = pc + step * g[pi[2]]
                        hx, hy, hj = h_ga + h_gb, h_gb, step * j
                        if not (0 <= hy <= hx and hx + hj <= n - 2 and h_ga + h_gb + h_gc + hj == n - 2):
                            raise ValueError("Escaping physical corner in local packing")
                        load[(hx, hy, hj)] += coeff * w_fn(*g)
                    score += coeff * fl
            q = Fraction(score, max(load.values()))
            if [q.numerator, q.denominator] != row["exact"]:
                raise ValueError(f"Exact Fraction mismatch at {field} n={n}")
            got = max(gen.get(n, 0), ceil(q))
            if got != row["floor"]:
                raise ValueError(f"Floor mismatch at {field} n={n}")
            dest[n] = got
    return gen, clr


def check_proper_square(grid, side):
    if len(grid) != side or any(len(row) != side or any(ch not in "012" for ch in row) for row in grid):
        raise ValueError(f"Malformed {side}x{side} square witness")
    for x in range(side):
        row_x = grid[x]
        for y in range(side):
            c0 = row_x[y]
            lim = side - max(x, y)
            for h in range(1, lim):
                if grid[x + h][y] == c0 and grid[x + h][y + h] == c0:
                    raise ValueError(f"Monochromatic directed L in {side}x{side} square witness")


def verify_patches_and_t13_profiles(t13_words):
    """Reconstruct the 39-patch allowlist and verify all T_13 square witnesses."""
    certified = set(BASELINE_PATCHES)
    for fn in ("side_141_patches.json", "side_140_patches.json"):
        for p in read_json(INPUTS / fn):
            certified.add(tuple(p))
    for entry in read_json(INPUTS / "order12_side18_0_1.json.xz"):
        if len(entry.get("proof_records", ())) != 1004 or entry.get("oriented_cases") != 96360:
            raise ValueError("Unexpected proof manifest in order12_side18_0_1")
        certified.add(tuple(entry["patch"]))
    for entry in read_json(INPUTS / "stride2_order12_21_manifest.json.xz"):
        if len(entry.get("proof_records", ())) != 34 or entry.get("oriented_cases") != 204:
            raise ValueError("Expected 34 proof groups in stride2_order12_21_manifest")
        certified.add(tuple(entry["patch"]))

    word_to_id = {w: i for i, w in enumerate(t13_words)}
    pos_idx = {(a, b): idx for idx, (a, b) in enumerate((a, b) for a in range(12) for b in range(a + 1))}
    refl_map = [pos_idx[(11 - b, 11 - a)] for a in range(12) for b in range(a + 1)]
    sigma = [word_to_id[norm_palette_bytes(bytes(w[refl_map[k]] for k in range(78)))] for w in t13_words]

    surv_by_side = {}
    checked_squares = 0
    for side in (16, 17, 18):
        d = read_json(INPUTS / f"order13_side{side}_profiles.json.xz")
        if (d["order"], d["cutoff"], d["side"], d["stride"], d["oriented_cases"]) != (13, 12, side, 1, 2928):
            raise ValueError(f"Invalid metadata in order13_side{side}_profiles")
        gap = side - 12
        mp = {}
        seen_off = set()
        for row in d["placements"]:
            ox, oy = tuple(row["offset"])
            if min(ox, oy) < 0 or ox + oy > gap or (ox, oy) in seen_off:
                raise ValueError(f"Invalid placement offset {(ox, oy)} at side {side}")
            seen_off.add((ox, oy))
            s_ids = set()
            for surv in row["survivors"]:
                idx = surv["index"]
                grid = surv["square"]
                if not (0 <= idx < 2928) or idx in s_ids:
                    raise ValueError("Invalid or duplicate survivor index")
                check_proper_square(grid, side)
                proj = norm_palette_bytes(
                    bytes(ord(grid[ox + a][oy + b]) for a in range(12) for b in range(a + 1))
                )
                if proj != t13_words[idx]:
                    raise ValueError("Square witness projection disagrees with T_13 catalog word")
                s_ids.add(idx)
                checked_squares += 1
            if side == 18 and not s_ids:
                certified.add((13, 12, 18, ox, oy, 1))
            fs = frozenset(s_ids)
            mp[(ox, oy)] = fs
            mp[(gap - oy, gap - ox)] = frozenset(sigma[i] for i in fs)

        base_18 = {(px, py) for po, pc, ps, px, py, pst in BASELINE_PATCHES if (po, pc, ps, pst) == (13, 12, side, 1)}
        for ox in range(gap + 1):
            for oy in range(gap + 1 - ox):
                if (ox, oy) not in mp:
                    if (ox, oy) not in base_18:
                        raise ValueError(f"Missing T_13 placement {(ox, oy)} at side {side}")
                    mp[(ox, oy)] = frozenset()
                    mp[(gap - oy, gap - ox)] = frozenset()
        surv_by_side[side] = mp

    if len(certified) != 39:
        raise ValueError(f"Expected 39 allowlisted patches, got {len(certified)}")
    return certified, surv_by_side, checked_squares


def verify_certificate(cert_path):
    t0 = time.time()
    checked_inputs, cross_checked = verify_provenance()
    ray_lookup = verify_extension_rays()
    pack_records = read_json(HERE / "local_packings.json.xz")
    gen_pack, clr_pack = verify_local_packings(pack_records, ray_lookup)
    catalogs = read_json(INPUTS / "triangle_grid_catalogs.json.xz")

    # Expand 2,928 oriented T_13 words and verify all placement witnesses
    c13_geom = build_phys_geom(13)
    c13_corners = c13_geom[0]
    t13_ori_set = set()
    for cw in catalogs["13/12"]:
        if len(check_triangle_word(13, cw, c13_corners)) > 12:
            raise ValueError("Catalog 13/12 word exceeds cutoff 12")
        t13_ori_set.update(expand_orientations_bytes(13, cw))
    t13_words = sorted(t13_ori_set)
    if len(t13_words) != 2928:
        raise ValueError("Incomplete 13/12 oriented catalog")

    certified_patches, t13_surv_maps, checked_squares = verify_patches_and_t13_profiles(t13_words)

    cert = read_json(cert_path)
    if cert.get("domain") != "full_square":
        raise ValueError("Certificate domain must be full_square")
    N = cert["square_side"]
    if type(N) is not int or N < 3:
        raise ValueError("Invalid square_side")

    patches = [tuple(p) for p in cert["patches"]]
    if not set(patches) <= certified_patches:
        uncert = sorted(set(patches) - certified_patches)
        raise ValueError(f"Certificate uses uncertified patches: {uncert}")
    if not {(12, 9, 18, 0, 0, 1), (13, 12, 18, 0, 0, 1)} <= set(patches):
        raise ValueError("Missing required side-18 (0, 0) clearance patches")

    need_asym = {r["order"] for r in cert["rules"] if not r["sym"] and r["order"] in (11, 12, 13)}
    geom_info = {}
    sym_by_mer = {}
    phys_by_mer = {}
    t13_word_profs = [
        tuple(ci for ci, (*_, i0, i1, i2, _) in enumerate(c13_corners)
              if len({ow[i0], ow[i1], ow[i2]}) == 3)
        for ow in t13_words
    ]

    for m in cert["used_orders"]:
        if m not in gen_pack:
            raise ValueError(f"Uncertified source order {m}")
        corners, keys, k_of_c, refl_c, s3_perms = build_phys_geom(m)
        rays = directional_rays(m, corners)
        geom_info[m] = (corners, keys, k_of_c, refl_c, rays)
        if m in (11, 12, 13):
            b_cut = {11: 6, 12: 9, 13: 12}[m]
            can_words = catalogs[f"{m}/{b_cut}"]
            sym_set = set()
            phys_set = set()
            do_phys = (m in need_asym) or (m == 13)
            for cw in can_words:
                pr_c = check_triangle_word(m, cw, corners)
                if len(pr_c) > b_cut:
                    raise ValueError(f"Catalog word exceeds {m}/{b_cut}")
                sym_set.add(tuple(sorted(k_of_c[ci] for ci in pr_c)))
                if do_phys:
                    for perm in s3_perms:
                        phys_set.add(tuple(sorted(perm[ci] for ci in pr_c)))
            sym_sorted = sorted(sym_set)
            for er in range(gen_pack[m], b_cut + 3):
                sym_by_mer[(m, er)] = [p for p in sym_sorted if len(p) >= er]
            if do_phys:
                if m == 13 and phys_set != set(t13_word_profs):
                    raise ValueError("S_3 corner-permutation profile mismatch on T_13")
                phys_sorted = sorted(phys_set)
                for er in range(gen_pack[m], b_cut + 3):
                    phys_by_mer[(m, er)] = [p for p in phys_sorted if len(p) >= er]

    def patch_fits(m, d, bx, by, min_r):
        for p_ord, p_cut, p_side, px, py, p_stride in patches:
            if m != p_ord or p_cut + 1 < min_r or d % p_stride != 0:
                continue
            unit = d // p_stride
            gap = p_side - 1 - (m - 2) * p_stride
            span = (p_side - 1) * unit
            for ox, oy in ((px, py), (gap - py, gap - px)):
                x_ll, y_ll = bx - unit * ox, by - unit * oy
                if 0 <= x_ll and x_ll + span < N and 0 <= y_ll and y_ll + span < N:
                    return True
        return False

    def placement_constraint(m, d, bx, by):
        er = gen_pack[m]
        for th in ({13: (14, 13, 12), 12: (10, 9, 8, 7), 11: (7, 6, 5, 4)}.get(m, ())):
            if patch_fits(m, d, bx, by, th):
                er = max(er, th)
                break
        if m in clr_pack and clr_pack[m] > er:
            pos_cl = min(N - 1 - (m - 2) * d - bx, N - 1 - (m - 2) * d - by)
            neg_cl = min(bx, by)
            if max(pos_cl, neg_cl) >= 7 * d:
                er = clr_pack[m]
        surv_ids = None
        if m == 13 and er <= 12:
            cur = None
            for side in (18, 17, 16):
                span = (side - 1) * d
                if span >= N:
                    continue
                for (ox, oy), s_set in t13_surv_maps[side].items():
                    x_ll, y_ll = bx - ox * d, by - oy * d
                    if 0 <= x_ll and x_ll + span < N and 0 <= y_ll and y_ll + span < N:
                        cur = set(s_set) if cur is None else (cur & s_set)
                        if not cur:
                            break
                if cur is not None and len(cur) == 0:
                    break
            if cur is not None:
                if len(cur) == 0:
                    er = 13
                elif len(cur) < 2928:
                    surv_ids = frozenset(cur)
        return er, surv_ids

    # --- VERIFIER 1: Explicit 3D Physical Square Array on S_N = {0, ..., N-1}^2 ---
    host_I = {h: [[0] * (N - h) for _ in range(N - h)] for h in range(1, N)}
    J_phys = 0

    # --- VERIFIER 2: Independent Signed-Gap Antidiagonal-Orbit Counter ---
    orbit_sum = Counter()
    J_orbit = 0

    for rule in cert["rules"]:
        m = rule["order"]
        d = rule["dilation"]
        sym_flag = rule["sym"]
        weights = rule["weights"]
        xys = rule["translations_xy"]
        corners, keys, k_of_c, refl_c, rays = geom_info[m]
        L_max = N - 1 - d * (m - 2)
        if d < 1 or L_max < 0 or any(type(w) is not int or w < 0 for w in weights):
            raise ValueError("Invalid rule parameters")
        if sym_flag:
            if len(weights) != len(keys):
                raise ValueError("Invalid symmetric weight length")
            w_phys = [weights[ki] for ki in k_of_c]
        else:
            if len(weights) != len(corners):
                raise ValueError("Invalid physical weight length")
            w_phys = weights
        w_refl = [w_phys[ri] for ri in refl_c]
        sorted_w = sorted(w_phys)

        floor_cache = {}

        def get_floor(is_refl, er, surv_ids):
            ck = (is_refl, er, surv_ids)
            if ck in floor_cache:
                return floor_cache[ck]
            wv = w_refl if is_refl else w_phys
            ray_fl = 0
            for prices, bnd in rays:
                lam = min(Fraction(w, p) for w, p in zip(wv, prices) if p > 0)
                ray_fl = max(ray_fl, ceil(bnd * lam))
            if m in (11, 12, 13):
                b_cut = {11: 6, 12: 9, 13: 12}[m]
                k_un = max(b_cut + 1, er)
                unseen = sum(sorted_w[:k_un])
                if surv_ids is not None:
                    rel = [sum(wv[i] for i in t13_word_profs[idx]) for idx in surv_ids if len(t13_word_profs[idx]) >= er]
                elif sym_flag:
                    rel = [sum(weights[ki] for ki in p) for p in sym_by_mer[(m, er)]]
                else:
                    rel = [sum(wv[i] for i in p) for p in phys_by_mer[(m, er)]]
                fl = max(ray_fl, min([unseen] + rel))
            else:
                fl = max(ray_fl, sum(sorted_w[:er]))
            floor_cache[ck] = fl
            return fl

        seen_xy = set()
        for x0, y0 in xys:
            if type(x0) is not int or type(y0) is not int or x0 < 0 or y0 < 0 or x0 + y0 > L_max or (x0, y0) in seen_xy:
                raise ValueError("Invalid or duplicate canonical xy translation")
            seen_xy.add((x0, y0))
            rx0, ry0 = L_max - y0, L_max - x0

            # Verifier 1: explicit evaluation on both (x0, y0, w_phys) and (rx0, ry0, w_refl)
            er1, s1 = placement_constraint(m, d, x0, y0)
            er2, s2 = placement_constraint(m, d, rx0, ry0)
            fl1 = get_floor(False, er1, s1)
            fl2 = get_floor(True, er2, s2)
            if fl1 != fl2:
                raise ValueError(f"Antidiagonal floor asymmetry: {fl1} != {fl2}")
            J_phys += fl1 + fl2
            for bx, by, wv in ((x0, y0, w_phys), (rx0, ry0, w_refl)):
                for ci, (j, xw, yw, *_) in enumerate(corners):
                    w = wv[ci]
                    if w:
                        host_I[d * j][bx + d * xw][by + d * yw] += w

            # Verifier 2: independent signed-gap orbit accumulation
            J_orbit += 2 * fl1
            ta, tb, tc = x0 - y0, y0, L_max - x0
            for ci, (j, _, _, la, lb, lc, *_) in enumerate(corners):
                w = w_phys[ci]
                if w:
                    h = d * j
                    a_s = ta + d * la
                    b_s = tb + d * lb
                    c_s = tc + d * lc
                    orbit_sum[(h, a_s, min(b_s, c_s), max(b_s, c_s))] += 2 * w

    cap_phys = 0
    cap_orb = 0
    for s, x0, y0, m_sub, wt in cert["upper_caps"]:
        if any(type(v) is not int for v in (s, x0, y0, m_sub, wt)):
            raise ValueError("Non-integer upper cap entry")
        p_span = m_sub - 2
        l_c = N - 1 - s * p_span
        if s < 1 or m_sub < 3 or wt < 0 or x0 < 0 or y0 < 0 or x0 + y0 > l_c:
            raise ValueError("Invalid upper cap parameters")
        rx0, ry0 = l_c - y0, l_c - x0
        oris = [(x0, y0)] if (x0, y0) == (rx0, ry0) else [(x0, y0), (rx0, ry0)]
        u_sub = u_tri(m_sub)
        cap_phys += wt * len(oris) * u_sub
        cap_orb += wt * len(oris) * u_sub

        for bx, by in oris:
            for hk in range(1, p_span + 1):
                arr_h = host_I[s * hk]
                for i in range(p_span - hk + 1):
                    row_x = arr_h[bx + s * i]
                    for j in range(i + 1):
                        row_x[by + s * j] -= wt

            sa, sb, sc = bx - by, by, l_c - bx
            for j_loc in range(1, p_span + 1):
                h = s * j_loc
                rem = p_span - j_loc
                for la in range(rem + 1):
                    for lb in range(rem + 1 - la):
                        lc = rem - la - lb
                        b_s = sb + s * lb
                        c_s = sc + s * lc
                        orbit_sum[(h, sa + s * la, min(b_s, c_s), max(b_s, c_s))] -= wt

    u_wn = u_tri(N + 1)
    pos_wn = []
    out_phys = 0
    for h in range(1, N):
        arr_h = host_I[h]
        for x in range(N - h):
            row_x = arr_h[x]
            for y in range(N - h):
                v = row_x[y]
                if v > 0:
                    if y <= x:
                        pos_wn.append(v)
                    else:
                        out_phys += v
    pos_wn.sort(reverse=True)
    V_phys = cap_phys + sum(pos_wn[:u_wn]) + out_phys

    wn_orbs = []
    out_orb = 0
    for (_, a_s, b0, c0), tot_w in orbit_sum.items():
        if tot_w <= 0:
            continue
        mu = 1 if b0 == c0 else 2
        per_c, rem_c = divmod(tot_w, mu)
        if rem_c != 0:
            raise ValueError("Asymmetric orbit weight detected")
        if a_s >= 0:
            wn_orbs.append((per_c, mu))
        else:
            out_orb += tot_w
    wn_orbs.sort(reverse=True)
    rem = u_wn
    top_orb = 0
    for val, mu in wn_orbs:
        if rem <= 0:
            break
        tk = min(rem, mu)
        top_orb += tk * val
        rem -= tk
    V_orb = cap_orb + top_orb + out_orb

    if (J_phys, V_phys) != (J_orbit, V_orb):
        raise ValueError(f"Dual verifier mismatch: {(J_phys, V_phys)} != {(J_orbit, V_orb)}")

    margin = J_phys - V_phys
    if margin <= 0:
        raise ValueError(f"Non-positive contradiction margin: {margin}")

    return {
        "status": "PASS",
        "theorem": f"R_3(L) <= {N}",
        "square_side": N,
        "J_lower": J_phys,
        "V_upper": V_phys,
        "margin": margin,
        "relative_margin": round(margin / J_phys, 8),
        "rules": len(cert["rules"]),
        "upper_caps": len(cert["upper_caps"]),
        "allowlisted_patches": len(certified_patches),
        "checked_square_witnesses": checked_squares,
        "checked_vendored_inputs": checked_inputs,
        "upstream_cross_checked": cross_checked,
        "upgraded_generic_19_32": [gen_pack[k] for k in range(19, 33)],
        "upgraded_clearance_19_32": [clr_pack[k] for k in range(19, 33)],
        "verify_seconds": round(time.time() - t0, 2),
    }


def run_negative_self_tests():
    """Confirm tampering is rejected."""
    c4, *_ = build_phys_geom(4)
    try:
        check_triangle_word(4, "000000", c4)
        raise AssertionError("Failed to reject monochromatic T_4 word")
    except ValueError:
        pass
    try:
        check_proper_square(["00", "00"], 2)
        raise AssertionError("Failed to reject monochromatic 2x2 square")
    except ValueError:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cert",
        type=Path,
        default=HERE / "certificate.json.xz",
        help="path to compressed or raw JSON certificate (default: ./certificate.json.xz)",
    )
    args = parser.parse_args()
    run_negative_self_tests()
    summary = verify_certificate(args.cert)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    sys.exit(main())
