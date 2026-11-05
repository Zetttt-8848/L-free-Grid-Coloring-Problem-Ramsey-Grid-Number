"""Construct an exact finite PSD+nonnegative dual at n=464, t=68.

For the longer requested windows, preserve exact witnesses that the deliberately
restricted positive-part/scaled-diagonal-dominance ansatz cannot work.
"""

import hashlib
import json
from pathlib import Path

import numpy as np


H = [0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106,
     127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480,
     492, 553, 585]
SCALE = 10**12


def q_d(n: int, d: int) -> int:
    positions = n - d
    span = positions - 1
    q = max(m for m, lower in enumerate(H) if lower <= span)
    return min(positions, q)


def coefficient(n: int, d: int) -> int:
    return n - d - 18 * q_d(n, d)


def twice_positive_matrix(n: int, t: int) -> list[list[int]]:
    return [[0 if i == j else max(coefficient(n, abs(i - j)), 0)
             for j in range(t)] for i in range(t)]


def floating_perron(A2: list[list[int]]) -> np.ndarray:
    A = np.asarray(A2, dtype=float) / 2.0
    values, vectors = np.linalg.eigh(A)
    v = vectors[:, -1]
    if np.sum(v) < 0:
        v = -v
    # The positive-interaction graph is connected, so its Perron vector is
    # strictly positive; reject any numerical violation of this expectation.
    if np.min(v) <= 0:
        raise RuntimeError("nonpositive coordinate in Perron proposal")
    return v


def integerize(v: np.ndarray) -> list[int]:
    v = v / np.max(v)
    return [int(z) for z in np.rint(SCALE * v)]


def matvec(A2: list[list[int]], s: list[int]) -> list[int]:
    return [sum(a * x for a, x in zip(row, s)) for row in A2]


def certificate_t68() -> dict:
    n, t, delta = 464, 68, 1
    A2 = twice_positive_matrix(n, t)
    s = integerize(floating_perron(A2))
    product = matvec(A2, s)
    margins2 = [2 * (n - delta) * s[i] - product[i] for i in range(t)]
    assert min(s) > 0 and min(margins2) > 0
    return {
        "status": "PROVED",
        "n": n,
        "t": t,
        "delta": delta,
        "scaling_vector_s": s,
        "twice_row_margins": margins2,
        "minimum_twice_row_margin": min(margins2),
        "identity": (
            "-B-delta*I=P+N; P_ii=n-delta, "
            "2P_ij=-max(c_|i-j|,0); 2N_ij=max(-c_|i-j|,0)"
        ),
        "sos": (
            "P quadratic = sum_i margin2_i/(2*s_i)*x_i^2 + "
            "sum_{i<j} A2_ij/(2*s_i*s_j)*(s_j*x_i-s_i*x_j)^2"
        ),
        "conclusion": "For every w>=0 in R^68, w^T B w <= -sum_i w_i^2.",
    }


def restricted_failure(n: int, t: int) -> dict:
    A2 = twice_positive_matrix(n, t)
    v = integerize(floating_perron(A2))
    norm2 = sum(x * x for x in v)
    # Since A=A2/2 and A2 is symmetric with zero diagonal,
    # v^T A v = sum_{i<j} A2_ij v_i v_j.
    quadratic_A = sum(A2[i][j] * v[i] * v[j]
                      for i in range(t) for j in range(i + 1, t))
    gap = quadratic_A - n * norm2
    assert min(v) > 0 and gap > 0
    return {
        "status": "PROVED restricted-ansatz obstruction",
        "n": n,
        "t": t,
        "witness_v": v,
        "norm2": norm2,
        "vT_A_v": quadratic_A,
        "vT_(A-464I)_v": gap,
        "conclusion": (
            "P=464I-A is not PSD, so discarding all favorable negative "
            "coefficients cannot give the desired PSD+nonnegative decomposition."
        ),
        "nonclaim": "This does not refute a general SPN, SDP, SOS, or copositive certificate.",
    }


def main() -> None:
    result = {
        "coefficient_convention": "c_d=n-d-18*q_d",
        "q_convention": "inherited H_0..H_28; n-d start positions",
        "finite_dual": certificate_t68(),
        "restricted_failures": [restricted_failure(464, t)
                                for t in (93, 120, 150)],
        "construction_note": (
            "Floating eigensolvers propose integer vectors only. Every claimed "
            "inequality in this artifact is checked over the integers."
        ),
    }
    path = Path(__file__).with_name("weights_sdd_dual_certificate.json")
    text = json.dumps(result, indent=2) + "\n"
    path.write_text(text, encoding="utf-8")
    print(json.dumps({
        "certificate_file": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "t68_minimum_twice_row_margin": result["finite_dual"]["minimum_twice_row_margin"],
        "restricted_failure_gaps": {
            str(r["t"]): r["vT_(A-464I)_v"] for r in result["restricted_failures"]
        },
    }, indent=2))


if __name__ == "__main__":
    main()
