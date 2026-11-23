"""Recompute the original PR 11 certificate with the weak triangle placed in side 143."""

import argparse
import sys
from pathlib import Path

from verify_143 import BASELINE, read_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    args = parser.parse_args()
    sys.path.insert(0, str(args.baseline.resolve()))
    import verify_triangle_grid as original
    from verify_square_patches import PATCHES

    def fits_weak_embedding(order, source, step, a, b, level, minimum=0):
        # The right and top margins are measured from the side-(order - 1) square.
        c = order - 2 - step * (source - 2) - a - b
        for patch in PATCHES[:level]:
            if patch.order != source or patch.cutoff + 1 < minimum or step % patch.stride:
                continue
            unit = step // patch.stride
            gap = patch.side - 1 - (source - 2) * patch.stride
            for x, y in ((patch.x, patch.y), (gap - patch.y, gap - patch.x)):
                if (a + b >= unit * x and b >= unit * y
                        and c >= unit * (gap - x) and a + c >= unit * (gap - y)):
                    return True
        return False

    original.fits_checked_square = fits_weak_embedding
    cert = read_json(args.baseline / "triangle_grid_certificate.json")
    if cert["host"] != 144:
        raise ValueError("Expected the side-144 certificate from PR 11")
    catalogs = read_json(args.baseline / "triangle_grid_catalogs.json.xz")
    margin = original.verify(cert, catalogs)
    print(f"Weak host lies in square side 143. Exact difference: {margin}.")


if __name__ == "__main__":
    main()
