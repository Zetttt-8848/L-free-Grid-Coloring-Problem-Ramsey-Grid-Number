#!/usr/bin/env python3
"""Enumerate the exact internal-repair profile and single-mark resonances.

The primary geometry uses horizontal pairs and the physical L definition.
No solver or third-party Python package is required. The analytic boundary
inequality is proved in README.md; this program checks its finite input.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import platform
import time

Q = (0, 1, 5, 6, 25, 26, 30, 31)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def geometry(marks):
    marks = sorted(marks)
    cells = [(v, u) for v in marks for u in marks if u < v]
    index = {p: i for i, p in enumerate(cells)}
    corners = []
    for u in marks:
        for x, v in combinations([a for a in marks if a > u], 2):
            r = (v, u + v - x)
            if r in index:
                corners.append((index[x, u], index[v, u], index[r]))
    return cells, corners


def enumerate_profile():
    cells, corners = geometry(Q)
    fibers = defaultdict(list)
    for i, (v, u) in enumerate(cells):
        fibers[v - u].append(i)
    fiber_data = [(sum(1 << i for i in indices), len(indices), indices)
                  for indices in fibers.values()]
    masks = [sum(1 << i for i in corner) for corner in corners]
    incident = [[] for _ in cells]
    for corner, mask in zip(corners, masks):
        for i in corner:
            incident[i].append(mask)
    # Different search order from independent_budget.py; no symmetry quotient.
    order = sorted(range(len(cells)), key=lambda i: (-len(incident[i]), i))
    histogram = defaultdict(Counter)
    witnesses = {}
    minima = {}
    phi_histogram = Counter()
    leaves = 0

    def leaf(word):
        nonlocal leaves
        leaves += 1
        phi = a = b = 0
        candidates = []
        for mask, size, indices in fiber_data:
            s = size - 2 * (word & mask).bit_count()
            phi += s * s
            if size == 4:
                require(abs(s) < 4, "Monochromatic primitive fiber")
                a += int(s != 0)
            if size == 2:
                b += int(s != 0)
            for i in indices:
                sign = 1 - 2 * ((word >> i) & 1)
                if sign * s <= 1:
                    continue
                flipped = word ^ (1 << i)
                if all(0 < (flipped & c) < c for c in incident[i]):
                    candidates.append(i)
        k = (phi - 4) // 4
        count = len(candidates)
        require(phi == 4 + 4 * (a + b), "Unbalanced fiber identity")
        require(count >= a + max(0, 2 * b - 2 * a), "Analytic candidate bound")
        require(3 * count >= 2 * k, "Finite proportional bound")
        histogram[k][count] += 1
        phi_histogram[phi] += 1
        if k not in minima or count < minima[k]:
            minima[k] = count
            witnesses[k] = {"word": word, "phi": phi, "a": a, "b": b,
                            "candidate_cells": [cells[i] for i in candidates],
                            "rows": ["".join(str((word >> i) & 1) for i, (v, u) in enumerate(cells)
                                               if v == mark) for mark in Q[1:]]}

    def visit(depth, assigned, word):
        if depth == len(cells):
            leaf(word)
            return
        i = order[depth]
        bit = 1 << i
        assigned |= bit
        for new in (word, word | bit):
            if all((c & assigned) != c or 0 < (new & c) < c for c in incident[i]):
                visit(depth + 1, assigned, new)

    visit(0, 0, 0)
    require(set(minima) == set(range(10)), "Missing potential stratum")
    require(minima[6] == 4, "Sharp ratio witness")
    return {"proper_colorings": leaves,
            "min_candidates_by_k": dict(sorted(minima.items())),
            "histogram_by_k": {k: dict(sorted(h.items())) for k, h in sorted(histogram.items())},
            "phi_histogram": dict(sorted(phi_histogram.items())),
            "minimizer_witnesses": dict(sorted(witnesses.items()))}


def resonance_geometry():
    qcells, qcorners = geometry(Q)
    qset = set(qcells)
    old = {tuple(qcells[i] for i in corner) for corner in qcorners}
    candidates = ({x + y - z for x, y, z in product(Q, repeat=3)}
                  | {(x + y) // 2 for x, y in product(Q, repeat=2) if (x + y) % 2 == 0}) - set(Q)
    data = []
    for t in sorted(candidates):
        cells, corners = geometry((*Q, t))
        new = [tuple(cells[i] for i in c) for c in corners
               if tuple(cells[i] for i in c) not in old]
        intersections = Counter(sum(p in qset for p in c) for c in new)
        require(set(intersections) <= {1, 2}, "Unexpected boundary intersection")
        require(new, "Unused resonance candidate in this example")
        data.append({"new_mark": t, "new_corners": len(new),
                     "intersection_histogram": dict(sorted(intersections.items()))})
    # Additional bounded sanity check; the all-integer exclusion is analytic.
    for t in range(-100, 101):
        if t not in Q and t not in candidates:
            _, corners = geometry((*Q, t))
            require(len(corners) == len(qcorners), "Corner outside resonance candidates")
    return {"candidate_count": len(candidates), "minimum": min(candidates),
            "maximum": max(candidates), "entries": data,
            "noncandidate_sanity_check_interval": [-100, 100],
            "scope": "Candidate formula is proved necessary in README; exact list and incidence counts apply to displayed Q."}


def check_boundary_witness():
    path = Path(__file__).with_name("witness.json")
    witness = json.loads(path.read_text())
    require(tuple(witness["Q"]) == Q, "Witness uses a different cube")
    cells, corners = geometry((*Q, *witness["added_marks"]))
    colors = [int(c) for row in witness["trap_rows"] for c in row]
    require(len(colors) == len(cells), "Incomplete boundary witness")
    require(all(len({colors[i] for i in c}) == 2 for c in corners), "Improper boundary witness")
    qcells, qcorners = geometry(Q)
    qindices = [cells.index(p) for p in qcells]
    internal = set(qindices)
    fibers = defaultdict(list)
    for i in qindices:
        v, u = cells[i]
        fibers[v - u].append(i)
    phi = sum(sum(1 - 2 * colors[i] for i in f) ** 2 for f in fibers.values())
    only_q = [tuple(qindices[i] for i in c) for c in qcorners]
    candidates = set()
    survivors = set()
    for i in qindices:
        f = fibers[cells[i][0] - cells[i][1]]
        s = sum(1 - 2 * colors[j] for j in f)
        if 4 * (1 - (1 - 2 * colors[i]) * s) >= 0:
            continue
        changed = colors.copy()
        changed[i] ^= 1
        if all(len({changed[j] for j in c}) == 2 for c in only_q):
            candidates.add(i)
            if all(len({changed[j] for j in c}) == 2 for c in corners):
                survivors.add(i)
    critical = []
    relevant = []
    for corner in corners:
        if set(corner) <= internal or not set(corner) & internal:
            continue
        counts = Counter(colors[i] for i in corner)
        minority = next(i for i in corner if counts[colors[i]] == 1)
        if minority in internal:
            critical.append(corner)
        if minority in candidates:
            relevant.append(corner)
    require(len(candidates) - len(survivors) <= len(relevant), "Boundary covering bound")
    require(phi <= 4 + 6 * (len(relevant) + len(survivors)), "Finite-assisted boundary budget")
    return {"witness_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "phi_Q": phi, "I_Q": [cells[i] for i in sorted(candidates)],
            "J_Q": [cells[i] for i in sorted(survivors)],
            "B_Q": len(critical), "B_Q_I": len(relevant),
            "relevant_boundary_corners": [[cells[i] for i in c] for c in relevant],
            "analytic_upper_bound": 4 + 8 * (len(relevant) + len(survivors)),
            "finite_assisted_upper_bound": 4 + 6 * (len(relevant) + len(survivors))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("budget_results.json"))
    parser.add_argument("--independent-report", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    profile = enumerate_profile()
    previous_path = Path(__file__).parent.parent / "three_cube_forcing" / "results.json"
    previous = json.loads(previous_path.read_text())["enumeration"]
    normalized = json.loads(json.dumps(profile))
    require(profile["proper_colorings"] == previous["proper_colorings"], "Previous total mismatch")
    require(normalized["phi_histogram"] == previous["phi_histogram"], "Previous distribution mismatch")
    report = {"status": "PASS", "python": platform.python_version(),
              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "previous_report_sha256": hashlib.sha256(previous_path.read_bytes()).hexdigest(),
              "marks": Q, "profile": profile, "single_mark_geometry": resonance_geometry(),
              "boundary_witness_budget": check_boundary_witness(),
              "scope": "All proper colorings of displayed Q; transfer to positive 2-dissociated cubes uses the proved labeled-constraint isomorphism. No global source or Ramsey bound."}
    if args.independent_report:
        independent = json.loads(args.independent_report.read_text())
        require(profile["proper_colorings"] == independent["count"], "Independent total mismatch")
        require(normalized["min_candidates_by_k"] == independent["min_by_k"], "Independent minima mismatch")
        require(normalized["histogram_by_k"] == independent["hist_by_k"], "Independent joint histogram mismatch")
        report["independent_cross_check"] = {"status": "PASS",
            "report_sha256": hashlib.sha256(args.independent_report.read_bytes()).hexdigest(),
            "fields": ["count", "all minima", "full joint histogram"]}
    report["elapsed_seconds"] = round(time.monotonic() - started, 3)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "proper_colorings": profile["proper_colorings"],
                      "min_candidates_by_k": profile["min_candidates_by_k"],
                      "resonance_candidates": report["single_mark_geometry"]["candidate_count"],
                      "elapsed_seconds": report["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
