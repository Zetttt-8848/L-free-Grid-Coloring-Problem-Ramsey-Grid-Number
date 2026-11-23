"""Replay rounded intermediate floors by adding every incidence in physical coordinates."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import ceil

from verify_143 import DATA, read_json


def expand(record, generic, with_clearance=None):
    n = record["n"]
    load = Counter()
    score = 0
    for m, step, a, b, c, coefficient in record["columns"]:
        if min(a, b, c) < 0 or min(coefficient, step) <= 0 or a+b+c+(m-2)*step != n-2:
            raise ValueError("An intermediate copy does not fit its host")
        floor = with_clearance[m] if with_clearance and step == 1 else generic[m]
        for left, bottom, right in permutations((a, b, c)):
            ox, oy = left + bottom, bottom
            for x in range(m - 1):
                for y in range(x + 1):
                    for j in range(1, m - 1 - x):
                        xy = (ox + step*x, oy + step*y, step*j)
                        if not 0 <= xy[1] <= xy[0] < xy[0]+xy[2] <= n-2:
                            raise ValueError("A charged physical corner escapes")
                        load[xy] += coefficient
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


if __name__ == "__main__":
    main()
