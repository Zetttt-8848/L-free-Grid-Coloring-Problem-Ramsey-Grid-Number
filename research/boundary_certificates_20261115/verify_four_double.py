"""Verify both discrete window applications and the 20-shift correction."""
from fractions import Fraction
from math import ceil, isqrt
from pathlib import Path
import json
import sys

from verify_four_window import HERE, load_window, require, verify_profile
from verify_four_twenty import outer_twenty

SIDE = 21_948_350
WIDTH = 34_950


def sidon_length(k, den, r, alpha, edge_saving=0, check_domain=None):
    """Return a certified lower bound for the number of occupied-interval positions."""
    c = Fraction((k - 1) * r[0], den)
    square = k * k * c / alpha
    center = isqrt(square.numerator // square.denominator) - c.numerator // c.denominator
    best = 0
    for block in range(max(1, center - 2), center + 3):
        length = ceil(Fraction(k * k * block, 1) / (block + c) - block * alpha)
        length += edge_saving
        if check_domain is not None:
            check_domain(k, length - 1, block)
        # Exclusion at length-1 also rules out all shorter intervals by embedding.
        require(length - 2 >= 2 * len(r) * block, "room for inner table")
        best = max(best, length)
    return best


def main():
    den, r, alpha = load_window(Path(sys.argv[1]) if len(sys.argv) > 1 else None)
    thresholds = [sidon_length(k, den, r, alpha) for k in range(4600, 4801)]
    rows = json.loads((HERE / "four_double_window_runs.json").read_text())
    verify_profile(rows, den, r, alpha, thresholds)
    count, raw, bonus, loss = outer_twenty(rows, SIDE, WIDTH)
    require((count, raw, bonus) == (544, -118_121_816_949_773_746_256_344_944,
                                   128_790_196_918_860_365_939_231_648), "final sum")
    require(raw + bonus > 0, "strict exclusion")
    print(f"{len(thresholds)} ordinary Sidon thresholds, {len(rows)} binary bounds, "
          f"{count} blocks of loss {loss}, side {SIDE:,}, margin {raw + bonus:,}.")


if __name__ == "__main__":
    main()
