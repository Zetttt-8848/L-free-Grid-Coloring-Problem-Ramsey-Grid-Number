"""Verify the four-color bound using the finite Sidon estimate in arXiv:2610.36207v1.

The only external numerical premise needed here is the explicit cardinality
inequality in that paper for ordinary Sidon sets of at least 483 marks.
"""
from bisect import bisect_right
import json
from pathlib import Path

from verify_four_rank import binary_spans, checked, golomb_spans

SIDE = 21_953_510
SUPPORT = 34_700
REFERENCE = 21_975_000
HERE = Path(__file__).resolve().parent


def lower_length(size):
    """Lower bound on the number of consecutive positions a Sidon set needs."""
    checked(size >= 483, "finite Sidon theorem size threshold")
    # k <= sqrt(N) + (94304/100000)*N^(1/4) + 44466/100000.
    # For Y=100000*k-44466, exclusion is equivalent to Y>S*sqrt(N)
    # and (Y-S*sqrt(N))^2 > B^2*sqrt(N). Clear the second radical.
    scale = 100_000
    b = 94_304
    y = scale*size - 44_466
    lo, hi = 0, size**2
    while hi-lo > 1:
        n = (lo+hi)//2
        impossible = (y*y > scale**2*n and
                      (y*y + scale**2*n)**2 > n*(2*y*scale+b*b)**2)
        if impossible:
            lo = n
        else:
            hi = n
    return hi


def cost_of_differences(positions, required, thresholds):
    """Count the cheapest required positive differences by constant-cap blocks."""
    # At distance h, stagger the minima of the two interior Golomb classes.
    h = 1
    cost = 0
    while required:
        remaining = positions - h
        i = bisect_right(thresholds, remaining)
        j = bisect_right(thresholds, remaining - 1)
        checked(0 < i < len(thresholds) and 0 < j < len(thresholds),
                "Sidon threshold coverage")
        # i thresholds are attained or passed; the next size is excluded.
        capacity = 2 * 4699 + i + j
        width = min(remaining - thresholds[i-1] + 1,
                    remaining - 1 - thresholds[j-1] + 1)
        full = min(width, required // capacity)
        cost += capacity * full * (2*h + full - 1) // 2
        h += full
        required -= full * capacity
        if full < width:
            cost += h * required
            break
    return cost


def correlation(distance):
    """Sum the degree-four weight products using power sums on their overlap."""
    length = SUPPORT - distance
    end = SUPPORT + 1
    sums = [length, length*(length+1)//2,
            length*(length+1)*(2*length+1)//6,
            (length*(length+1)//2)**2,
            length*(length+1)*(2*length+1)*(3*length**2+3*length-1)//30]
    # i*(end-i)*(i+d)*(end-d-i)
    d = distance
    coefficients = (0, end*d*(end-d), end*(end-2*d) - d*(end-d),
                    2*d-2*end, 1)
    return sum(a*b for a,b in zip(coefficients, sums))


def main():
    rows = json.loads((HERE / "four_sidon_runs.json").read_text(encoding="utf-8"))
    front = REFERENCE - SIDE + 1
    back = REFERENCE - SIDE + SUPPORT - 1 + 11
    checked(rows[0][0] <= front <= back and rows[-1][0] <= back, "coverage")
    offsets = [row[0] for row in rows]
    checked(all(a < b for a,b in zip(offsets, offsets[1:])), "run ordering")
    thresholds = [lower_length(k) for k in range(4700, 4801)]
    checked(all(a < b for a,b in zip(thresholds, thresholds[1:])), "threshold ordering")
    lengths = binary_spans(golomb_spans(), max(row[2] for row in rows))
    for offset, cap, rank in rows:
        positions = REFERENCE - offset
        size = cap + 1
        checked(1 <= rank < size and cap > 0, "rank domain")
        pairs = rank*size - rank*(rank+1)//2
        cost = cost_of_differences(positions, pairs, thresholds)
        edges = sum((rank-i)*lengths[i+1] for i in range(rank))
        checked(2*cost + 4*edges > (positions-1)*rank*(rank+1),
                f"rank witness at {offset}")
    for d in (0, 1, 137, SUPPORT//2, SUPPORT-1):
        literal = sum(i*(SUPPORT+1-i)*(i+d)*(SUPPORT+1-i-d)
                      for i in range(1, SUPPORT-d+1))
        checked(literal == correlation(d), "power-sum formula")
    margin = -3 * SIDE * correlation(0)
    for d in range(1, SUPPORT):
        start = REFERENCE - SIDE + d
        cap = sum(rows[bisect_right(offsets, start+j)-1][1] for j in range(12))
        margin += 2*(SIDE-d-4*cap)*correlation(d)
    checked(margin == 3_322_828_120_073_118_722_559_272, "exact final margin")
    print(f"Verified {len(rows)} rank witnesses and {SUPPORT-1:,} shifts "
          f"at side {SIDE:,}. Doubled margin {margin:,}.")


if __name__ == "__main__":
    main()

