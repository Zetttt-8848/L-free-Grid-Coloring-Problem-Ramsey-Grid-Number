"""Bounded exact n-scan for the fixed t=36000 polynomial-1 profile."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from four_multi_certify import capacity
from weights_four_profiles import correlations, prefix_power_sums


T, CQ, C = 36_000, 62, 662
COARSE = list(range(21_980_000, 22_007_001, 1_000))
ROOT = Path(__file__).resolve().parents[1]


def coefficient_by_s(s: int) -> int:
    q = capacity(s - 1, 1, CQ)
    k = capacity(s - 1, 2 * q, C)
    return s - 48 * k


def main() -> None:
    sums = prefix_power_sums(T)
    a = correlations("poly1", T, sums)
    # For d>=1, the dynamic coefficient depends only on s=n-d.
    min_s = min(COARSE) - (T - 1)
    max_s = max(COARSE) - 1
    by_s = {s: coefficient_by_s(s) for s in range(min_s, max_s + 1)}

    def score(n: int) -> dict:
        weighted = sum(by_s[n - d] * a[d] for d in range(1, T))
        margin = 2 * weighted - 3 * n * a[0]
        quotient = Fraction(margin, a[0])
        return {
            "n": n,
            "doubled_margin": margin,
            "normalized_margin_numerator": quotient.numerator,
            "normalized_margin_denominator": quotient.denominator,
            "positive": margin > 0,
        }

    coarse = [score(n) for n in COARSE]
    bracket = None
    for left, right in zip(coarse, coarse[1:]):
        if not left["positive"] and right["positive"]:
            bracket = [left["n"], right["n"]]
            break
    refined = []
    best_positive = None
    if bracket is not None:
        # Extend the precomputed s range only if a bracket endpoint requires it.
        for n in range(bracket[0] + 1, bracket[1] + 1):
            rec = score(n)
            refined.append(rec)
            if rec["positive"] and (best_positive is None or n < best_positive["n"]):
                best_positive = rec

    result = {
        "honesty_label": "PROVED exact bounded scan",
        "profile": "w_i=i(36001-i), 1<=i<=36000",
        "t": T,
        "a0": a[0],
        "correlation_sha256": hashlib.sha256(
            (",".join(map(str, a))).encode("ascii")).hexdigest(),
        "coarse_grid": {"first": COARSE[0], "last": COARSE[-1], "step": 1000},
        "coarse": coarse,
        "first_nonpositive_to_positive_bracket": bracket,
        "refined": refined,
        "least_positive_in_refined_bracket": best_positive,
        "nonclaim": (
            "Nonmonotone capacity cliffs mean this scan does not exclude positive "
            "certificates between earlier coarse grid points or for other profiles."
        ),
    }
    path = ROOT / "checks" / "weights_four_bracket_scan_result.json"
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "result_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "coarse_signs": [int(r["positive"]) for r in coarse],
        "bracket": bracket,
        "refined_count": len(refined),
        "least_positive_in_refined_bracket": best_positive,
    }, indent=2))


if __name__ == "__main__":
    main()
