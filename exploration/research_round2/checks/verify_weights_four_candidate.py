"""Independent exact verifier for the 22,007,052 polynomial-weight certificate.

This file imports neither the generator nor its correlation/capacity modules.
It computes all 36,000 autocorrelations by three-modulus NTT and CRT.
"""

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
                u = values[start + offset]
                v = values[start + offset + half] * omega % modulus
                values[start + offset] = (u + v) % modulus
                values[start + offset + half] = (u - v) % modulus
                omega = omega * root % modulus
        length *= 2
    if invert:
        inverse_n = pow(n, modulus - 2, modulus)
        for i in range(n):
            values[i] = values[i] * inverse_n % modulus


def convolution_mod(a: list[int], b: list[int], modulus: int,
                    primitive_root: int) -> list[int]:
    size = 1
    while size < len(a) + len(b) - 1:
        size *= 2
    fa = [x % modulus for x in a] + [0] * (size - len(a))
    fb = [x % modulus for x in b] + [0] * (size - len(b))
    ntt(fa, modulus, primitive_root, False)
    ntt(fb, modulus, primitive_root, False)
    for i in range(size):
        fa[i] = fa[i] * fb[i] % modulus
    ntt(fa, modulus, primitive_root, True)
    return fa[:len(a) + len(b) - 1]


def crt3(r1: int, r2: int, r3: int) -> int:
    m1, m2, m3 = (x[0] for x in PRIMES)
    x = r1
    x += m1 * (((r2 - x) * pow(m1, -1, m2)) % m2)
    m12 = m1 * m2
    x += m12 * (((r3 - x) * pow(m12, -1, m3)) % m3)
    return x


def exact_autocorrelations(t: int) -> list[int]:
    weights = [i * (t + 1 - i) for i in range(1, t + 1)]
    residues = [convolution_mod(weights, weights[::-1], p, root)
                for p, root in PRIMES]
    product = PRIMES[0][0] * PRIMES[1][0] * PRIMES[2][0]
    a = []
    for d in range(t):
        index = t - 1 - d
        value = crt3(residues[0][index], residues[1][index], residues[2][index])
        assert 0 <= value < product
        a.append(value)
    # A simple a priori upper bound proves CRT uniqueness over the integers.
    assert max(a) <= t * max(weights) ** 2 < product
    return a


def minsum(h: int, v: int) -> int:
    quotient, residue = divmod(h, v)
    return v * quotient * (quotient + 1) // 2 + residue * (quotient + 1)


def main() -> None:
    source = Path(__file__).resolve().parents[1] / "certificates" / "weights_four_candidate_22007052.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    n, t = data["n"], data["t"]
    cq = data["golomb_neighbor_parameter"]
    c = data["capacity_neighbor_parameter"]
    assert (n, t, cq, c) == (22_007_052, 36_000, 62, 662)

    a = exact_autocorrelations(t)
    assert a[0] == data["a0"]
    assert a[1] == data["a1"] and a[-1] == data["a_last"]
    assert min(a) > 0
    digest = hashlib.sha256((",".join(map(str, a))).encode("ascii")).hexdigest()
    assert digest == data["correlation_sha256"]

    expected_lo = 1
    weighted_sum = 0
    checked_distances = 0
    for run in data["runs"]:
        lo, hi, q, k = run["lo"], run["hi"], run["q"], run["K"]
        assert lo == expected_lo and lo <= hi < t
        expected_lo = hi + 1
        checked_distances += hi - lo + 1
        longest = n - lo - 1
        assert longest == run["longest_span"]

        hq = cq * (q + 1) - cq * (cq + 1) // 2
        lhs_q = 2 * minsum(hq, 1)
        rhs_q = longest * cq * (cq + 1)
        assert lhs_q == run["golomb_first_forbidden_lhs"]
        assert rhs_q == run["golomb_first_forbidden_rhs"]
        assert lhs_q > rhs_q

        hk = c * (k + 1) - c * (c + 1) // 2
        lhs_k = 2 * minsum(hk, 2 * q)
        rhs_k = longest * c * (c + 1)
        assert lhs_k == run["capacity_first_forbidden_lhs"]
        assert rhs_k == run["capacity_first_forbidden_rhs"]
        assert lhs_k > rhs_k

        for d in range(lo, hi + 1):
            weighted_sum += (n - d - 48 * k) * a[d]
    assert expected_lo == t and checked_distances == t - 1
    assert len(data["runs"]) == data["run_count"] == 380
    assert weighted_sum == data["weighted_sum"]
    lhs = 2 * weighted_sum
    rhs = 3 * n * a[0]
    margin = lhs - rhs
    assert lhs == data["doubled_lhs"]
    assert rhs == data["doubled_rhs"]
    assert margin == data["doubled_margin"] == 10_738_351_366_697_728_567_324_267_584
    assert margin > 0

    report = {
        "status": "PASS",
        "arithmetic": "integer NTT under three primes, exact CRT, and Python integers",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "n": n,
        "t": t,
        "profile": data["profile"],
        "correlations_checked": len(a),
        "capacity_runs_checked": len(data["runs"]),
        "distances_checked": checked_distances,
        "a0": a[0],
        "doubled_lhs": lhs,
        "doubled_rhs": rhs,
        "doubled_margin": margin,
        "proved_implication": "FM1+FM2-4+FM3 imply R_4(L)<=22007052.",
        "lower_bound_implication": "none",
    }
    output = Path(__file__).with_name("weights_four_candidate_verified.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
