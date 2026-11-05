"""Exact fixed-grid non-unit weight discriminator for the FM2-4 inequality."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from four_multi_certify import capacity


N = 22_007_053
WINDOWS = [20_000, 28_443, 30_000, 40_000, 50_000, 60_000]
PROFILES = ["unit", "tent", "poly1", "poly2"]
ROOT = Path(__file__).resolve().parents[1]


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def prefix_power_sums(limit: int, degree: int = 8) -> list[list[int]]:
    sums = [[0] * (limit + 1) for _ in range(degree + 1)]
    for x in range(1, limit + 1):
        power = 1
        for r in range(degree + 1):
            sums[r][x] = sums[r][x - 1] + power
            power *= x
    return sums


def sum_polynomial(coefficients: list[int], endpoint: int,
                   sums: list[list[int]]) -> int:
    if endpoint <= 0:
        return 0
    return sum(c * sums[r][endpoint] for r, c in enumerate(coefficients))


def polynomial_correlation(t: int, d: int, p: int,
                           sums: list[list[int]]) -> int:
    m = t + 1
    base = [1]
    for factor in ([0, 1], [m, -1], [d, 1], [m - d, -1]):
        base = mul(base, factor)
    polynomial = [1]
    for _ in range(p):
        polynomial = mul(polynomial, base)
    return sum_polynomial(polynomial, t - d, sums)


def tent_correlation(t: int, d: int, sums: list[list[int]]) -> int:
    m = t + 1
    h = m // 2
    endpoint = t - d
    total = 0
    # Both terms on the increasing branch: i(i+d).
    right = min(endpoint, h - d)
    if right >= 1:
        total += sum_polynomial([0, d, 1], right, sums)
    # First increasing, second decreasing: i(m-d-i).
    left = max(1, h - d + 1)
    right = min(endpoint, h)
    if left <= right:
        prefix = sum_polynomial([0, m - d, -1], right, sums)
        before = sum_polynomial([0, m - d, -1], left - 1, sums)
        total += prefix - before
    # Both terms on the decreasing branch.
    left = max(1, h + 1)
    right = endpoint
    if left <= right:
        # (m-i)(m-d-i)=m(m-d)-(2m-d)i+i^2.
        coeff = [m * (m - d), -(2 * m - d), 1]
        total += (sum_polynomial(coeff, right, sums)
                  - sum_polynomial(coeff, left - 1, sums))
    return total


def correlations(profile: str, t: int, sums: list[list[int]]) -> list[int]:
    if profile == "unit":
        return [t - d for d in range(t)]
    if profile == "tent":
        return [tent_correlation(t, d, sums) for d in range(t)]
    if profile == "poly1":
        return [polynomial_correlation(t, d, 1, sums) for d in range(t)]
    if profile == "poly2":
        return [polynomial_correlation(t, d, 2, sums) for d in range(t)]
    raise ValueError(profile)


def direct_weights(profile: str, t: int) -> list[int]:
    if profile == "unit":
        return [1] * t
    if profile == "tent":
        return [min(i, t + 1 - i) for i in range(1, t + 1)]
    p = {"poly1": 1, "poly2": 2}[profile]
    return [(i * (t + 1 - i)) ** p for i in range(1, t + 1)]


def selfcheck_formulas() -> None:
    sums = prefix_power_sums(12)
    for t in range(1, 11):
        for profile in PROFILES:
            w = direct_weights(profile, t)
            direct = [sum(w[i] * w[i + d] for i in range(t - d))
                      for d in range(t)]
            assert correlations(profile, t, sums) == direct


def dynamic_coefficients(n: int, max_t: int) -> list[int]:
    out = [0] * max_t
    for d in range(1, max_t):
        length = n - d - 1
        q = capacity(length, 1, 62)
        k = capacity(length, 2 * q, 662)
        out[d] = n - d - 48 * k
    return out


def main() -> None:
    selfcheck_formulas()
    max_t = max(WINDOWS)
    sums = prefix_power_sums(max_t)
    coeff = dynamic_coefficients(N, max_t)
    records = []
    for t in WINDOWS:
        for profile in PROFILES:
            a = correlations(profile, t, sums)
            margin = 2 * sum(coeff[d] * a[d] for d in range(1, t)) - 3 * N * a[0]
            quotient = Fraction(margin, a[0])
            records.append({
                "n": N,
                "t": t,
                "profile": profile,
                "a0": a[0],
                "doubled_margin": margin,
                "normalized_margin_numerator": quotient.numerator,
                "normalized_margin_denominator": quotient.denominator,
                "positive": margin > 0,
                "correlation_sha256": hashlib.sha256(
                    (",".join(map(str, a))).encode("ascii")).hexdigest(),
            })
    best = max(records, key=lambda r: Fraction(r["normalized_margin_numerator"],
                                               r["normalized_margin_denominator"]))
    result = {
        "honesty_label": "PROVED exact fixed-grid scores",
        "coefficient_convention": "n-d-48*K_d with dynamic spans n-d-1, cq=62,c=662",
        "n": N,
        "windows": WINDOWS,
        "profiles": PROFILES,
        "records": records,
        "best_by_normalized_margin": best,
        "nonclaim": "This fixed grid does not optimize weights, windows, n, or capacity parameters.",
    }
    path = ROOT / "checks" / "weights_four_profile_grid.json"
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "result_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "best": best,
        "positive_records": sum(r["positive"] for r in records),
    }, indent=2))


if __name__ == "__main__":
    main()
