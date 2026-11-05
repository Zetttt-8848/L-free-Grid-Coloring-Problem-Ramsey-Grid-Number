#!/usr/bin/env python3
"""Closure audit for the Round-2 lower-route finite artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LOWER_CHECKS = ROOT / "research_round2" / "checks" / "lower"
LOWER_CERTS = ROOT / "research_round2" / "certificates" / "lower"
LOWER_ROUTES = ROOT / "research_round2" / "routes" / "lower"


def read_json(name: str) -> dict:
    return json.loads((LOWER_CHECKS / name).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    assertions: list[dict[str, object]] = []

    def check(label: str, condition: bool, detail: object) -> None:
        assertions.append({"label": label, "pass": bool(condition), "detail": detail})

    bench_bad = read_json("benchmark20_verify.json")
    bench_good = read_json("benchmark20_transposed_verify.json")
    check("raw benchmark records R10 mismatch", bench_bad["violations"] == 204, bench_bad["violations"])
    check("transposed benchmark verifies", bench_good["verified_corner_free"] and bench_good["geometric_triples"] == 2470, bench_good)

    cube_expected = {
        21: ("cube_n21_maplechrono.json", 1323, 10815),
        22: ("cube_n22_maplechrono.json", 1452, 12353),
        23: ("cube_n23_maplechrono.json", 1587, 14030),
    }
    for n, (name, variables, clauses) in cube_expected.items():
        rec = read_json(name)
        ok = (
            rec["mathematical_status"] == "UNDECIDED"
            and rec["cubes_attempted"] == 81
            and rec["statuses"] == {"SAT": 0, "UNSAT": 33, "UNDECIDED": 48}
            and rec["counts"]["variables"] == variables
            and rec["counts"]["total_clauses"] == clauses
        )
        check(f"cube n={n}", ok, {"statuses": rec["statuses"], "counts": rec["counts"]})

    breakout_expected = {
        21: ("breakout_n21_corrected.json", 9, 8, 359256),
        22: ("breakout_n22.json", 108, 18, 181931),
        23: ("breakout_n23.json", 148, 53, 175415),
    }
    for n, (name, initial, best, moves) in breakout_expected.items():
        rec = read_json(name)
        ok = rec["status"] == "UNDECIDED" and rec["initial_conflicts"] == initial and rec["best_conflicts"] == best and rec["moves"] == moves
        check(f"breakout n={n}", ok, {key: rec[key] for key in ("initial_conflicts", "best_conflicts", "moves", "wall_seconds")})

    cpsat_expected = {21: "cpsat_n21.json", 22: "cpsat_n22.json", 23: "cpsat_n23.json"}
    for n, name in cpsat_expected.items():
        rec = read_json(name)
        check(f"CP-SAT n={n}", rec["raw_solver_status"] == "UNKNOWN" and rec["witness"] is None, {"raw": rec["raw_solver_status"], "wall": rec["solver_wall_time_seconds"]})

    hamming = read_json("cpsat_n21_hamming12_nosym.json")
    check("symmetry-free Hamming radius 12", hamming["raw_solver_status"] == "UNKNOWN" and hamming["constraints"] == 3753 and hamming["symmetry_breaking"] is None, hamming["raw_solver_status"])

    product = read_json("product_n9_verify.json")
    check("product certificate", product["verified_corner_free"] and product["geometric_triples"] == 204 and product["color_counts"] == {"1": 27, "2": 27, "3": 27}, product)

    alteration = read_json("alteration_exact.json")
    selected = {row["n"]: row for row in alteration["rows"] if row["n"] in (21, 22, 23)}
    check("alteration exact values", [(selected[n]["geometric_triples"], selected[n]["partial_domain_cells_retained"]) for n in (21, 22, 23)] == [(2870, 123), (3311, 117), (3795, 108)], selected)

    candidate_names = [
        "breakout_n21_matrix.txt",
        "breakout_n21_corrected_matrix.txt",
        "breakout_n22_matrix.txt",
        "breakout_n23_matrix.txt",
        "cpsat_n21_matrix.txt",
        "cpsat_n22_matrix.txt",
        "cpsat_n23_matrix.txt",
        "cpsat_n21_hamming12_nosym_matrix.txt",
    ]
    check("no claimed certificate at n=21..23", not any((LOWER_CERTS / name).exists() for name in candidate_names), candidate_names)

    invalid = LOWER_CHECKS / "r10_invalid_breakout_n21_four_symbol_matrix.txt"
    invalid_values = {int(t) for t in invalid.read_text(encoding="ascii").split()}
    disposition = read_json("breakout_n21_rejection_disposition.json")
    check("R10 invalid candidate preserved and explicitly rejected",
          4 in invalid_values and disposition["current_status"] == "REJECTED_INVALID_COLOR_DOMAIN"
          and disposition["mathematical_status"] == "NO_LOWER_BOUND_CLAIM",
          {"symbols": sorted(invalid_values), "current_status": disposition["current_status"]})

    artifacts = []
    for directory in (LOWER_ROUTES, LOWER_CHECKS, LOWER_CERTS):
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.name != "artifact_index.json":
                artifacts.append({"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})

    passed = all(item["pass"] for item in assertions)
    record = {
        "schema": "round2_lower_artifact_audit_v1",
        "status": "PASS" if passed else "FAIL",
        "assertions": assertions,
        "artifacts": artifacts,
        "non_claims": ["Artifact integrity is not an independent mathematical proof"],
    }
    out = LOWER_CHECKS / "artifact_index.json"
    out.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": record["status"], "assertion_count": len(assertions), "artifact_count": len(artifacts)}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
