"""Independent exact verifier for weights_four_22006246.json."""

import hashlib
import json
from pathlib import Path

# This NTT/CRT implementation is independent of every profile generator.
from verify_weights_four_candidate import exact_autocorrelations, minsum


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "certificates" / "weights_four_22006246.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    n, t = data["n"], data["t"]
    cq = data["golomb_neighbor_parameter"]
    c = data["capacity_neighbor_parameter"]
    assert (n, t, cq, c) == (22_006_246, 36_000, 62, 662)

    a = exact_autocorrelations(t)
    assert len(a) == t and min(a) > 0
    assert (a[0], a[1], a[-1]) == (data["a0"], data["a1"], data["a_last"])
    digest = hashlib.sha256((",".join(map(str, a))).encode("ascii")).hexdigest()
    assert digest == data["correlation_sha256"]

    expected = 1
    weighted = 0
    distance_count = 0
    for run in data["runs"]:
        lo, hi, q, k = run["lo"], run["hi"], run["q"], run["K"]
        assert lo == expected and lo <= hi < t
        expected = hi + 1
        distance_count += hi - lo + 1
        span = n - lo - 1
        assert span == run["longest_span"]

        hq = cq * (q + 1) - cq * (cq + 1) // 2
        qlhs, qrhs = 2 * minsum(hq, 1), span * cq * (cq + 1)
        assert qlhs == run["golomb_first_forbidden_lhs"]
        assert qrhs == run["golomb_first_forbidden_rhs"] and qlhs > qrhs

        hk = c * (k + 1) - c * (c + 1) // 2
        klhs, krhs = 2 * minsum(hk, 2 * q), span * c * (c + 1)
        assert klhs == run["capacity_first_forbidden_lhs"]
        assert krhs == run["capacity_first_forbidden_rhs"] and klhs > krhs

        for d in range(lo, hi + 1):
            weighted += (n - d - 48 * k) * a[d]

    assert expected == t and distance_count == t - 1
    assert len(data["runs"]) == data["run_count"] == 380
    lhs, rhs = 2 * weighted, 3 * n * a[0]
    margin = lhs - rhs
    assert weighted == data["weighted_sum"]
    assert lhs == data["doubled_lhs"] == 133_088_683_635_976_942_314_364_072_128
    assert rhs == data["doubled_rhs"] == 133_081_836_421_722_301_787_705_942_400
    assert margin == data["doubled_margin"] == 6_847_214_254_640_526_658_129_728
    assert margin > 0

    report = {
        "status": "PASS",
        "arithmetic": "three-prime integer NTT, exact CRT, and Python integers",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "n": n,
        "t": t,
        "profile": data["profile"],
        "correlations_checked": len(a),
        "capacity_runs_checked": len(data["runs"]),
        "distances_checked": distance_count,
        "a0": a[0],
        "doubled_lhs": lhs,
        "doubled_rhs": rhs,
        "doubled_margin": margin,
        "proved_implication": "FM1+FM2-4+FM3 imply R_4(L)<=22006246.",
        "lower_bound_implication": "none",
        "claim_boundary": "No optimality or exact-value claim.",
    }
    output = Path(__file__).with_name("weights_four_final_verified.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
