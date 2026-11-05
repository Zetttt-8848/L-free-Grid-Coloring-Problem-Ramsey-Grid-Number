"""Exact scan of a genuinely signed weight family with a_d >= 0."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]
T = 93
D = 64


def q_d(n: int, d: int) -> int:
    positions = n - d
    span = positions - 1
    q = max(m for m, lower in enumerate(H) if lower <= span)
    return min(positions, q)


def correlations(defect: int, k: int) -> list[int]:
    # All entries are D except w_defect=-k.  For d>0, ``touches`` counts
    # ordered-by-position pairs at lag d incident with the defect.
    values = [(T - 1) * D * D + k * k]
    for d in range(1, T):
        touches = int(defect - d >= 0) + int(defect + d < T)
        ordinary = (T - d) - touches
        values.append(ordinary * D * D - touches * k * D)
    return values


def score(n: int, a: list[int]) -> int:
    return sum((n - d - 18 * q_d(n, d)) * a[d]
               for d in range(1, T)) - n * a[0]


def all_ones(n: int) -> Fraction:
    a = [T - d for d in range(T)]
    return Fraction(score(n, a), a[0])


def max_feasible_k(defect: int) -> int:
    bounds = []
    for d in range(1, T):
        touches = int(defect - d >= 0) + int(defect + d < T)
        if touches:
            ordinary = (T - d) - touches
            bounds.append((ordinary * D) // touches)
    return min(bounds)


def main() -> None:
    records = []
    feasible_count = 0
    best = {464: None, 465: None}
    for defect in range(1, T - 1):
        limit = max_feasible_k(defect)
        for k in range(1, limit + 1):
            a = correlations(defect, k)
            assert min(a) >= 0
            feasible_count += 1
            for n in (464, 465):
                value = score(n, a)
                quotient = Fraction(value, a[0])
                key = (quotient, -defect, -k)
                if best[n] is None or key > best[n][0]:
                    best[n] = (key, {
                        "n": n,
                        "t": T,
                        "positive_background": D,
                        "defect_index_zero_based": defect,
                        "negative_defect_weight": -k,
                        "weights": [(-k if i == defect else D) for i in range(T)],
                        "autocorrelations": a,
                        "minimum_autocorrelation": min(a),
                        "a0": a[0],
                        "score": value,
                        "quotient_numerator": quotient.numerator,
                        "quotient_denominator": quotient.denominator,
                    })
    for n in (464, 465):
        record = best[n][1]
        baseline = all_ones(n)
        record["all_ones_quotient_numerator"] = baseline.numerator
        record["all_ones_quotient_denominator"] = baseline.denominator
        record["strictly_improves_all_ones"] = (
            Fraction(record["quotient_numerator"], record["quotient_denominator"])
            > baseline
        )
        records.append(record)
    output = {
        "honesty_label": "PROVED exact finite-family scan",
        "family": "t=93; w_i=64 except one interior w_j=-k; all exact-feasible k>=1",
        "feasible_signed_profiles_scanned": feasible_count,
        "records": records,
        "nonclaim": "This finite one-defect family does not optimize the full signed cone.",
    }
    path = Path(__file__).with_name("weights_signed_scan_result.json")
    text = json.dumps(output, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "result_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "feasible_signed_profiles_scanned": feasible_count,
        "best": [{k: r[k] for k in (
            "n", "defect_index_zero_based", "negative_defect_weight",
            "minimum_autocorrelation", "a0", "score", "quotient_numerator",
            "quotient_denominator", "strictly_improves_all_ones")}
                 for r in records],
    }, indent=2))


if __name__ == "__main__":
    main()
