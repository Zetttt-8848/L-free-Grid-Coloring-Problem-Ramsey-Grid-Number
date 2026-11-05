"""Exact one-step lower-side profile discriminator after W4-P1 erratum."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from weights_four_profiles import (
    correlations, dynamic_coefficients, prefix_power_sums, selfcheck_formulas,
)


N = 22_007_052
WINDOWS = [36_000, 38_000, 39_000, 40_000, 41_000, 42_000, 44_000]
PROFILES = ["tent", "poly1", "poly2"]
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    selfcheck_formulas()
    sums = prefix_power_sums(max(WINDOWS))
    coeff = dynamic_coefficients(N, max(WINDOWS))
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
        "coefficient_convention": "n-d-48*K_d with n-d-1 dynamic spans, cq=62,c=662",
        "n": N,
        "windows": WINDOWS,
        "profiles": PROFILES,
        "records": records,
        "best_by_normalized_margin": best,
        "positive_records": sum(r["positive"] for r in records),
        "nonclaim": "These 21 profiles do not optimize the nonnegative-weight relaxation.",
    }
    path = ROOT / "checks" / "weights_four_lower_step_result.json"
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "result_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "best": best,
        "positive_records": result["positive_records"],
    }, indent=2))


if __name__ == "__main__":
    main()
