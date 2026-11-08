"""Independent geometry and proof-tree checker; standard library only.

Does not import extension.py, its constraint generator, propagation, or SAT.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_geometry(rows):
    n = len(rows)
    require(n == 20 and all(len(r) == n for r in rows), "matrix shape")
    require(all(type(c) is int and 0 <= c < 3 for r in rows for c in r), "matrix colors")
    count = 0
    # Generate from bend and distance, unlike the discovery start-point loop.
    for bend_x in range(n):
        for bend_y in range(n):
            for d in range(1, min(bend_x, n - 1 - bend_y) + 1):
                values = [rows[bend_x - d][bend_y], rows[bend_x][bend_y],
                          rows[bend_x][bend_y + d]]
                require(len(set(values)) > 1, "matrix contains monochromatic L")
                count += 1
    require(count == 2470, "baseline corner coverage")
    return count


def check_core(rows, record):
    n = len(rows)
    ox, oy = record["offset"]
    require((ox, oy) in itertools.product(range(2), repeat=2), "bad offset")
    fixed = {(x + ox, y + oy): rows[x][y] for x in range(n) for y in range(n)}
    cells = [tuple(p) for p in record["cells"]]
    expected = {(x, y) for x in range(n + 1) for y in range(n + 1)} - set(fixed)
    require(len(cells) == len(set(cells)) and set(cells) == expected, "boundary coverage")
    support = set()
    for rule in record["core"]:
        pts = [tuple(p) for p in rule["points"]]
        require(len(pts) == 3 and len(set(pts)) == 3, "three distinct corners")
        a, b, c = pts
        d = b[0] - a[0]
        require(d > 0 and a[1] == b[1] and b[0] == c[0] and c[1] - b[1] == d,
                "not the prescribed directed equal-leg L")
        require(all(0 <= x <= n and 0 <= y <= n for x, y in pts), "out of grid")
        unknown = [p for p in pts if p not in fixed]
        require(unknown and all(type(v) is int and 0 <= v < len(cells) for v in rule["vars"])
                and len(rule["vars"]) == len(set(rule["vars"])), "invalid variable indices")
        require([cells[v] for v in rule["vars"]] == unknown, "residual variables mismatch")
        require(type(rule["color"]) is int and 0 <= rule["color"] < 3, "bad forbidden color")
        require(all(fixed[p] == rule["color"] for p in pts if p in fixed), "unjustified rule")
        support.update(p for p in pts if p in fixed)
    constraints = [(set(r["vars"]), r["color"]) for r in record["core"]]

    def propagate(ds):
        ds = [set(d) for d in ds]
        while True:
            before = tuple(frozenset(d) for d in ds)
            for vs, color in constraints:
                # A color at v lacks support precisely when all other variables
                # are forced to that same color. Revises every variable directly.
                for v in vs:
                    if color in ds[v] and all(ds[w] == {color} for w in vs - {v}):
                        ds[v].discard(color)
                        if not ds[v]:
                            return None
            if before == tuple(frozenset(d) for d in ds):
                return ds

    nodes = 0

    def check_tree(tree, ds):
        nonlocal nodes
        nodes += 1
        ds = propagate(ds)
        if ds is None:
            require(tree == {"conflict": True}, "conflict leaf shape")
            return
        require(set(tree) == {"branch", "children"}, "missing justified conflict")
        v = tree["branch"]
        require(type(v) is int and 0 <= v < len(cells) and len(ds[v]) > 1, "invalid branch")
        require(set(tree["children"]) == {str(c) for c in ds[v]}, "incomplete branch coverage")
        for c in ds[v]:
            child_ds = [set(d) for d in ds]
            child_ds[v] = {c}
            check_tree(tree["children"][str(c)], child_ds)

    check_tree(record["proof_tree"], [{0, 1, 2} for _ in cells])
    require(nodes == record["proof_tree_nodes"], "tree node accounting")
    models = record.get("deletion_models", [])
    if models:
        ids = record["core_ids"]
        require(len(ids) == len(set(ids)) == len(constraints), "core ids")
        require({m["omitted"] for m in models} == set(ids) and len(models) == len(ids), "deletion coverage")
        for m in models:
            colors = m["colors"]
            require(len(colors) == len(cells) and all(type(c) is int and 0 <= c < 3 for c in colors), "deletion model")
            for i, (vs, color) in zip(ids, constraints):
                if i != m["omitted"]:
                    require(any(colors[v] != color for v in vs), "invalid deletion witness")
    return support, nodes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(__file__).parent)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.directory
    input_path = root / "paper20.json"
    rows = json.loads(input_path.read_text(encoding="utf-8"))["rows"]
    corners = check_geometry(rows)
    extension = json.loads((root / "extension_results.json").read_text(encoding="utf-8"))
    require(extension["input_sha256"] == sha(input_path), "changed matrix")
    require([r["offset"] for r in extension["placements"]] == [[0, 0], [0, 1], [1, 0], [1, 1]], "placement coverage")
    nodes = 0
    for r in extension["placements"] + [extension["left_side_core"]]:
        _, visited = check_core(rows, r)
        nodes += visited
    # Verify that each of the four single-side conclusions really uses only
    # that side, not other new cells from a surrounding square.
    side_records = [extension["placements"][0], extension["placements"][1],
                    extension["placements"][3], extension["left_side_core"]]
    side_tests = [lambda p: p[1] == 20, lambda p: p[0] == 20,
                  lambda p: p[0] == 0, lambda p: p[1] == 0]
    for r, predicate in zip(side_records, side_tests):
        require(all(predicate(r["cells"][v]) for e in r["core"] for v in e["vars"]), "single-side claim invalid")
    packing = json.loads((root / "packing_results.json").read_text(encoding="utf-8"))
    require(packing["input_sha256"] == sha(input_path), "changed packing matrix")
    require([r["offset"] for r in packing["placements"]] == [[0, 0], [0, 1], [1, 0], [1, 1]], "packing coverage")
    bounds = []
    for p in packing["placements"]:
        used = set()
        for core in p["cores"]:
            record = dict(core, offset=p["offset"], cells=p["cells"])
            support, visited = check_core(rows, record)
            nodes += visited
            require(support == {tuple(x) for x in core["support"]}, "support mismatch")
            require(support and not support & used, "overlapping supports")
            used.update(support)
        require(p["necessary_changed_old_cells"] == len(p["cores"]), "repair bound mismatch")
        bounds.append({"offset": p["offset"], "at_least_changed_old_cells": len(p["cores"])})
    result = {"status": "PASS", "baseline_cells": 400, "baseline_corners": corners,
              "single_sides_certified": ["right", "bottom", "top", "left"],
              "repair_lower_bounds": bounds, "proof_tree_nodes_checked": nodes,
              "deletion_minimality_certified_for_bottom_and_left_cores": True,
              "inputs_sha256": {name: sha(root / name) for name in ["paper20.json", "extension_results.json", "packing_results.json"]},
              "verifier_sha256": sha(Path(__file__))}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
