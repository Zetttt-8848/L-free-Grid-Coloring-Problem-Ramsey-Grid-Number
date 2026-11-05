#!/usr/bin/env python3
"""Independent exact verifier for the endpoint/profile R4 certificate.

This file imports no claimant or generator code.  Correlations use three
independent NTTs and CRT.  Capacity minima use independently rebuilt prefix
arrays, and every c=650..760 is checked at every active main distance.
"""

from __future__ import annotations

from bisect import bisect_left
import hashlib
import json
from pathlib import Path


PRIMES = [(998244353, 3), (1004535809, 3), (469762049, 3)]


def ntt(values: list[int], modulus: int, primitive_root: int, invert: bool) -> None:
    n = len(values)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            values[i], values[j] = values[j], values[i]
    length = 2
    while length <= n:
        root = pow(primitive_root, (modulus - 1) // length, modulus)
        if invert:
            root = pow(root, modulus - 2, modulus)
        half = length // 2
        for start in range(0, n, length):
            omega = 1
            for offset in range(half):
                left = values[start + offset]
                right = values[start + offset + half] * omega % modulus
                values[start + offset] = (left + right) % modulus
                values[start + offset + half] = (left - right) % modulus
                omega = omega * root % modulus
        length *= 2
    if invert:
        inverse = pow(n, modulus - 2, modulus)
        for i in range(n):
            values[i] = values[i] * inverse % modulus


def convolution_mod(a: list[int], b: list[int], modulus: int,
                    primitive_root: int) -> list[int]:
    size = 1
    while size < len(a) + len(b) - 1:
        size *= 2
    left = [x % modulus for x in a] + [0] * (size - len(a))
    right = [x % modulus for x in b] + [0] * (size - len(b))
    ntt(left, modulus, primitive_root, False)
    ntt(right, modulus, primitive_root, False)
    for i in range(size):
        left[i] = left[i] * right[i] % modulus
    ntt(left, modulus, primitive_root, True)
    return left[:len(a) + len(b) - 1]


def crt3(r1: int, r2: int, r3: int) -> int:
    m1, m2, m3 = (item[0] for item in PRIMES)
    value = r1
    value += m1 * (((r2 - value) * pow(m1, -1, m2)) % m2)
    m12 = m1 * m2
    value += m12 * (((r3 - value) * pow(m12, -1, m3)) % m3)
    return value


def exact_autocorrelations(t: int) -> list[int]:
    weights = [i * (t + 1 - i) for i in range(1, t + 1)]
    residues = [convolution_mod(weights, weights[::-1], p, root)
                for p, root in PRIMES]
    product = PRIMES[0][0] * PRIMES[1][0] * PRIMES[2][0]
    answer = []
    for d in range(t):
        index = t - 1 - d
        value = crt3(residues[0][index], residues[1][index], residues[2][index])
        assert 0 <= value < product
        answer.append(value)
    assert max(answer) <= t * max(weights) ** 2 < product
    return answer


def correction(c: int) -> int:
    return 4 * (c + 1) * c * (c - 1) // 6


def rebuild_thresholds(first_size: int, last_size: int) -> tuple[list[int], dict[int, dict]]:
    thresholds = []
    records = {}
    previous = -1
    for size in range(first_size, last_size + 1):
        maximum = -1
        cs = []
        for c in range(1, size):
            H = c * size - c * (c + 1) // 2
            span = (H * (H + 1) + correction(c) - 1) // (c * (c + 1))
            if span > maximum:
                maximum, cs = span, [c]
            elif span == maximum:
                cs.append(c)
        assert maximum > previous
        previous = maximum
        thresholds.append(maximum)
        records[size] = {"excluded_size": size, "max_span": maximum,
                         "maximizing_c": cs}
    return thresholds, records


class IndependentProfile:
    def __init__(self, n: int, max_u: int, thresholds: list[int], first_size: int):
        self.n = n
        self.q = [0] * (max_u + 1)
        self.count_prefix = [0] * (max_u + 1)
        self.weight_prefix = [0] * (max_u + 1)
        for u in range(1, max_u + 1):
            span = n - u - 1
            index = bisect_left(thresholds, span)
            assert index < len(thresholds)
            q = first_size + index - 1
            self.q[u] = q
            self.count_prefix[u] = self.count_prefix[u - 1] + 2 * q
            self.weight_prefix[u] = self.weight_prefix[u - 1] + 2 * u * q

    def minsum(self, d: int, number: int) -> tuple[int, int]:
        target = self.count_prefix[d] + number
        u = bisect_left(self.count_prefix, target, lo=d + 1)
        assert u < len(self.count_prefix)
        full_count = self.count_prefix[u - 1] - self.count_prefix[d]
        # Convert absolute u weights into h=u-d weights.
        full_weight = (self.weight_prefix[u - 1] - self.weight_prefix[d]
                       - d * full_count)
        remainder = number - full_count
        cap_at_frontier = self.count_prefix[u] - self.count_prefix[u - 1]
        assert 0 < remainder <= cap_at_frontier
        return full_weight + remainder * (u - d), u - d


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "r4_profile_endpoint_21991300.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    n, t = data["n"], data["t"]
    assert (n, t) == (21_991_300, 36_000)
    assert data["outer_c_candidate_range"] == [650, 760]

    first_size, last_size = data["golomb_threshold_size_range"]
    thresholds, q_records = rebuild_thresholds(first_size, last_size)
    for supplied in data["golomb_transition_records_used"]:
        assert supplied == q_records[supplied["excluded_size"]]

    max_u = (t - 1) + 50_000
    profile = IndependentProfile(n, max_u, thresholds, first_size)
    certificate_max_u = (t - 1) + data["max_profile_frontier"]
    q_values = profile.q[2:certificate_max_u + 1]
    q_digest = hashlib.sha256(
        (",".join(map(str, q_values))).encode("ascii")
    ).hexdigest()
    assert q_digest == data["q_profile_sha256"]

    runs = data["runs"]
    assert len(runs) == data["run_count"]
    k_by_d = [0] * t
    run_c_by_d = [0] * t
    expected_lo = 1
    for run in runs:
        lo, hi, K, c = run["lo"], run["hi"], run["K"], run["c"]
        assert lo == expected_lo and lo <= hi < t
        expected_lo = hi + 1
        assert K >= c
        for d in range(lo, hi + 1):
            k_by_d[d] = K
            run_c_by_d[d] = c

        L = n - lo - 1
        H = c * (K + 1) - c * (c + 1) // 2
        value, frontier = profile.minsum(lo, H)
        lhs = 2 * value
        rhs = L * c * (c + 1) - correction(c)
        assert lhs > rhs
        assert run["longest_span"] == L
        assert run["H"] == H
        assert run["profile_frontier"] == frontier
        assert run["minsum"] == value
        assert run["doubled_endpoint_correction"] == correction(c)
        assert run["lhs"] == lhs and run["rhs"] == rhs
        assert run["margin"] == lhs - rhs
    assert expected_lo == t

    # Independently certify the minimum K over the declared c range at every d.
    selected_cs = []
    for d in range(1, t):
        K = k_by_d[d]
        L = n - d - 1
        excluding_cs = []
        for c in range(650, 761):
            H_allowed = c * K - c * (c + 1) // 2
            allowed_sum, _ = profile.minsum(d, H_allowed)
            rhs = L * c * (c + 1) - correction(c)
            assert 2 * allowed_sum <= rhs

            H_forbidden = H_allowed + c
            forbidden_sum, _ = profile.minsum(d, H_forbidden)
            if 2 * forbidden_sum > rhs:
                excluding_cs.append(c)
        assert excluding_cs
        selected_cs.append(excluding_cs[0])

    k_digest = hashlib.sha256(
        (",".join(map(str, k_by_d[1:]))).encode("ascii")
    ).hexdigest()
    c_digest = hashlib.sha256(
        (",".join(map(str, selected_cs))).encode("ascii")
    ).hexdigest()
    assert k_digest == data["expanded_K_sha256"]
    assert c_digest == data["selected_c_sha256"]

    a = exact_autocorrelations(t)
    assert min(a) > 0
    assert (a[0], a[1], a[-1]) == (data["a0"], data["a1"], data["a_last"])
    a_digest = hashlib.sha256(
        (",".join(map(str, a))).encode("ascii")
    ).hexdigest()
    assert a_digest == data["correlation_sha256"]

    weighted = sum((n - d - 48 * k_by_d[d]) * a[d] for d in range(1, t))
    lhs = 2 * weighted
    rhs = 3 * n * a[0]
    margin = lhs - rhs
    assert weighted == data["weighted_sum"]
    assert lhs == data["doubled_lhs"] and rhs == data["doubled_rhs"]
    assert margin == data["doubled_margin"] == 551_211_731_377_452_489_346_057_152
    assert margin > 0

    result = {
        "status": "PASS",
        "arithmetic": "three-prime integer NTT, exact CRT, exhaustive integer c and threshold scans",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "n": n,
        "t": t,
        "correlations_checked": len(a),
        "golomb_target_sizes_checked": last_size - first_size + 1,
        "capacity_runs_checked": len(runs),
        "distances_checked": t - 1,
        "outer_c_values_checked_per_distance": 111,
        "doubled_lhs": lhs,
        "doubled_rhs": rhs,
        "doubled_margin": margin,
        "proved_implication": "Inherited FM1/FM2-4/FM3 plus the endpoint lemma imply R_4(L)<=21991300.",
        "global_optimality": "not claimed over n, t, weights, or c outside 650..760",
        "lower_bound_implication": "none",
    }
    output = root / "r4_profile_endpoint_21991300_verified.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
