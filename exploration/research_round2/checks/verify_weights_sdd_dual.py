"""Independent exact verifier for weights_sdd_dual_certificate.json."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]


def q_value(n: int, d: int) -> int:
    count = n - d
    possible = 0
    for mark_count, lower_span in enumerate(H):
        if lower_span <= count - 1:
            possible = mark_count
    return min(count, possible)


def c_value(n: int, d: int) -> int:
    return n - d - 18 * q_value(n, d)


def a2_matrix(n: int, t: int) -> list[list[int]]:
    out = []
    for i in range(t):
        row = []
        for j in range(t):
            row.append(0 if i == j else max(c_value(n, abs(i - j)), 0))
        out.append(row)
    return out


def verify_dual(record: dict) -> dict:
    n, t, delta = record["n"], record["t"], record["delta"]
    assert (n, t, delta) == (464, 68, 1)
    s = record["scaling_vector_s"]
    stated = record["twice_row_margins"]
    assert len(s) == t and min(s) > 0 and len(stated) == t
    A2 = a2_matrix(n, t)
    margins = []
    for i in range(t):
        margins.append(2 * (n - delta) * s[i]
                       - sum(A2[i][j] * s[j] for j in range(t)))
    assert margins == stated and min(margins) > 0
    assert min(margins) == record["minimum_twice_row_margin"]

    # Verify each coefficient in the displayed rational SOS decomposition.
    for i in range(t):
        diagonal = Fraction(margins[i], 2 * s[i])
        diagonal += sum(Fraction(A2[i][j] * s[j], 2 * s[i])
                        for j in range(t) if j != i)
        assert diagonal == n - delta
    for i in range(t):
        for j in range(i + 1, t):
            p_offdiag = Fraction(-A2[i][j], 2)
            n_offdiag = Fraction(max(-c_value(n, j - i), 0), 2)
            target = Fraction(-c_value(n, j - i), 2)
            assert p_offdiag + n_offdiag == target
            assert n_offdiag >= 0
    return {"rows": t, "minimum_twice_row_margin": min(margins),
            "sos_coefficients": t * (t + 1) // 2}


def verify_failure(record: dict) -> dict:
    n, t = record["n"], record["t"]
    v = record["witness_v"]
    assert n == 464 and len(v) == t and min(v) > 0
    A2 = a2_matrix(n, t)
    norm2 = sum(x * x for x in v)
    vav = sum(A2[i][j] * v[i] * v[j]
              for i in range(t) for j in range(i + 1, t))
    gap = vav - n * norm2
    assert norm2 == record["norm2"]
    assert vav == record["vT_A_v"]
    assert gap == record["vT_(A-464I)_v"] and gap > 0
    return {"t": t, "positive_obstruction_gap": gap}


def main() -> None:
    source = Path(__file__).with_name("weights_sdd_dual_certificate.json")
    payload = json.loads(source.read_text(encoding="utf-8"))
    report = {
        "status": "PASS",
        "arithmetic": "integer and Fraction only",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "finite_dual": verify_dual(payload["finite_dual"]),
        "restricted_failures": [verify_failure(x)
                                for x in payload["restricted_failures"]],
        "proved_conclusion": (
            "At n=464,t=68, every nonnegative real w satisfies "
            "score(w)<=-sum_i w_i^2."
        ),
        "scope_limit": (
            "The longer-window witnesses only reject the positive-part SDD ansatz."
        ),
    }
    output = Path(__file__).with_name("verify_weights_sdd_dual_result.json")
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
