"""Exact Route-1 polynomial-weight scan.

The output contains raw integer scores for the prescribed representatives and
the scale-invariant rational quotient score/a0.  The Golomb table entries H_m
are inherited lower bounds for the minimum span of an m-mark ruler.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [
    0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106, 127,
    151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480, 492,
    553, 585,
]


def q_from_span(span: int) -> int:
    """Largest tabulated mark count not excluded at the given span."""
    if not 0 <= span < H[-1]:
        raise ValueError(f"span {span} outside inherited table range")
    return max(m for m, lower in enumerate(H) if lower <= span)


def q_d(n: int, d: int) -> int:
    # There are n-d possible start positions.  The forced-color fiber lies in
    # those positions and has span at most n-d-1.
    positions = n - d
    return min(positions, q_from_span(positions - 1))


def exact_record(n: int, p: int) -> dict:
    weights = [(i * (94 - i)) ** p for i in range(1, 94)]
    autocorrelations = [
        sum(weights[i] * weights[i + d] for i in range(93 - d))
        for d in range(93)
    ]
    terms = [
        (n - d - 18 * q_d(n, d)) * autocorrelations[d]
        for d in range(1, 93)
    ]
    score = sum(terms) - n * autocorrelations[0]
    quotient = Fraction(score, autocorrelations[0])
    return {
        "n": n,
        "t": 93,
        "p": p,
        "weight_formula": "w_i=(i(94-i))^p, 1<=i<=93",
        "a0": autocorrelations[0],
        "score": score,
        "normalized_score": {
            "numerator": quotient.numerator,
            "denominator": quotient.denominator,
        },
        "minimum_weight": min(weights),
        "maximum_weight": max(weights),
        "q_ranges": _q_ranges(n, 92),
    }


def _q_ranges(n: int, max_d: int) -> list[dict]:
    values = [q_d(n, d) for d in range(1, max_d + 1)]
    ranges = []
    start = 1
    for d in range(2, max_d + 2):
        if d == max_d + 1 or values[d - 1] != values[start - 1]:
            ranges.append({"d_first": start, "d_last": d - 1,
                           "q_d": values[start - 1]})
            start = d
    return ranges


def main() -> None:
    records = [exact_record(n, p) for n in (464, 465) for p in range(5)]
    tent = [min(i, 94 - i) for i in range(1, 94)]
    a = [sum(tent[i] * tent[i + d] for i in range(93 - d))
         for d in range(93)]
    tent_score = sum((465 - d - 18 * q_d(465, d)) * a[d]
                     for d in range(1, 93)) - 465 * a[0]
    assert a[0] == 69231 and tent_score == 285630
    assert q_d(465, 39) == 24 and q_d(465, 40) == 23
    assert q_d(464, 38) == 24 and q_d(464, 39) == 23
    assert q_d(464, 91) == 23 and q_d(464, 92) == 22
    output = {
        "honesty_label": "PROVED finite exact arithmetic",
        "nonclaim": "This finite family does not bound the global relaxation optimum.",
        "scale_erratum": (
            "Raw scores depend quadratically on arbitrary scaling; only score/a0 "
            "is comparable across profiles."
        ),
        "inherited_H_0_through_28": H,
        "tent_benchmark_465": {"a0": a[0], "score": tent_score,
                                "quotient_numerator": Fraction(tent_score, a[0]).numerator,
                                "quotient_denominator": Fraction(tent_score, a[0]).denominator},
        "records": records,
    }
    path = Path(__file__).with_name("weights_polynomial_result.json")
    text = json.dumps(output, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(text, end="")
    print("sha256", hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
