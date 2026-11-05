"""Independent integer verification of the exact signed one-defect scan."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]
T, BACKGROUND = 93, 64


def q(n: int, d: int) -> int:
    positions = n - d
    allowed = [idx for idx, lower in enumerate(H) if lower <= positions - 1]
    return min(positions, allowed[-1])


def direct_autocorrelation(w: list[int]) -> list[int]:
    return [sum(x * y for x, y in zip(w, w[d:])) for d in range(len(w))]


def objective(n: int, a: list[int]) -> int:
    value = -n * a[0]
    for d in range(1, len(a)):
        value += (n - d - 18 * q(n, d)) * a[d]
    return value


def main() -> None:
    source = Path(__file__).with_name("weights_signed_scan_result.json")
    claimed = json.loads(source.read_text(encoding="utf-8"))
    claimed_by_n = {r["n"]: r for r in claimed["records"]}

    count = 0
    best: dict[int, tuple[Fraction, int, int]] = {}
    for defect in range(1, T - 1):
        # Derive the exact feasible interval independently by checking every
        # integer k until the first failure.  Feasibility is monotone here
        # because each positive-lag correlation is affine decreasing in k.
        k = 1
        while True:
            w = [BACKGROUND] * T
            w[defect] = -k
            a = direct_autocorrelation(w)
            if min(a) < 0:
                break
            count += 1
            for n in (464, 465):
                value = Fraction(objective(n, a), a[0])
                key = (value, -defect, -k)
                if n not in best or key > (best[n][0], -best[n][1], -best[n][2]):
                    best[n] = (value, defect, k)
            k += 1

    assert count == claimed["feasible_signed_profiles_scanned"] == 111840
    summaries = []
    for n in (464, 465):
        value, defect, k = best[n]
        record = claimed_by_n[n]
        assert defect == record["defect_index_zero_based"]
        assert -k == record["negative_defect_weight"]
        assert value.numerator == record["quotient_numerator"]
        assert value.denominator == record["quotient_denominator"]
        w = record["weights"]
        a = direct_autocorrelation(w)
        assert a == record["autocorrelations"]
        assert min(a) == record["minimum_autocorrelation"] >= 0
        assert objective(n, a) == record["score"] < 0
        baseline = Fraction(record["all_ones_quotient_numerator"],
                            record["all_ones_quotient_denominator"])
        assert value > baseline and record["strictly_improves_all_ones"]
        summaries.append({
            "n": n,
            "defect_index_zero_based": defect,
            "negative_defect_weight": -k,
            "score": record["score"],
            "a0": a[0],
            "minimum_autocorrelation": min(a),
            "quotient_numerator": value.numerator,
            "quotient_denominator": value.denominator,
        })
    report = {
        "status": "PASS",
        "arithmetic": "integer convolution and fractions.Fraction only",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "feasible_profiles_reenumerated": count,
        "summaries": summaries,
        "scope_limit": "Finite one-defect family only.",
    }
    output = Path(__file__).with_name("verify_weights_signed_scan_result.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
