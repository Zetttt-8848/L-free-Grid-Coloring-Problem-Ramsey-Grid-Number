"""Export and cross-check integer weighted rainbow certificates."""

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


def certified_packing_tables():
    """Independently verify and return (generic, clearance) from local_boundary_packings.json."""
    records = read_json(DATA / "local_boundary_packings.json")
    generic = {10: 1, 11: 3, 12: 6, 13: 11, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18}
    clearance = {10: 1, 11: 3, 12: 10, 13: 13}
    for field, destination in (("generic", generic), ("with_clearance", clearance)):
        for n, row in zip(range(14, 33), records[field], strict=True):
            external = clearance if field == "with_clearance" else None
            if row["n"] != n or vlp.expand(row, generic, external) != row["floor"]:
                raise ValueError(f"Unverified {field} boundary-weighted floor at order {n}")
            destination[n] = row["floor"]
    return generic, clearance


def recorded_patches():
    """Return all archived and manifest-recorded square patches in this package."""
    patches = set(BASELINE_PATCHES)
    patches.update(map(tuple, read_json(DATA / "side_141_patches.json")))
    if (DATA / "side_140_patches.json").exists():
        patches.update(map(tuple, read_json(DATA / "side_140_patches.json")))
    for entry in read_json(DATA / "order12_side18_0_1.json.xz"):
        patches.add(tuple(entry["patch"]))
    for row in read_json(DATA / "order13_side18_profiles.json.xz")["placements"]:
        if not row["survivors"]:
            patches.add((13, 12, 18, *row["offset"], 1))
    return sorted(patches)


