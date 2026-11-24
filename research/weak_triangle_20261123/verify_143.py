"""Independent physical-coordinate verifier for R_3(L) <= 143 (and general N) via Weak-Triangle Isomorphism.

Uses ONLY the Python 3.10+ standard library and ZERO shared code with verify_triangle_grid.py.
Works directly in physical square coordinates S_N = {0, 1, ..., N-1}^2 and its weak lower-right triangle
  W_N = {(x, y) in S_N : 0 <= y <= x <= N - 1},
which has C(N+1, 2) cells and C(N+1, 3) directed equal-leg Ls {(x, y), (x+h, y), (x+h, y+h)} (h >= 1).
"""
import argparse
import json
import lzma
from collections import Counter
from itertools import permutations
from math import comb
from pathlib import Path

BASELINE = Path(__file__).resolve().parent.parent / "boundary_certificates_20261115"
DATA = Path(__file__).resolve().parent / "data"


def read_json(path):
    raw = path.read_bytes()
    return json.loads(lzma.decompress(raw) if path.suffix == ".xz" else raw)


# Exact baseline square patches (order, cutoff, side, px, py, stride)
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


def check_weak_triangle_line_identity_small():
    """Verify exact line identity D + 2R - 4B = (N+1)*N directly on W_N subset S_N for N = 1..7."""
    for N in range(1, 8):
        cells = [(x, y) for x in range(N) for y in range(x + 1)]
        if len(cells) != comb(N + 1, 2):
            raise ValueError("Cell count mismatch")
        Ls = []
        for x, y in cells:
            for d in range(1, N - x):
                p1, p2, p3 = (x, y), (x + d, y), (x + d, y + d)
                if not (p2 in cells and p3 in cells):
                    raise ValueError("L escaped W_N!")
                Ls.append((p1, p2, p3))
        if len(Ls) != comb(N + 1, 3):
            raise ValueError("L count mismatch")
        # Test random/deterministic colorings on W_N
        for seed in range(5):
            col = {c: (c[0] * 7 + c[1] * 13 + seed) % 3 for c in cells}
            R = sum(1 for a, b, c in Ls if len({col[a], col[b], col[c]}) == 3)
            B = sum(1 for a, b, c in Ls if len({col[a], col[b], col[c]}) == 1)
            # Three line families in W_N:
            # 1. Rows y = const (x = y .. N-1, length N - y)
            # 2. Columns x = const (y = 0 .. x, length x + 1)
            # 3. Diagonals x - y = const >= 0 (length N - (x - y))
            lines = []
            for y0 in range(N):
                lines.append([(x, y0) for x in range(y0, N)])
            for x0 in range(N):
                lines.append([(x0, y) for y in range(x0 + 1)])
            for diff in range(N):
                lines.append([(y + diff, y) for y in range(N - diff)])
            D_num = 0  # 9 * D to stay in exact integers: sum (3*n_i - L)^2 = 9 * sum (n_i - L/3)^2
            for ln in lines:
                L = len(ln)
                cnt = [sum(1 for p in ln if col[p] == c) for c in range(3)]
                D_num += sum((3 * cnt[c] - L) ** 2 for c in range(3))
            if D_num + 18 * R - 36 * B != 9 * (N + 1) * N:
                raise ValueError(f"Line identity failed at N={N}")


def physical_source_geometry(m):
    """Build local geometry of W_{m-1} ~= T_m on cells {(u, v) : 0 <= v <= u <= m-2}."""
    # Note: in row-major order of T_m = {(x, y): 1 <= x < m, 0 <= y < x}, index(x, y) = x*(x-1)//2 + y.
    # Under x_w = x - 1 in {0..m-2}, index(x_w, y) = (x_w + 1)*x_w // 2 + y.
    corners_by_key = Counter()
    raw_corners = []
    for xw in range(m - 1):
        for y in range(xw + 1):
            for j in range(1, m - 1 - xw):
                # Gaps inside W_{m-1}: diag gap = xw - y, bottom gap = y, right gap = (m - 2) - (xw + j)
                key = (j, *sorted((xw - y, y, m - 2 - xw - j)))
                i0 = (xw + 1) * xw // 2 + y
                i1 = (xw + j + 1) * (xw + j) // 2 + y
                i2 = i1 + j
                corners_by_key[key] += 1
                raw_corners.append((key, xw, y, j, i0, i1, i2))
    keys = sorted(corners_by_key)
    key_to_id = {k: idx for idx, k in enumerate(keys)}
    indexed = [(key_to_id[k], xw, y, j, i0, i1, i2) for k, xw, y, j, i0, i1, i2 in raw_corners]
    return keys, indexed


