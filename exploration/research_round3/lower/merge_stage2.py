#!/usr/bin/env python3
"""Audit and merge the two completed hard-cube portfolio shards."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--worker", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cubes = json.loads(args.cubes.read_text(encoding="utf-8"))
    workers = [json.loads(path.read_text(encoding="utf-8")) for path in args.worker]
    expected = [r for r in cubes["records"] if r["round2_raw_status"] == "UNDECIDED"]
    expected_by_order = {r["order"]: r for r in expected}
    actual = [r for worker in workers for r in worker["records"]]
    orders = [r["order"] for r in actual]
    exact_records = all(
        r["order"] in expected_by_order
        and r["cube_colors_0_based"] == expected_by_order[r["order"]]["cube_colors_0_based"]
        and r["assumption_literals"] == expected_by_order[r["order"]]["assumption_literals"]
        for r in actual
    )
    coverage = len(actual) == 48 and len(set(orders)) == 48 and set(orders) == set(expected_by_order)
    statuses = {s: sum(r["status"] == s for r in actual) for s in sorted({r["status"] for r in actual})}
    result = {
        "schema": "round3_lower_hard_cube_portfolio_merge_v1",
        "worker_files": [str(path) for path in args.worker],
        "worker_sha256": [hashlib.sha256(path.read_bytes()).hexdigest() for path in args.worker],
        "expected_hard_cubes": 48,
        "actual_records": len(actual),
        "unique_orders": len(set(orders)),
        "exact_cube_records": exact_records,
        "all_48_hard_cubes_accounted_for": coverage,
        "statuses": statuses,
        "records": sorted(actual, key=lambda r: r["order"]),
        "sat_found": any(r["status"] == "SAT" for r in actual),
    }
    if result["sat_found"]:
        result["mathematical_status"] = "SAT_WITNESS_REQUIRES_DIRECT_CHECK"
    elif statuses == {"INTERRUPTED_UNDECIDED": 48}:
        result["mathematical_status"] = "UNDECIDED_48_INTERRUPTED"
    else:
        result["mathematical_status"] = "UNDECIDED_PENDING_ANY_NEGATIVE_CERTIFICATE_CHECKS"
    result["audit_pass"] = exact_records and coverage
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("actual_records", "unique_orders", "exact_cube_records", "all_48_hard_cubes_accounted_for", "statuses", "sat_found", "mathematical_status", "audit_pass")}, indent=2))
    return 0 if result["audit_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
