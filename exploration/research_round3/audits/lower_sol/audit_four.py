#!/usr/bin/env python3
"""Independent integer audit of the Round-3 four-color certificate.

No claimant checker is imported or invoked.  Autocorrelations are evaluated
from quartic power sums.  Golomb thresholds, residual profiles, all run
comparisons, and the declared 650..760 outer scan are rebuilt from scratch.
"""

from __future__ import annotations

from bisect import bisect_left
from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
F = ROOT / "four"
CERT_PATH = F / "r4_profile_endpoint_21991300.json"


def digest_numbers(values) -> str:
    return sha256(",".join(map(str, values)).encode("ascii")).hexdigest()


def sum_powers_0_to_4(m: int):
    """Return sum_{i=1}^m i^k for k=0,...,4 in exact integers."""
    s0 = m
    s1 = m * (m + 1) // 2
    s2 = m * (m + 1) * (2 * m + 1) // 6
    s3 = s1 * s1
    s4 = m * (m + 1) * (2 * m + 1) * (3 * m * m + 3 * m - 1) // 30
    return s0, s1, s2, s3, s4


def correlation(t: int, d: int) -> int:
    """Quartic expansion of sum i(A-i)(i+d)(A-i-d), A=t+1."""
    A = t + 1
    m = t - d
    _, s1, s2, s3, s4 = sum_powers_0_to_4(m)
    constant = d * (A - d)
    return (s4
            + (-2 * A + 2 * d) * s3
            + (A * (A - 2 * d) - constant) * s2
            + A * constant * s1)


def direct_correlation(t: int, d: int) -> int:
    A = t + 1
    return sum(i * (A - i) * (i + d) * (A - i - d)
               for i in range(1, t - d + 1))


def golomb_tau(s: int):
    best = -1
    maximizers = []
    for c in range(1, s):
        H = c * s - c * (c + 1) // 2
        threshold = (H * (H + 1) + 4 * math.comb(c + 1, 3) - 1) // (c * (c + 1))
        if threshold > best:
            best = threshold
            maximizers = [c]
        elif threshold == best:
            maximizers.append(c)
    return best, maximizers


