"""Bounded discovery for anchored square-source column graphs (0038).

No source-coloring/SAT calls are made.  For the first anchor whose ordinary
column graph has an odd cycle, record a shortest BFS-found odd cycle.
"""
from __future__ import annotations

import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "SQUARE_COLUMN_DISCOVERY_0038.json"


def make_graph(anchor_root: int, max_root: int = 300):
    vertices = list(range(anchor_root + 1, max_root + 1))
    squares = {t * t: t for t in range(anchor_root, max_root + 1)}
    adj = {b: set() for b in vertices}
    edges = []
    a2 = anchor_root * anchor_root
    for i, b in enumerate(vertices):
        for c in vertices[i + 1 :]:
            target = c * c - b * b + a2
            t = squares.get(target)
            if t is not None:
                adj[b].add(c)
                adj[c].add(b)
                edges.append((b, c, t))
    return vertices, adj, edges


def cycle_from_same_parity_edge(u, v, parent):
    path_u, path_v = [], []
    x = u
    while x is not None:
        path_u.append(x)
        x = parent[x]
    y = v
    while y is not None:
        path_v.append(y)
        y = parent[y]
    index_u = {q: i for i, q in enumerate(path_u)}
    lca_index_v = next(i for i, q in enumerate(path_v) if q in index_u)
    lca = path_v[lca_index_v]
    return path_u[: index_u[lca] + 1] + list(reversed(path_v[:lca_index_v]))


def shortest_odd_cycle(vertices, adj):
    best = None
    for start in vertices:
        distance = {start: 0}
        parent = {start: None}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in sorted(adj[u]):
                if v not in distance:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and (distance[u] - distance[v]) % 2 == 0:
                    cycle = cycle_from_same_parity_edge(u, v, parent)
                    if len(cycle) % 2 and (best is None or len(cycle) < len(best)):
                        best = cycle
        if best is not None and len(best) == 3:
            return best
    return best


def run():
    records = []
    for anchor_root in (1, 2, 3):
        vertices, adj, edges = make_graph(anchor_root)
        cycle = shortest_odd_cycle(vertices, adj)
        record = {
            "anchor_root": anchor_root,
            "anchor_square": anchor_root * anchor_root,
            "vertex_roots": vertices,
            "edge_count": len(edges),
            "bipartite": cycle is None,
            "odd_cycle_roots": cycle,
        }
        if cycle is not None:
            # Each cycle edge b--c has label t satisfying c^2-b^2+a^2=t^2.
            labels = []
            support = {anchor_root * anchor_root}
            for b, c in zip(cycle, cycle[1:] + cycle[:1]):
                lo, hi = sorted((b, c))
                t = next(t for x, y, t in edges if x == lo and y == hi)
                labels.append({"b_root": lo, "c_root": hi, "label_root": t,
                               "equation": f"{hi}^2-{lo}^2+{anchor_root}^2={t}^2"})
                support.update((lo * lo, hi * hi, t * t))
            record["cycle_edges"] = labels
            record["square_mark_support"] = sorted(support)
            if len(cycle) == 3:
                p, q, rroot = sorted(cycle)
                a2 = anchor_root * anchor_root
                x = p * p - a2
                rstep = q * q - p * p
                sstep = rroot * rroot - q * q
                expressions = {
                    "a": a2,
                    "a+x": a2 + x,
                    "a+r": a2 + rstep,
                    "a+s": a2 + sstep,
                    "a+x+r": a2 + x + rstep,
                    "a+r+s": a2 + rstep + sstep,
                    "a+x+r+s": a2 + x + rstep + sstep,
                }
                record["partial_cube_parameters"] = {"x": x, "r": rstep, "s": sstep}
                record["literal_seven_partial_cube_expressions"] = expressions
            records.append(record)
            break
        records.append(record)
    OUT.write_text(json.dumps({
        "scope": "ordinary BFS odd-cycle discovery in C_a for square roots through 300; no SAT or coloring check",
        "records": records,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: records[-1][k] for k in records[-1]
                      if k not in {"vertex_roots"}}, indent=2))


if __name__ == "__main__":
    run()
