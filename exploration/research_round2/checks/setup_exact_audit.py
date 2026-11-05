#!/usr/bin/env python3
"""R2-S0: deterministic integer audit of inherited numerical specifications."""
from fractions import Fraction
from math import comb
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tent_audit():
    h = 47
    w = [min(i, 2 * h - i) for i in range(1, 2 * h)]
    a = [sum(w[i] * w[i + d] for i in range(len(w) - d)) for d in range(len(w))]
    a0 = a[0]
    p = sum(a[1:40])
    q = sum(a[40:93])
    dmass = sum(d * a[d] for d in range(1, 93))
    score = sum((465 - d - 18 * (24 if d <= 39 else 23)) * a[d]
                for d in range(1, 93)) - 465 * a0
    assert (a0, p, q, dmass, score) == (69231, 2038439, 366786, 53496528, 285630)
    assert sum(w) == 2209
    assert p + q == (2209**2 - a0) // 2
    assert score == 33 * p + 51 * q - dmass - 465 * a0
    return {"a0": a0, "P": p, "Q": q, "D": dmass, "score": score,
            "score_over_a0": str(Fraction(score, a0))}


def reviewer_a8_audit():
    h = 47
    w = [min(i, 2 * h - i) for i in range(1, 2 * h)]
    a = [sum(w[i] * w[i + d] for i in range(len(w) - d)) for d in range(len(w))]

    def cap(n, d):
        if n - 1 - d >= 425:
            return 24
        if n - 1 - d >= 372:
            return 23
        return 22

    def score(n):
        return sum((n - d - 18 * cap(n, d)) * a[d] for d in range(1, 93)) - n * a[0]

    observed = {n: score(n) for n in range(462, 468)}
    expected = {462: -5167602, 463: -3375316, 464: -1557434,
                465: 285630, 466: 2153426, 467: 4045468}
    assert observed == expected
    mass_term = -(sum(a[1:]) - a[0])
    recovery = 18 * (a[39] + a[92])
    assert (a[39], a[92], mass_term, recovery) == (27384, 1, -2335994, 492930)
    assert observed[464] - observed[465] == mass_term + recovery == -1843064

    coefficient = {d: 465 - d - 18 * cap(465, d) for d in range(1, 93)}
    positive = sum(coefficient[d] * a[d] for d in coefficient if coefficient[d] > 0)
    negative = sum(coefficient[d] * a[d] for d in coefficient if coefficient[d] < 0)
    zeros = [d for d in coefficient if coefficient[d] == 0]
    negative_distances = [d for d in coefficient if coefficient[d] < 0]
    assert (positive, negative, 465 * a[0]) == (34324365, -1846320, 32192415)
    assert zeros == [33, 51]
    assert negative_distances == list(range(34, 40)) + list(range(52, 93))
    assert positive + negative - 465 * a[0] == observed[465]
    return {"scores": observed, "a39": a[39], "a92": a[92],
            "465_to_464": {"mass_term": mass_term, "cap_recovery": recovery,
                            "total": observed[464] - observed[465]},
            "sign_map": {"zeros": zeros, "negative_distances": "34..39, 52..92",
                         "positive_contribution": positive,
                         "negative_contribution": negative,
                         "n_a0": 465 * a[0]}}


def four_color_audit():
    n = 91**4
    s = (n + 3) // 4
    lhs = s * (s - 1)
    rhs_numerator = 28 * 91**7 + 20 * 91**6 + 30 * 91**5 + 18 * 91**4
    # rhs_numerator/5 is the inherited upper expression for 6 sum H_3.
    margin_numerator = 5 * lhs - rhs_numerator
    assert n == 68574961
    assert s == 17143741
    assert lhs == 293907838331340
    assert rhs_numerator == 1458476683234116
    assert margin_numerator == 11062508422584
    assert 5 * (comb(s, 2) - Fraction(rhs_numerator, 10)) == margin_numerator // 2
    return {"N": n, "s": s, "twice_binomial_lhs": lhs,
            "six_sum_H3_upper_numerator_over_5": rhs_numerator,
            "five_times_lhs_minus_rhs": margin_numerator,
            "correct_binomial_factor": 3}


def homogeneity_audit():
    # a_0(lambda w)=lambda^2 a_0(w), S(lambda w)=lambda^2 S(w).
    # The accepted tent supplies an explicit positive S at n=465.
    a0, score = 69231, 285630
    assert score > 0 and a0 > 0
    assert Fraction(4 * score, 4 * a0) == Fraction(score, a0)
    return {"normalization": "a0(w)=1 (equivalently score/a0 for nonzero w)",
            "tent_quotient": str(Fraction(score, a0)),
            "unrestricted_maximum_at_465": "unbounded_above"}


def main():
    result = {
        "status": "PROVED: finite arithmetic identities only",
        "arithmetic": "Python unbounded integers and fractions.Fraction",
        "tent": tent_audit(),
        "reviewer_A8": reviewer_a8_audit(),
        "four_color": four_color_audit(),
        "route1": homogeneity_audit(),
    }
    output = ROOT / "checks" / "setup_exact_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