def main():
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    n, t = cert["n"], cert["t"]
    failures = []

    # Exact correlations by an independent closed form, with direct summation
    # checks at boundary and interior indices.
    correlations = [correlation(t, d) for d in range(t)]
    direct_indices = [0, 1, 2, 17, 997, 17999, 35997, 35998, 35999]
    direct_checks = {str(d): direct_correlation(t, d) == correlations[d]
                     for d in direct_indices}
    correlation_checks = {
        "all_positive": all(x > 0 for x in correlations),
        "direct_samples": all(direct_checks.values()),
        "a0": correlations[0] == cert["a0"],
        "a1": correlations[1] == cert["a1"],
        "a_last": correlations[-1] == cert["a_last"],
        "serialized_sha256": digest_numbers(correlations) == cert["correlation_sha256"],
    }
    if not all(correlation_checks.values()):
        failures.append({"correlations": correlation_checks})

    # Exhaust every inner Golomb neighbor parameter, not merely c=68.
    size_lo, size_hi = cert["golomb_threshold_size_range"]
    tau_records = {}
    tau_values = []
    tau_maximizers = []
    for s in range(size_lo, size_hi + 1):
        value, maximizers = golomb_tau(s)
        tau_values.append(value)
        tau_maximizers.append(maximizers)
        tau_records[s] = (value, maximizers)
    strictly_increasing = all(a < b for a, b in zip(tau_values, tau_values[1:]))

    used_expected = [
        {"excluded_size": s, "max_span": tau_records[s][0], "maximizing_c": tau_records[s][1]}
        for s in range(4751, 4760)
    ]
    golomb_checks = {
        "sizes_scanned": size_hi - size_lo + 1,
        "all_c_scanned": sum(s - 1 for s in range(size_lo, size_hi + 1)),
        "strict_threshold_order": strictly_increasing,
        "used_transitions": used_expected == cert["golomb_transition_records_used"],
        "used_maximizer_68": all(tau_records[s][1] == [68] for s in range(4751, 4760)),
    }
    if not all(golomb_checks.values()):
        failures.append({"golomb": golomb_checks})

    def Q(span: int) -> int:
        pos = bisect_left(tau_values, span)
        if pos == len(tau_values):
            raise ValueError(f"Golomb scan does not cover residual span {span}")
        # Minimal excluded size is size_lo+pos, so the order cap is one less.
        return size_lo + pos - 1

    # The profile depends on d+h only.  Prefixing that one sequence supports
    # independent O(log t) run checks and the complete 111-c scan.
    max_r = 100000
    cap_prefix = [0] * (max_r + 1)
    indexed_cap_prefix = [0] * (max_r + 1)
    q_used = []
    for r in range(1, max_r + 1):
        q = Q(n - 1 - r)
        q_used.append(q)
        v = 2 * q
        cap_prefix[r] = cap_prefix[r - 1] + v
        indexed_cap_prefix[r] = indexed_cap_prefix[r - 1] + r * v

    def prefix_count(d: int, endpoint: int) -> int:
        return cap_prefix[endpoint] - cap_prefix[d]

    def prefix_weight(d: int, endpoint: int) -> int:
        count = prefix_count(d, endpoint)
        return indexed_cap_prefix[endpoint] - indexed_cap_prefix[d] - d * count

    def profile_minimum(H: int, d: int):
        """Sum first H entries of V_{d,h}=2Q(n-d-1-h)."""
        lo, hi = d, min(max_r, d + 50000)
        if prefix_count(d, hi) < H:
            raise ValueError("profile prefix too short")
        while lo < hi:
            mid = (lo + hi) // 2
            if prefix_count(d, mid) >= H:
                hi = mid
            else:
                lo = mid + 1
        endpoint = lo
        before = endpoint - 1
        used = prefix_count(d, before)
        frontier = endpoint - d
        total = prefix_weight(d, before) + (H - used) * frontier
        return total, frontier

    # Validate every serialized run at its longest span, including endpoint
    # correction, integer indexing, and the strict first-forbidden comparison.
    run_results = []
    coverage = []
    expanded_K = []
    run_cs = []
    for index, run in enumerate(cert["runs"]):
        lo, hi, K, c = run["lo"], run["hi"], run["K"], run["c"]
        L = n - lo - 1
        H = c * (K + 1) - c * (c + 1) // 2
        minimum, frontier = profile_minimum(H, lo)
        correction = 4 * math.comb(c + 1, 3)
        lhs = 2 * minimum
        rhs = L * c * (c + 1) - correction
        margin = lhs - rhs
        checks = {
            "longest_span_index": L == run["longest_span"],
            "H": H == run["H"],
            "profile_minimum": minimum == run["minsum"],
            "frontier": frontier == run["profile_frontier"],
            "endpoint_correction": correction == run["doubled_endpoint_correction"],
            "lhs": lhs == run["lhs"],
            "rhs": rhs == run["rhs"],
            "margin": margin == run["margin"] and margin > 0,
            "valid_neighbor_parameter": 1 <= c < K + 1,
        }
        if not all(checks.values()):
            failures.append({"run": index, "interval": [lo, hi], "checks": checks})
        run_results.append({
            "index": index,
            "lo": lo,
            "hi": hi,
            "K": K,
            "c": c,
            "H": H,
            "minsum": minimum,
            "frontier": frontier,
            "lhs": lhs,
            "rhs": rhs,
            "margin": margin,
            "pass": all(checks.values()),
        })
        coverage.extend(range(lo, hi + 1))
        expanded_K.extend([K] * (hi - lo + 1))
        run_cs.extend([c] * (hi - lo + 1))

    coverage_checks = {
        "run_count": len(run_results) == cert["run_count"] == 561,
        "all_35999_distances_once": coverage == list(range(1, t)),
        "distances_covered": len(coverage) == cert["distances_covered"] == 35999,
        "expanded_K_sha256": digest_numbers(expanded_K) == cert["expanded_K_sha256"],
        "max_frontier": max(x["frontier"] for x in run_results) == cert["max_profile_frontier"],
        "all_strict": all(x["margin"] > 0 for x in run_results),
    }
    if not all(coverage_checks.values()):
        failures.append({"coverage": coverage_checks})

    # Reconstruct the entire declared bounded outer optimization.  For a fixed
    # d,c, the endpoint RHS is a budget on P.  Inverting the ordered profile
    # gives the largest allowed H directly, then the largest allowed s=K.
    def K_for_c(d: int, c: int) -> int:
        L = n - d - 1
        doubled_rhs = L * c * (c + 1) - 4 * math.comb(c + 1, 3)
        budget = doubled_rhs // 2  # P is integral; handles odd RHS exactly.
        lo, hi = d, min(max_r, d + 50000)
        if prefix_weight(d, hi) <= budget:
            raise ValueError("weighted profile prefix too short")
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if prefix_weight(d, mid) <= budget:
                lo = mid
            else:
                hi = mid - 1
        endpoint = lo
        allowed_H = prefix_count(d, endpoint)
        next_h = endpoint - d + 1
        next_capacity = 2 * Q(n - 1 - (endpoint + 1))
        remaining_budget = budget - prefix_weight(d, endpoint)
        allowed_H += min(next_capacity, remaining_budget // next_h)
        return (allowed_H + c * (c + 1) // 2) // c

    selected_K = []
    selected_c = []
    tie_count = 0
    candidate_lo, candidate_hi = cert["outer_c_candidate_range"]
    for d in range(1, t):
        choices = [(K_for_c(d, c), c) for c in range(candidate_lo, candidate_hi + 1)]
        best_K = min(k for k, _ in choices)
        best_cs = [c for k, c in choices if k == best_K]
        selected_K.append(best_K)
        selected_c.append(best_cs[0])  # claimant's deterministic first tie rule
        tie_count += len(best_cs) > 1
    declared_counts = {int(k): v for k, v in cert["sensitivity"]["selected_c_counts"].items()}
    outer_checks = {
        "parameters_per_distance": candidate_hi - candidate_lo + 1 == 111,
        "evaluations": (candidate_hi - candidate_lo + 1) * (t - 1),
        "selected_K_matches_runs": selected_K == expanded_K,
        "expanded_K_hash": digest_numbers(selected_K) == cert["expanded_K_sha256"],
        "selected_c_hash": digest_numbers(selected_c) == cert["selected_c_sha256"],
        "selected_c_counts": Counter(selected_c) == Counter(declared_counts),
        "selected_c_range": min(selected_c) == cert["sensitivity"]["selected_c_min"]
                            and max(selected_c) == cert["sensitivity"]["selected_c_max"],
    }
    if not all(outer_checks.values()):
        failures.append({"bounded_outer_scan": outer_checks})

    # Exact FM2-4 weighted score using the reconstructed K at every distance.
    terms = [(n - d - 48 * selected_K[d - 1]) * correlations[d]
             for d in range(1, t)]
    weighted_sum = sum(terms)
    doubled_lhs = 2 * weighted_sum
    doubled_rhs = 3 * n * correlations[0]
    doubled_margin = doubled_lhs - doubled_rhs
    score_checks = {
        "weighted_sum": weighted_sum == cert["weighted_sum"],
        "doubled_lhs": doubled_lhs == cert["doubled_lhs"],
        "doubled_rhs": doubled_rhs == cert["doubled_rhs"],
        "doubled_margin": doubled_margin == cert["doubled_margin"],
        "target_margin": doubled_margin == 551211731377452489346057152,
        "strictly_positive": doubled_margin > 0,
        "improvement": 22006246 - n == cert["improvement_over_22006246"] == 14946,
        # The substitution is through -48*a_d*K_d.  Since a_d>0 and the
        # true capacity is <=K_d, this is a valid lower substitution; the
        # resulting whole bracket n-d-48K_d need not itself be positive.
        "capacity_substitution_sign": all(correlations[d] > 0 for d in range(1, t)),
    }
    if not all(score_checks.values()):
        failures.append({"score": score_checks})

    output = {
        "audit": "R3 core F independent lower_sol review",
        "verdict": "PASS" if not failures else "MAJOR",
        "failures": failures,
        "certificate_sha256": sha256(CERT_PATH.read_bytes()).hexdigest(),
        "correlations": {
            "method": "quartic expansion plus exact sums of powers through degree 4",
            "checks": correlation_checks,
            "direct_sample_checks": direct_checks,
            "a0": correlations[0],
            "a1": correlations[1],
            "a_last": correlations[-1],
            "own_sha256": digest_numbers(correlations),
        },
        "golomb_thresholds": {
            "checks": golomb_checks,
            "used": used_expected,
            "tau_4600": tau_records[4600],
            "tau_4900": tau_records[4900],
            "own_sha256": digest_numbers(tau_values),
            "q_range_in_prefix": [min(q_used), max(q_used)],
            "q_prefix_100000_sha256": digest_numbers(q_used),
        },
        "runs": run_results,
        "coverage": coverage_checks,
        "bounded_outer_scan": {
            "checks": outer_checks,
            "tie_distances": tie_count,
            "selected_c_counts": dict(sorted(Counter(selected_c).items())),
            "selected_K_sha256": digest_numbers(selected_K),
            "selected_c_sha256": digest_numbers(selected_c),
            "scope": "Exact only for fixed n,t,weights and c=650..760; no global optimization over other parameters is inferred.",
        },
        "score": {
            "checks": score_checks,
            "weighted_sum": weighted_sum,
            "doubled_lhs": doubled_lhs,
            "doubled_rhs": doubled_rhs,
            "doubled_margin": doubled_margin,
            "term_vector_sha256": digest_numbers(terms),
        },
        "structural_audit": {
            "residual_span": "For x,x+h in a span-L set, x lies between the first mark and last mark minus h, hence each FM1 completion-color fiber has span at most L-h. Summing the two Golomb fiber caps gives r_B(h)<=2Q(L-h).",
            "endpoint_identity": "Summing rank gaps j=1..c cancels interior coefficients and gives sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1}), with 1-based ranks exactly as serialized.",
            "endpoint_bound": "Distinct integer ranks give b_{i+1}>=b_1+i and b_{s-i}<=b_s-i even when endpoint blocks overlap, so each paired difference is at most L-2i. The weighted correction is 2*sum(c-i)i=2*C(c+1,3), or 4*C(c+1,3) after doubling.",
            "strict_rounding": "For Golomb V_h=1, exclusion is H(H+1)>L*c(c+1)-4*C(c+1,3). Thus the largest excluded integer L is floor((H(H+1)+4*C(c+1,3)-1)/(c(c+1))), explaining the -1. For a general integer P, P<=floor(RHS/2) is the exact non-strict feasibility budget, including odd RHS.",
            "run_monotonicity": "Within a constant-K run, increasing d decreases L=n-d-1 and weakly decreases every Q(L-h). The ordered-profile minimum therefore weakly increases, while the endpoint RHS decreases. The check at lo is the weakest comparison.",
            "optimization_scope": "The per-run valid c witnesses alone prove the K caps. The exhaustive c=650..760 reconstruction additionally verifies the reported bounded selection, but makes no claim for c outside that set or for other n,t,weights.",
        },
    }
    out_path = HERE / "four_audit.json"
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "verdict": output["verdict"],
        "golomb": golomb_checks,
        "runs_passed": sum(x["pass"] for x in run_results),
        "minimum_run_margin": min(x["margin"] for x in run_results),
        "coverage": coverage_checks,
        "outer": outer_checks,
        "score": output["score"],
    }, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
