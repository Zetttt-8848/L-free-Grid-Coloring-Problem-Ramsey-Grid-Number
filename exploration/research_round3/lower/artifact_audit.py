#!/usr/bin/env python3
"""Build certificate manifests and audit the final Route-5 package."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--circulant-manifest", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()

    witness = root / "difference_circulant_n3.txt"
    verification = root / "difference_circulant_n3_verify.json"
    checker = root / "verify_coloring.py"
    property_file = root / "PROPERTY.md"
    circulant = {
        "schema": "round3_lower_concrete_witness_manifest_v1",
        "claim_scope": "difference-circulant family has attainable side n=3",
        "exact_size": 3,
        "witness": witness.name,
        "checker": checker.name,
        "property": property_file.name,
        "verification_log": verification.name,
        "hashes_sha256": {p.name: sha(p) for p in (witness, checker, property_file, verification)},
        "verification_command": "python verify_coloring.py difference_circulant_n3.txt --n 3 --output difference_circulant_n3_verify.json",
        "verifier_result": "PASS: 5 corners inspected, 0 violations, symbols exactly {1,2,3}",
    }
    args.circulant_manifest.write_text(json.dumps(circulant, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    exact = json.loads((root / "exact_claims.json").read_text(encoding="utf-8"))
    instance = json.loads((root / "n21_instance_audit.json").read_text(encoding="utf-8"))
    global_audit = json.loads((root / "n21_global_checkpoint_audit.json").read_text(encoding="utf-8"))
    direct = json.loads(verification.read_text(encoding="utf-8"))
    hard = json.loads((root / "n21_stage2_portfolio_merged.json").read_text(encoding="utf-8"))
    easy = json.loads((root / "n21_quick_cube_rup_audit.json").read_text(encoding="utf-8"))
    phase = json.loads((root / "phase_hint_audit.json").read_text(encoding="utf-8"))
    errata_text = (root / "ERRATA.md").read_text(encoding="utf-8")
    checks = {
        "exact_claims_pass": exact.get("all_exact_checks_pass") is True,
        "instance_audit_pass": instance.get("audit_pass") is True,
        "global_checkpoint_audit_pass": global_audit.get("audit_pass") is True,
        "difference_circulant_witness_pass": direct.get("verified_corner_free") is True and direct.get("corners_inspected") == 5,
        "hard_merge_pass": hard.get("audit_pass") is True and hard.get("statuses") == {"INTERRUPTED_UNDECIDED": 48},
        "easy_rup_pass": easy.get("proofs_verified_all_rup") == 33 and easy.get("all_present_proofs_verified") is True,
        "phase_hint_domain_and_eight_conflicts_pass": phase.get("audit_pass") is True,
        "no_n21_witness_file": not any(root.glob("n21*_witness.txt")) and not any(root.glob("affine_n21_witness*.txt")),
        "six_r10_entries": errata_text.count("## R3-R5-E") == 6,
        "report_present": (root / "SUBTASK_REPORT.md").is_file(),
    }

    files = []
    excluded = {args.index.resolve()}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.resolve() in excluded or "__pycache__" in path.parts:
            continue
        files.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)})
    index = {
        "schema": "round3_lower_artifact_index_v1",
        "scope": str(root),
        "files": files,
        "file_count": len(files),
        "closure_checks": checks,
        "all_closure_checks_pass": all(checks.values()),
        "mathematical_status": "UNDECIDED at side 21; scoped certificates only",
    }
    args.index.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"file_count": index["file_count"], "closure_checks": checks, "all_closure_checks_pass": index["all_closure_checks_pass"]}, indent=2))
    return 0 if index["all_closure_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
