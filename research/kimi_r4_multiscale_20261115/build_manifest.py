#!/usr/bin/env python3
"""Validate ASCII/syntax and build deterministic round-3 evidence manifests."""

import ast
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NEW = ROOT / "research" / "kimi_r4_multiscale_20261115"
OLD = ROOT / "research" / "kimi_r4_quotient_multiscale_20261115"


def digest(path):
    raw = path.read_bytes()
    raw.decode("ascii")
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main():
    verification = json.loads((NEW / "verification.json").read_text(encoding="utf-8"))
    standard = json.loads((NEW / "standard_coloring_check.json").read_text(encoding="utf-8"))
    audit = json.loads((NEW / "audit_results.json").read_text(encoding="utf-8"))
    witness = json.loads((NEW / "counterexample_6.json").read_text(encoding="utf-8"))
    assert verification["status"] == "PASS"
    assert standard["proper"] is True and standard["corners"] == 55
    assert audit["proper_witness"]["old_Q3a_lhs"] == "1381/144"
    assert verification["checked_multiplicity_entries"] == 1063

    new_hashes = {}
    for path in sorted(NEW.iterdir()):
        if not path.is_file() or path.name == "manifest.json":
            continue
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="ascii"), filename=str(path))
        new_hashes[path.name] = digest(path)

    old_hashes = {}
    for path in sorted(OLD.iterdir()):
        if not path.is_file() or path.name == "manifest.json":
            continue
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="ascii"), filename=str(path))
        old_hashes[path.name] = digest(path)

    old_manifest = {
        "date": "2026-11-15",
        "branch": "kimi/r4-quotient-multiscale-20261115",
        "base_commit": "14647e607c2525b0cd12081b03899827d306a030",
        "correction_branch": "kimi/r4-multiscale-20261115",
        "status": "SUPERSEDED IN PART: Q3a and its averaging evidence are withdrawn",
        "checks": {
            "counterexample_independent_verifier": "PASS; Q1/Q2 evidence unaffected",
            "contiguous_averaging_independent_verifier": "INVALID for Q3a; it checked aggregate identities but not the claimed inequality",
            "old_averaging_results": "WITHDRAWN; historical artifact only",
            "current_ascii_and_syntax": "PASS",
        },
        "superseded_statements": [
            "Q3a weighted pair-tight inequality",
            "position-independent fixed-L block multiplicity",
            "structural interpretation of the unweighted pair-tight count",
        ],
        "unaffected_statements": ["Q1", "Q2", "unequal-subselection obstruction"],
        "superseded_by": "research/kimi_r4_multiscale_20261115/THEOREM.md",
        "python": "3.12.16",
        "dependencies": "Python standard library only",
        "sha256": old_hashes,
        "scope": "Current hashes on the correction branch; no numerical Ramsey bound changed",
    }
    write_json(OLD / "manifest.json", old_manifest)

    new_manifest = {
        "date": "2026-11-15",
        "branch": "kimi/r4-multiscale-20261115",
        "base_commit": "af166bc27aaa3f22b4f62907d983fbecb20f4aec",
        "contract_commit": "f81582ee8b307b17b796655952cdaa76e3d44e7b",
        "python": "3.12.16",
        "dependencies": "Python standard library only",
        "checks": {
            "generator": "PASS",
            "independent_verifier": "PASS",
            "standard_coloring_checker": "PASS",
            "temporary_directory_reproduction": "PASS; all four output files byte-identical",
            "ascii_only_new_package": "PASS",
            "python_syntax": "PASS",
        },
        "coverage": {
            "color_words": 64,
            "witness_cells": 36,
            "witness_geometric_Ls": 55,
            "scale_rows": 6,
            "multiplicity_entries": 1063,
        },
        "results": {
            "old_Q3a": "REFUTED",
            "signature_trichotomy": "PROVED",
            "multiscale_pair_tight_identity": "PROVED and coloring-independent",
            "seven_quotient_consumer": "DOMINATED by a trivial bound",
            "Q1_and_Q2": "unaffected",
            "new_R3_bound": False,
            "new_R4_bound": False,
        },
        "source_input_sha256": witness["provenance"]["source_sha256"],
        "sha256": new_hashes,
        "corrected_round1_manifest_sha256": digest(OLD / "manifest.json"),
        "project_plan_sha256": digest(ROOT / "KIMI_RESEARCH_PLAN.md"),
        "scope": "Internal reproducibility only; not external review or formalization",
    }
    write_json(NEW / "manifest.json", new_manifest)
    print(json.dumps({"status": "PASS", "new_files_hashed": len(new_hashes),
                      "old_files_hashed": len(old_hashes),
                      "multiplicity_entries": 1063,
                      "new_R3_bound": False, "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
