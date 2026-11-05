#!/usr/bin/env python3
"""Cross-check the complete 81-cube checkpoint from immutable artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cubes", type=Path, required=True)
    parser.add_argument("--stage1", type=Path, required=True)
    parser.add_argument("--easy-audit", type=Path, required=True)
    parser.add_argument("--hard-merge", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cubes = json.loads(args.cubes.read_text(encoding="utf-8"))
    stage1 = json.loads(args.stage1.read_text(encoding="utf-8"))
    easy = json.loads(args.easy_audit.read_text(encoding="utf-8"))
    hard = json.loads(args.hard_merge.read_text(encoding="utf-8"))
    cube_by_order = {r["order"]: r for r in cubes["records"]}
    stage_by_order = {r["order"]: r for r in stage1["records"]}
    stage_exact = len(stage_by_order) == 81 and all(
        order in cube_by_order
        and record["cube_colors_0_based"] == cube_by_order[order]["cube_colors_0_based"]
        and record["assumption_literals"] == cube_by_order[order]["assumption_literals"]
        for order, record in stage_by_order.items()
    )
    easy_orders = {r["order"] for r in easy["records"] if r["verified_all_rup_unsat"]}
    expected_easy = {order for order, r in stage_by_order.items() if r["status"] == "RAW_UNSAT_UNVERIFIED"}
    hard_orders = {r["order"] for r in hard["records"]}
    expected_hard = {order for order, r in stage_by_order.items() if r["status"] == "INTERRUPTED_UNDECIDED"}
    result = {
        "schema": "round3_lower_global_checkpoint_audit_v1",
        "input_hashes": {str(path): sha(path) for path in (args.cubes, args.stage1, args.easy_audit, args.hard_merge)},
        "stage1_all_81_exact_manifest_match": stage_exact,
        "easy_certified_orders": len(easy_orders),
        "easy_order_set_exact_match": easy_orders == expected_easy,
        "hard_record_orders": len(hard_orders),
        "hard_order_set_exact_match": hard_orders == expected_hard,
        "easy_hard_disjoint": easy_orders.isdisjoint(hard_orders),
        "easy_hard_union_is_all_81": easy_orders | hard_orders == set(cube_by_order),
        "hard_merge_audit_pass": hard.get("audit_pass") is True,
        "sat_witnesses": sum(r["status"] == "SAT" for r in stage1["records"]),
        "certified_unit_unsat_cubes": len(easy_orders),
        "unresolved_hard_cubes": len(hard_orders),
        "mathematical_status": "UNDECIDED",
        "reason": "48 disjoint cubes remain interrupted; no SAT witness and no certified UNSAT result covers them",
    }
    result["audit_pass"] = all((
        stage_exact,
        easy.get("all_present_proofs_verified") is True,
        result["easy_order_set_exact_match"],
        result["hard_order_set_exact_match"],
        result["easy_hard_disjoint"],
        result["easy_hard_union_is_all_81"],
        result["hard_merge_audit_pass"],
        result["sat_witnesses"] == 0,
        result["certified_unit_unsat_cubes"] == 33,
        result["unresolved_hard_cubes"] == 48,
    ))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["audit_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
