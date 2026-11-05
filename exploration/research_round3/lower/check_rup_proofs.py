#!/usr/bin/env python3
"""Small independent checker for DRAT traces whose every addition is RUP.

This intentionally does not implement RAT.  A trace containing a non-RUP
addition receives UNDECIDED, never rejection of the underlying UNSAT claim.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path


def parse_cnf(path: Path) -> tuple[int, list[tuple[int, ...]]]:
    nvars = None
    clauses = []
    declared = None
    for raw in path.read_text(encoding="ascii").splitlines():
        fields = raw.split()
        if not fields or fields[0] == "c":
            continue
        if fields[0] == "p":
            if len(fields) != 4 or fields[1] != "cnf":
                raise ValueError("bad DIMACS header")
            nvars, declared = int(fields[2]), int(fields[3])
        else:
            values = tuple(map(int, fields))
            if not values or values[-1] != 0:
                raise ValueError("unterminated input clause")
            clauses.append(values[:-1])
    if nvars is None or declared != len(clauses):
        raise ValueError("missing or inconsistent DIMACS header")
    return nvars, clauses


def parse_trace(path: Path) -> list[tuple[bool, tuple[int, ...]]]:
    steps = []
    for raw in path.read_text(encoding="ascii").splitlines():
        fields = raw.split()
        if not fields:
            continue
        deletion = fields[0] == "d"
        values = tuple(map(int, fields[1:] if deletion else fields))
        if not values or values[-1] != 0:
            raise ValueError("unterminated proof step")
        steps.append((deletion, values[:-1]))
    return steps


def assign_literal(values: dict[int, bool], literal: int) -> bool:
    variable = abs(literal)
    wanted = literal > 0
    if variable in values:
        return values[variable] == wanted
    values[variable] = wanted
    return True


def rup(clauses: list[tuple[int, ...]], candidate: tuple[int, ...]) -> bool:
    # Candidate C is RUP iff F and all negations of C unit-propagate to a
    # contradiction.  Tautological C is automatically entailed.
    if any(-q in candidate for q in candidate):
        return True
    values: dict[int, bool] = {}
    for q in candidate:
        if not assign_literal(values, -q):
            return True
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            satisfied = False
            open_literals = []
            for q in clause:
                value = values.get(abs(q))
                if value is None:
                    open_literals.append(q)
                elif value == (q > 0):
                    satisfied = True
                    break
            if satisfied:
                continue
            if not open_literals:
                return True
            if len(open_literals) == 1:
                if not assign_literal(values, open_literals[0]):
                    return True
                changed = True
    return False


def remove_one(active: list[tuple[int, ...]], clause: tuple[int, ...]) -> bool:
    target = collections.Counter(clause)
    for index, current in enumerate(active):
        if collections.Counter(current) == target:
            active.pop(index)
            return True
    return False


def check_one(base: list[tuple[int, ...]], assumptions: list[int], path: Path) -> dict[str, object]:
    active = list(base) + [(q,) for q in assumptions]
    steps = parse_trace(path)
    additions = deletions = 0
    empty_added = False
    first_non_rup = None
    missing_deletions = 0
    for index, (deletion, clause) in enumerate(steps, start=1):
        if deletion:
            deletions += 1
            if not remove_one(active, clause):
                missing_deletions += 1
            continue
        additions += 1
        if not rup(active, clause):
            first_non_rup = index
            break
        active.append(clause)
        if not clause:
            empty_added = True
            break
    verified = first_non_rup is None and empty_added
    return {
        "proof_path": str(path),
        "proof_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "proof_steps": len(steps),
        "additions_checked": additions,
        "deletions_processed": deletions,
        "missing_deletions": missing_deletions,
        "first_non_rup_step": first_non_rup,
        "empty_clause_rup_added": empty_added,
        "verified_all_rup_unsat": verified,
        "verdict": "PASS" if verified else "UNDECIDED",
    }


def check_units_only(base: list[tuple[int, ...]], assumptions: list[int]) -> dict[str, object]:
    active = list(base) + [(q,) for q in assumptions]
    verified = rup(active, ())
    return {
        "proof_path": None,
        "proof_sha256": None,
        "proof_steps": 0,
        "additions_checked": 0,
        "deletions_processed": 0,
        "missing_deletions": 0,
        "first_non_rup_step": None,
        "empty_clause_rup_added": verified,
        "verified_all_rup_unsat": verified,
        "certificate_kind": "direct unit-propagation contradiction in base CNF plus cube units",
        "verdict": "PASS" if verified else "UNDECIDED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--proof-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    _, base = parse_cnf(args.cnf)
    manifest = json.loads(args.proof_manifest.read_text(encoding="utf-8"))
    results = []
    for record in manifest["records"]:
        checked = check_one(base, record["assumption_literals"], Path(record["proof_path"])) if record["proof_path"] else check_units_only(base, record["assumption_literals"])
        results.append({
            "order": record["order"],
            "solver_status": record["status"],
            "assumption_literals": record["assumption_literals"],
            **checked,
        })
    passed = sum(r["verified_all_rup_unsat"] for r in results)
    result = {
        "schema": "round3_lower_independent_all_rup_check_v1",
        "checker_scope": "RUP additions and deletion bookkeeping; RAT is deliberately unsupported",
        "input_cnf_sha256": hashlib.sha256(args.cnf.read_bytes()).hexdigest(),
        "proof_manifest_sha256": hashlib.sha256(args.proof_manifest.read_bytes()).hexdigest(),
        "proofs_present": len(results),
        "proofs_verified_all_rup": passed,
        "all_present_proofs_verified": passed == len(results),
        "records": results,
        "global_n21_verdict": "UNDECIDED because this package targets only 33 of 81 cubes",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("proofs_present", "proofs_verified_all_rup", "all_present_proofs_verified", "global_n21_verdict")}, indent=2))
    return 0 if result["all_present_proofs_verified"] and results else 2


if __name__ == "__main__":
    raise SystemExit(main())
