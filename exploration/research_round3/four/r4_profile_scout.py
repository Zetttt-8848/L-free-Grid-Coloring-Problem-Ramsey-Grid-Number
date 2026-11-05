#!/usr/bin/env python3
"""Exact-integer scout for the distance-refined R4 inner capacity.

The output is a candidate-selection aid, not an independent certificate.
No file is written.  Golomb capacities are globally optimized by an exact
threshold table; outer capacities use the requested c choices.
"""

from __future__ import annotations

import argparse
from bisect import bisect_left
import json


T = 36_000
MAX_D = T - 1


def doubled_endpoint_correction(c: int) -> int:
    # 4*binom(c+1,3), matching the doubled 2*M comparison.
    return 4 * (c + 1) * c * (c - 1) // 6


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def prefix_power_sums(limit: int, degree: int = 4) -> list[list[int]]:
    out = [[0] * (limit + 1) for _ in range(degree + 1)]
    for x in range(1, limit + 1):
        power = 1
        for degree_index in range(degree + 1):
            out[degree_index][x] = out[degree_index][x - 1] + power
            power *= x
    return out


def correlations() -> list[int]:
    sums = prefix_power_sums(T)
    m = T + 1
    answer = []
    for d in range(T):
        polynomial = [1]
        for factor in ([0, 1], [m, -1], [d, 1], [m - d, -1]):
            polynomial = mul(polynomial, factor)
        endpoint = T - d
        answer.append(sum(coef * sums[p][endpoint]
                          for p, coef in enumerate(polynomial)))
    return answer


def golomb_thresholds(first_size: int = 4_600, last_size: int = 4_900,
                      endpoint: bool = False) -> tuple[list[int], dict[int, dict]]:
    """Maximum span at which each target size is excluded, all c scanned."""
    thresholds: list[int] = []
    records: dict[int, dict] = {}
    previous = -1
    for size in range(first_size, last_size + 1):
        best_span = -1
        best_cs: list[int] = []
        for c in range(1, size):
            count = c * size - c * (c + 1) // 2
            # V=1: 2*minsum=count*(count+1).
            correction = doubled_endpoint_correction(c) if endpoint else 0
            threshold = (count * (count + 1) + correction - 1) // (c * (c + 1))
            if threshold > best_span:
                best_span, best_cs = threshold, [c]
            elif threshold == best_span:
                best_cs.append(c)
        assert best_span > previous
        previous = best_span
        thresholds.append(best_span)
        records[size] = {"excluded_size": size, "max_span": best_span,
                         "maximizing_c": best_cs}
    return thresholds, records


class ProfileOracle:
    def __init__(self, n: int, max_u: int, thresholds: list[int],
                 records: dict[int, dict], first_size: int = 4_600):
        self.n = n
        self.first_size = first_size
        self.thresholds = thresholds
        self.records = records
        self.q = [0] * (max_u + 1)
        self.pq = [0] * (max_u + 1)
        self.puq = [0] * (max_u + 1)
        for u in range(1, max_u + 1):
            span = n - u - 1
            index = bisect_left(thresholds, span)
            if index == len(thresholds):
                raise ValueError("Golomb threshold table too short")
            excluded_size = first_size + index
            q = excluded_size - 1
            self.q[u] = q
            self.pq[u] = self.pq[u - 1] + q
            self.puq[u] = self.puq[u - 1] + u * q

    def minsum(self, d: int, count: int) -> tuple[int, int]:
        # V_h=2*q(n-(d+h)-1).  Find the last partly filled h.
        target_half = self.pq[d] + (count + 1) // 2
        u = bisect_left(self.pq, target_half, lo=d + 1)
        if u >= len(self.pq):
            raise ValueError("profile prefix too short")
        sum_q = self.pq[u - 1] - self.pq[d]
        full_count = 2 * sum_q
        full_weight = 2 * ((self.puq[u - 1] - self.puq[d]) - d * sum_q)
        h = u - d
        remainder = count - full_count
        assert 0 < remainder <= 2 * self.q[u]
        return full_weight + remainder * h, h