def verify_physical_square(sq_side, cert, catalogs, patches=BASELINE_PATCHES):
    """Verify impossibility of 3-coloring S_{sq_side} = {0, ..., sq_side - 1}^2."""
    M = cert["host"]
    if M != sq_side + 1:
        raise ValueError(f"Expected weak-triangle order M = sq_side + 1 = {sq_side+1}, got {M}")

    # 1. Check catalogs & extract rainbow profiles
    src_info = {}
    for m, b in cert["sources"]:
        keys, indexed = physical_source_geometry(m)
        words = catalogs[f"{m}/{b}"]
        if len(words) != len(set(words)):
            raise ValueError(f"Duplicate words in catalog {m}/{b}")
        ncells = comb(m, 2)
        profiles = set()
        for w in words:
            if len(w) != ncells or not set(w) <= set("012"):
                raise ValueError("Malformed catalog word")
            prof = []
            for kid, _, _, _, i0, i1, i2 in indexed:
                c0, c1, c2 = w[i0], w[i1], w[i2]
                if c0 == c1 == c2:
                    raise ValueError("Improper word in catalog!")
                if c0 != c1 and c1 != c2 and c0 != c2:
                    prof.append(kid)
            if len(prof) > b:
                raise ValueError("Catalog word exceeds rainbow cutoff")
            profiles.add(tuple(sorted(prof)))
        src_info[m] = (b, keys, indexed, profiles)

    # 2. Physical L accumulator on W_{sq_side}: indexed by (h, X, Y) with 0 <= Y <= X <= sq_side - 1 - h
    # Store 1D difference array along Y for each (h, X)? Wait: for total independence from verify_triangle_grid.py's
    # difference-array algorithm, let's compute J directly by enumerating translations, AND compute host corner
    # incidences by 1D prefix differences on physical square coordinate X for each fixed (h, x_minus_y)!!
    # (Different coordinate axis than verify_triangle_grid.py!)
    # Even simpler and 100% transparent: for each h in 1..sq_side-1, X in 0..sq_side-1-h, Y in 0..X:
    # At sq_side = 143, total host Ls = C(144, 3) = 487,344!
    # Let's check: how many (rule, translation) pairs exist in cert? Let's use physical (X, Y) 2D prefix sums
    # vs verify_triangle_grid's barycentric inclusion-exclusion!
    # Wait: for each rule, iterating over admissible translations (a, b, c) and adding to a 2D array? No,
    # if a rule has 2000 translations and 286 corners -> 570k ops * 2273 rules would be slow in pure Python
    # UNLESS we first sum the rule weights at each physical translation (m, d, x_off, y_off)!!
    # YES!! Look how clean AND independent that is:
    # For fixed (m, d), there are AT MOST C(142, 2) <= 10,011 physical translations (x_off, y_off) in S_{sq_side}!
    # Summing the corner-weight vectors of all rules that cover (x_off, y_off) gives ONE combined weight vector
    # W_{m, d, x_off, y_off}[kid], and then convolving W_{m, d} (at most ~8,000 translations at d=1, ~2,000 at d=2, etc.
    # -> ONLY ~18,000 total (m, d, x_off, y_off) across ALL m and ALL d!!) with the <= 364 corners of T_m is ONLY
    # 18,000 * 286 = 5 MILLION integer additions TOTAL in pure Python (~1.5 seconds), ZERO inclusion-exclusion formulas!!

    def patch_fits_phys(m, d, x_off, y_off, min_rainbows):
        for p_ord, p_cut, p_side, px, py, p_stride in patches:
            if m != p_ord or p_cut + 1 < min_rainbows or d % p_stride != 0:
                continue
            unit = d // p_stride
            gap = p_side - 1 - (m - 2) * p_stride
            for ox, oy in ((px, py), (gap - py, gap - px)):
                x0 = x_off - unit * ox
                y0 = y_off - unit * oy
                span = (p_side - 1) * unit
                if 0 <= x0 and x0 + span < sq_side and 0 <= y0 and y0 + span < sq_side:
                    return True
        return False

    def band_holds(rule_tail, Q, a, b, c):
        if len(rule_tail) == 3:
            kind, lo, hi = rule_tail
        else:
            kind = "min"
            lo, hi = rule_tail if rule_tail else (0, Q // 3 + 1)
        if kind == "both":
            return lo[0] <= min(a, b, c) < hi[0] and lo[1] <= max(a, b, c) < hi[1]
        val = min(a, b, c) if kind == "min" else max(a, b, c)
        return lo <= val < hi

    J_total = 0
    # Accumulate combined class weights per (m, d, x_off, y_off)
    combined_md = {}  # (m, d) -> dict of (x_off, y_off) -> list of weights per kid

    for rule in cert["rules"]:
        m, d, weights, *tail = rule
        b, keys, indexed, profiles = src_info[m]
        if len(weights) != len(keys) or any(type(w) is not int or w < 0 for w in weights):
            raise ValueError("Invalid weight vector")
        Q = sq_side - 1 - d * (m - 2)
        if Q < 0:
            raise ValueError("Invalid dilation for host square")

        w_min = min(weights)
        base_floor = (b + 1) * w_min
        for p in profiles:
            s = sum(weights[i] for i in p)
            if s < base_floor:
                base_floor = s

        # Precompute floors at each possible rainbow threshold
        floor_at = {0: base_floor}
        thresholds = [12, 13] if m == 13 else ([8, 9] if m == 12 else [])
        for th in thresholds:
            fl = max(b + 1, th) * w_min
            for p in profiles:
                if len(p) >= th:
                    s = sum(weights[i] for i in p)
                    if s < fl:
                        fl = s
            floor_at[th] = max(base_floor, fl)

        md_map = combined_md.setdefault((m, d), {})
        n_keys = len(keys)

        # Literally visit every physical placement (a, b_gap, c_gap) in W_{sq_side}!
        for a in range(Q + 1):
            for b_gap in range(Q + 1 - a):
                c_gap = Q - a - b_gap
                if not band_holds(tail, Q, a, b_gap, c_gap):
                    continue
                x_off = a + b_gap
                y_off = b_gap
                # Check physical containment of W_{m-1} copy inside W_{sq_side}:
                # (x_off, y_off) has 0 <= y_off <= x_off, and x_off + d*(m-2) = sq_side - 1 - c_gap <= sq_side - 1!
                best_fl = base_floor
                for th in thresholds:
                    if floor_at[th] > best_fl and patch_fits_phys(m, d, x_off, y_off, th):
                        best_fl = floor_at[th]
                J_total += best_fl

                acc = md_map.get((x_off, y_off))
                if acc is None:
                    md_map[(x_off, y_off)] = list(weights)
                else:
                    for ki in range(n_keys):
                        acc[ki] += weights[ki]

    # 3. Directly map every combined (m, d, x_off, y_off) onto physical host Ls (h, X, Y) in W_{sq_side}!
    # Flatten host L index: for each h in 1..sq_side-1, X in 0..sq_side-1-h, Y in 0..X
    host_I = {}
    for h in range(1, sq_side):
        max_X = sq_side - 1 - h
        host_I[h] = [0] * ((max_X + 1) * (max_X + 2) // 2)

    for (m, d), md_map in combined_md.items():
        _, _, indexed, _ = src_info[m]
        for (x_off, y_off), w_vec in md_map.items():
            for kid, xw, y, j, _, _, _ in indexed:
                w = w_vec[kid]
                if w:
                    h = d * j
                    X = x_off + d * xw
                    Y = y_off + d * y
                    host_I[h][X * (X + 1) // 2 + Y] += w

    # 4. Subtract physical sub-triangle upper caps H_{i, j, k} subset W_{sq_side}!
    # In physical coordinates (X, Y) of W_{sq_side}, a host L {(X, Y), (X+h, Y), (X+h, Y+h)} has:
    #   diag_gap = X - Y >= 0, bottom_gap = Y >= 0, right_gap = (sq_side - 1) - (X + h) >= 0.
    # Sub-triangle shift (p0, p1, p2) covers this L iff X - Y >= p0, Y >= p1, and sq_side - 1 - X - h >= p2!
    cap_cost = 0
    for i, j, k, wt in cert.get("upper_caps", ()):
        if not (0 <= i <= j <= k and i + j + k <= sq_side - 2):
            raise ValueError("Invalid upper cap")
        sub_order = (sq_side + 1) - i - j - k
        sub_U = comb(sub_order, 2) - (sub_order - 1) + (sub_order - 1) // 3
        perms = sorted(set(permutations((i, j, k))))
        cap_cost += wt * len(perms) * sub_U
        for p0, p1, p2 in perms:
            for h in range(1, sub_order - 1):
                arr = host_I[h]
                max_X = sq_side - 1 - h - p2
                for X in range(p0 + p1, max_X + 1):
                    base_idx = X * (X + 1) // 2
                    y_hi = X - p0
                    for Y in range(p1, y_hi + 1):
                        arr[base_idx + Y] -= wt

    # 5. Collect positive residuals across all C(sq_side + 1, 3) physical Ls in W_{sq_side}
    U_host = comb(sq_side + 1, 2) - sq_side + sq_side // 3
    pos_vals = []
    max_inc = 0
    for h in range(1, sq_side):
        for val in host_I[h]:
            if val > 0:
                if val > max_inc:
                    max_inc = val
                pos_vals.append(val)
    pos_vals.sort(reverse=True)
    V_total = cap_cost + sum(pos_vals[:U_host])
    margin = J_total - V_total
    if margin <= 0:
        raise ValueError(f"Nonpositive margin: {margin}")
    return {
        "square_side": sq_side,
        "weak_triangle_order": sq_side + 1,
        "host_Ls": comb(sq_side + 1, 3),
        "U_host": U_host,
        "J_lower": J_total,
        "V_ceiling": V_total,
        "max_residual": max_inc,
        "margin": margin,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    args = parser.parse_args()
    check_weak_triangle_line_identity_small()
    cert = read_json(args.baseline / "triangle_grid_certificate.json")
    catalogs = read_json(args.baseline / "triangle_grid_catalogs.json.xz")
    print(json.dumps(verify_physical_square(143, cert, catalogs), indent=2))


if __name__ == "__main__":
    main()
