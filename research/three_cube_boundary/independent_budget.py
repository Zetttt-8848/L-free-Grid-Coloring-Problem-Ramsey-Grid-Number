#!/usr/bin/env python3
"""Enumerate all internally improving flips on the fixed three-cube.

This standard-library checker reuses the earlier source geometry, then performs
its own increasing-cell-order coloring enumeration and budget accounting. A
separate checker using independent geometry and a different variable order can
compare the complete (k, number of improving flips) histogram with this output.
No symmetry quotient or sampled coloring is used.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import time


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_geometry():
    path = Path(__file__).resolve().parent.parent / "three_cube_forcing" / "verify.py"
    spec = importlib.util.spec_from_file_location("three_cube_forcing_geometry", path)
    require(spec is not None and spec.loader is not None, "Cannot load source geometry")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def enumerate_budgets(cells, fibers, corners, marks):
    n = len(cells)
    closing = [[] for _ in cells]
    incident = [[] for _ in cells]
    for corner in corners:
        require(len(set(corner)) == 3, "Degenerate corner")
        mask = sum(1 << i for i in corner)
        closing[max(corner)].append(mask)
        for i in corner:
            incident[i].append(mask)
    fiber_data = [(sum(1 << i for i in indices), len(indices), indices)
                  for indices in fibers.values()]
    histogram = defaultdict(Counter)
    minima = {}
    maxima = {}
    witnesses = {}
    count = 0
    state_sum = 0
    state_xor = 0

    def inspect(word):
        nonlocal count, state_sum, state_xor
        count += 1
        state_sum += word
        state_xor ^= word
        phi = 0
        primitive_unbalanced = 0
        double_monochromatic = 0
        improving = []
        for mask, size, indices in fiber_data:
            signed_sum = size - 2 * (word & mask).bit_count()
            phi += signed_sum * signed_sum
            if size == 4 and signed_sum:
                require(abs(signed_sum) == 2, "Monochromatic primitive fiber")
                primitive_unbalanced += 1
            if size == 2 and signed_sum:
                double_monochromatic += 1
            for i in indices:
                sign = 1 - 2 * ((word >> i) & 1)
                delta = 4 * (1 - sign * signed_sum)
                if delta >= 0:
                    continue
                flipped = word ^ (1 << i)
                if all(0 < (flipped & constraint) < constraint
                       for constraint in incident[i]):
                    require(delta == -4, "Unexpected improving-flip size")
                    improving.append(i)
        require(phi >= 4 and (phi - 4) % 4 == 0, "Unexpected potential")
        k = (phi - 4) // 4
        require(k == primitive_unbalanced + double_monochromatic,
                "Unbalanced-fiber identity failed")
        budget = len(improving)
        histogram[k][budget] += 1
        maxima[k] = max(maxima.get(k, 0), budget)
        if k not in minima or budget < minima[k]:
            minima[k] = budget
            witnesses[k] = {
                "word": word,
                "phi": phi,
                "primitive_unbalanced": primitive_unbalanced,
                "double_monochromatic": double_monochromatic,
                "improving_flip_indices": sorted(improving),
                "improving_flip_cells": [cells[i] for i in sorted(improving)],
                "rows": ["".join(str((word >> i) & 1)
                                 for i, (v, u) in enumerate(cells) if v == mark)
                         for mark in marks[1:]],
            }

    def visit(depth, word):
        if depth == n:
            inspect(word)
            return
        for extended in (word, word | (1 << depth)):
            if all(0 < (extended & constraint) < constraint
                   for constraint in closing[depth]):
                visit(depth + 1, extended)

    visit(0, 0)
    require(count == 258228, "Proper-coloring count mismatch")
    require([minima[k] for k in range(10)] == [0, 2, 3, 3, 4, 4, 4, 6, 8, 10],
            "Minimum budget table mismatch")
    require(all(3 * budget >= 2 * k for k, budget in minima.items()),
            "Two-thirds budget bound failed")
    return {
        "count": count,
        "min_by_k": dict(sorted(minima.items())),
        "max_by_k": dict(sorted(maxima.items())),
        "hist_by_k": {k: dict(sorted(h.items())) for k, h in sorted(histogram.items())},
        "argmins": dict(sorted(witnesses.items())),
        "state_sum": state_sum,
        "state_xor": state_xor,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("independent_budget_results.json"))
    args = parser.parse_args()
    started = time.monotonic()
    geometry, geometry_path = load_geometry()
    marks, labels, cells, fibers, corners = geometry.source((1, 5, 25))
    require(len(cells) == 28 and len(corners) == 24, "Unexpected representative geometry")
    result = enumerate_budgets(cells, fibers, corners, marks)
    # Reconstruct every minimizing witness using the upstream direct measurer.
    for k, witness in result["argmins"].items():
        measured = geometry.measure(witness["word"], marks, cells, fibers, corners)
        require(measured["phi"] == 4 + 4 * k, "Witness potential mismatch")
        require(measured["rows"] == witness["rows"], "Witness row-word mismatch")
        for i in witness["improving_flip_indices"]:
            changed = geometry.measure(witness["word"] ^ (1 << i),
                                       marks, cells, fibers, corners)
            require(changed["phi"] == measured["phi"] - 4,
                    "Witness improving flip mismatch")
    report = {
        "status": "PASS",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "upstream_geometry": "../three_cube_forcing/verify.py",
        "upstream_geometry_sha256": hashlib.sha256(geometry_path.read_bytes()).hexdigest(),
        "marks": marks,
        "cells": cells,
        "corners": corners,
        "scope": "All proper colorings of the fixed eight-mark source, without symmetry quotient."
                 " Geometry is imported; coloring enumeration and complete flip-budget accounting"
                 " are performed here. General transfer and boundary interpretation are separate proofs.",
        **result,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "count": result["count"],
                      "min_by_k": result["min_by_k"],
                      "elapsed_seconds": report["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
