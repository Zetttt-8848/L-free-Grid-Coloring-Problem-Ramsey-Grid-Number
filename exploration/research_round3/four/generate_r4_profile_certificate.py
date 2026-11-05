#!/usr/bin/env python3
"""Generate the frozen follow-up n=21,991,300 endpoint/profile certificate."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

from r4_profile_scout import (
    MAX_D,
    T,
    ProfileOracle,
    correlations,
    doubled_endpoint_correction,
    golomb_thresholds,
    profile_capacity,
    profile_capacity_from_seed,
)


N = 21_991_300
C_VALUES = list(range(650, 761))


def minsum_uniform(number: int, cap: int) -> int:
    a, b = divmod(number, cap)
    return cap * a * (a + 1) // 2 + b * (a + 1)


def uniform_capacity(L: int, V: int, c: int) -> int:
    rhs = L * c * (c + 1)
    lo, hi = c, 600_000
    while hi - lo > 1:
        size = (lo + hi) // 2
        h = c * size - c * (c + 1) // 2
        if 2 * minsum_uniform(h, V) > rhs:
            hi = size
        else:
            lo = size
    return hi - 1


def profile_first_forbidden(n: int, d: int, K: int, c: int,
                            oracle: ProfileOracle) -> dict:
    L = n - d - 1
    h = c * (K + 1) - c * (c + 1) // 2
    value, frontier = oracle.minsum(d, h)
    lhs = 2 * value
    correction = doubled_endpoint_correction(c)
    rhs = L * c * (c + 1) - correction
    assert K >= c and lhs > rhs
    return {
        "longest_span": L,
        "H": h,
        "profile_frontier": frontier,
        "minsum": value,
        "doubled_endpoint_correction": correction,
        "lhs": lhs,
        "rhs": rhs,
        "margin": lhs - rhs,
    }


def main() -> None:
    thresholds, q_records = golomb_thresholds(endpoint=True)
    a = correlations()
    oracle = ProfileOracle(N, 110_000, thresholds, q_records)

    weighted = 0
    weighted_fixed662 = 0
    weighted_uniform = 0
    seeds: dict[int, int] = {}
    fixed_seed = None
    runs = []
    expanded_k = []
    chosen_cs = []
    drops = []
    max_frontier = 0

    for d in range(1, T):
        choices = []
        for c in C_VALUES:
            if c in seeds:
                k, frontier = profile_capacity_from_seed(
                    N, d, c, oracle, seeds[c], endpoint=True
                )
            else:
                k, frontier = profile_capacity(N, d, c, oracle, endpoint=True)
            seeds[c] = k
            choices.append((k, c, frontier))
        k, c, frontier = min(choices)

        if fixed_seed is None:
            k_fixed, _ = profile_capacity(N, d, 662, oracle, endpoint=True)
        else:
            k_fixed, _ = profile_capacity_from_seed(
                N, d, 662, oracle, fixed_seed, endpoint=True
            )
        fixed_seed = k_fixed

        L = N - d - 1
        q_uniform = uniform_capacity(L, 1, 62)
        k_uniform = uniform_capacity(L, 2 * q_uniform, 662)

        expanded_k.append(k)
        chosen_cs.append(c)
        drops.append(k_uniform - k)
        max_frontier = max(max_frontier, frontier)
        weighted += (N - d - 48 * k) * a[d]
        weighted_fixed662 += (N - d - 48 * k_fixed) * a[d]
        weighted_uniform += (N - d - 48 * k_uniform) * a[d]

        if not runs or runs[-1]["K"] != k:
            run = {"lo": d, "hi": d, "K": k, "c": c}
            run.update(profile_first_forbidden(N, d, k, c, oracle))
            runs.append(run)
        else:
            runs[-1]["hi"] = d

    doubled_lhs = 2 * weighted
    doubled_rhs = 3 * N * a[0]
    margin = doubled_lhs - doubled_rhs
    assert margin == 551_211_731_377_452_489_346_057_152 > 0

    max_u = MAX_D + max_frontier
    q_values = oracle.q[2:max_u + 1]
    used_q = sorted(set(q_values))
    q_transition_records = [q_records[q + 1] for q in used_q]
    result = {
        "certificate_type": "exact candidate certificate; Ramsey implication conditional on inherited FM1/FM2-4/FM3",
        "statement": "R_4(L) <= 21991300",
        "honesty_label": "PROVED implication pending independent certificate verification",
        "base": "R3-CP0",
        "n": N,
        "t": T,
        "profile": "w_i=i(36001-i), 1<=i<=36000",
        "outer_c_candidate_range": [C_VALUES[0], C_VALUES[-1]],
        "outer_selection": "minimum exact K_d over every integer c in the candidate range; no global-c optimality claim",
        "golomb_selection": "global optimum of endpoint-refined FM3 over every integer 1<=c<excluded_size",
        "endpoint_correction": "distinctness ell_i=i; doubled RHS subtracts 4*binom(c+1,3)",
        "golomb_threshold_size_range": [4600, 4900],
        "golomb_transition_records_used": q_transition_records,
        "runs": runs,
        "run_count": len(runs),
        "distances_covered": T - 1,
        "max_profile_frontier": max_frontier,
        "a0": a[0],
        "a1": a[1],
        "a_last": a[-1],
        "correlation_sha256": hashlib.sha256(
            (",".join(map(str, a))).encode("ascii")
        ).hexdigest(),
        "expanded_K_sha256": hashlib.sha256(
            (",".join(map(str, expanded_k))).encode("ascii")
        ).hexdigest(),
        "selected_c_sha256": hashlib.sha256(
            (",".join(map(str, chosen_cs))).encode("ascii")
        ).hexdigest(),
        "q_profile_sha256": hashlib.sha256(
            (",".join(map(str, q_values))).encode("ascii")
        ).hexdigest(),
        "weighted_sum": weighted,
        "doubled_lhs": doubled_lhs,
        "doubled_rhs": doubled_rhs,
        "doubled_margin": margin,
        "improvement_over_22006246": 22_006_246 - N,
        "support_size": T,
        "active_constraints": [
            "integer n and c",
            "positive polynomial weights",
            "profile first-forbidden inequality on every capacity run",
            "FM2-4 strict score inequality",
        ],
        "sensitivity": {
            "fixed_outer_c662_margin": 2 * weighted_fixed662 - doubled_rhs,
            "inherited_uniform_inner_profile_margin": 2 * weighted_uniform - doubled_rhs,
            "capacity_drop_vs_inherited_same_n": {
                "minimum": min(drops),
                "maximum": max(drops),
                "positive_distance_count": sum(x > 0 for x in drops),
                "sum": sum(drops),
            },
            "selected_c_min": min(chosen_cs),
            "selected_c_max": max(chosen_cs),
            "selected_c_counts": {str(c): count for c, count in sorted(Counter(chosen_cs).items())},
        },
        "global_bound_status": "No global optimum over n, t, weights, or outer c is claimed.",
        "lower_bound_implication": "none",
        "dependencies": ["accepted Round-2 FM1", "accepted Round-2 FM2-4", "accepted Round-2 FM3"],
    }
    output = Path(__file__).with_name("r4_profile_endpoint_21991300.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "run_count": len(runs),
        "margin": margin,
        "improvement": result["improvement_over_22006246"],
        "max_profile_frontier": max_frontier,
        "drop_summary": result["sensitivity"]["capacity_drop_vs_inherited_same_n"],
        "fixed_c662_margin": result["sensitivity"]["fixed_outer_c662_margin"],
        "uniform_profile_margin": result["sensitivity"]["inherited_uniform_inner_profile_margin"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
