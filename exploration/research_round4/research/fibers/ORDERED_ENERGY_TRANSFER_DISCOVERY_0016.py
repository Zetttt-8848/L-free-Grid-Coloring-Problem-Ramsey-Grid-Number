"""Bounded discovery scan for the proposed ordered-energy transfer inequality.

For each deterministic source A, this computes T=sum_d binom(r_A(d),2),
M=binom(|A|,2), and Lambda=max U(B,C)/(|B||C|), with B,C obtained from
one contiguous source-index interval and one split.  It is a finite
conjecture-diagnosis scan only: no colorability, proof, or audit pass.
"""

from __future__ import annotations

import json
import random
import time
from fractions import Fraction
from math import comb
from pathlib import Path


OUT = Path(__file__).with_name("ORDERED_ENERGY_TRANSFER_DISCOVERY_0016.json")
LIMIT = 100


def diffs(A: list[int]) -> dict[int, int]:
    S = set(A)
    return {h: sum(a + h in S for a in A) for h in range(1, A[-1] - A[0] + 1) if any(a + h in S for a in A)}


def U(B: list[int], C: list[int]) -> int:
    rB, rC = diffs(B), diffs(C)
    return sum(rB.get(h, 0) * rC.get(h, 0) for h in set(rB) | set(rC))


def lambda_witness(A: list[int]):
    best = Fraction(-1, 1)
    witness = None
    m = len(A)
    # [i,j] is a contiguous source-index interval, split just before k.
    for i in range(m - 1):
        for j in range(i + 2, m + 1):
            for k in range(i + 1, j):
                B, C = A[i:k], A[k:j]
                u = U(B, C)
                value = Fraction(u, len(B) * len(C))
                if value > best:
                    best = value
                    witness = {"i": i, "k": k, "j": j, "B": B, "C": C,
                               "U": u, "bc": len(B) * len(C),
                               "lambda_numerator": value.numerator,
                               "lambda_denominator": value.denominator}
    return best, witness


def add(pool: list[tuple[str, list[int]]], name: str, A: list[int]) -> None:
    if len(A) >= 8 and len(A) <= 30 and A[-1] - A[0] <= 200 and A not in [x[1] for x in pool]:
        pool.append((name, A))


def sources():
    pool: list[tuple[str, list[int]]] = []
    for n in range(8, 31):
        add(pool, f"interval_{n}", list(range(n)))
    for n in range(8, 31):
        add(pool, f"even_{n}", [2 * x for x in range(n)])
        add(pool, f"square_prefix_{n}", [x * x for x in range(n)])
    for n in range(8, 21):
        half = n // 2
        symmetric = ([-(q * q + 1) for q in range(half, 0, -1)]
                     + ([0] if n % 2 else [])
                     + [q * q + 1 for q in range(1, half + 1)])
        add(pool, f"symmetric_squares_{n}", [x - symmetric[0] for x in symmetric])
        add(pool, f"two_blocks_{n}", list(range(n // 2)) + list(range(40, 40 + n - n // 2)))
    # Fixed-seed sparse sets, all sampled from [0,200] and normalized to 0.
    rng = random.Random(20260912)
    for n in range(8, 31):
        A = sorted(rng.sample(range(201), n))
        add(pool, f"fixedseed_{n}", [x - A[0] for x in A])
    return pool[:LIMIT]


def main() -> None:
    started = time.monotonic()
    examined = []
    counterexample = None
    for name, A in sources():
        T = sum(comb(r, 2) for r in diffs(A).values())
        M = comb(len(A), 2)
        lam, witness = lambda_witness(A)
        # Exact comparison T > (1+2 Lambda) M, retained without simplification.
        rhs = (Fraction(1, 1) + 2 * lam) * M
        record = {
            "name": name, "A": A, "size": len(A), "span": A[-1] - A[0],
            "T": T, "M": M, "lambda_numerator": lam.numerator,
            "lambda_denominator": lam.denominator, "lambda_decimal": float(lam),
            "lambda_witness": witness,
            "rhs_numerator": rhs.numerator, "rhs_denominator": rhs.denominator,
            "strict_transfer_counterexample": T > rhs,
        }
        examined.append(record)
        if T > rhs:
            counterexample = record
            break
    result = {
        "purpose": "bounded ordered-energy transfer discovery; one full contiguous-cut enumeration per saved source",
        "conjecture_tested": "T <= (1+2 Lambda) M",
        "definitions": {"T": "sum_{d>0} binom(r_A(d),2)", "M": "binom(|A|,2)", "Lambda": "max U(B,C)/(|B||C|) over contiguous source-index subinterval splits"},
        "source_cap": LIMIT, "examined_count": len(examined), "seconds": time.monotonic() - started,
        "examined": examined, "counterexample_candidate": counterexample,
        "scope": "Bounded discovery only. An absent counterexample in this list proves no universal transfer statement.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"examined_count": len(examined), "counterexample_candidate": counterexample}))


if __name__ == "__main__":
    main()
