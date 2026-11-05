"""Integer-only verifier for weights_multistart_result.json."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]


def cap_index(n: int, d: int) -> int:
    positions = n - d
    span = positions - 1
    candidates = [m for m, lower in enumerate(H) if lower <= span]
    return min(positions, candidates[-1])


def recompute(n: int, w: list[int]) -> tuple[int, int, int]:
    t = len(w)
    autocorrelations = []
    for d in range(t):
        value = 0
        for i in range(t - d):
            value += w[i] * w[i + d]
        autocorrelations.append(value)
    score = -n * autocorrelations[0]
    for d in range(1, t):
        coefficient = n - d - 18 * cap_index(n, d)
        score += coefficient * autocorrelations[d]
    return score, autocorrelations[0], min(autocorrelations)


def main() -> None:
    source = Path(__file__).with_name("weights_multistart_result.json")
    payload = json.loads(source.read_text(encoding="utf-8"))
    summaries = []
    prior_by_n: dict[int, Fraction] = {}
    total = 0
    for case in payload["cases"]:
        n, t = case["n"], case["t"]
        exact_values = []
        for candidate in case["candidates"]:
            total += 1
            w = candidate["integer_weights"]
            assert len(w) == t and min(w) >= 0 and max(w) > 0
            score, norm2, min_a = recompute(n, w)
            quotient = Fraction(score, norm2)
            assert score == candidate["exact_score"]
            assert norm2 == candidate["exact_norm2"]
            assert min_a == candidate["minimum_autocorrelation"]
            assert quotient.numerator == candidate["exact_quotient_numerator"]
            assert quotient.denominator == candidate["exact_quotient_denominator"]
            exact_values.append(quotient)
        best = max(exact_values)
        best_index = exact_values.index(best)
        assert best_index == case["best_candidate_index"]
        assert best.numerator == case["best_exact_quotient_numerator"]
        assert best.denominator == case["best_exact_quotient_denominator"]
        if n in prior_by_n:
            assert best >= prior_by_n[n]
        prior_by_n[n] = best
        summaries.append({
            "n": n,
            "t": t,
            "candidate_count": len(exact_values),
            "best_index": best_index,
            "best_score": case["best_exact_score"],
            "best_norm2": case["best_exact_norm2"],
            "best_quotient_numerator": best.numerator,
            "best_quotient_denominator": best.denominator,
            "best_sign": (best > 0) - (best < 0),
        })
    assert total == 166
    assert [s["best_sign"] for s in summaries] == [-1, -1, -1, -1, 1, 1, 1, 1]
    report = {
        "status": "PASS",
        "arithmetic": "integers and fractions.Fraction only",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "candidates_recomputed": total,
        "summaries": summaries,
        "nonclaim": "This verifies saved candidates, not global optimality.",
    }
    output = Path(__file__).with_name("verify_weights_multistart_result.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
