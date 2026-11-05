#!/usr/bin/env python3
"""Exact claimant computation for Round-3 Module A.7.

This program uses cumulative integer capacities and a greedy fill of the
smallest distance classes.  It prints JSON to stdout and writes no files.
"""

from __future__ import annotations

import json


H_TABLE = (
    0, 1, 2, 4, 7, 12, 18, 26, 35, 45, 56, 73, 86, 107, 128,
    152, 178, 200, 217, 247, 284, 334, 357, 373, 426, 481, 493,
    554, 586,
)


def q_positions(m: int) -> int:
    assert 0 <= m <= H_TABLE[-1]
    return max(j for j, h in enumerate(H_TABLE) if h <= m)


def minsum_uniform(number: int, cap: int) -> int:
    a, b = divmod(number, cap)
    return cap * a * (a + 1) // 2 + b * (a + 1)


def inherited_caps(n: int) -> list[int]:
    # Index d has cap 2*q(n-d); index zero is unused.
    return [0] + [2 * q_positions(n - d) for d in range(1, n)]


def low_profile(n: int, cap: int, through: int) -> list[int]:
    out = inherited_caps(n)
    for d in range(1, min(through, n - 1) + 1):
        out[d] = min(out[d], cap)
    return out


def minsum_profile(number: int, caps: list[int]) -> tuple[int, list[dict]]:
    remaining = number
    total = 0
    allocation = []
    for d in range(1, len(caps)):
        used = min(remaining, caps[d])
        if used:
            allocation.append({"distance": d, "used": used, "cap": caps[d]})
            total += d * used
            remaining -= used
        if remaining == 0:
            return total, allocation
    raise ValueError("profile has insufficient total capacity")


