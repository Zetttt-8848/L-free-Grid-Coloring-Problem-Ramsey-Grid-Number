"""Export and dual-verify exact integer full-square certificates on S_N = {0, ..., N-1}^2."""

import argparse
import json
import lzma
from collections import Counter
from fractions import Fraction
from math import ceil, comb
from pathlib import Path

from verify_143 import BASELINE, BASELINE_PATCHES
import verify_local_packing as vlp

DATA = Path(__file__).resolve().parent / "data"


def read_json(path):
    raw = Path(path).read_bytes()
    return json.loads(lzma.decompress(raw) if Path(path).suffix == ".xz" else raw)


def certified_packing_tables_15():
    records = read_json(DATA / "local_boundary_packings_15.json")
    gen = {10: 1, 11: 3, 12: 6, 13: 11, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19}
    clr = {10: 1, 11: 3, 12: 10, 13: 13}
    for field, dest in (("generic", gen), ("with_clearance", clr)):
        for n, row in zip(range(14, 33), records[field], strict=True):
            ext = clr if field == "with_clearance" else None
            if row["n"] != n or vlp.expand(row, gen, ext, True) != row["floor"]:
                raise ValueError(f"Unverified {field} r_14>=15 floor at order {n}")
            dest[n] = row["floor"]
    return gen, clr


def all_recorded_patches():
    patches = set(BASELINE_PATCHES)
    patches.update(map(tuple, read_json(DATA / "side_141_patches.json")))
    if (DATA / "side_140_patches.json").exists():
        patches.update(map(tuple, read_json(DATA / "side_140_patches.json")))
    for entry in read_json(DATA / "order12_side18_0_1.json.xz"):
        patches.add(tuple(entry["patch"]))
    if (DATA / "stride2_order12_21_manifest.json.xz").exists():
        for entry in read_json(DATA / "stride2_order12_21_manifest.json.xz"):
            patches.add(tuple(entry["patch"]))
    for row in read_json(DATA / "order13_side18_profiles.json.xz")["placements"]:
        if not row["survivors"]:
            patches.add((13, 12, 18, *row["offset"], 1))
    return sorted(patches)


