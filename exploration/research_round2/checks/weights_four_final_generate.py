"""Generate the exact final polynomial-weight certificate at n=22,006,246."""

import hashlib
import json
from pathlib import Path

from four_multi_certify import capacity, minsum
from weights_four_profiles import correlations, prefix_power_sums, selfcheck_formulas


N, T, CQ, C = 22_006_246, 36_000, 62, 662
ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    selfcheck_formulas()
    a = correlations("poly1", T, prefix_power_sums(T))
    triples = []
    weighted_sum = 0
    for d in range(1, T):
        span = N - d - 1
        q = capacity(span, 1, CQ)
        k = capacity(span, 2 * q, C)
        triples.append((d, q, k))
        weighted_sum += (N - d - 48 * k) * a[d]

    runs = []
    start = 0
    while start < len(triples):
        d0, q0, k0 = triples[start]
        stop = start + 1
        while stop < len(triples) and triples[stop][1:] == (q0, k0):
            stop += 1
        hi = triples[stop - 1][0]
        longest = N - d0 - 1
        hq = CQ * (q0 + 1) - CQ * (CQ + 1) // 2
        hk = C * (k0 + 1) - C * (C + 1) // 2
        runs.append({
            "lo": d0,
            "hi": hi,
            "q": q0,
            "K": k0,
            "longest_span": longest,
            "golomb_first_forbidden_lhs": 2 * minsum(hq, 1),
            "golomb_first_forbidden_rhs": longest * CQ * (CQ + 1),
            "capacity_first_forbidden_lhs": 2 * minsum(hk, 2 * q0),
            "capacity_first_forbidden_rhs": longest * C * (C + 1),
        })
        start = stop

    lhs = 2 * weighted_sum
    rhs = 3 * N * a[0]
    margin = lhs - rhs
    assert margin == 6_847_214_254_640_526_658_129_728 and margin > 0
    result = {
        "statement": "R_4(L) <= 22006246",
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
        "doubled_lhs": lhs,
        "doubled_rhs": rhs,
        "doubled_margin": margin,
        "dependencies": ["FM1", "FM2-4", "FM3"],
        "lower_bound_implication": "none",
        "claim_boundary": (
            "Explicit certificate only; no minimality over n,t,weights,or capacity parameters."
        ),
    }
    path = ROOT / "certificates" / "weights_four_22006246.json"
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "certificate_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "run_count": len(runs),
        "a0": a[0],
        "doubled_lhs": lhs,
        "doubled_rhs": rhs,
        "doubled_margin": margin,
    }, indent=2))


if __name__ == "__main__":
    main()
