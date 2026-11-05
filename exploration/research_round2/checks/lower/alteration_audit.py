#!/usr/bin/env python3
"""Exact-integer arithmetic for the elementary random-deletion calculation."""

import json
from pathlib import Path


def main() -> int:
    rows = []
    for n in range(1, 24):
        triples = (n - 1) * n * (2 * n - 1) // 6
        quotient, remainder = divmod(triples, 9)
        rows.append(
            {
                "n": n,
                "geometric_triples": triples,
                "expected_monochromatic_corners": f"{triples}/9",
                "floor_expected": quotient,
                "expected_numerator_mod_9": remainder,
                "partial_domain_cells_retained": n * n - quotient,
                "lower_bound_implication": None,
            }
        )
    record = {
        "schema": "round2_lower_alteration_v1",
        "probability_one_triple_monochromatic": "1/9",
        "reason": "3*(1/3)^3=1/9",
        "rows": rows,
        "non_claims": [
            "The retained cells need not contain a full Cartesian subgrid",
            "Deleting cells does not yield a coloring of [m]^2",
            "No Ramsey lower bound follows from this partial-domain alteration",
        ],
    }
    out = Path("research_round2/checks/lower/alteration_exact.json")
    out.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"n21": rows[20], "n22": rows[21], "n23": rows[22]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