def export_full_square_certificate(sol_path, out_path, scale=10**11):
    raw = read_json(sol_path)
    N = raw["sq_side"]
    gen15, _ = certified_packing_tables_15()
    patches = all_recorded_patches()

    grouped = {}
    used_sources = set()
    for m, d, w_10k, er, xys, alpha_val in raw["rules"]:
        if alpha_val <= 0:
            continue
        mult = alpha_val * (scale / 10000.0)
        w_int = [int(round(w * mult)) for w in w_10k]
        if max(w_int) == 0:
            continue
        L_max = N - 1 - d * (m - 2)
        canon = sorted({
            (x, y) if x + y <= L_max else (L_max - y, L_max - x)
            for x, y in xys
        })
        key = (m, d, tuple(w_10k), tuple(canon))
        if key not in grouped:
            grouped[key] = [m, d, w_int, [list(p) for p in canon]]
        else:
            acc = grouped[key][2]
            for i in range(len(acc)):
                acc[i] += w_int[i]

    int_rules = []
    for _, (m, d, w_int, canon) in sorted(grouped.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        if max(w_int) > 0:
            int_rules.append({"order": m, "dilation": d, "weights": w_int, "translations_xy": canon})
            used_sources.add(m)

    int_caps = []
    for s, X0, Y0, m_sub, c_val in raw["caps"]:
        wt = int(round(c_val * scale))
        if wt > 0:
            int_caps.append([s, X0, Y0, m_sub, wt])

    cutoffs = {11: 6, 12: 9, 13: 12, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18}
    for m in used_sources:
        if m >= 19:
            cutoffs[m] = gen15[m] - 1

    cert = {
        "domain": "full_square",
        "square_side": N,
        "sources": [[m, cutoffs[m]] for m in sorted(used_sources)],
        "patches": [list(p) for p in patches],
        "upper_caps": int_caps,
        "rules": int_rules,
        "use_order14_min15": True,
        "use_clearance_floors": True,
    }
    enc = json.dumps(cert, separators=(",", ":")).encode("ascii")
    out = Path(out_path)
    out.write_bytes(lzma.compress(enc, preset=6) if out.suffix == ".xz" else enc)
    return cert


def physical_rays_15(m, keys, rep_by_kid):
    rays = []
    if m == 14:
        for s, base, extra, bound in ((13, 3, 2, 123), (12, 6, 1, 150), (11, 10, 1, 220), (11, 20, 3, 490)):
            offsets = [(ox, oy) for ox in range(14 - s + 1) for oy in range(ox + 1)]
            prices = []
            for ki in range(len(keys)):
                xw, y, j = rep_by_kid[ki]
                cnt = sum(0 <= y - oy <= xw - ox and xw - ox + j <= s - 2 for ox, oy in offsets)
                prices.append(base + extra * cnt)
            rays.append((prices, bound))
    elif m == 15:
        for s, base, extra, bound in ((13, 6, 1, 174), (12, 20, 1, 420), (12, 10, 1, 250), (11, 30, 1, 585)):
            offsets = [(ox, oy) for ox in range(15 - s + 1) for oy in range(ox + 1)]
            prices = []
            for ki in range(len(keys)):
                xw, y, j = rep_by_kid[ki]
                cnt = sum(0 <= y - oy <= xw - ox and xw - ox + j <= s - 2 for ox, oy in offsets)
                prices.append(base + extra * cnt)
            rays.append((prices, bound))
    if 14 <= m <= 18:
        p_single, p_mult, p_bnd = [], [], []
        for ki in range(len(keys)):
            xw, y, j = rep_by_kid[ki]
            faces = (y == 0) + (xw == y) + (xw + j == m - 2)
            p_single.append(2 + int(faces == 1))
            p_mult.append(3 - max(0, faces - 1))
            p_bnd.append(1 + int(faces > 0))
        rays.append((p_single, 2 * m + 2))
        rays.append((p_mult, 3 * m + 1 if m >= 15 else 3 * m))
        if m >= 17:
            rays.append((p_bnd, m + 2))
    return rays


def barycentric_rays_15(m, keys):
    rays = []
    if m == 14:
        specs = ((13, 3, 2, 123), (12, 6, 1, 150), (11, 10, 1, 220), (11, 20, 3, 490))
    elif m == 15:
        specs = ((13, 6, 1, 174), (12, 20, 1, 420), (12, 10, 1, 250), (11, 30, 1, 585))
    else:
        specs = ()
    for s, base, extra, bound in specs:
        delta = m - s
        margins = [(u, v, delta - u - v) for u in range(delta + 1) for v in range(delta + 1 - u)]
        prices = [
            base + extra * sum(u <= a and v <= bb and w <= c for u, v, w in margins)
            for _, a, bb, c in keys
        ]
        rays.append((prices, bound))
    if 14 <= m <= 18:
        zeros = [(a == 0) + (bb == 0) + (c == 0) for _, a, bb, c in keys]
        rays.append(([2 + int(z == 1) for z in zeros], 2 * m + 2))
        rays.append(([3 - max(0, z - 1) for z in zeros], 3 * m + 1 if m >= 15 else 3 * m))
        if m >= 17:
            rays.append(([1 + int(z > 0) for z in zeros], m + 2))
    return rays


def verify_physical_square(cert, catalogs, gen_pack, clr_pack):
    """Verifier 1: Direct physical square coordinates in S_N = {0, ..., N-1}^2."""
    N = cert["square_side"]
    patches = [tuple(p) for p in cert["patches"]]
    if not {(12, 9, 18, 0, 0, 1), (13, 12, 18, 0, 0, 1)} <= set(patches):
        raise ValueError("Missing required side-18 (0, 0) clearance patches")

    src_info = {}
    for m, b in cert["sources"]:
        expected_b = {11: 6, 12: 9, 13: 12, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18}.get(m, gen_pack.get(m, 0) - 1)
        if b != expected_b:
            raise ValueError(f"Uncertified cutoff {b} for order {m}")
        raw_c = []
        key_set = set()
        for xw in range(m - 1):
            for yw in range(xw + 1):
                for j in range(1, m - 1 - xw):
                    key = (j, *sorted((xw - yw, yw, m - 2 - xw - j)))
                    key_set.add(key)
                    i0 = (xw + 1) * xw // 2 + yw
                    i1 = (xw + j + 1) * (xw + j) // 2 + yw
                    i2 = i1 + j
                    raw_c.append((key, xw, yw, j, i0, i1, i2))
        keys = sorted(key_set)
        kid = {k: idx for idx, k in enumerate(keys)}
        indexed = [(kid[k], xw, yw, j, i0, i1, i2) for k, xw, yw, j, i0, i1, i2 in raw_c]
        rep_by_kid = {ki: (xw, yw, j) for ki, xw, yw, j, *_ in indexed}
        words = catalogs.get(f"{m}/{b}", []) if m <= 13 else []
        profiles = set()
        for w in words:
            prof = tuple(sorted(ki for ki, _, _, _, i0, i1, i2 in indexed if len({w[i0], w[i1], w[i2]}) == 3))
            profiles.add(prof)
        rays = physical_rays_15(m, keys, rep_by_kid)
        src_info[m] = (b, keys, indexed, profiles, rays)

    def patch_fits(m, d, x0, y0, min_r):
        for p_ord, p_cut, p_side, px, py, p_stride in patches:
            if m != p_ord or p_cut + 1 < min_r or d % p_stride != 0:
                continue
            unit = d // p_stride
            gap = p_side - 1 - (m - 2) * p_stride
            span = (p_side - 1) * unit
            for ox, oy in ((px, py), (gap - py, gap - px)):
                bx, by = x0 - unit * ox, y0 - unit * oy
                if 0 <= bx and bx + span < N and 0 <= by and by + span < N:
                    return True
        return False

    host_I = {h: [[0] * (N - h) for _ in range(N - h)] for h in range(1, N)}
    J_lower = 0
    for rule in cert["rules"]:
        m, d, weights, xys = rule["order"], rule["dilation"], rule["weights"], rule["translations_xy"]
        b, keys, indexed, profiles, rays = src_info[m]
        if len(weights) != len(keys) or any(type(w) is not int or w < 0 for w in weights):
            raise ValueError("Invalid weights")
        L_max = N - 1 - d * (m - 2)
        if d < 1 or L_max < 0:
            raise ValueError("Invalid dilation")
        w_min = min(weights)
        ray_fl = 0
        for prices, bound in rays:
            lam = min(Fraction(w, p) for w, p in zip(weights, prices))
            ray_fl = max(ray_fl, ceil(bound * lam))

        ths = sorted({0, *(p[1] + 1 for p in patches if p[0] == m), *([clr_pack[m]] if m in clr_pack else [])}, reverse=True)
        floors = {
            th: max(ray_fl, min([max(b + 1, th) * w_min] + [sum(weights[i] for i in p) for p in profiles if len(p) >= th]))
            for th in ths
        }
        seen = set()
        for x0, y0 in xys:
            if x0 < 0 or y0 < 0 or x0 + y0 > L_max or (x0, y0) in seen:
                raise ValueError("Invalid or duplicate canonical xy translation")
            seen.add((x0, y0))
            rx0, ry0 = L_max - y0, L_max - x0
            oris = [(x0, y0)] if (x0, y0) == (rx0, ry0) else [(x0, y0), (rx0, ry0)]
            for bx, by in oris:
                best_th = 0
                for th in ths:
                    if th > best_th and patch_fits(m, d, bx, by, th):
                        best_th = th
                        break
                if m in clr_pack and clr_pack[m] > best_th:
                    pos_cl = min(N - 1 - (m - 2) * d - bx, N - 1 - (m - 2) * d - by)
                    neg_cl = min(bx, by)
                    if max(pos_cl, neg_cl) >= 7 * d:
                        best_th = clr_pack[m]
                J_lower += floors[best_th]
                for ki, xw, yw, j, *_ in indexed:
                    w = weights[ki]
                    if w:
                        host_I[d * j][bx + d * xw][by + d * yw] += w

    cap_cost = 0
    for s, X0, Y0, m_sub, wt in cert["upper_caps"]:
        if s < 1 or m_sub < 3 or wt < 0:
            raise ValueError("Invalid upper cap")
        P = m_sub - 2
        L_c = N - 1 - s * P
        if X0 < 0 or Y0 < 0 or X0 + Y0 > L_c:
            raise ValueError("Upper cap escapes square")
        U_sub = comb(m_sub, 2) - (m_sub - 1) + (m_sub - 1) // 3
        rX0, rY0 = L_c - Y0, L_c - X0
        oris = [(X0, Y0)] if (X0, Y0) == (rX0, rY0) else [(X0, Y0), (rX0, rY0)]
        cap_cost += wt * len(oris) * U_sub
        for bx, by in oris:
            for hk in range(1, P + 1):
                arr_h = host_I[s * hk]
                for i in range(P - hk + 1):
                    row_x = arr_h[bx + s * i]
                    for j in range(i + 1):
                        row_x[by + s * j] -= wt

    U_wn = comb(N + 1, 2) - N + N // 3
    pos_wn = []
    out_sum = 0
    for h in range(1, N):
        arr_h = host_I[h]
        for X in range(N - h):
            row_x = arr_h[X]
            for Y in range(N - h):
                v = row_x[Y]
                if v > 0:
                    if Y <= X:
                        pos_wn.append(v)
                    else:
                        out_sum += v
    pos_wn.sort(reverse=True)
    V_upper = cap_cost + sum(pos_wn[:U_wn]) + out_sum
    return J_lower, V_upper, J_lower - V_upper


def verify_signed_barycentric(cert, catalogs, gen_pack, clr_pack):
    """Verifier 2: Independent signed-gap antidiagonal-orbit checker."""
    N = cert["square_side"]
    patches = [tuple(p) for p in cert["patches"]]
    src_bary = {}
    for m, b in cert["sources"]:
        bary_idx = {(u - v - 1, v, m - 1 - u): u * (u - 1) // 2 + v for u in range(1, m) for v in range(u)}
        key_set = set()
        corners = []
        for j in range(1, m - 1):
            rem = m - 2 - j
            for a in range(rem + 1):
                for bb in range(rem + 1 - a):
                    c = rem - a - bb
                    key = (j, *sorted((a, bb, c)))
                    key_set.add(key)
                    corners.append((key, j, a, bb, c, bary_idx[(a, bb, c + j)], bary_idx[(a + j, bb, c)], bary_idx[(a, bb + j, c)]))
        keys = sorted(key_set)
        kid = {k: idx for idx, k in enumerate(keys)}
        words = catalogs.get(f"{m}/{b}", []) if m <= 13 else []
        profiles = {
            tuple(sorted(kid[key] for key, _, _, _, _, i0, i1, i2 in corners if len({w[i0], w[i1], w[i2]}) == 3))
            for w in words
        }
        rays = barycentric_rays_15(m, keys)
        src_bary[m] = (b, keys, [(kid[key], j, a, bb, c) for key, j, a, bb, c, *_ in corners], profiles, rays)

    # Signed-gap orbit key: (h, a_signed = X - Y, min(Y, N - 1 - h - X), max(Y, N - 1 - h - X))
    orbit_sum = Counter()
    J_lower = 0
    for rule in cert["rules"]:
        m, d, weights, xys = rule["order"], rule["dilation"], rule["weights"], rule["translations_xy"]
        b, keys, b_corners, profiles, rays = src_bary[m]
        L_max = N - 1 - d * (m - 2)
        w_min = min(weights)
        ray_fl = max([0] + [ceil(bound * min(Fraction(w, p) for w, p in zip(weights, prices))) for prices, bound in rays])
        ths = sorted({0, *(p[1] + 1 for p in patches if p[0] == m), *([clr_pack[m]] if m in clr_pack else [])}, reverse=True)
        floors = {
            th: max(ray_fl, min([max(b + 1, th) * w_min] + [sum(weights[i] for i in p) for p in profiles if len(p) >= th]))
            for th in ths
        }
        for x0, y0 in xys:
            ta, tb, tc = x0 - y0, y0, L_max - x0
            mult_t = 1 if tb == tc else 2
            best_th = 0
            for p_ord, p_cut, p_side, px, py, p_stride in patches:
                if p_ord != m or p_cut + 1 <= best_th or d % p_stride != 0:
                    continue
                unit = d // p_stride
                gap = p_side - 1 - (m - 2) * p_stride
                span = (p_side - 1) * unit
                for ox, oy in ((px, py), (gap - py, gap - px)):
                    if 0 <= x0 - unit * ox <= N - 1 - span and 0 <= y0 - unit * oy <= N - 1 - span:
                        best_th = p_cut + 1
                        break
            if m in clr_pack and clr_pack[m] > best_th:
                if max(min(L_max - x0, L_max - y0), min(x0, y0)) >= 7 * d:
                    best_th = clr_pack[m]
            J_lower += mult_t * floors[best_th]
            oris = [(ta, tb, tc)] if tb == tc else [(ta, tb, tc), (ta, tc, tb)]
            for sa, sb, sc in oris:
                for ki, j_loc, la, lb, lc in b_corners:
                    w = weights[ki]
                    if w:
                        h = d * j_loc
                        A_s = sa + d * la
                        B_s = sb + d * lb
                        C_s = sc + d * lc
                        orbit_sum[(h, A_s, min(B_s, C_s), max(B_s, C_s))] += w

    cap_cost = 0
    for s, X0, Y0, m_sub, wt in cert["upper_caps"]:
        P = m_sub - 2
        L_c = N - 1 - s * P
        ta, tb, tc = X0 - Y0, Y0, L_c - X0
        oris = [(ta, tb, tc)] if tb == tc else [(ta, tb, tc), (ta, tc, tb)]
        U_sub = comb(m_sub, 2) - (m_sub - 1) + (m_sub - 1) // 3
        cap_cost += wt * len(oris) * U_sub
        for sa, sb, sc in oris:
            for j_loc in range(1, P + 1):
                h = s * j_loc
                rem = P - j_loc
                for la in range(rem + 1):
                    for lb in range(rem + 1 - la):
                        lc = rem - la - lb
                        B_s = sb + s * lb
                        C_s = sc + s * lc
                        orbit_sum[(h, sa + s * la, min(B_s, C_s), max(B_s, C_s))] -= wt

    U_wn = comb(N + 1, 2) - N + N // 3
    wn_orbits = []
    out_sum = 0
    for (_, A_s, b0, c0), tot_w in orbit_sum.items():
        if tot_w <= 0:
            continue
        mu = 1 if b0 == c0 else 2
        per_corner = tot_w // mu
        if per_corner * mu != tot_w:
            raise ValueError("Asymmetric orbit weight detected")
        if A_s >= 0:
            wn_orbits.append((per_corner, mu))
        else:
            out_sum += tot_w
    wn_orbits.sort(reverse=True)
    rem = U_wn
    top_wn = 0
    for val, mu in wn_orbits:
        if rem <= 0:
            break
        tk = min(rem, mu)
        top_wn += tk * val
        rem -= tk
    V_upper = cap_cost + top_wn + out_sum
    return J_lower, V_upper, J_lower - V_upper


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    exp = sub.add_parser("export")
    exp.add_argument("solver_json", type=Path)
    exp.add_argument("out_cert", type=Path)
    exp.add_argument("--scale", type=int, default=10**11)
    ver = sub.add_parser("verify")
    ver.add_argument("cert", type=Path)
    args = parser.parse_args()

    if args.cmd == "export":
        export_full_square_certificate(args.solver_json, args.out_cert, args.scale)
        return

    cert = read_json(args.cert)
    allowed = set(all_recorded_patches())
    if not set(map(tuple, cert["patches"])) <= allowed:
        raise ValueError("Unrecorded patch in certificate")
    gen15, clr15 = certified_packing_tables_15()
    catalogs = read_json(BASELINE / "triangle_grid_catalogs.json.xz")
    res_phys = verify_physical_square(cert, catalogs, gen15, clr15)
    res_bary = verify_signed_barycentric(cert, catalogs, gen15, clr15)
    if res_phys != res_bary:
        raise ValueError(f"Verifiers disagree: {res_phys} vs {res_bary}")
    lower, upper, margin = res_phys
    print(json.dumps({
        "square_side": cert["square_side"],
        "lower": lower,
        "upper": upper,
        "margin": margin,
    }, indent=2))
    if margin <= 0:
        raise ValueError("Non-positive certificate margin")


if __name__ == "__main__":
    main()
