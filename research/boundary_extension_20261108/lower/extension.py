"""Exact residual constraints and finite proof trees for one-layer extensions.

No SAT solver is needed for the main certificate generation. Coordinates are
zero based, and the only forbidden shape is (x,y),(x+d,y),(x+d,y+d), d>0.
"""
import argparse
import hashlib
import itertools
import json
import time
from collections import Counter
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def residual(rows, offset):
    n = len(rows)
    ox, oy = offset
    fixed = {(x + ox, y + oy): rows[x][y]
             for x in range(n) for y in range(n)}
    cells = [(x, y) for x in range(n + 1) for y in range(n + 1)
             if (x, y) not in fixed]
    indices = {p: i for i, p in enumerate(cells)}
    constraints = []
    for x in range(n + 1):
        for y in range(n + 1):
            for d in range(1, min(n - x, n - y) + 1):
                points = [(x, y), (x + d, y), (x + d, y + d)]
                unknown = [indices[p] for p in points if p not in fixed]
                colors = {fixed[p] for p in points if p in fixed}
                if len(colors) > 1:
                    continue
                if not unknown:
                    raise ValueError("Input contains a monochromatic L")
                for color in (sorted(colors) if colors else range(3)):
                    constraints.append({"vars": unknown, "color": color,
                                        "points": points})
    return cells, constraints


def closure(domains, constraints):
    """Each constraint forbids all its variables equalling one named color."""
    domains = list(domains)
    while True:
        changed = False
        for rule in constraints:
            bit = 1 << rule["color"]
            vs = rule["vars"]
            if any(not domains[v] & bit for v in vs):
                continue
            flexible = [v for v in vs if domains[v] != bit]
            if not flexible:
                return None
            if len(flexible) == 1:
                v = flexible[0]
                domains[v] &= ~bit
                if not domains[v]:
                    return None
                changed = True
        if not changed:
            return domains


def proof_tree(cell_count, constraints, seconds=60):
    deadline = time.monotonic() + seconds
    nodes = 0
    degree = Counter(v for rule in constraints for v in rule["vars"])

    def visit(ds):
        nonlocal nodes
        nodes += 1
        if nodes % 64 == 0 and time.monotonic() > deadline:
            raise TimeoutError("Proof-tree deadline")
        ds = closure(ds, constraints)
        if ds is None:
            return {"conflict": True}
        choices = [v for v in range(cell_count) if ds[v].bit_count() > 1]
        if not choices:
            return {"model": [d.bit_length() - 1 for d in ds]}
        v = min(choices, key=lambda t: (ds[t].bit_count(), -degree[t], t))
        children = {}
        for color in range(3):
            if ds[v] & (1 << color):
                child_ds = ds[:]
                child_ds[v] = 1 << color
                child = visit(child_ds)
                if "model" in child:
                    return child
                children[str(color)] = child
        return {"branch": v, "children": children}

    tree = visit([7] * cell_count)
    return tree, nodes


def minimize_core(cell_count, constraints):
    """Deletion-minimal, not minimum-cardinality. Solver only discovers core."""
    from pysat.solvers import Solver
    base = []
    for v in range(cell_count):
        ids = [3 * v + c + 1 for c in range(3)]
        base.append(ids)
        base.extend([[-a, -b] for a, b in itertools.combinations(ids, 2)])
    selectors = [3 * cell_count + i + 1 for i in range(len(constraints))]
    for i, rule in enumerate(constraints):
        base.append([-selectors[i]] + [-(3 * v + rule["color"] + 1)
                                      for v in rule["vars"]])
    with Solver(name="g4", bootstrap_with=base) as solver:
        if solver.solve(assumptions=selectors):
            raise ValueError("Expected inconsistent residual constraints")
        active = [i for i in range(len(constraints)) if selectors[i] in solver.get_core()]
        for i in active[:]:
            others = [j for j in active if j != i]
            if not solver.solve(assumptions=[selectors[j] for j in others]):
                active = others
        # Positive witnesses for every single deletion establish minimality.
        deletion_models = []
        for i in active:
            if not solver.solve(assumptions=[selectors[j] for j in active if j != i]):
                raise RuntimeError("Core not deletion-minimal")
            model = set(solver.get_model())
            deletion_models.append({"omitted": i, "colors": [
                next(c for c in range(3) if 3 * v + c + 1 in model)
                for v in range(cell_count)]})
    return active, deletion_models


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("paper20.json"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    rows = json.loads(args.input.read_text(encoding="utf-8"))["rows"]
    results = []
    for offset in itertools.product(range(2), repeat=2):
        cells, rules = residual(rows, offset)
        unary = {}
        for i, r in enumerate(rules):
            if len(r["vars"]) == 1:
                unary.setdefault(r["vars"][0], {}).setdefault(r["color"], i)
        blockers = [v for v, exclusions in unary.items() if len(exclusions) == 3]
        if blockers:
            v = min(blockers)
            ids = [unary[v][c] for c in range(3)]
            deletion_models = []
        else:
            ids, deletion_models = minimize_core(len(cells), rules)
        core = [rules[i] for i in ids]
        tree, nodes = proof_tree(len(cells), core)
        if "model" in tree:
            raise RuntimeError("Core unexpectedly satisfiable")
        results.append({"offset": offset, "cells": cells,
                        "residual_arity_counts": dict(Counter(len(r["vars"]) for r in rules)),
                        "unary_blocked_cells": [cells[v] for v in sorted(blockers)],
                        "core_ids": ids, "core": core,
                        "deletion_models": deletion_models,
                        "proof_tree": tree, "proof_tree_nodes": nodes})
    cells, rules = residual(rows, (0, 1))
    left_rules = [r for r in rules if all(cells[v][1] == 0 for v in r["vars"])]
    ids, models = minimize_core(len(cells), left_rules)
    left_core = [left_rules[i] for i in ids]
    tree, nodes = proof_tree(len(cells), left_core)
    if "model" in tree:
        raise RuntimeError("Left-column core unexpectedly satisfiable")
    left = {"offset": [0, 1], "cells": cells, "core_ids": ids,
            "core": left_core, "deletion_models": models,
            "proof_tree": tree, "proof_tree_nodes": nodes}
    report = {"status": "FINITE-CHECKED", "assertion_tested":
              "This fixed published 20-square cannot append even one full row or column on any of its four sides.",
              "non_claim": "Does not exclude other 20-squares or any 21-square with changed interior.",
              "input_sha256": sha(args.input), "script_sha256": sha(__file__),
              "elapsed_seconds": time.monotonic() - started, "placements": results,
              "left_side_core": left}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{"offset": r["offset"], "core_size": len(r["core"]),
                      "nodes": r["proof_tree_nodes"]} for r in results]))


if __name__ == "__main__":
    main()
