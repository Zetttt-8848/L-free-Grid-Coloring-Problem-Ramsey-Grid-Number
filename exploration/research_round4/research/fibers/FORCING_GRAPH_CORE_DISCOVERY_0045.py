"""Raw forcing-graph invariant for the saved unrestricted four-cube coloring."""
from collections import Counter
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__)
model_path = HERE.with_name("FULL_FOUR_CUBE_DISCOVERY_0045.json")
saved = json.loads(model_path.read_text(encoding="utf-8"))

A = saved["source"]
cells = [(v, u) for v in A for u in A if u < v]
cell_set = set(cells)
one = {tuple(q) for q in saved["one_colored_cells"]}

# This reconstructs only the corner list and the requested graph from the
# saved assignment. It performs no properness test.
corners = []
for x, y in cells:
    for d in range(1, max(A) - x + 1):
        edge = ((x, y), (x + d, y), (x + d, y + d))
        if all(q in cell_set for q in edge):
            corners.append(edge)

edges = set()
active_corners = 0
for left, outer, right in corners:
    if (left in one) == (right in one):
        active_corners += 1
        edges.add(tuple(sorted((outer, left))))
        edges.add(tuple(sorted((outer, right))))

adjacency = {v: set() for v in cells}
for a, b in edges:
    adjacency[a].add(b)
    adjacency[b].add(a)

# Exact minimum-degree peeling, retaining every removed vertex and its
# current degree. Ties use the lexicographic cell order.
remaining = {v: set(ns) for v, ns in adjacency.items()}
peeling = []
while remaining:
    v = min(remaining, key=lambda q: (len(remaining[q]), q))
    degree = len(remaining[v])
    peeling.append({"vertex": list(v), "degree_at_removal": degree})
    for w in remaining[v]:
        remaining[w].remove(v)
    del remaining[v]

# Direct k-core survival calculation, kept separate because a vertex's
# degree at removal in a minimum-degree ordering need not equal its core number.
core = {}
for k in range(max(map(len, adjacency.values()), default=0) + 1):
    live = {v: set(ns) for v, ns in adjacency.items()}
    changed = True
    while changed:
        doomed = [v for v, ns in live.items() if len(ns) < k]
        changed = bool(doomed)
        for v in doomed:
            for w in live[v]:
                live[w].remove(v)
            del live[v]
    for v in live:
        core[v] = k

record = {
    "scope": "One raw graph-invariant observation from the saved 120-cell coloring. No coloring solver or properness recheck was run.",
    "source": A,
    "vertices": len(cells),
    "corners_read": len(corners),
    "active_equal_endpoint_corners": active_corners,
    "simple_edges": len(edges),
    "maximum_degree": max(map(len, adjacency.values()), default=0),
    "peeling_maximum_degree": max((x["degree_at_removal"] for x in peeling), default=0),
    "peeling_degree_histogram": {str(k): v for k, v in sorted(Counter(x["degree_at_removal"] for x in peeling).items())},
    "core_histogram": {str(k): v for k, v in sorted(Counter(core.values()).items())},
    "maximum_core": max(core.values(), default=0),
    "peeling_order": peeling,
    "core_numbers": [{"vertex": list(v), "core": core[v]} for v in cells],
}
HERE.with_suffix(".json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in record.items() if k not in ("peeling_order", "core_numbers")}))

