#!/usr/bin/env python3
"""Independent checker for the R3 A.7 JSON certificate.

Unlike the claimant, this expands each distance cap into an explicit sorted
multiset and takes exact prefixes.  It computes expected values before it
loads the claimant JSON, then compares selected fields.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


H = [0, 1, 2, 4, 7, 12, 18, 26, 35, 45, 56, 73, 86, 107, 128,
     152, 178, 200, 217, 247, 284, 334, 357, 373, 426, 481, 493, 554,
     586]


def q_by_scan(position_count: int) -> int:
    answer = 0
    for order, needed in enumerate(H):
        if needed <= position_count:
            answer = order
        else:
            break
    return answer


def make_caps(n: int, level: int | None = None, through: int = 0) -> list[int]:
    ans = [0]
    for d in range(1, n):
        v = 2 * q_by_scan(n - d)
        if level is not None and d <= through:
            v = min(v, level)
        ans.append(v)
    return ans


def expanded_prefix(caps: list[int]) -> list[int]:
    bag: list[int] = []
    for distance, multiplicity in enumerate(caps):
        bag.extend([distance] * multiplicity)
    # The construction is already sorted because distances are enumerated.
    prefix = [0]
    for value in bag:
        prefix.append(prefix[-1] + value)
    return prefix


def explicit_prefix_sum(amount: int, prefix: list[int]) -> int:
    assert amount < len(prefix)
    return prefix[amount]


def c_bound(n: int, caps: list[int], prefix: list[int], c: int) -> int:
    right = (n - 1) * c * (c + 1)
    total_capacity = sum(caps)
    def forbidden(size: int) -> bool:
        count = sum(size - h for h in range(1, c + 1))
        if count > total_capacity:
            return True
        return 2 * explicit_prefix_sum(count, prefix) > right

    lo, hi = c, n + 1
    assert forbidden(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if forbidden(mid):
            hi = mid
        else:
            lo = mid
    return hi - 1


def all_c_best(n: int, caps: list[int]) -> tuple[int, list[int]]:
    values = []
    current_best = n
    prefix = expanded_prefix(caps)
    for c in range(1, n):
        if c > current_best:
            break
        value = c_bound(n, caps, prefix, c)
        values.append((value, c))
        current_best = min(current_best, value)
    best = min(value for value, _ in values)
    return best, [c for value, c in values if value == best]


def uniform_caps(L: int, V: int) -> list[int]:
    return [0] + [V] * L


def target(n: int, size: int, c: int, caps: list[int]) -> dict:
    count = sum(size - h for h in range(1, c + 1))
    m = explicit_prefix_sum(count, expanded_prefix(caps))
    right = (n - 1) * c * (c + 1)
    return {"H": count, "minsum": m, "twice_minsum": 2 * m,
            "rhs": right, "margin": 2 * m - right,
            "strict_contradiction": 2 * m > right}


def compute_expected() -> dict:
    uniforms = {}
    for v in [48, 45, 46]:
        uniforms[str(v)] = all_c_best(464, uniform_caps(463, v))

    ladder = []
    for n in range(450, 466):
        caps = make_caps(n, 45, 27)
        best, cs = all_c_best(n, caps)
        req = (n + 2) // 3
        ladder.append((n, req, best, cs, best < req))

    p45 = make_caps(464, 45, 27)
    p46 = make_caps(464, 46, 27)
    p45_26 = make_caps(464, 45, 26)

    prefix45 = []
    for dmax in range(40):
        caps = make_caps(464, 45, dmax)
        best, cs = all_c_best(464, caps)
        prefix45.append((dmax, target(464, 155, 8, caps), best, cs))
    close45 = next(row for row in prefix45 if row[2] < 155)

    base46 = make_caps(464, 46, 27)
    shave = []
    for dmax in range(28):
        caps = base46.copy()
        for d in range(1, dmax + 1):
            caps[d] = min(caps[d], 45)
        best, cs = all_c_best(464, caps)
        shave.append((dmax, target(464, 155, 8, caps), best, cs))
    close_shave = next(row for row in shave if row[2] < 155)

    conc46 = []
    for r in range(base46[1] + 1):
        caps = base46.copy()
        caps[1] -= r
        t = target(464, 155, 8, caps)
        best, cs = all_c_best(464, caps)
        conc46.append((r, caps[1], t, best, cs))
    close_conc46 = next(row for row in conc46 if row[3] < 155)

    base = make_caps(464)
    concbase = []
    for r in range(base[1] + 1):
        caps = base.copy()
        caps[1] -= r
        t = target(464, 155, 8, caps)
        best, cs = all_c_best(464, caps)
        concbase.append((r, caps[1], t, best, cs))
    close_concbase = next(row for row in concbase if row[3] < 155)

    return {
        "uniforms": uniforms,
        "ladder": ladder,
        "p45": (all_c_best(464, p45), target(464, 155, 8, p45)),
        "p46": (all_c_best(464, p46), target(464, 155, 8, p46)),
        "p45_26": target(464, 155, 8, p45_26),
        "prefix45_boundary": (prefix45[close45[0] - 1], close45),
        "shave_boundary": (shave[close_shave[0] - 1], close_shave),
        "shave_global_witness": target(464, 155, close_shave[3][0],
            (lambda caps: [min(value, 45) if 1 <= d <= close_shave[0] else value
                           for d, value in enumerate(caps)])(base46.copy())),
        "conc46_boundary": (conc46[close_conc46[0] - 1], close_conc46),
        "concbase_boundary": (concbase[close_concbase[0] - 1], close_concbase),
        "index": {
            "literal": (425, q_by_scan(425), 2 * q_by_scan(425)),
            "accepted": (426, 425, q_by_scan(426), 2 * q_by_scan(426)),
        },
    }


def compare(cert: dict, expected: dict) -> list[str]:
    errors: list[str] = []
    if cert["H_table_literal"] != H:
        errors.append("H table")
    got_index = cert["source_index_check"]
    if (got_index["literal_mandate_at_n465_d39"]["argument"],
            got_index["literal_mandate_at_n465_d39"]["q"],
            got_index["literal_mandate_at_n465_d39"]["cap"]) != expected["index"]["literal"]:
        errors.append("literal index")
    if (got_index["accepted_position_count_at_n465_d39"]["positions"],
            got_index["accepted_position_count_at_n465_d39"]["span"],
            got_index["accepted_position_count_at_n465_d39"]["q"],
            got_index["accepted_position_count_at_n465_d39"]["cap"]) != expected["index"]["accepted"]:
        errors.append("accepted index")
    for v, (bound, cs) in expected["uniforms"].items():
        got = cert["uniform_L463"][v]
        if (got["best_bound"], got["best_c"]) != (bound, cs):
            errors.append(f"uniform {v}")

    got_ladder = cert["ladder_n450_465_cap45_through27"]
    for got, exp in zip(got_ladder, expected["ladder"], strict=True):
        n, req, bound, cs, closes = exp
        if (got["n"], got["required_ceil_n_over_3"], got["best_bound"],
                got["best_c"], got["closes_required_size"]) != exp:
            errors.append(f"ladder n={n}")

    for name in ("p45", "p46"):
        (bound, cs), detail = expected[name]
        key = "cap45_through27" if name == "p45" else "cap46_through27"
        got = cert["n464_partial_profiles"][key]
        if (got["best_bound"], got["best_c"]) != (bound, cs):
            errors.append(name + " bound")
        for field, value in detail.items():
            if got["target"][field] != value:
                errors.append(name + " target " + field)

    for field, value in expected["p45_26"].items():
        if cert["n464_partial_profiles"]["cap45_through26_only"][field] != value:
            errors.append("p45_26 " + field)

    checks = [
        ("cap45_prefix_from_inherited", expected["prefix45_boundary"]),
        ("cap46_to45_prefix", expected["shave_boundary"]),
    ]
    sens = cert["distance_sensitivity_n464"]
    for key, boundary in checks:
        before, after = boundary
        got_before, got_after = sens[key]["boundary_rows"]
        for got, exp in ((got_before, before), (got_after, after)):
            dmax, detail, bound, cs = exp
            wanted = {"through": dmax, "minsum": detail["minsum"],
                      "margin": detail["margin"], "best_bound": bound,
                      "best_c": cs}
            if got != wanted:
                errors.append(key + f" through={dmax}")

    witness = cert["distance_sensitivity_n464"]["cap46_to45_prefix"]["global_closing_witness"]
    for field, value in expected["shave_global_witness"].items():
        if witness[field] != value:
            errors.append("cap46_to45 global witness " + field)

    for key, boundary in [
        ("concentrated_reductions_from_cap46_profile", expected["conc46_boundary"]),
        ("concentrated_reductions_from_inherited_profile", expected["concbase_boundary"]),
    ]:
        before, after = boundary
        got_before = sens[key]["previous"]
        got_after = sens[key]["first_closing"]
        for got, exp in ((got_before, before), (got_after, after)):
            reduction, newcap, detail, bound, cs = exp
            wanted = {"reduction_units": reduction, "new_cap_d1": newcap,
                      "minsum": detail["minsum"], "margin": detail["margin"],
                      "best_bound": bound, "best_c": cs}
            if got != wanted:
                errors.append(key + f" reduction={reduction}")

    return errors


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: a7_independent_check.py CERTIFICATE.json")
    expected = compute_expected()  # isolate before reading claimant output
    cert = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = compare(cert, expected)
    result = {
        "checker": "explicit expanded distance multiset; no claimant imports",
        "arithmetic": "Python unbounded integers only",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "checked_ladder_rows": 16,
        "checked_uniform_caps": [45, 46, 48],
        "checked_sensitivity_boundaries": 4,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
