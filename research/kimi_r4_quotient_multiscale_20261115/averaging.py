#!/usr/bin/env python3
"""HISTORICAL AND WITHDRAWN: Q3a is false; do not use this output as evidence.

See ERRATUM.md and research/kimi_r4_multiscale_20261115/. This file is retained
only to preserve the original audited artifact and its correction history.
"""

import argparse
import json
from pathlib import Path


def values(n):
    if n < 5:
        return None
    blocks = (n - 4) ** 2
    # For fixed d<=4, a given L is contained in exactly (5-d)^2 contiguous
    # 5-blocks. Sum P_d/(5-d)^2 >= 3*(n-4)^2, where P_d counts pair-tight Ls.
    total_ls = n * (n - 1) * (2 * n - 1) // 6
    # Since 1/(5-d)^2 <= 1, the unweighted pair-tight count is at least
    # 3*(n-4)^2. The density formula below is only a scale diagnostic.
    density_num = 3 * (n - 4) ** 2
    return {
        "n": n,
        "contiguous_5_blocks": blocks,
        "step_multiplicities": {str(d): (5 - d) ** 2 for d in range(1, 5)},
        "weighted_lower_bound": f"sum(P_d/(5-d)^2, d=1..4) >= 3*{blocks}",
        "unweighted_pair_tight_L_lower_bound": density_num,
        "all_geometric_Ls": total_ls,
        "density_lower_bound_numerator": density_num,
        "density_lower_bound_denominator": total_ls,
        "density_float_diagnostic_only": density_num / total_ls,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [values(n) for n in (5, 6, 10, 100, 1000, 21947865)]
    result = {
        "status": "PROVED contiguous-block arithmetic; no Ramsey contradiction",
        "invalid_previous_mechanism": "Arbitrary combinatorial row/column subsquares do not preserve equal-leg L geometry",
        "proved_lower_bound_asymptotic": "9/n for the unweighted density lower bound; not an estimate of the true density",
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
