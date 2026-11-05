#!/usr/bin/env python3
"""Independent exact audit of Round-3 joint-core certificates.

This file deliberately imports no claimant code.  It rebuilds the strict
completion geometry, CNFs, RUP checks, window classification, affine-copy
catalogue, and literal witness predicates from the definitions in the report.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import reduce
from hashlib import sha256
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
J = ROOT / "joint"
H = (0, 1, 2, 4, 7, 12, 18, 26, 35, 45, 56, 73, 86,
     107, 128, 152, 178, 200, 217, 247, 284, 334, 357, 373,
     426, 481, 493, 554, 586)


def load(name: str):
    with (J / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def cells_for(marks):
    marks = sorted(marks)
    return [(x, y) for yi, y in enumerate(marks) for x in marks[yi + 1 :]]


def corners_for(marks):
    """All additive rectangles y,y+d,x,x+d in the strict triangle."""
    marks = sorted(marks)
    support = set(marks)
    out = []
    for d in range(1, marks[-1] - marks[0] + 1):
        for y in marks:
            if y + d not in support:
                continue
            for x in marks:
                if x > y and x + d in support:
                    out.append((x, y, d))
    return out


def cnf_for(marks):
    cells = cells_for(marks)
    number = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for x, y, d in corners_for(marks):
        variables = [number[(x, y)], number[(x + d, y)], number[(x + d, y + d)]]
        clauses.append(variables)
        clauses.append([-v for v in variables])
    clauses.append([1])  # complete color-complement symmetry pin
    return cells, clauses


def parse_dimacs(path: Path):
    nvars = nclauses = None
    clauses = []
    pending = []
    for raw in path.read_text(encoding="ascii").splitlines():
        line = raw.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            _, kind, nv, nc = line.split()
            assert kind == "cnf"
            nvars, nclauses = int(nv), int(nc)
            continue
        for token in map(int, line.split()):
            if token == 0:
                clauses.append(pending)
                pending = []
            else:
                pending.append(token)
    assert not pending and nvars is not None and nclauses == len(clauses)
    return nvars, clauses


def parse_rup(path: Path):
    clauses = []
    pending = []
    for raw in path.read_text(encoding="ascii").splitlines():
        line = raw.strip()
        if not line or line.startswith("c"):
            continue
        for token in map(int, line.split()):
            if token == 0:
                clauses.append(pending)
                pending = []
            else:
                pending.append(token)
    assert not pending
    return clauses


def clause_key(clause):
    return tuple(sorted(clause))


def unit_conflict(clauses, assumptions):
    """Plain unit propagation; returns True exactly on a found conflict."""
    assignment = {}

    def force(lit):
        var, val = abs(lit), lit > 0
        old = assignment.get(var)
        if old is not None:
            return old != val
        assignment[var] = val
        return False

    for lit in assumptions:
        if force(lit):
            return True
    while True:
        changed = False
        for clause in clauses:
            satisfied = False
            unassigned = []
            for lit in clause:
                val = assignment.get(abs(lit))
                if val is None:
                    unassigned.append(lit)
                elif val == (lit > 0):
                    satisfied = True
                    break
            if satisfied:
                continue
            if not unassigned:
                return True
            if len(unassigned) == 1:
                if force(unassigned[0]):
                    return True
                changed = True
        if not changed:
            return False


def verify_rup(base, proof):
    working = [list(c) for c in base]
    for line_no, addition in enumerate(proof, 1):
        if not unit_conflict(working, [-lit for lit in addition]):
            return False, line_no
        working.append(list(addition))
    return bool(proof and proof[-1] == []), None


def assignment_satisfies(clauses, colors):
    for clause in clauses:
        if not any(colors[abs(lit) - 1] == (lit > 0) for lit in clause):
            return False
    return True


def no_k_ap(marks, n, k):
    support = set(marks)
    groups = 0
    violations = []
    per_step = []
    for d in range(1, (n - 1) // (k - 1) + 1):
        contained = []
        for a in range(1, n - (k - 1) * d + 1):
            groups += 1
            if all(a + j * d in support for j in range(k)):
                contained.append(a)
        per_step.append(len(contained))
        if k == 6 and contained:
            violations.extend((a, d) for a in contained)
        if k == 5 and len(contained) > 1:
            violations.append((d, contained))
    return groups, per_step, violations


def difference_profile(marks, n):
    profile = [0] * n
    for i, a in enumerate(marks):
        for b in marks[i + 1 :]:
            profile[b - a] += 1
    return profile


def caps_for(n):
    out = []
    for d in range(1, n):
        j = max(i for i, height in enumerate(H) if height <= n - d)
        out.append(2 * j)
    return out


def normalized(marks):
    marks = sorted(marks)
    shifted = [x - marks[0] for x in marks]
    g = reduce(math.gcd, shifted)
    return tuple(x // g for x in shifted)


def affine_copy_check(marks, patterns, n):
    support = set(marks)
    count = 0
    violations = []
    for p_index, pattern in enumerate(patterns):
        span = pattern[-1]
        for h in range(1, (n - 1) // span + 1):
            for start in range(1, n - h * span + 1):
                count += 1
                if all(start + h * off in support for off in pattern):
                    violations.append((p_index, start, h))
    return count, violations


def block_starts(support, offsets, h, n):
    return [a for a in range(1, n - h * max(offsets) + 1)
            if all(a + h * off in support for off in offsets)]


def first_parametric_check(marks, n):
    support = set(marks)
    Loff, Koff, Joff = (0, 1, 2, 4, 5, 6), (0, 3, 4, 5), (0, 1, 2, 5)
    forward = []
    reflected = []
    start_counts = {"L": 0, "K": 0, "J": 0}
    for h in range(1, (n - 2) // 11 + 1):
        L = block_starts(support, Loff, h, n)
        K = block_starts(support, Koff, h, n)
        JJ = block_starts(support, Joff, h, n)
        start_counts["L"] += len(L)
        start_counts["K"] += len(K)
        start_counts["J"] += len(JJ)
        forward.extend((h, i, z) for i in L for z in K if z > i + 6 * h)
        reflected.extend((h, y, i) for y in JJ for i in L if i > y + 5 * h)
    return start_counts, forward, reflected


def coefficient_audit(tag, literal_marks, mapping, separation):
    """Check every source corner as a polynomial identity and all order gaps."""
    corners = corners_for(literal_marks)

    def sub(a, b):
        return tuple(x - y for x, y in zip(a, b))

    identities = []
    for x, y, d in corners:
        lhs = sub(mapping[y + d], mapping[y])
        rhs = sub(mapping[x + d], mapping[x])
        identities.append(lhs == rhs)

    ordered = sorted(literal_marks)
    positive = []
    for lo, hi in zip(ordered, ordered[1:]):
        dx, dh, db = sub(mapping[hi], mapping[lo])
        assert dx == 0
        # b is unbounded above, so db must be nonnegative.  Its minimum is
        # b=separation*h+1; h>=1.
        if db < 0:
            positive.append(False)
        else:
            hcoef = dh + separation * db
            positive.append(hcoef > 0 or (hcoef == 0 and db > 0))
    return {
        "tag": tag,
        "corners": len(corners),
        "all_identities": all(identities),
        "all_adjacent_gaps_positive": all(positive),
    }


def main():
    failures = []

    # The four standalone triangle refutations.
    triangle_results = []
    for tag in ("triangle_core", "triangle_core_v2", "triangle_core_v3", "triangle_core_v4"):
        meta = load(tag + ".json")
        marks = meta["marks"]
        cells, expected = cnf_for(marks)
        nvars, actual = parse_dimacs(J / (tag + ".cnf"))
        proof = parse_rup(J / (tag + ".rup"))
        rup_ok, bad_line = verify_rup(expected, proof)
        checks = {
            "cells_rebuilt": [list(x) for x in cells] == meta["cells"],
            "corners_rebuilt": [list(x) for x in corners_for(marks)] == meta["corners"],
            "cnf_rebuilt": nvars == len(cells) and Counter(map(clause_key, actual)) == Counter(map(clause_key, expected)),
            "clause_count": len(expected) == meta["clause_count"],
            "rup_valid": rup_ok,
        }
        if not all(checks.values()):
            failures.append({"triangle": tag, "checks": checks, "bad_rup_line": bad_line})
        triangle_results.append({
            "tag": tag,
            "marks": len(marks),
            "cells": len(cells),
            "corners": len(corners_for(marks)),
            "clauses": len(expected),
            "rup_additions": len(proof),
            "checks": checks,
            "cnf_sha256": file_hash(J / (tag + ".cnf")),
            "rup_sha256": file_hash(J / (tag + ".rup")),
        })

    # Complete width-13 certificate, reconstructed from the raw masks.
    window = load("window13.json")
    assert window["width"] == 13 and len(window["status"]) == 8192
    status = window["status"]
    minimal = window["minimal_bad"]
    maximal = window["maximal_good"]
    min_masks = [item["mask"] for item in minimal]
    max_masks = [item["mask"] for item in maximal]
    rup_total = 0
    bad_proofs_ok = True
    external_files_ok = True
    proof_failures = []
    for item in minimal:
        mask = item["mask"]
        marks = [i for i in range(13) if mask >> i & 1]
        cells, base = cnf_for(marks)
        proof = item["proof"]
        ok, bad_line = verify_rup(base, proof)
        rup_total += len(proof)
        if not ok:
            bad_proofs_ok = False
            proof_failures.append((mask, bad_line))
        nvars, disk_cnf = parse_dimacs(J / "window13" / f"bad_{mask}.cnf")
        disk_rup = parse_rup(J / "window13" / f"bad_{mask}.rup")
        if not (nvars == len(cells)
                and Counter(map(clause_key, disk_cnf)) == Counter(map(clause_key, base))
                and disk_rup == proof):
            external_files_ok = False
    good_colorings_ok = True
    for item in maximal:
        marks = [i for i in range(13) if item["mask"] >> i & 1]
        cells, clauses = cnf_for(marks)
        colors = [bool(x) for x in item["colors"]]
        if len(colors) != len(cells) or not assignment_satisfies(clauses, colors):
            good_colorings_ok = False

    derived_status = []
    exclusive = True
    for mask in range(8192):
        bad_cover = any(mask & m == m for m in min_masks)
        good_cover = any(mask & m == mask for m in max_masks)
        exclusive &= bad_cover != good_cover
        derived_status.append(good_cover and not bad_cover)
    minimality = all(not status[m] and all(status[m ^ (1 << bit)] for bit in range(13) if m >> bit & 1)
                     for m in min_masks)
    maximality = all(status[m] and all(not status[m | (1 << bit)] for bit in range(13) if not (m >> bit & 1))
                     for m in max_masks)
    capacities = {}
    for width in range(1, 14):
        capacities[str(width)] = max(mask.bit_count() for mask in range(1 << width) if status[mask])
    window_checks = {
        "all_8192_covered_exclusively": exclusive and derived_status == status,
        "counts": sum(status) == 7147 and len(status) - sum(status) == 1045,
        "109_minimal_bad": len(minimal) == 109 and len(set(min_masks)) == 109 and minimality,
        "334_maximal_good": len(maximal) == 334 and len(set(max_masks)) == 334 and maximality,
        "all_bad_rup": bad_proofs_ok,
        "external_cnf_rup_match": external_files_ok,
        "all_good_colorings": good_colorings_ok,
        "rup_additions": rup_total == 31605,
        "capacities": capacities == window["capacities"],
    }
    if not all(window_checks.values()):
        failures.append({"window13": window_checks, "proof_failures": proof_failures})

    # Derive the 56 normalized patterns from the 109 labeled minimal bad masks.
    catalogue = load("patterns_window13.json")
    derived_groups = defaultdict(list)
    for item in minimal:
        derived_groups[normalized(item["marks"])].append(item["mask"])
    patterns = [tuple(p) for p in catalogue["patterns"]]
    source_map = {key: value for key, value in catalogue["source_masks"].items()}
    source_map_expected = {str(key): value for key, value in derived_groups.items()}
    catalogue_checks = {
        "56_unique_normalized_patterns": len(patterns) == len(set(patterns)) == len(derived_groups) == 56,
        "pattern_set_rebuilt": set(patterns) == set(derived_groups),
        "source_masks_rebuilt": source_map == source_map_expected,
    }
    if not all(catalogue_checks.values()):
        failures.append({"catalogue": catalogue_checks})

    # Base and two strengthened witnesses: all 463 caps and every AP group.
    witness_results = []
    witnesses = [
        "witness_464.json",
        "witness_464_window_ap5.json",
        "witness_464_parametric.json",
    ]
    caps = caps_for(464)
    for name in witnesses:
        data = load(name)
        marks = data["marks"]
        profile = difference_profile(marks, 464)
        cap_bad = [(d, profile[d], caps[d - 1]) for d in range(1, 464) if profile[d] > caps[d - 1]]
        ap6_groups, ap6_per_step, ap6_bad = no_k_ap(marks, 464, 6)
        result = {
            "file": name,
            "literal_set": len(marks) == 155 and len(set(marks)) == 155 and min(marks) == 1 and max(marks) <= 464,
            "caps_checked": 463,
            "cap_violations": cap_bad,
            "ap6_groups": ap6_groups,
            "ap6_step_groups": len(ap6_per_step),
            "ap6_violations": ap6_bad,
            "max_difference_count": max(profile),
        }
        if name != "witness_464.json":
            ap5_groups, ap5_per_step, ap5_bad = no_k_ap(marks, 464, 5)
            copy_count, copy_bad = affine_copy_check(marks, patterns, 464)
            result.update({
                "ap5_groups": ap5_groups,
                "ap5_step_groups": len(ap5_per_step),
                "ap5_max_per_step": max(ap5_per_step),
                "ap5_uniqueness_violations": ap5_bad,
                "affine_copies_checked": copy_count,
                "affine_copy_violations": copy_bad,
            })
        ok = (result["literal_set"] and not cap_bad and not ap6_bad and ap6_groups == 21298)
        if name != "witness_464.json":
            ok &= (not result["ap5_uniqueness_violations"] and result["ap5_groups"] == 26680
                   and result["ap5_step_groups"] == 115 and result["affine_copies_checked"] == 543170
                   and not result["affine_copy_violations"])
        result["pass"] = ok
        if not ok:
            failures.append({"witness": result})
        witness_results.append(result)

    final = load("witness_464_parametric.json")
    starts, forward_bad, reflected_bad = first_parametric_check(final["marks"], 464)
    parametric_literal = {
        "h_values_checked": 42,
        "actual_start_counts": starts,
        "forward_violations": forward_bad,
        "reflected_violations": reflected_bad,
        "larger_h_cannot_fit": 11 * 43 + 1 > 463,
    }
    if forward_bad or reflected_bad or not parametric_literal["larger_h_cannot_fit"]:
        failures.append({"first_parametric_literal": parametric_literal})

    # Coefficientwise transfer of the two fixed triangle cores.
    v3_marks = [2, 3, 4, 6, 7, 8, 22, 25, 26, 27]
    v3_map = {
        2: (1, 0, 0), 3: (1, 1, 0), 4: (1, 2, 0),
        6: (1, 4, 0), 7: (1, 5, 0), 8: (1, 6, 0),
        22: (1, 0, 1), 25: (1, 3, 1), 26: (1, 4, 1), 27: (1, 5, 1),
    }
    v4_marks = [1, 2, 3, 5, 10, 11, 12, 13, 14]
    v4_map = {
        1: (1, 0, 0), 2: (1, 1, 0), 3: (1, 2, 0), 5: (1, 4, 0),
        10: (1, 0, 1), 11: (1, 1, 1), 12: (1, 2, 1),
        13: (1, 3, 1), 14: (1, 4, 1),
    }
    coefficient_results = [
        coefficient_audit("first_family_v3", v3_marks, v3_map, 6),
        coefficient_audit("second_hook_ap5_v4", v4_marks, v4_map, 4),
    ]
    coefficient_results[0]["source_marks_match"] = v3_marks == load("triangle_core_v3.json")["marks"]
    coefficient_results[0]["source_specialization_match"] = [
        2 * a + 1 * b + 20 * c for a, b, c in (v3_map[q] for q in v3_marks)
    ] == v3_marks
    coefficient_results[1]["source_marks_match"] = v4_marks == load("triangle_core_v4.json")["marks"]
    coefficient_results[1]["source_specialization_match"] = [
        1 * a + 1 * b + 9 * c for a, b, c in (v4_map[q] for q in v4_marks)
    ] == v4_marks
    if not all(x["all_identities"] and x["all_adjacent_gaps_positive"]
               and x["source_marks_match"] and x["source_specialization_match"]
               for x in coefficient_results):
        failures.append({"coefficient_audits": coefficient_results})

    latest_support = set(final["marks"])
    second_hook_status = {
        "literal_v4_subset": set(v4_marks) <= latest_support,
        "source_specialization": {"x": 1, "h": 1, "b": 9},
        "latest_witness_satisfies_second_family": False,
        "interpretation": "The saved witness predates the second family and is not a YES for it.",
    }
    if not second_hook_status["literal_v4_subset"]:
        failures.append({"second_hook_status": second_hook_status})

    inputs = ([J / name for name in witnesses]
              + [J / "REPORT.md", J / "property.md", J / "PARAMETRIC_MODEL.md",
                 J / "patterns_window13.json", J / "window13.json"]
              + [J / f"triangle_core{suffix}{ext}"
                 for suffix in ("", "_v2", "_v3", "_v4")
                 for ext in (".json", ".cnf", ".rup")]
              + sorted((J / "window13").glob("*")))
    output = {
        "audit": "R3 core J independent lower_sol review",
        "verdict": "PASS" if not failures else "MAJOR",
        "failures": failures,
        "triangle_refutations": triangle_results,
        "window13": {
            "checks": window_checks,
            "good": sum(status),
            "bad": len(status) - sum(status),
            "minimal_bad": len(minimal),
            "maximal_good": len(maximal),
            "rup_additions": rup_total,
            "capacities": capacities,
        },
        "normalized_catalogue": catalogue_checks,
        "witnesses": witness_results,
        "first_parametric_literal": parametric_literal,
        "coefficient_preservation": coefficient_results,
        "reflection_argument": "Negating every coordinate preserves each equality (y+d)-y=(x+d)-x and reverses the ordered support; hence the same abstract cell CNF and RUP trace apply after relabeling.",
        "second_hook_status": second_hook_status,
        "input_sha256": {str(p.relative_to(ROOT)): file_hash(p) for p in inputs},
    }
    out_path = HERE / "joint_audit.json"
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "verdict": output["verdict"],
        "triangles": [(x["tag"], x["rup_additions"]) for x in triangle_results],
        "window": output["window13"],
        "witness_pass": [x["pass"] for x in witness_results],
        "affine_copies": witness_results[-1]["affine_copies_checked"],
        "parametric_violations": [len(forward_bad), len(reflected_bad)],
    }, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
