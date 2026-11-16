#!/usr/bin/env python3
"""Validate the round-4 package, run English checks, and write hashes."""

import ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEW = ROOT / "research" / "kimi_r4_energy_20261115"
MANIFEST = NEW / "manifest.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def english_check():
    # Use a temporary index so the repository's own tracked-file checker sees
    # this not-yet-committed package without modifying the user's real index.
    with tempfile.TemporaryDirectory(prefix=".tmp-kimi-index-", dir=ROOT) as tmp:
        index = Path(tmp) / "index"
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(index)
        subprocess.run(["git", "read-tree", "HEAD"], cwd=ROOT, env=env, check=True)
        subprocess.run(["git", "add", "--", "KIMI_RESEARCH_PLAN.md",
                        "research/kimi_r4_energy_20261115"],
                       cwd=ROOT, env=env, check=True)
        run = subprocess.run([sys.executable, "scripts/check_english_only.py"],
                             cwd=ROOT, env=env, check=True, text=True,
                             stdout=subprocess.PIPE)
    lines = run.stdout.strip().splitlines()
    summary = lines[-1]
    assert summary.endswith("0 violations"), run.stdout
    return summary


def main():
    if MANIFEST.exists():
        MANIFEST.unlink()
    for name in ("energy_verification.json", "kernel_verification.json",
                 "consumer_verification.json", "reproduction.json"):
        value = json.loads((NEW / name).read_text(encoding="ascii"))
        assert value["status"] == "PASS", name
    for m, corners in ((3, 5), (4, 14), (5, 30)):
        standard = json.loads((NEW / f"standard_{m}.json").read_text(encoding="ascii"))
        assert standard["proper"] is True
        assert standard["monochromatic"] == 0
        assert standard["rainbows"] == 0
        assert standard["corners"] == corners
    kernels = json.loads((NEW / "kernel_results.json").read_text(encoding="ascii"))
    assert [row["rho_m"] for row in kernels["orders"]] == [0, 0, 0]
    energy = json.loads((NEW / "energy_results.json").read_text(encoding="ascii"))
    assert sum(row["all_four_color_words_checked"] for row in energy["exhaustive_checks"]) == 4164
    consumer = json.loads((NEW / "consumer_results.json").read_text(encoding="ascii"))
    consumer_check = json.loads((NEW / "consumer_verification.json").read_text(encoding="ascii"))
    assert consumer_check["uniform_asymptotic_consumer_closed_for_all_m"] is True
    assert all(row["consumer_closed"] is True for row in consumer["thresholds"])
    reproduction = json.loads((NEW / "reproduction.json").read_text(encoding="ascii"))
    assert reproduction["output_count"] == 12
    assert reproduction["temporary_directory_removed"] is True

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
        "date": "2026-11-15",
        "branch": "kimi/r4-energy-20261115",
        "base_commit": "b7d52434061f7cb15395d50edc949e2700356926",
        "contract_commit": "2f56b6e8c774adc534cf7e67dcd360d77c04b474",
        "preregistration_amendment_commit": "7b5fa53293f1791ae52d5d7546565648beff7348",
        "python": sys.version.split()[0],
        "dependencies": "Python standard library only; project coloring checker for standard_*.json",
        "checks": {
            "energy_generator": "PASS",
            "energy_independent_verifier": "PASS",
            "kernel_witnesses_and_known_answers": "PASS",
            "consumer_geometry_and_exact_asymptotics": "PASS",
            "standard_coloring_checker": "PASS for all three witnesses",
            "temporary_copy_reproduction": "PASS; 12 output files byte-identical; copy removed",
            "ascii_and_python_syntax_new_package": "PASS",
            "english_only": english_summary,
        },
        "coverage": {
            "all_four_color_words": 4164,
            "energy_formula_rows": 10,
            "zero_rainbow_full_squares": [3, 4, 5],
            "full_square_Ls_checked": [5, 14, 30],
            "known_answer_two_color_squares": [4, 5],
            "consumer_host_scenarios": 5,
            "consumer_scale_rows": 7,
            "asymptotic_coefficients_independently_reconstructed": [3, 4, 5, 6, 7, 8],
        },
        "results": {
            "general_line_identity": "PROVED",
            "pure_four_color_energy_consumer": "CLOSED; no contradiction",
            "rho_3_4_5": "PROVED equal to zero",
            "contracted_copy_count": "REFUTED for the intended host-triangle consumer; corrected",
            "uniform_asymptotic_consumer": "CLOSED for every m; finite isolated sides not classified",
            "nonuniform_weights": "UNDECIDED",
            "new_R3_bound": False,
            "new_R4_bound": False,
        },
        "sha256": hashes,
        "project_plan_sha256": digest(plan),
        "scope": "Internal reproducibility and mathematical checks; not external review or formalization",
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="ascii")
    # Recheck the final manifest text directly; the temporary-index run already
    # covered every other file intended for the commit.
    MANIFEST.read_bytes().decode("ascii")
    print(json.dumps({"status": "PASS", "files_hashed": len(hashes),
                      "english_only": english_summary,
                      "reproduced_outputs": 12,
                      "new_R3_bound": False, "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
