#!/usr/bin/env python3
"""Regression checks for the new Route-5 generators and verifiers."""

from __future__ import annotations

import itertools

from build_instance import expected_clauses, var
from check_rup_proofs import rup


def main() -> int:
    assert var(21, 0, 0, 0) == 1
    assert var(21, 0, 1, 0) == 4
    assert var(21, 1, 0, 0) == 64
    assert var(21, 20, 20, 2) == 1323
    for n in (1, 2, 5, 21):
        clauses, counts = expected_clauses(n)
        triples = sum(m * m for m in range(1, n))
        assert counts["geometric_triples"] == triples
        assert counts["variables"] == 3 * n * n
        assert counts["clauses_before_symmetry"] == 4 * n * n + 3 * triples
        assert counts["total_clauses"] == 5 * n * n + 3 * triples
        assert len(clauses) == counts["total_clauses"]
    assert len(set(itertools.product(range(3), repeat=4))) == 81
    _, side21 = expected_clauses(21)
    assert side21 == {
        "variables": 1323,
        "geometric_triples": 2870,
        "cell_clauses": 1764,
        "forbidden_color_clauses": 8610,
        "symmetry_clauses": 441,
        "clauses_before_symmetry": 10374,
        "total_clauses": 10815,
    }
    assert rup([(1,), (-1,)], ())
    xor_block = [(1, 2), (-1, 2), (1, -2), (-1, -2)]
    assert not rup(xor_block, ())
    assert rup(xor_block, (2,))
    assert rup(xor_block, (-2,))
    assert not rup([], (1,))
    print("ROUTE5 SELF-TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
