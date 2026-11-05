"""Generate the exact poly1 certificate for the W4-P2 candidate."""

import hashlib
import json
from pathlib import Path

from four_multi_certify import capacity, minsum
from weights_four_profiles import correlations, prefix_power_sums, selfcheck_formulas


N, T, CQ, C = 22_007_052, 36_000, 62, 662
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    selfcheck_formulas()
    sums = prefix_power_sums(T)
    a = correlations("poly1", T, sums)
    entries = []
    weighted_sum = 0
    for d in range(1, T):
        length = N - d - 1
        q = capacity(length, 1, CQ)
        k = capacity(length, 2 * q, C)
        coeff = N - d - 48 * k
        weighted_sum += coeff * a[d]
        entries.append((d, q, k))
    runs = []
    lo = 1
    q0, k0 = entries[0][1], entries[0][2]
    for index in range(1, len(entries) + 1):
        changed = (index == len(entries) or
                   entries[index][1] != q0 or entries[index][2] != k0)
        if changed:
            hi = entries[index - 1][0]
            longest_span = N - lo - 1
            hq = CQ * (q0 + 1) - CQ * (CQ + 1) // 2
            hk = C * (k0 + 1) - C * (C + 1) // 2
            runs.append({
                "lo": lo,
                "hi": hi,
                "q": q0,
                "K": k0,
                "longest_span": longest_span,
                "golomb_first_forbidden_lhs": 2 * minsum(hq, 1),
                "golomb_first_forbidden_rhs": longest_span * CQ * (CQ + 1),
                "capacity_first_forbidden_lhs": 2 * minsum(hk, 2 * q0),
                "capacity_first_forbidden_rhs": longest_span * C * (C + 1),
            })
            if index < len(entries):
                lo = entries[index][0]
                q0, k0 = entries[index][1], entries[index][2]
    margin = 2 * weighted_sum - 3 * N * a[0]
    assert margin == 10_738_351_366_697_728_567_324_267_584 and margin > 0
    result = {
        "statement": "R_4(L) <= 22007052",
        "honesty_label": "PROVED implication pending independent certificate verification",
        "corner": "(x,y),(x+d,y),(x+d,y+d), d>0",
        "n": N,
        "t": T,
        "profile": "w_i=i(36001-i), 1<=i<=36000",
        "golomb_neighbor_parameter": CQ,
        "capacity_neighbor_parameter": C,
        "runs": runs,
        "run_count": len(runs),
        "a0": a[0],
        "a1": a[1],
        "a_last": a[-1],
        "correlation_sha256": hashlib.sha256(
            (",".join(map(str, a))).encode("ascii")).hexdigest(),
        "weighted_sum": weighted_sum,
        "doubled_lhs": 2 * weighted_sum,
        "doubled_rhs": 3 * N * a[0],
        "doubled_margin": margin,
        "dependencies": ["FM1", "FM2-4", "FM3"],
        "lower_bound_implication": "none",
    }
    path = ROOT / "certificates" / "weights_four_candidate_22007052.json"
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "certificate_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "run_count": len(runs),
        "a0": a[0],
        "doubled_lhs": 2 * weighted_sum,
        "doubled_rhs": 3 * N * a[0],
        "doubled_margin": margin,
    }, indent=2))


if __name__ == "__main__":
    main()
