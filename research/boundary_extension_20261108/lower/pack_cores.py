"""Find disjoint interior supports of certified frozen-extension obstructions."""
import argparse
import itertools
import json
import time
from pathlib import Path
from extension import minimize_core, proof_tree, residual, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("paper20.json"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text())["rows"]
    started = time.monotonic()
    results = []
    for offset in itertools.product(range(2), repeat=2):
        cells, rules = residual(rows, offset)
        boundary = set(cells)
        used = set()
        packs = []
        for iteration in range(15):
            available = [r for r in rules if not any(tuple(p) in used for p in r["points"])]
            try:
                ids, models = minimize_core(len(cells), available)
            except ValueError:
                disposition = "remaining_constraints_satisfiable_solver_observation"
                break
            core = [available[i] for i in ids]
            support = {tuple(p) for r in core for p in r["points"] if tuple(p) not in boundary}
            tree, nodes = proof_tree(len(cells), core)
            if "model" in tree or not support:
                raise RuntimeError("Invalid obstruction")
            if support & used:
                raise RuntimeError("Supports overlap")
            packs.append({"core": core, "support": sorted(support),
                          "proof_tree": tree, "proof_tree_nodes": nodes})
            used.update(support)
        else:
            disposition = "packing_iteration_cap_15"
        results.append({"offset": offset, "cells": cells, "cores": packs,
                        "necessary_changed_old_cells": len(packs),
                        "disposition": disposition})
    report = {"input_sha256": sha(args.input), "script_sha256": sha(__file__),
              "elapsed_seconds": time.monotonic() - started,
              "claim": "Any 21-square extension with old colors allowed to change must change at least one old cell in each disjoint support.",
              "non_claim": "The packing is not proved maximum and the repair bound is not sufficient or proved sharp.",
              "placements": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{ "offset": x["offset"], "repair_lower_bound": len(x["cores"]),
                       "core_sizes": [len(y["core"]) for y in x["cores"]]}
                     for x in results]))


if __name__ == "__main__":
    main()
