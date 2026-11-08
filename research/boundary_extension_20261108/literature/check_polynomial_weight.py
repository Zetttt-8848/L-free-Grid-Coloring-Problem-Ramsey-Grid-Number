"""Exact diagnostics of two different polynomial-step probability measures.

This does not test the density theorem of arXiv:2606.08890v1. See WEIGHT_AUDIT.md.
Only Python's standard library is used. Output contains exact rational numbers.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def case(p, degree):
    require(p > degree * degree, "Source size hypothesis failed")
    require(all(p % k for k in range(2, int(p ** 0.5) + 1)), "p is not prime")
    multiplicity = Counter(pow(z, degree, p) for z in range(p))
    image = set(multiplicity)
    w = [Fraction(p, len(image)) if t in image else Fraction(0) for t in range(p)]
    require(sum(w) == p, "Image weight normalization")
    # The three singleton test functions force x=y=0 and step=1.
    # Direct enumeration over the *parameter* z, with no reweighting.
    parameter_count = sum(1 for z in range(p) if pow(z, degree, p) == 1)
    parameter_average = Fraction(parameter_count, p ** 3)
    image_average = w[1] / p ** 3
    pushforward_average = Fraction(multiplicity[1], p ** 3)
    require(parameter_average == pushforward_average, "Pushforward identity failed")
    require(parameter_average != image_average, "Expected mismatch absent")

    # A separate exact test of the displayed Fourier equality in Prop. 4.1.
    # f=w-1; r=1; X stands for exp(2*pi*i/p). Coefficients are rational.
    lhs = [Fraction(0) for _ in range(p)]
    rhs = [Fraction(0) for _ in range(p)]
    for t in range(p):
        lhs[(-t) % p] += (w[t] - 1) / p
    for z in range(p):
        rhs[(-pow(z, degree, p)) % p] += Fraction(1, len(image))
    difference = [a-b for a,b in zip(lhs,rhs)]
    # Phi_p(X)=1+X+...+X^(p-1), so a polynomial of degree <=p-1
    # vanishes at a primitive p-th root iff all coefficients are equal.
    remainder = [difference[i] - difference[-1] for i in range(p-1)]
    require(any(remainder), "Expected Fourier mismatch absent")
    return {
        "prime": p, "polynomial": f"z^{degree}", "degree": degree,
        "image_size": len(image), "preimages_of_1": parameter_count,
        "parameter_average": str(parameter_average),
        "uniform_image_average": str(image_average),
        "multiplicity_average": str(pushforward_average),
        "parameter_minus_image": str(parameter_average-image_average),
        "fourier_difference_mod_cyclotomic":
            {str(i): str(v) for i,v in enumerate(remainder) if v},
        "verdict": "COUNTEREXAMPLE_TO_WEIGHT_SUBSTITUTION_AND_DISPLAYED_FOURIER_EQUALITY",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = {
        "source": "https://arxiv.org/html/2606.08890v1#S4",
        "assertion_tested": "Uniform-image and parameter-pushforward weights differ; the indicated Fourier equality fails.",
        "cases": [case(5, 2), case(101, 2), case(103, 3)],
        "non_claims": ["No refutation of the main density theorem", "No refutation of the stated norm inequality", "No change to the L-grid Ramsey bounds"],
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cases": len(report["cases"]), "status": "exact mismatches confirmed"}))


if __name__ == "__main__":
    main()
