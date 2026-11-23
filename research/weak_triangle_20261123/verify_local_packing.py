"""Replay rounded intermediate floors by adding every incidence in physical coordinates."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import ceil

from verify_143 import DATA, read_json


@lru_cache(maxsize=None)
def weighted_corners(m, rule):
    if rule == "uniform":
        bound = None
    elif rule in ("single", "multiple") and 14 <= m <= 18:
        bound = 2*m + 2 if rule == "single" else 3*m
    elif rule == "boundary" and m in (17, 18):
        bound = m + 2
    elif m == 14 and rule in ("11", "12", "13"):
        s = int(rule)
        base, extra, bound = {11: (20, 3, 490), 12: (24, 5, 636), 13: (6, 5, 279)}[s]
        offsets = [(u + v, v) for u in range(m-s+1) for v in range(m-s+1-u)]
    else:
        raise ValueError(f"Uncertified order-{m} weight rule {rule}")
    corners = []
    for x in range(m-1):
        for y in range(x+1):
            for j in range(1, m-1-x):
                faces = (y == 0) + (x == y) + (x + j == m-2)
                if rule == "uniform":
                    weight = 1
                elif rule == "single":
                    weight = 2 + (faces == 1)
                elif rule == "multiple":
                    weight = 3 - max(0, faces-1)
                elif rule == "boundary":
                    weight = 1 + (faces > 0)
                else:
                    containing = sum(0 <= y-oy <= x-ox and x-ox+j <= s-2 for ox, oy in offsets)
                    weight = base + extra*containing
                corners.append((x, y, j, weight))
    return bound, corners


def expand(record, generic, with_clearance=None):
    n = record["n"]
    load = Counter()
    score = 0
    for column in record["columns"]:
        if len(column) == 6:
            m, step, a, b, c, coefficient = column
            rule = "uniform"
        else:
            m, step, a, b, c, rule, coefficient = column
        if min(a, b, c) < 0 or min(coefficient, step) <= 0 or a+b+c+(m-2)*step != n-2:
            raise ValueError("An intermediate copy does not fit its host")
        if m >= n or m not in generic:
            raise ValueError("The induction requires a smaller certified source")
        floor, corners = weighted_corners(m, rule)
        if floor is None:
            floor = with_clearance[m] if with_clearance and step == 1 else generic[m]
        for left, bottom, right in permutations((a, b, c)):
            ox, oy = left + bottom, bottom
            for x, y, j, weight in corners:
                xy = (ox + step*x, oy + step*y, step*j)
                if not 0 <= xy[1] <= xy[0] < xy[0]+xy[2] <= n-2:
                    raise ValueError("A charged physical corner escapes")
                load[xy] += coefficient*weight
            score += coefficient * floor
    value = Fraction(score, max(load.values()))
    if list(record["exact"]) != [value.numerator, value.denominator]:
        raise ValueError("Physical packing quotient disagrees with the certificate")
    return max(ceil(value), generic.get(n, 0))


def main():
    records = read_json(DATA / "local_packing_floors.json")
    generic = {10: 1, 11: 3, 12: 6, 13: 11, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18}
    for n, row in zip(range(19, 29), records["generic"], strict=True):
        if row["n"] != n or expand(row, generic) != row["floor"]:
            raise ValueError(f"Unverified unconditional floor for order {n}")
        generic[n] = row["floor"]
    clearance = {10: 1, 11: 3, 12: 10, 13: 13}
    for n, row in zip(range(14, 29), records["with_clearance"], strict=True):
        if row["n"] != n or expand(row, generic, clearance) != row["floor"]:
            raise ValueError(f"Unverified seven-step clearance floor for order {n}")
        clearance[n] = row["floor"]
    print("Order:", *range(19, 29))
    print("Generic:", *(generic[n] for n in range(19, 29)))
    print("With clearance:", *(clearance[n] for n in range(19, 29)))

    records = read_json(DATA / "local_boundary_packings.json")
    generic = {10: 1, 11: 3, 12: 6, 13: 11, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18}
    clearance = {10: 1, 11: 3, 12: 10, 13: 13}
    for field, destination in (("generic", generic), ("with_clearance", clearance)):
        for n, row in zip(range(14, 33), records[field], strict=True):
            external = clearance if field == "with_clearance" else None
            if row["n"] != n or expand(row, generic, external) != row["floor"]:
                raise ValueError(f"Incorrect {field} boundary-weighted floor at order {n}")
            destination[n] = row["floor"]
    print("Orders with boundary weights:", *range(19, 33))
    print("Generic:", *(generic[n] for n in range(19, 33)))
    print("With clearance:", *(clearance[n] for n in range(19, 33)))


if __name__ == "__main__":
    main()
