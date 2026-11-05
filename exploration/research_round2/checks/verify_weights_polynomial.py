"""Independent integer-only verifier for weights_polynomial_result.json."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]


def q(n: int, d: int) -> int:
    positions = n - d
    mark_count = 0
    for candidate, lower_span in enumerate(H):
        if lower_span <= positions - 1:
            mark_count = candidate
    return min(positions, mark_count)


def evaluate(n: int, p: int) -> tuple[int, int, Fraction]:
    w = [(i * (94 - i)) ** p for i in range(1, 94)]
    a = []
    for d in range(93):
        a.append(sum(w[i] * w[i + d] for i in range(93 - d)))
    value = -n * a[0]
    for d in range(1, 93):
        value += (n - d - 18 * q(n, d)) * a[d]
    return value, a[0], Fraction(value, a[0])


def main() -> None:
    source = Path(__file__).with_name("weights_polynomial_result.json")
    payload = json.loads(source.read_text(encoding="utf-8"))
    records = {(r["n"], r["p"]): r for r in payload["records"]}
    assert len(records) == 10
    summaries = []
    for n in (464, 465):
        quotients = []
        for p in range(5):
            value, norm2, quotient = evaluate(n, p)
            record = records[n, p]
            assert value == record["score"]
            assert norm2 == record["a0"]
            assert quotient.numerator == record["normalized_score"]["numerator"]
            assert quotient.denominator == record["normalized_score"]["denominator"]
            quotients.append(quotient)
        assert max(range(5), key=lambda p: quotients[p]) == 2
        summaries.append({
            "n": n,
            "best_p": 2,
            "best_score": records[n, 2]["score"],
            "best_a0": records[n, 2]["a0"],
            "best_quotient_numerator": quotients[2].numerator,
            "best_quotient_denominator": quotients[2].denominator,
            "best_sign": (quotients[2] > 0) - (quotients[2] < 0),
        })
    assert [s["best_sign"] for s in summaries] == [-1, 1]
    assert q(465, 39) == 24 and q(465, 40) == 23
    assert q(464, 38) == 24 and q(464, 39) == 23
    assert q(464, 91) == 23 and q(464, 92) == 22
    report = {
        "status": "PASS",
        "arithmetic": "integers and fractions.Fraction only",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "records_recomputed": 10,
        "summaries": summaries,
        "nonclaim": "The five-profile grid is not a global optimization.",
    }
    output = Path(__file__).with_name("verify_weights_polynomial_result.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
