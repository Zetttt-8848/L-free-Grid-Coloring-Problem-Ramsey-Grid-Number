"""Export and cross-check integer weighted rainbow certificates."""

import argparse
import json
import lzma
from collections import Counter
from math import comb
from pathlib import Path

from verify_143 import BASELINE, BASELINE_PATCHES

DATA = Path(__file__).resolve().parent / "data"


def read_json(path):
    raw = Path(path).read_bytes()
    return json.loads(lzma.decompress(raw) if Path(path).suffix == ".xz" else raw)


def build_integer_certificate(sol_json_path, patches, out_cert_path, scale=10**11):
    raw = read_json(sol_json_path)
    sq_side = raw["sq_side"]

    # Combine rules that share the exact same (m, d, tlist_key) by summing their integer corner-weight vectors!
    grouped_rules = {}
    for m, d, w_10k, er, tlist, alpha_val in raw["rules"]:
        if alpha_val <= 0:
            continue
        # Multiply w_10k (which has min ~ 10000) by alpha_val * scale / 10000
        mult = alpha_val * (scale / 10000.0)
        w_int = [int(round(w * mult)) for w in w_10k]
        if max(w_int) == 0:
            continue
        t_key = (m, d, tuple((a, b0, c0) for a, b0, c0 in tlist))
        if t_key not in grouped_rules:
            grouped_rules[t_key] = [m, d, w_int, tlist]
        else:
            acc = grouped_rules[t_key][2]
            for i in range(len(acc)):
                acc[i] += w_int[i]

    int_rules = []
    used_sources = set()
    for _, (m, d, w_int, tlist) in sorted(grouped_rules.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        if max(w_int) > 0:
            int_rules.append({"order": m, "dilation": d, "weights": w_int, "translations": tlist})
            used_sources.add(m)

    int_caps = []
    for s, i, j, k, c_val in raw["caps"]:
        wt = int(round(c_val * scale))
        if wt > 0:
            int_caps.append([s, i, j, k, wt])

    source_cutoffs = {11: 6, 12: 9, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17}
    cert = {
        "square_side": sq_side,
        "weak_triangle_order": sq_side + 1,
        "sources": [[m, source_cutoffs[m]] for m in sorted(used_sources)],
        "patches": [list(p) for p in patches],
        "upper_caps": int_caps,
        "rules": int_rules,
    }
    encoded = json.dumps(cert, separators=(",", ":")).encode("ascii")
    output = Path(out_cert_path)
    output.write_bytes(lzma.compress(encoded, preset=6) if output.suffix == ".xz" else encoded)
    return cert


def verify_A_physical(cert, catalogs):
    """Verifier A: Direct physical square coordinates in S_N = {0, ..., N-1}^2."""
    N = cert["square_side"]
    patches = [tuple(p) for p in cert["patches"]]

    src_info = {}
    for m, b in cert["sources"]:
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
        words = catalogs[f"{m}/{b}"]
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
        src_info[m] = (b, keys, indexed, profiles)

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

    J_total = 0
    combined_md = {}
    for rule in cert["rules"]:
        m, d, weights, tlist = rule["order"], rule["dilation"], rule["weights"], rule["translations"]
        b, keys, indexed, profiles = src_info[m]
        if len(weights) != len(keys) or any(type(w) is not int or w < 0 for w in weights):
            raise ValueError("Bad weights")
        Q = N - 1 - d * (m - 2)
        if d < 1 or Q < 0:
            raise ValueError("Bad dilation")
        w_min = min(weights)
        # Precompute floor for every threshold
        possible_ths = sorted({p_cut + 1 for p_ord, p_cut, *_ in patches if p_ord == m}, reverse=True)
        floor_cache = {}
        for th in [0] + possible_ths:
            fl = max(b + 1, th) * w_min
            for p in profiles:
                if len(p) >= th:
                    s = sum(weights[i] for i in p)
                    if s < fl:
                        fl = s
            floor_cache[th] = fl

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
                best_fl = floor_cache[0]
                for th in possible_ths:
                    if patch_fits(m, d, x_off, y_off, th):
                        best_fl = max(best_fl, floor_cache[th])
                        break
                J_total += best_fl
                acc = md_map.get((x_off, y_off))
                if acc is None:
                    md_map[(x_off, y_off)] = list(weights)
                else:
                    for ki in range(n_keys):
                        acc[ki] += weights[ki]

    host_I = {h: [0] * ((N - h) * (N - h + 1) // 2) for h in range(1, N)}
    for (m, d), md_map in combined_md.items():
        _, _, indexed, _ = src_info[m]
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
                        lc = rem_bc - lb
                        B = p1 + s * lb
                        X = A + B
                        Y = B
                        arr[X * (X + 1) // 2 + Y] -= wt

    U_host = comb(N + 1, 2) - N + N // 3
    pos = [v for h in range(1, N) for v in host_I[h] if v > 0]
    pos.sort(reverse=True)
    V_total = cap_cost + sum(pos[:U_host])
    return J_total, V_total, J_total - V_total


def verify_B_barycentric(cert, catalogs):
    """Verifier B: Independent barycentric-coordinate checker on T_{N+1}."""
    M = cert["weak_triangle_order"]
    N = M - 1
    if N != cert["square_side"]:
        raise ValueError("M != N + 1")
    patches = [tuple(p) for p in cert["patches"]]

    # Build barycentric geometry directly on triples (a, b, c) + step j with a+b+c+j = m-2
    src_bary = {}
    for m, b in cert["sources"]:
        # Map cell (u, v) in T_m (1<=u<m, 0<=v<u) to barycentric (u-v-1, v, m-1-u)
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
        words = catalogs[f"{m}/{b}"]
        profiles = set()
        for w in words:
            prof = tuple(sorted(
                kid[key] for key, _, _, _, _, i0, i1, i2 in corners
                if len({w[i0], w[i1], w[i2]}) == 3
            ))
            profiles.add(prof)
        src_bary[m] = (b, keys, [(kid[key], j, a, bb, c) for key, j, a, bb, c, _, _, _ in corners], profiles)

    host_bary = Counter()
    J_total = 0
    for rule in cert["rules"]:
        m, d, weights, tlist = rule["order"], rule["dilation"], rule["weights"], rule["translations"]
        b, keys, b_corners, profiles = src_bary[m]
        w_min = min(weights)
        # Floors depend on the rule and the certified rainbow threshold.
        possible_thresholds = {0, *(p[1] + 1 for p in patches if p[0] == m)}
        floors = {
            threshold: min(
                [max(b + 1, threshold) * w_min]
                + [sum(weights[i] for i in profile) for profile in profiles if len(profile) >= threshold]
            )
            for threshold in possible_thresholds
        }
        for a, b0, c0 in tlist:
            oris = [(a, b0, c0)] if b0 == c0 else [(a, b0, c0), (a, c0, b0)]
            for ta, tb, tc in oris:
                # Check best patch threshold in barycentric coordinates:
                # Condition for patch (p_ord, p_cut, p_side, px, py, p_stride) with gap = p_side-1-(m-2)*p_stride:
                # ta + tb >= unit*ox, tc >= unit*(gap - ox), tb >= unit*oy, ta + tc >= unit*(gap - oy)!
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
    verify = commands.add_parser("verify", help="reconstruct both integer scores")
    verify.add_argument("certificate", type=Path)
    verify.add_argument("--baseline", type=Path, default=BASELINE)
    verify.add_argument("--archived-patches-only", action="store_true")
    args = parser.parse_args()

    if args.command == "export":
        patches = [*BASELINE_PATCHES, *read_json(DATA / "side_141_patches.json")]
        build_integer_certificate(args.solver_output, patches, args.certificate)
        return

    cert = read_json(args.certificate)
    archived = set(BASELINE_PATCHES)
    additional = set(map(tuple, read_json(DATA / "side_141_patches.json")))
    patches = set(map(tuple, cert["patches"]))
    if not patches <= archived | additional:
        raise ValueError("Certificate refers to a patch outside the recorded run")
    if args.archived_patches_only:
        cert["patches"] = sorted(patches & archived)
        patches &= archived
    missing_proof_patches = sorted(patches - archived)
    catalogs = read_json(args.baseline / "triangle_grid_catalogs.json.xz")
    # The archived interior and boundary refutations prove these empty cases.
    catalogs.update({"17/16": [], "18/17": []})
    physical = verify_A_physical(cert, catalogs)
    barycentric = verify_B_barycentric(cert, catalogs)
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
