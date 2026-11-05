#!/usr/bin/env python3
"""Independently validate the inherited phase hint's domain and conflicts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("checkpoint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.checkpoint.read_text(encoding="utf-8"))
    n = int(source["n"])
    flat = source["best_grid"]
    if len(flat) != n * n:
        raise ValueError("phase grid has wrong cell count")
    if any(v not in (0, 1, 2) for v in flat):
        raise ValueError("phase grid is not zero-based three-symbol data")
    rows = [flat[x * n:(x + 1) * n] for x in range(n)]
    conflicts = []
    inspected = 0
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                inspected += 1
                if rows[x][y] == rows[x + d][y] == rows[x + d][y + d]:
                    conflicts.append([x, y, d, rows[x][y]])
    canonical = "\n".join(" ".join(map(str, row)) for row in rows) + "\n"
    result = {
        "schema": "round3_lower_independent_phase_hint_audit_v1",
        "n": n,
        "cell_count": len(flat),
        "domain_exactly_subset_0_1_2": True,
        "corners_inspected": inspected,
        "conflicts": len(conflicts),
        "conflict_records_0_based": conflicts,
        "canonical_zero_based_matrix_sha256": hashlib.sha256(canonical.encode("ascii")).hexdigest(),
        "source_file_sha256": hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
        "audit_pass": n == 21 and inspected == 2870 and len(conflicts) == 8,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["audit_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