def profile_capacity(n: int, d: int, c: int, oracle: ProfileOracle,
                     endpoint: bool = False) -> tuple[int, int]:
    L = n - d - 1
    rhs = L * c * (c + 1)
    if endpoint:
        rhs -= doubled_endpoint_correction(c)

    def forbidden(size: int) -> tuple[bool, int]:
        count = c * size - c * (c + 1) // 2
        value, frontier = oracle.minsum(d, count)
        return 2 * value > rhs, frontier

    lo, hi = c, 600_000
    assert forbidden(hi)[0]
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if forbidden(mid)[0]:
            hi = mid
        else:
            lo = mid
    passed, frontier = forbidden(hi)
    assert passed
    return hi - 1, frontier


def profile_capacity_from_seed(n: int, d: int, c: int, oracle: ProfileOracle,
                               seed: int, endpoint: bool = False) -> tuple[int, int]:
    """Exact capacity using a nearby previously certified integer as seed."""
    L = n - d - 1
    rhs = L * c * (c + 1)
    if endpoint:
        rhs -= doubled_endpoint_correction(c)

    def forbidden(size: int) -> tuple[bool, int]:
        count = c * size - c * (c + 1) // 2
        value, frontier = oracle.minsum(d, count)
        return 2 * value > rhs, frontier

    k = max(c, seed)
    while k > c and forbidden(k)[0]:
        k -= 1
    while not forbidden(k + 1)[0]:
        k += 1
    assert not forbidden(k)[0]
    passed, frontier = forbidden(k + 1)
    assert passed
    return k, frontier


def score(n: int, c_values: list[int], a: list[int], thresholds: list[int],
          records: dict[int, dict], endpoint: bool = False) -> dict:
    oracle = ProfileOracle(n, 110_000, thresholds, records)
    weighted = 0
    runs = []
    last = None
    max_frontier = 0
    capacity_sum = 0
    seeds: dict[int, int] = {}
    for d in range(1, T):
        choices = []
        for c in c_values:
            if c in seeds:
                k, frontier = profile_capacity_from_seed(
                    n, d, c, oracle, seeds[c], endpoint=endpoint
                )
            else:
                k, frontier = profile_capacity(n, d, c, oracle, endpoint=endpoint)
            seeds[c] = k
            choices.append((k, c, frontier))
        k, c, frontier = min(choices)
        max_frontier = max(max_frontier, frontier)
        capacity_sum += k
        weighted += (n - d - 48 * k) * a[d]
        item = (k, c)
        if item != last:
            runs.append({"lo": d, "hi": d, "K": k, "c": c})
            last = item
        else:
            runs[-1]["hi"] = d
    margin = 2 * weighted - 3 * n * a[0]
    used_q = sorted(set(oracle.q[2:MAX_D + max_frontier + 1]))
    return {
        "n": n,
        "t": T,
        "outer_c_values": c_values,
        "a0": a[0],
        "weighted_sum": weighted,
        "doubled_margin": margin,
        "positive": margin > 0,
        "capacity_sum": capacity_sum,
        "max_profile_frontier": max_frontier,
        "K_c_run_count": len(runs),
        "first_run": runs[0],
        "last_run": runs[-1],
        "used_optimal_golomb_bounds": used_q,
        "endpoint_distinctness_correction": endpoint,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, nargs="+", required=True)
    parser.add_argument("--c", type=int, nargs="+", default=[662])
    parser.add_argument("--c-range", type=int, nargs=2)
    parser.add_argument("--endpoint", action="store_true")
    args = parser.parse_args()
    c_values = args.c
    if args.c_range is not None:
        lo, hi = args.c_range
        c_values = list(range(lo, hi + 1))
    thresholds, records = golomb_thresholds(endpoint=args.endpoint)
    a = correlations()
    output = {
        "honesty_label": "HEURISTIC candidate selection; scores are exact integers",
        "golomb_threshold_size_range": [4600, 4900],
        "scores": [score(n, c_values, a, thresholds, records,
                         endpoint=args.endpoint) for n in args.n],
        "nonclaim": "No global minimum over n, weights, windows, or outer c.",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