def bound_for_c_uniform(L: int, V: int, c: int) -> int:
    rhs = L * c * (c + 1)
    def forbidden(s: int) -> bool:
        h = c * s - c * (c + 1) // 2
        return 2 * minsum_uniform(h, V) > rhs

    lo, hi = c, L + 2
    assert forbidden(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if forbidden(mid):
            hi = mid
        else:
            lo = mid
    return hi - 1


def best_uniform_bound(L: int, V: int) -> tuple[int, list[int]]:
    best = L + 1
    cs: list[int] = []
    for c in range(1, L + 2):
        if c > best:
            break
        k = bound_for_c_uniform(L, V, c)
        if k < best:
            best, cs = k, [c]
        elif k == best:
            cs.append(c)
    return best, cs


def bound_for_c_profile(n: int, caps: list[int], c: int) -> int:
    L = n - 1
    rhs = L * c * (c + 1)
    total_capacity = sum(caps)
    def forbidden(s: int) -> bool:
        h = c * s - c * (c + 1) // 2
        if h > total_capacity:
            return True
        value, _ = minsum_profile(h, caps)
        return 2 * value > rhs

    lo, hi = c, n + 1
    assert forbidden(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if forbidden(mid):
            hi = mid
        else:
            lo = mid
    return hi - 1


def best_profile_bound(n: int, caps: list[int]) -> tuple[int, list[int]]:
    best = n
    cs: list[int] = []
    for c in range(1, n):
        if c > best:
            break
        k = bound_for_c_profile(n, caps, c)
        if k < best:
            best, cs = k, [c]
        elif k == best:
            cs.append(c)
    return best, cs


def target_detail(n: int, s: int, c: int, caps: list[int]) -> dict:
    h = c * s - c * (c + 1) // 2
    value, allocation = minsum_profile(h, caps)
    rhs = (n - 1) * c * (c + 1)
    return {
        "n": n,
        "span": n - 1,
        "target_size": s,
        "c": c,
        "H": h,
        "minsum": value,
        "twice_minsum": 2 * value,
        "rhs": rhs,
        "margin": 2 * value - rhs,
        "strict_contradiction": 2 * value > rhs,
        "allocation": allocation,
    }


def prefix_replacement(n: int, level: int, through: int) -> list[int]:
    return low_profile(n, level, through)


def main() -> None:
    n = 464
    s = 155
    c = 8

    uniform = {}
    for V in (48, 45, 46):
        best, cs = best_uniform_bound(463, V)
        uniform[str(V)] = {"L": 463, "best_bound": best, "best_c": cs}

    p45 = low_profile(n, 45, 27)
    p46 = low_profile(n, 46, 27)
    b45, b45c = best_profile_bound(n, p45)
    b46, b46c = best_profile_bound(n, p46)

    ladder = []
    for nn in range(450, 466):
        target = (nn + 2) // 3
        caps = low_profile(nn, 45, 27)
        bound, cs = best_profile_bound(nn, caps)
        witness_c = cs[0]
        detail = target_detail(nn, target, witness_c, caps)
        ladder.append({
            "n": nn,
            "required_ceil_n_over_3": target,
            "best_bound": bound,
            "best_c": cs,
            "closes_required_size": bound < target,
            "target_at_first_best_c": {
                key: detail[key]
                for key in ("c", "H", "minsum", "twice_minsum", "rhs", "margin", "strict_contradiction")
            },
        })

    # Prefix sensitivity from the inherited cap 48 profile.
    prefix45 = []
    for D in range(0, 40):
        caps = prefix_replacement(n, 45, D)
        d = target_detail(n, s, c, caps)
        bound, cs = best_profile_bound(n, caps)
        prefix45.append({
            "through": D,
            "minsum": d["minsum"],
            "margin": d["margin"],
            "best_bound": bound,
            "best_c": cs,
        })
    first_prefix45 = next(row for row in prefix45 if row["best_bound"] < s)

    # Begin at cap 46 through 27, then shave one further unit on a prefix.
    base46 = low_profile(n, 46, 27)
    prefix46_to45 = []
    for D in range(0, 28):
        caps = base46.copy()
        for d in range(1, D + 1):
            caps[d] = min(caps[d], 45)
        detail = target_detail(n, s, c, caps)
        bound, cs = best_profile_bound(n, caps)
        prefix46_to45.append({
            "through": D,
            "minsum": detail["minsum"],
            "margin": detail["margin"],
            "best_bound": bound,
            "best_c": cs,
        })
    first_prefix46_to45 = next(
        row for row in prefix46_to45 if row["best_bound"] < s
    )
    first_prefix46_to45["global_closing_witness"] = target_detail(
        n, s, first_prefix46_to45["best_c"][0],
        (lambda caps: caps)(
            (lambda caps: [
                min(value, 45) if 1 <= d <= first_prefix46_to45["through"] else value
                for d, value in enumerate(caps)
            ])(base46.copy())
        ),
    )

    # Allow several unit reductions to concentrate at distance 1.
    concentrated_from_46 = []
    for reduction in range(0, base46[1] + 1):
        caps = base46.copy()
        caps[1] -= reduction
        detail = target_detail(n, s, c, caps)
        bound, cs = best_profile_bound(n, caps)
        concentrated_from_46.append({
            "reduction_units": reduction,
            "new_cap_d1": caps[1],
            "minsum": detail["minsum"],
            "margin": detail["margin"],
            "best_bound": bound,
            "best_c": cs,
        })
    first_concentrated_46 = next(
        row for row in concentrated_from_46 if row["best_bound"] < s
    )

    inherited = inherited_caps(n)
    concentrated_from_inherited = []
    for reduction in range(0, inherited[1] + 1):
        caps = inherited.copy()
        caps[1] -= reduction
        detail = target_detail(n, s, c, caps)
        bound, cs = best_profile_bound(n, caps)
        concentrated_from_inherited.append({
            "reduction_units": reduction,
            "new_cap_d1": caps[1],
            "minsum": detail["minsum"],
            "margin": detail["margin"],
            "best_bound": bound,
            "best_c": cs,
        })
    first_concentrated_inherited = next(
        row for row in concentrated_from_inherited if row["best_bound"] < s
    )

    p45_through26 = low_profile(n, 45, 26)
    source_index = {
        "literal_mandate_at_n465_d39": {
            "argument": 465 - 1 - 39,
            "q": q_positions(465 - 1 - 39),
            "cap": 2 * q_positions(465 - 1 - 39),
        },
        "accepted_position_count_at_n465_d39": {
            "positions": 465 - 39,
            "span": 465 - 39 - 1,
            "q": q_positions(465 - 39),
            "cap": 2 * q_positions(465 - 39),
        },
    }

    output = {
        "base": "R3-CP0",
        "arithmetic": "Python unbounded integers only",
        "H_table_literal": list(H_TABLE),
        "index_convention": "q(n-d) for n-d positions; corresponding span n-d-1",
        "source_index_check": source_index,
        "uniform_L463": uniform,
        "n464_partial_profiles": {
            "cap45_through27": {
                "best_bound": b45,
                "best_c": b45c,
                "target": target_detail(n, s, c, p45),
            },
            "cap46_through27": {
                "best_bound": b46,
                "best_c": b46c,
                "target": target_detail(n, s, c, p46),
            },
            "cap45_through26_only": target_detail(n, s, c, p45_through26),
        },
        "distance_sensitivity_n464": {
            "required_one_sided_minsum": 33336 // 2 + 1,
            "cap45_prefix_from_inherited": {
                "first_closing_prefix": first_prefix45,
                "boundary_rows": [prefix45[max(0, first_prefix45["through"] - 1)], first_prefix45],
            },
            "cap46_to45_prefix": {
                "first_closing_prefix": first_prefix46_to45,
                "boundary_rows": [
                    prefix46_to45[max(0, first_prefix46_to45["through"] - 1)],
                    first_prefix46_to45,
                ],
            },
            "concentrated_reductions_from_cap46_profile": {
                "first_closing": first_concentrated_46,
                "previous": concentrated_from_46[first_concentrated_46["reduction_units"] - 1],
            },
            "concentrated_reductions_from_inherited_profile": {
                "first_closing": first_concentrated_inherited,
                "previous": concentrated_from_inherited[first_concentrated_inherited["reduction_units"] - 1],
            },
        },
        "ladder_n450_465_cap45_through27": ladder,
        "dual_bracket_audit": {
            "exact_certified_statement": "sup(S_464/a0) <= -16 on the inherited domain",
            "decimal_lower_endpoint": "-17.29",
            "lower_endpoint_status": "HEURISTIC_ONLY: no literal exact candidate/score supplied in the mandate",
            "rigorous_bracket_status": "UNDECIDED",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
