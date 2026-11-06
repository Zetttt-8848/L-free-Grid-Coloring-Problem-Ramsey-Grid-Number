#!/usr/bin/env python3
"""Independently enumerate a pinned boundary and certify exact repair barriers.

Standard library only. Geometry is built by equal-offset pairs and independently
compared with physical horizontal pairs. All free cells are exhaustively assigned;
the search program's state list and reachability results are never trusted.
"""

import argparse
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
import hashlib
import heapq
from itertools import combinations
import json
from pathlib import Path
import platform
import time


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(witness):
    require(witness["schema_version"] == 1, "Unknown schema")
    q = witness["Q"]
    require(q == sorted(set(q)) and len(q) == 8, "Expected eight distinct sorted marks")
    require(witness["added_mark"] not in q, "Added mark already in Q")
    marks = sorted(q + [witness["added_mark"]])
    cells = [(v, u) for v in marks for u in marks if u < v]
    index = {p: i for i, p in enumerate(cells)}
    qcells = [(v, u) for v in q for u in q if u < v]
    internal = [index[p] for p in qcells]
    outside = sorted(set(range(len(cells))) - set(internal))
    fibers = defaultdict(list)
    for i, (v, u) in enumerate(cells):
        fibers[v - u].append(i)
    corners = []
    for d, indices in fibers.items():
        for p, r in combinations(sorted(indices, key=lambda i: cells[i][1]), 2):
            corners.append((p, index[cells[r][0], cells[p][1]], r))
    physical = []
    for u in marks:
        for x, v in combinations([a for a in marks if a > u], 2):
            r = (v, u + v - x)
            if r in index:
                physical.append((index[x, u], index[v, u], index[r]))
    require(set(corners) == set(physical) and len(set(corners)) == len(corners),
            "Independent corner geometry mismatch")
    masks = [sum(1 << i for i in c) for c in corners]
    incident = [[] for _ in cells]
    for corner, mask in zip(corners, masks):
        for i in corner:
            incident[i].append(mask)

    def parse(rows):
        require(len(rows) == len(marks) - 1, "Missing row")
        require(all(isinstance(r, str) and len(r) == k and not set(r) - {"0", "1"}
                    for k, r in enumerate(rows, 1)), "Bad row")
        return sum(int(b) << i for i, b in enumerate("".join(rows)))

    start_full, target_full = parse(witness["trap_rows"]), parse(witness["balanced_rows"])
    ext_mask = sum(1 << i for i in outside)
    fixed = start_full & ext_mask
    require((target_full & ext_mask) == fixed, "Balanced witness changes boundary")

    def proper(word):
        return all(0 < (word & c) < c for c in masks)

    require(proper(start_full) and proper(target_full), "Improper supplied coloring")

    def compress(word):
        return sum(((word >> p) & 1) << i for i, p in enumerate(internal))

    def expand(word):
        return fixed | sum(((word >> i) & 1) << p for i, p in enumerate(internal))

    qfibers = defaultdict(list)
    for i, (v, u) in enumerate(qcells):
        qfibers[v - u].append(i)
    fmasks = [(sum(1 << i for i in f), len(f)) for f in qfibers.values()]

    def phi(word):
        return sum((size - 2 * (word & mask).bit_count()) ** 2 for mask, size in fmasks)

    parity_bound = sum(size % 2 for _, size in fmasks)
    require(parity_bound == 4 and phi(compress(target_full)) == parity_bound, "Not a balanced target")
    # Fixed exterior bits are assigned first. A branch is rejected only after
    # all three vertices of an actual L are assigned the same color.
    order = sorted(internal, key=lambda i: (-len(incident[i]), i))
    states = []
    visits = 0

    def dfs(depth, assigned, word):
        nonlocal visits
        visits += 1
        if depth == len(order):
            require(proper(word), "Enumeration accepted an improper state")
            states.append(compress(word))
            return
        i = order[depth]
        assigned |= 1 << i
        for new in (word, word | (1 << i)):
            if all((c & assigned) != c or 0 < (new & c) < c for c in incident[i]):
                dfs(depth + 1, assigned, new)

    require(all((c & ext_mask) != c or 0 < (fixed & c) < c for c in masks), "Improper fixed exterior")
    dfs(0, ext_mask, fixed)
    states.sort()
    require(len(states) == len(set(states)), "Duplicate assignments")
    ids = {s: i for i, s in enumerate(states)}
    potentials = [phi(s) for s in states]
    start = ids[compress(start_full)]
    goals = {i for i, p in enumerate(potentials) if p == parity_bound}
    require(goals and start not in goals, "Missing nonoptimal start or targets")
    # All candidate edges are compared directly between the complete legal
    # states, so no cutoff on the number of flipped coordinates is hidden.
    distances = [bytearray((s ^ t).bit_count() for t in states) for s in states]

    def closure(radius, monotone):
        parent = {start: None}
        queue = deque([start])
        first_goal = None
        while queue:
            i = queue.popleft()
            if i in goals and first_goal is None:
                first_goal = i
            for j, d in enumerate(distances[i]):
                if j in parent or d > radius:
                    continue
                if monotone and potentials[j] > potentials[i]:
                    continue
                parent[j] = i
                queue.append(j)
        return parent, first_goal

    def trace(parent, last):
        path = []
        while last is not None:
            path.append(last)
            last = parent[last]
        return list(reversed(path))

    def describe(i):
        full = expand(states[i])
        return {"q_word": states[i], "full_word": full, "phi_Q": potentials[i],
                "rows": ["".join(str((full >> j) & 1) for j, (v, u) in enumerate(cells) if v == a)
                         for a in marks[1:]]}

    def describe_path(path):
        return {"states": [describe(i) for i in path],
                "flipped_cells": [[qcells[k] for k in range(len(qcells))
                                   if ((states[i] ^ states[j]) >> k) & 1]
                                  for i, j in zip(path, path[1:])],
                "block_sizes": [distances[i][j] for i, j in zip(path, path[1:])]}

    monotone = {}
    minimum_monotone = None
    monotone_path = []
    for radius in range(1, len(qcells) + 1):
        parents, goal = closure(radius, True)
        monotone[radius] = {"state_count": len(parents),
                           "phi_histogram": dict(sorted(Counter(potentials[i] for i in parents).items())),
                           "contains_balanced_state": goal is not None,
                           "q_words": sorted(states[i] for i in parents)}
        if goal is not None:
            minimum_monotone = radius
            monotone_path = trace(parents, goal)
            break
    require(minimum_monotone is not None, "No repair despite balanced target")

    unrestricted = {}
    minimum_unrestricted = None
    unrestricted_path = []
    for radius in range(1, minimum_monotone + 1):
        parents, goal = closure(radius, False)
        unrestricted[radius] = {"state_count": len(parents),
                               "phi_histogram": dict(sorted(Counter(potentials[i] for i in parents).items())),
                               "contains_balanced_state": goal is not None,
                               "q_words": sorted(states[i] for i in parents)}
        if goal is not None:
            minimum_unrestricted = radius
            unrestricted_path = trace(parents, goal)
            break

    # Among paths using the smallest unrestricted block radius, find the exact
    # minimum peak Phi_Q; Dijkstra replaces addition by max in its path cost.
    best = {start: potentials[start]}
    parents = {start: None}
    heap = [(potentials[start], start)]
    reached_goal = None
    while heap:
        cost, i = heapq.heappop(heap)
        if cost != best[i]:
            continue
        if i in goals:
            reached_goal = i
            break
        for j, d in enumerate(distances[i]):
            if not 0 < d <= minimum_unrestricted:
                continue
            candidate = max(cost, potentials[j])
            if candidate < best.get(j, float("inf")):
                best[j] = candidate
                parents[j] = i
                heapq.heappush(heap, (candidate, j))
    require(reached_goal is not None, "Unrestricted path contradiction")
    peak_path = trace(parents, reached_goal)
    nearest = min(goals, key=lambda i: (distances[start][i], states[i]))
    cut_words = set(unrestricted[2]["q_words"])
    cut_side = [i for i, s in enumerate(states) if s in cut_words]
    cut_other = [i for i, s in enumerate(states) if s not in cut_words]
    require(cut_other and not goals.intersection(cut_side), "Invalid separation cut")
    cut_distance, cut_i, cut_j = min((distances[i][j], i, j) for i in cut_side for j in cut_other)
    counts = {"source_cells": len(cells), "source_corners": len(corners),
              "same_boundary_legal_count": len(states), "balanced_count": len(goals),
              "trap_phi_Q": potentials[start],
              "two_flip_nonincreasing_closure": monotone[2]["state_count"],
              "two_flip_unrestricted_component": unrestricted[2]["state_count"],
              "nearest_balance_hamming": distances[start][nearest],
              "minimum_monotone_block_size": minimum_monotone,
              "minimum_unrestricted_block_size": minimum_unrestricted,
              "minimum_peak_at_unrestricted_minimum_radius": best[reached_goal]}
    for key, value in witness.get("expected", {}).items():
        require(counts[key] == value, "Unexpected count: " + key)
    return {"status": "FINITE-CHECKED", "Q": q, "marks": marks,
            "counts": counts, "all_legal_q_words": states,
            "all_legal_phi_histogram": dict(sorted(Counter(potentials).items())),
            "enumeration_node_count": visits, "cells": cells,
            "corners": [[cells[i] for i in c] for c in corners],
            "fixed_boundary_colors": [[*cells[i], (fixed >> i) & 1] for i in outside],
            "trap": describe(start), "balanced_witness": describe(ids[compress(target_full)]),
            "nearest_balance": describe(nearest),
            "cut_certificate": {
                "side_is": "unrestricted_components_by_max_block_size[2].q_words",
                "side_count": len(cut_side), "complement_count": len(cut_other),
                "balanced_targets_on_side": 0,
                "minimum_cross_cut_hamming": cut_distance,
                "cross_cut_pair": [describe(cut_i), describe(cut_j)],
                "all_cross_cut_pairs_checked": len(cut_side) * len(cut_other)},
            "monotone_closures_by_max_block_size": monotone,
            "unrestricted_components_by_max_block_size": unrestricted,
            "shortest_minimum_radius_monotone_path": describe_path(monotone_path),
            "shortest_minimum_radius_unrestricted_path": describe_path(unrestricted_path),
            "minimum_peak_path_at_unrestricted_minimum_radius": describe_path(peak_path),
            "scope": "Complete displayed frozen-boundary group only. This refutes universal two-cell repair; the radii and peak values are exact for this witness, not universal bounds."}


def main():
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness", type=Path, default=directory / "witness.json")
    parser.add_argument("--output", type=Path, default=directory / "verification_results.json")
    args = parser.parse_args()
    started = time.monotonic()
    raw = args.witness.read_bytes()
    report = verify(json.loads(raw))
    report["provenance"] = {"python": platform.python_version(),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "witness_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.monotonic() - started, 3)}
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "counts": report["counts"],
                      "elapsed_seconds": report["provenance"]["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