def build_integer_certificate(
    sol_json_path, patches, out_cert_path, scale=10**11,
    use_boundary_rays=False, use_clearance_floors=False,
):
    raw = read_json(sol_json_path)
    sq_side = raw["sq_side"]

    int_rules = []
    used_sources = set()
    grouped_rules = {}
    for m, d, w_10k, er, tlist, alpha_val in raw["rules"]:
        if alpha_val <= 0:
            continue
        mult = alpha_val * (scale / 10000.0)
        w_int = [int(round(w * mult)) for w in w_10k]
        if max(w_int) == 0:
            continue
        t_tuple = tuple((a, b0, c0) for a, b0, c0 in tlist)
        key = (m, d, tuple(w_10k), t_tuple) if use_boundary_rays else (m, d, t_tuple)
        if key not in grouped_rules:
            grouped_rules[key] = [m, d, w_int, tlist]
        else:
            acc = grouped_rules[key][2]
            for i in range(len(acc)):
                acc[i] += w_int[i]

    for _, (m, d, w_int, tlist) in sorted(grouped_rules.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        if max(w_int) > 0:
            int_rules.append({"order": m, "dilation": d, "weights": w_int, "translations": tlist})
            used_sources.add(m)

    int_caps = []
    for s, i, j, k, c_val in raw["caps"]:
        wt = int(round(c_val * scale))
        if wt > 0:
            int_caps.append([s, i, j, k, wt])

    generic, _ = (
        certified_packing_tables()
        if (any(m >= 19 for m in used_sources) or use_clearance_floors)
        else ({}, {})
    )
    source_cutoffs = {11: 6, 12: 9, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17}
    for m in used_sources:
        if m >= 19:
            source_cutoffs[m] = generic[m] - 1

    cert = {
        "square_side": sq_side,
        "weak_triangle_order": sq_side + 1,
        "sources": [[m, source_cutoffs[m]] for m in sorted(used_sources)],
        "patches": [list(p) for p in patches],
        "upper_caps": int_caps,
        "rules": int_rules,
    }
    if use_boundary_rays:
        cert["use_boundary_rays"] = True
    if use_clearance_floors:
        cert["use_clearance_floors"] = True
    encoded = json.dumps(cert, separators=(",", ":")).encode("ascii")
    output = Path(out_cert_path)
    output.write_bytes(lzma.compress(encoded, preset=6) if output.suffix == ".xz" else encoded)
    return cert


def physical_rays_for_order(m, keys, rep_by_kid):
    """Build certified weighted inequalities directly in physical coordinates of W_{m-1}."""
    rays = []
    if m == 14:
        for s, base, extra, bound in ((13, 6, 5, 279), (12, 24, 5, 636), (11, 20, 3, 490)):
            offsets = [(ox, oy) for ox in range(14 - s + 1) for oy in range(ox + 1)]
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
        rays.append((p_mult, 3 * m))
        if m >= 17:
            rays.append((p_bnd, m + 2))
    return rays


def barycentric_rays_for_order(m, keys):
    """Build certified weighted inequalities directly in barycentric coordinates (j, a, b, c)."""
    rays = []
    if m == 14:
        for s, base, extra, bound in ((13, 6, 5, 279), (12, 24, 5, 636), (11, 20, 3, 490)):
            delta = 14 - s
            margins = [(u, v, delta - u - v) for u in range(delta + 1) for v in range(delta + 1 - u)]
            prices = [
                base + extra * sum(u <= a and v <= bb and w <= c for u, v, w in margins)
                for _, a, bb, c in keys
            ]
            rays.append((prices, bound))
    if 14 <= m <= 18:
        zeros = [(a == 0) + (bb == 0) + (c == 0) for _, a, bb, c in keys]
        rays.append(([2 + int(z == 1) for z in zeros], 2 * m + 2))
        rays.append(([3 - max(0, z - 1) for z in zeros], 3 * m))
        if m >= 17:
            rays.append(([1 + int(z > 0) for z in zeros], m + 2))
    return rays


def verify_A_physical(cert, catalogs, generic_pack, clearance_pack):
    """Verifier A: Direct physical square coordinates in S_N = {0, ..., N-1}^2."""
    N = cert["square_side"]
    patches = [tuple(p) for p in cert["patches"]]
    use_rays = bool(cert.get("use_boundary_rays", False))
    use_clearance = bool(cert.get("use_clearance_floors", False))
    if use_clearance and not {(12, 9, 18, 0, 0, 1), (13, 12, 18, 0, 0, 1)} <= set(patches):
        raise ValueError("Seven-step clearance floors require side-18 (0, 0) patches at orders 12 and 13")

    src_info = {}
    for m, b in cert["sources"]:
        if m >= 19 and b + 1 != generic_pack[m]:
            raise ValueError(f"Uncertified source cutoff {b} at order {m}")
        corners_by_key = Counter()
        raw_c = []
        for xw in range(m - 1):
            for y in range(xw + 1):
                for j in range(1, m - 1 - xw):
                    key = (j, *sorted((xw - y, y, m - 2 - xw - j)))
                    i0 = (xw + 1) * xw // 2 + y
                    i1 = (xw + j + 1) * (xw + j) // 2 + y
                    i2 = i1 + j
                    corners_by_key[key] += 1
                    raw_c.append((key, xw, y, j, i0, i1, i2))
        keys = sorted(corners_by_key)
        kid = {k: idx for idx, k in enumerate(keys)}
        indexed = [(kid[k], xw, y, j, i0, i1, i2) for k, xw, y, j, i0, i1, i2 in raw_c]
        rep_by_kid = {ki: (xw, y, j) for ki, xw, y, j, *_ in indexed}
        words = [] if m >= 19 else catalogs[f"{m}/{b}"]
        ncells = comb(m, 2)
        profiles = set()
        for w in words:
            if len(w) != ncells or not set(w) <= set("012"):
                raise ValueError("Invalid catalog word")
            prof = []
            for ki, _, _, _, i0, i1, i2 in indexed:
                c0, c1, c2 = w[i0], w[i1], w[i2]
                if c0 == c1 == c2:
                    raise ValueError("Monochromatic L in catalog")
                if c0 != c1 and c1 != c2 and c0 != c2:
                    prof.append(ki)
            if len(prof) > b:
                raise ValueError("Catalog cutoff exceeded")
            profiles.add(tuple(sorted(prof)))
        rays = physical_rays_for_order(m, keys, rep_by_kid) if use_rays else []
        src_info[m] = (b, keys, indexed, profiles, rays)

    def patch_fits(m, d, x_off, y_off, min_r):
        for p_ord, p_cut, p_side, px, py, p_stride in patches:
            if m != p_ord or p_cut + 1 < min_r or d % p_stride != 0:
                continue
            unit = d // p_stride
            gap = p_side - 1 - (m - 2) * p_stride
            for ox, oy in ((px, py), (gap - py, gap - px)):
                x0, y0 = x_off - unit * ox, y_off - unit * oy
                span = (p_side - 1) * unit
                if 0 <= x0 and x0 + span < N and 0 <= y0 and y0 + span < N:
                    return True
        return False

    def physical_has_7step_clearance(m, d, x_off, y_off):
        span_m = (m - 2) * d
        pos_ok = (x_off + span_m + 7 * d < N) and (y_off + span_m + 7 * d < N)
        neg_ok = (x_off - 7 * d >= 0) and (y_off - 7 * d >= 0)
        return pos_ok or neg_ok

    J_total = 0
    combined_md = {}
    for rule in cert["rules"]:
        m, d, weights, tlist = rule["order"], rule["dilation"], rule["weights"], rule["translations"]
        b, keys, indexed, profiles, rays = src_info[m]
        if len(weights) != len(keys) or any(type(w) is not int or w < 0 for w in weights):
            raise ValueError("Bad weights")
        Q = N - 1 - d * (m - 2)
        if d < 1 or Q < 0:
            raise ValueError("Bad dilation")
        w_min = min(weights)
        ray_fl = 0
        for prices, bound in rays:
            lam = min(Fraction(w, p) for w, p in zip(weights, prices))
            ray_fl = max(ray_fl, ceil(bound * lam))

        possible_ths = {0, *(p_cut + 1 for p_ord, p_cut, *_ in patches if p_ord == m)}
        if use_clearance and m in clearance_pack:
            possible_ths.add(clearance_pack[m])
        possible_ths = sorted(possible_ths, reverse=True)
        floor_cache = {}
        for th in possible_ths:
            fl = max(b + 1, th) * w_min
            for p in profiles:
                if len(p) >= th:
                    s = sum(weights[i] for i in p)
                    if s < fl:
                        fl = s
            floor_cache[th] = max(fl, ray_fl)

        md_map = combined_md.setdefault((m, d), {})
        seen_pairs = set()
        n_keys = len(keys)
        for a, b0, c0 in tlist:
            if a < 0 or b0 < 0 or c0 < 0 or b0 > c0 or a + b0 + c0 != Q:
                raise ValueError("Bad translation tuple")
            if (a, b0, c0) in seen_pairs:
                raise ValueError("Duplicate translation in rule! Would double count!")
            seen_pairs.add((a, b0, c0))
            oris = [(a, b0, c0)] if b0 == c0 else [(a, b0, c0), (a, c0, b0)]
            for ta, tb, tc in oris:
                x_off, y_off = ta + tb, tb
                best_th = 0
                for th in possible_ths:
                    if th > best_th and patch_fits(m, d, x_off, y_off, th):
                        best_th = th
                        break
                if use_clearance and m in clearance_pack and clearance_pack[m] > best_th:
                    if physical_has_7step_clearance(m, d, x_off, y_off):
                        best_th = clearance_pack[m]
                J_total += floor_cache[best_th]
                acc = md_map.get((x_off, y_off))
                if acc is None:
                    md_map[(x_off, y_off)] = list(weights)
                else:
                    for ki in range(n_keys):
                        acc[ki] += weights[ki]

    host_I = {h: [0] * ((N - h) * (N - h + 1) // 2) for h in range(1, N)}
    for (m, d), md_map in combined_md.items():
        _, _, indexed, _, _ = src_info[m]
        for (x_off, y_off), w_vec in md_map.items():
            for ki, xw, y, j, _, _, _ in indexed:
                w = w_vec[ki]
                if w:
                    h = d * j
                    X = x_off + d * xw
                    Y = y_off + d * y
                    host_I[h][X * (X + 1) // 2 + Y] += w

    cap_cost = 0
    for s, i, j, k, wt in cert["upper_caps"]:
        if s < 1 or i < 0 or j < 0 or j > k or wt < 0:
            raise ValueError("Bad upper cap")
        rem = (N - 1) - (i + j + k)
        if rem < s * 2 or rem % s != 0:
            raise ValueError("Misaligned stride cap")
        m_sub = rem // s + 2
        U_sub = comb(m_sub, 2) - (m_sub - 1) + (m_sub - 1) // 3
        oris = [(i, j, k)] if j == k else [(i, j, k), (i, k, j)]
        cap_cost += wt * len(oris) * U_sub
        for p0, p1, p2 in oris:
            for j_loc in range(1, m_sub - 1):
                h = s * j_loc
                arr = host_I[h]
                sum_abc = m_sub - 2 - j_loc
                for la in range(sum_abc + 1):
                    A = p0 + s * la
                    rem_bc = sum_abc - la
                    for lb in range(rem_bc + 1):
                        B = p1 + s * lb
                        X = A + B
                        Y = B
                        arr[X * (X + 1) // 2 + Y] -= wt

    U_host = comb(N + 1, 2) - N + N // 3
    pos = [v for h in range(1, N) for v in host_I[h] if v > 0]
    pos.sort(reverse=True)
    V_total = cap_cost + sum(pos[:U_host])
    return J_total, V_total, J_total - V_total


def verify_B_barycentric(cert, catalogs, generic_pack, clearance_pack):
    """Verifier B: Independent barycentric-coordinate checker on T_{N+1}."""
    M = cert["weak_triangle_order"]
    N = M - 1
    if N != cert["square_side"]:
        raise ValueError("M != N + 1")
    patches = [tuple(p) for p in cert["patches"]]
    use_rays = bool(cert.get("use_boundary_rays", False))
    use_clearance = bool(cert.get("use_clearance_floors", False))
    if use_clearance and not {(12, 9, 18, 0, 0, 1), (13, 12, 18, 0, 0, 1)} <= set(patches):
        raise ValueError("Seven-step clearance floors require side-18 (0, 0) patches at orders 12 and 13")

    src_bary = {}
    for m, b in cert["sources"]:
        if m >= 19 and b + 1 != generic_pack[m]:
            raise ValueError(f"Uncertified source cutoff {b} at order {m}")
        bary_to_idx = {}
        for u in range(1, m):
            for v in range(u):
                bary_to_idx[(u - v - 1, v, m - 1 - u)] = u * (u - 1) // 2 + v
        key_set = set()
        corners = []
        for j in range(1, m - 1):
            rem = m - 2 - j
            for a in range(rem + 1):
                for bb in range(rem + 1 - a):
                    c = rem - a - bb
                    key = (j, *sorted((a, bb, c)))
                    key_set.add(key)
                    i0 = bary_to_idx[(a, bb, c + j)]
                    i1 = bary_to_idx[(a + j, bb, c)]
                    i2 = bary_to_idx[(a, bb + j, c)]
                    corners.append((key, j, a, bb, c, i0, i1, i2))
        keys = sorted(key_set)
        kid = {k: idx for idx, k in enumerate(keys)}
        words = [] if m >= 19 else catalogs[f"{m}/{b}"]
        profiles = set()
        for w in words:
            prof = tuple(sorted(
                kid[key] for key, _, _, _, _, i0, i1, i2 in corners
                if len({w[i0], w[i1], w[i2]}) == 3
            ))
            profiles.add(prof)
        rays = barycentric_rays_for_order(m, keys) if use_rays else []
        src_bary[m] = (b, keys, [(kid[key], j, a, bb, c) for key, j, a, bb, c, _, _, _ in corners], profiles, rays)

    host_bary = Counter()
    J_total = 0
    for rule in cert["rules"]:
        m, d, weights, tlist = rule["order"], rule["dilation"], rule["weights"], rule["translations"]
        b, keys, b_corners, profiles, rays = src_bary[m]
        w_min = min(weights)
        ray_fl = 0
        for prices, bound in rays:
            lam = min(Fraction(w, p) for w, p in zip(weights, prices))
            ray_fl = max(ray_fl, ceil(bound * lam))

        possible_thresholds = {0, *(p[1] + 1 for p in patches if p[0] == m)}
        if use_clearance and m in clearance_pack:
            possible_thresholds.add(clearance_pack[m])
        floors = {
            threshold: max(
                ray_fl,
                min(
                    [max(b + 1, threshold) * w_min]
                    + [sum(weights[i] for i in profile) for profile in profiles if len(profile) >= threshold]
                ),
            )
            for threshold in possible_thresholds
        }
        for a, b0, c0 in tlist:
            oris = [(a, b0, c0)] if b0 == c0 else [(a, b0, c0), (a, c0, b0)]
            for ta, tb, tc in oris:
                best_th = 0
                for p_ord, p_cut, p_side, px, py, p_stride in patches:
                    if p_ord != m or p_cut + 1 <= best_th or d % p_stride != 0:
                        continue
                    unit = d // p_stride
                    gap = p_side - 1 - (m - 2) * p_stride
                    for ox, oy in ((px, py), (gap - py, gap - px)):
                        if (ta + tb >= unit * ox and tc >= unit * (gap - ox)
                                and tb >= unit * oy and ta + tc >= unit * (gap - oy)):
                            best_th = p_cut + 1
                            break
                if use_clearance and m in clearance_pack and clearance_pack[m] > best_th:
                    if max(tb, tc) >= 7 * d:
                        best_th = clearance_pack[m]
                J_total += floors[best_th]
                for ki, j_loc, la, lb, lc in b_corners:
                    w = weights[ki]
                    if w:
                        host_bary[(d * j_loc, ta + d * la, tb + d * lb, tc + d * lc)] += w

    cap_cost = 0
    for s, i, j, k, wt in cert["upper_caps"]:
        m_sub = (M - 2 - i - j - k) // s + 2
        U_sub = comb(m_sub, 2) - (m_sub - 1) + (m_sub - 1) // 3
        oris = [(i, j, k)] if j == k else [(i, j, k), (i, k, j)]
        cap_cost += wt * len(oris) * U_sub
        for p0, p1, p2 in oris:
            for j_loc in range(1, m_sub - 1):
                h = s * j_loc
                rem = m_sub - 2 - j_loc
                for la in range(rem + 1):
                    for lb in range(rem + 1 - la):
                        lc = rem - la - lb
                        host_bary[(h, p0 + s * la, p1 + s * lb, p2 + s * lc)] -= wt

    U_host = comb(M, 2) - (M - 1) + (M - 1) // 3
    pos = sorted((v for v in host_bary.values() if v > 0), reverse=True)
    V_total = cap_cost + sum(pos[:U_host])
    return J_total, V_total, J_total - V_total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export", help="round discovery weights to exact integers")
    export.add_argument("solver_output", type=Path)
    export.add_argument("certificate", type=Path)
    export.add_argument("--scale", type=int, default=10**11)
    export.add_argument("--all-patches", action="store_true")
    export.add_argument("--use-boundary-rays", action="store_true")
    export.add_argument("--use-clearance-floors", action="store_true")
    verify = commands.add_parser("verify", help="reconstruct both integer scores")
    verify.add_argument("certificate", type=Path)
    verify.add_argument("--baseline", type=Path, default=BASELINE)
    verify.add_argument("--archived-patches-only", action="store_true")
    args = parser.parse_args()

    if args.command == "export":
        patches = (
            recorded_patches()
            if args.all_patches
            else [*BASELINE_PATCHES, *read_json(DATA / "side_141_patches.json")]
        )
        build_integer_certificate(
            args.solver_output, patches, args.certificate,
            scale=args.scale,
            use_boundary_rays=args.use_boundary_rays,
            use_clearance_floors=args.use_clearance_floors,
        )
        return

    cert = read_json(args.certificate)
    archived = set(BASELINE_PATCHES)
    allowed = set(recorded_patches())
    patches = set(map(tuple, cert["patches"]))
    if not patches <= allowed:
        raise ValueError("Certificate refers to a patch outside the recorded run")
    if args.archived_patches_only:
        cert["patches"] = sorted(patches & archived)
        patches &= archived
    missing_proof_patches = sorted(patches - archived)
    need_pack = any(m >= 19 for m, _ in cert["sources"]) or bool(cert.get("use_clearance_floors", False))
    generic_pack, clearance_pack = certified_packing_tables() if need_pack else ({}, {})
    catalogs = read_json(args.baseline / "triangle_grid_catalogs.json.xz")
    catalogs.update({"17/16": [], "18/17": []})
    physical = verify_A_physical(cert, catalogs, generic_pack, clearance_pack)
    barycentric = verify_B_barycentric(cert, catalogs, generic_pack, clearance_pack)
    if physical != barycentric:
        raise ValueError(f"Coordinate verifiers disagree: {physical} versus {barycentric}")
    lower, ceiling, margin = physical
    print(json.dumps({
        "square_side": cert["square_side"],
        "lower": lower,
        "ceiling": ceiling,
        "margin": margin,
        "additional_patches_requiring_local_replay": missing_proof_patches,
    }, indent=2))


if __name__ == "__main__":
    main()
