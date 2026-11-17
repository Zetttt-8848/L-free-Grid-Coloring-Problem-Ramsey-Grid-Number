#!/usr/bin/env python3
"""Validate the round-5 package, run English checks, and write hashes."""

import ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEW = ROOT / "research" / "kimi_r4_nonuniform_dual_20261116"
MANIFEST = NEW / "manifest.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def english_check():
    with tempfile.TemporaryDirectory(prefix=".tmp-kimi-index-", dir=ROOT) as tmp:
        index = Path(tmp) / "index"
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(index)
        subprocess.run(["git", "read-tree", "HEAD"], cwd=ROOT, env=env, check=True)
        subprocess.run(["git", "add", "--", "KIMI_RESEARCH_PLAN.md",
                        "research/kimi_r4_nonuniform_dual_20261116"],
                       cwd=ROOT, env=env, check=True)
        run = subprocess.run([sys.executable, "scripts/check_english_only.py"],
                             cwd=ROOT, env=env, check=True, text=True,
                             stdout=subprocess.PIPE)
    summary = run.stdout.strip().splitlines()[-1]
    assert summary.endswith("0 violations"), run.stdout
    return summary


def main():
    if MANIFEST.exists():
        MANIFEST.unlink()
    verification = json.loads((NEW / "dual_verification.json").read_text(encoding="ascii"))
    assert verification["status"] == "PASS"
    assert verification["negative_controls_rejected"] == 2
    assert len(verification["rows"]) == 3
    assert all(row["exact_optimum_certified_by_equal_feasible_values"]
               for row in verification["rows"])
    assert verification["new_Ramsey_bound"] is False
    results = json.loads((NEW / "dual_results.json").read_text(encoding="ascii"))
    assert results["pairs"] == [[30, 6], [60, 6], [120, 6]]
    assert results["new_Ramsey_bound"] is False

    hashes = {}
    for path in sorted(NEW.iterdir()):
        if not path.is_file():
            continue
        raw = path.read_bytes()
        raw.decode("ascii")
        if path.suffix == ".py":
            ast.parse(raw.decode("ascii"), filename=str(path))
        hashes[path.name] = digest(path)
    plan = ROOT / "KIMI_RESEARCH_PLAN.md"
    plan.read_bytes().decode("ascii")
    english_summary = english_check()

    manifest = {
        "date": "2026-11-16",
        "branch": "kimi/r4-hybrid-dual-20261116",
        "base_commit": "e1a62f30ce74d03681c04b58d0486e551e775124",
        "python": sys.version.split()[0],
        "discovery_dependencies": "NumPy 2.4.4 and SciPy 1.18.1; floating point used for discovery only",
        "verification_dependencies": "Python standard library only",
        "checks": {
            "exact_primal_and_dual_verifier": "PASS",
            "negative_controls": "PASS; both rejected",
            "python_syntax_new_package": "PASS by AST parsing",
            "english_only": english_summary,
        },
        "coverage": {
            "pairs": [[30, 6], [60, 6], [120, 6]],
            "primal_host_step_constraints": 204,
            "dual_scale_constraints": 39,
            "origin_count_cross_checks": 8,
            "actual_rho_6_search": False,
        },
        "results": {
            "three_finite_optima": "PROVED by equal exact feasible primal and dual values",
            "N30_best_case_consumer": "CLOSED",
            "N60_N120_best_case_margins": "POSITIVE; actual consumer UNDECIDED",
            "nonuniform_all_N_consumer": "UNDECIDED",
            "new_R3_bound": False,
            "new_R4_bound": False,
        },
        "sha256": hashes,
        "project_plan_sha256": digest(plan),
        "scope": "Internal finite mathematical checks; not external review or formalization",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="ascii")
    MANIFEST.read_bytes().decode("ascii")
    print(json.dumps({"status": "PASS", "files_hashed": len(hashes),
                      "english_only": english_summary,
                      "new_R3_bound": False, "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
