#!/usr/bin/env python3
"""Small known-positive and known-negative tests for the independent audits."""

from itertools import combinations

from audit_joint import cnf_for, unit_conflict, verify_rup
from audit_four import correlation, direct_correlation, golomb_tau


def endpoint_direct(marks, c):
    s = len(marks)
    return sum(marks[i + j] - marks[i]
               for j in range(1, c + 1) for i in range(s - j))


def endpoint_cancelled(marks, c):
    s = len(marks)
    return sum((c - i) * (marks[s - 1 - i] - marks[i]) for i in range(c))


def main():
    # One literal unit makes the empty clause RUP; an unrelated unit is not RUP.
    assert unit_conflict([[1]], [-1])
    assert verify_rup([[1], [-1]], [[]]) == (True, None)
    assert verify_rup([[1]], [[2]]) == (False, 1)

    cells, clauses = cnf_for([0, 1, 2])
    assert cells == [(1, 0), (2, 0), (2, 1)]
    assert clauses == [[1, 2, 3], [-1, -2, -3], [1]]

    for t in range(2, 12):
        for d in range(t):
            assert correlation(t, d) == direct_correlation(t, d)

    # Exhaust small distinct integer mark sets.  This tests the 1-based endpoint
    # indexing, the cancellation identity, and the overlap-safe correction.
    for s in range(2, 8):
        for marks in combinations(range(9), s):
            L = marks[-1] - marks[0]
            for c in range(1, s):
                direct = endpoint_direct(marks, c)
                cancelled = endpoint_cancelled(marks, c)
                bound = L * c * (c + 1) // 2 - 2 * __import__("math").comb(c + 1, 3)
                assert direct == cancelled <= bound

    # Independently brute the -1 rounding in Tau on small target sizes.
    for s in range(2, 24):
        formula, _ = golomb_tau(s)
        brute = -1
        for c in range(1, s):
            H = c * s - c * (c + 1) // 2
            for L in range(formula + 2):
                if H * (H + 1) > L * c * (c + 1) - 4 * __import__("math").comb(c + 1, 3):
                    brute = max(brute, L)
        assert formula == brute

    print("SELFTEST PASS")


if __name__ == "__main__":
    main()
