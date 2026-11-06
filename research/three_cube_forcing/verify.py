#!/usr/bin/env python3
"""Exact three-cube experiment; Python standard library, no SAT dependency.

The proof of the optimum is in README.md. Enumeration separately verifies
the complete distribution and the single-cell descent statement. Run without
-O. A second, independently encoded C++ enumeration can be cross-checked.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import platform
import time


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source(weights):
    labels = {sum(w for i, w in enumerate(weights) if mask >> i & 1): mask
              for mask in range(8)}
    require(len(labels) == 8, "Noninjective cube")
    marks = sorted(labels)
    cells = [(v, u) for v in marks for u in marks if u < v]
    index = {cell: i for i, cell in enumerate(cells)}
    fibers = defaultdict(list)
    for i, (v, u) in enumerate(cells):
        fibers[v - u].append(i)
    # Primary encoding: every pair of equal-offset inputs has one completion.
    corners = []
    for indices in fibers.values():
        for p, r in combinations(indices, 2):
            v, u = cells[p]
            w, t = cells[r]
            require(u < t and v < w, "Fiber ordering")
            corners.append((p, index[w, u], r))
    # Independent geometric construction: pairs of points in a horizontal row.
    physical = []
    for u in marks:
        for x, v in combinations([a for a in marks if a > u], 2):
            third = (v, u + v - x)
            if third in index:
                physical.append((index[x, u], index[v, u], index[third]))
    require(set(corners) == set(physical), "Geometric/offset encoding mismatch")
    return marks, labels, cells, fibers, sorted(corners)


def make_word(cells, labels, rule):
    return sum(rule(labels[v], labels[u]) << i
               for i, (v, u) in enumerate(cells))


def optimal_rule(a, b):
    return 1 if {a, b} == {0, 7} else (a & b).bit_count() % 2


def old_rule(a, b):
    return int((a == 0 and b.bit_count() in (1, 2))
               or (b == 0 and a.bit_count() in (1, 2))
               or (a == 7 and b.bit_count() == 1)
               or (b == 7 and a.bit_count() == 1)
               or ((a ^ b) == 7 and sorted((a.bit_count(), b.bit_count())) == [1, 2]))


def measure(word, marks, cells, fibers, corners):
    colors = [(word >> i) & 1 for i in range(len(cells))]
    require(all(len({colors[i] for i in c}) == 2 for c in corners),
            "Monochromatic directed L")
    edge_set = set()
    forcing = []
    for p, q, r in corners:
        if colors[p] == colors[r]:
            forcing.append([p, q, r])
            edge_set.update((tuple(sorted((p, q))), tuple(sorted((r, q)))))
    details = []
    for d, indices in sorted(fibers.items()):
        signed_sum = sum(1 - 2 * colors[i] for i in indices)
        details.append({"offset": d, "indices": indices, "size": len(indices),
                        "ones": sum(colors[i] for i in indices), "signed_sum": signed_sum})
    phi = sum(f["signed_sum"] ** 2 for f in details)
    require(2 * len(corners) == len(cells) + 2 * len(edge_set) - phi,
            "Forcing identity mismatch")
    require(len(edge_set) == 2 * len(forcing), "Repeated forcing edge")
    return {"word": word, "rows": ["".join(str(colors[i]) for i, (v, u) in enumerate(cells)
                                           if v == a) for a in marks[1:]],
            "colors": colors, "phi": phi, "forcing_corners": len(forcing),
            "mixed_corners": len(corners) - len(forcing), "forcing_edges": len(edge_set),
            "fiber_details": details, "forcing_corner_indices": forcing}


def enumerate_all(cells, fibers, corners):
    n = len(cells)
    masks = [sum(1 << p for p in c) for c in corners]
    closing = [[] for _ in cells]
    incident = [[] for _ in cells]
    for c, mask in zip(corners, masks):
        closing[max(c)].append(mask)
        for i in c:
            incident[i].append(mask)
    fiber_masks = [(sum(1 << i for i in f), len(f)) for f in fibers.values()]
    cell_fiber = {i: (mask, size) for (mask, size), indices in zip(fiber_masks, fibers.values())
                  for i in indices}
    histogram = Counter()
    local_histogram = Counter()
    delta_histogram = Counter()
    statistics = {"visited_partial_assignments": 0, "rejected_branches": 0,
                  "proper_word_sum": 0, "proper_word_xor": 0}
    witness = {}

    def improving_moves(word):
        out = []
        for i in range(n):
            mask, size = cell_fiber[i]
            s = size - 2 * (word & mask).bit_count()
            sign = 1 - 2 * ((word >> i) & 1)
            delta = 4 * (1 - sign * s)
            if delta >= 0:
                continue
            new = word ^ (1 << i)
            if all(0 < (new & c) < c for c in incident[i]):
                out.append((i, delta))
        return out

    def visit(depth, word):
        statistics["visited_partial_assignments"] += 1
        if depth == n:
            phi = sum((size - 2 * (word & mask).bit_count()) ** 2 for mask, size in fiber_masks)
            histogram[phi] += 1
            statistics["proper_word_sum"] += word
            statistics["proper_word_xor"] ^= word
            moves = improving_moves(word)
            if not moves:
                local_histogram[phi] += 1
            for _, delta in moves:
                delta_histogram[delta] += 1
            witness.setdefault(phi, word)
            return
        for new in (word, word | (1 << depth)):
            if all(0 < (new & c) < c for c in closing[depth]):
                visit(depth + 1, new)
            else:
                statistics["rejected_branches"] += 1

    visit(0, 0)
    require(min(histogram) == 4, "Minimum mismatch")
    require(set(local_histogram) == {4}, "Nonoptimal local minimum found")
    require(set(delta_histogram) == {-4}, "Unexpected decreasing flip")
    summary = {"proper_colorings": sum(histogram.values()),
               "phi_histogram": dict(sorted(histogram.items())),
               "single_flip_local_minimum_histogram": dict(sorted(local_histogram.items())),
               "improving_directed_move_delta_histogram": dict(delta_histogram), **statistics}
    return summary, improving_moves, incident


def labeled_hypergraph(weights):
    marks, labels, cells, fibers, corners = source(weights)
    label = [tuple(sorted((labels[v], labels[u]))) for v, u in cells]
    return {tuple(sorted(label[i] for i in corner)) for corner in corners}


def check_weight_variants():
    reference = labeled_hypergraph((1, 5, 25))
    checked = 0
    # Bounded regression evidence; the README gives the separate general proof.
    for weights in combinations(range(1, 16), 3):
        if any(sum(c * w for c, w in zip(coeff, weights)) == 0
               for coeff in product(range(-2, 3), repeat=3) if coeff != (0, 0, 0)):
            continue
        require(labeled_hypergraph(weights) == reference, "Labeled constraint mismatch")
        for ordered in permutations(weights):
            marks, labels, cells, fibers, corners = source(ordered)
            result = measure(make_word(cells, labels, optimal_rule), marks, cells, fibers, corners)
            require(result["phi"] == 4, "Symbolic rule mismatch")
            checked += 1
    return {"positive_weights_at_most": 15, "ordered_triples_checked": checked,
            "condition": "2-dissociated", "sorted_weight_constraint_systems_equal": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--independent-report", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    marks, labels, cells, fibers, corners = source((1, 5, 25))
    optimum = measure(make_word(cells, labels, optimal_rule), marks, cells, fibers, corners)
    original = measure(make_word(cells, labels, old_rule), marks, cells, fibers, corners)
    require((optimum["phi"], optimum["forcing_edges"]) == (4, 12), "Optimum certificate")
    require((original["phi"], original["forcing_edges"]) == (40, 30), "Original certificate")
    enumeration, moves, incident = enumerate_all(cells, fibers, corners)
    path = []
    word = original["word"]
    while True:
        current = measure(word, marks, cells, fibers, corners)
        choices = moves(word)
        path.append({"word": word, "phi": current["phi"], "rows": current["rows"],
                     "forcing_edges": current["forcing_edges"],
                     "next_flip_index": choices[0][0] if choices else None,
                     "next_flip_cell": cells[choices[0][0]] if choices else None})
        if not choices:
            break
        word ^= 1 << choices[0][0]
    require(len(path) == 10 and path[-1]["phi"] == 4, "Descent path mismatch")
    blocked = []
    word = original["word"]
    for i, cell in enumerate(cells):
        indices = fibers[cell[0] - cell[1]]
        s = sum(1 - 2 * ((word >> j) & 1) for j in indices)
        delta = 4 * (1 - (1 - 2 * ((word >> i) & 1)) * s)
        if delta >= 0:
            continue
        new = word ^ (1 << i)
        bad = [list(c) for c in corners if i in c and len({(new >> j) & 1 for j in c}) == 1]
        if bad:
            blocked.append({"cell": cell, "index": i, "delta_phi": delta,
                            "monochromatic_corner_indices_after_flip": bad})
    report = {"status": "PASS", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "python": platform.python_version(),
              "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "marks": marks, "cells": cells, "corners": corners,
              "M": len(cells), "T": len(corners), "optimal_symbolic_coloring": optimum,
              "manuscript_coloring": original, "enumeration": enumeration,
              "greedy_descent_from_manuscript": path, "blocked_improving_flips_at_manuscript": blocked,
              "weight_variants": check_weight_variants(),
              "scope": "Exact representative enumeration; general optimum and transfer proved separately in README.md. No global source bound or Ramsey improvement."}
    if args.independent_report:
        independent = json.loads(args.independent_report.read_text())
        mapping = {"proper_colorings": "proper_coloring_count", "phi_histogram": "phi_histogram",
                   "single_flip_local_minimum_histogram": "no_strictly_decreasing_legal_single_flip_histogram",
                   "proper_word_sum": "state_sum", "proper_word_xor": "state_xor"}
        require(independent["cells"] == [list(c) for c in cells], "Cell indexing mismatch")
        require(independent["corner_count"] == len(corners), "Corner count mismatch")
        for field, external_field in mapping.items():
            require(json.loads(json.dumps(enumeration[field])) == independent[external_field],
                    "Independent enumeration mismatch: " + field)
        report["independent_cross_check"] = {
            "status": "PASS", "fields": ["count", "histogram", "local minima", "word sum", "word xor"],
            "report_sha256": hashlib.sha256(args.independent_report.read_bytes()).hexdigest(),
            "checker_sha256": hashlib.sha256(Path(__file__).with_name("independent_enumeration.cpp").read_bytes()).hexdigest()}
    report["elapsed_seconds"] = round(time.monotonic() - started, 3)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "minimum_phi": optimum["phi"],
                      "minimum_forcing_edges": optimum["forcing_edges"],
                      "enumeration": enumeration, "elapsed_seconds": report["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
