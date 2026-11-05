"""Exact one-profile slack audit one side below the verified R4 candidate."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from weights_four_profiles import correlations, dynamic_coefficients, prefix_power_sums


N, T = 22_007_051, 36_000


def main() -> None:
    sums = prefix_power_sums(T)
    a = correlations("poly1", T, sums)
    coeff = dynamic_coefficients(N, T)
    weighted = sum(coeff[d] * a[d] for d in range(1, T))
    margin = 2 * weighted - 3 * N * a[0]
    quotient = Fraction(margin, a[0])
    result = {
        "honesty_label": "PROVED exact single-profile score",
        "n": N,
        "t": T,
        "profile": "w_i=i(36001-i), 1<=i<=36000",
        "a0": a[0],
        "doubled_margin": margin,
        "normalized_margin_numerator": quotient.numerator,
        "normalized_margin_denominator": quotient.denominator,
        "positive": margin > 0,
        "correlation_sha256": hashlib.sha256(
            (",".join(map(str, a))).encode("ascii")).hexdigest(),
        "scope_limit": "One profile at one n; no relaxation optimum claim.",
    }
    path = Path(__file__).with_name("weights_four_slack_step_result.json")
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
