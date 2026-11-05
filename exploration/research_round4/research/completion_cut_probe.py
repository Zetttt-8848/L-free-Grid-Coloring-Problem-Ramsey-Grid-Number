"""Bounded discovery for the proved integer completion-cut criterion.

The input is one literal source, not the family of all sources. Greedy
edge-disjoint clique packings give lower bounds only; they are not optima.
"""
from pathlib import Path
from collections import Counter
import json
import time

ROOT = Path(__file__).resolve().parent
INPUT = ROOT.parent.parent / "research_round3/joint/witness_464_parametric.json"
start = time.monotonic()
A = json.loads(INPUT.read_text(encoding="utf-8"))["marks"]
S = set(A)
counts = Counter(y-x for x in A for y in A if x < y)
corners = sum(r*(r-1)//2 for r in counts.values())
diagonal = sum((r-1)**2//4 for r in counts.values())
rows = []

def pack(vertices, adjacent):
    graph = {x: {y for y in vertices if x != y and adjacent(x, y)}
             for x in vertices}
    original_edges = sum(map(len, graph.values()))//2
    packing = []
    value = 0
    while any(graph.values()):
        if time.monotonic()-start > 50:
            return original_edges, value, packing, False
        seed = max(graph, key=lambda x: (len(graph[x]), -x))
        clique = [seed]
        candidates = set(graph[seed])
        while candidates:
            v = max(candidates,
                    key=lambda x: (len(graph[x] & candidates), len(graph[x]), -x))
            clique.append(v)
            candidates &= graph[v]
        for x in clique:
            for y in clique:
                graph[x].discard(y)
        if len(clique) >= 3:
            packing.append(clique)
            value += (len(clique)-1)**2//4
    return original_edges, value, packing, True

for direction in ("row", "column"):
    for anchor in A:
        if time.monotonic()-start > 50:
            break
        if direction == "row":
            vertices = [u for u in A if u < anchor]
            adjacent = lambda x, y: anchor-abs(x-y) in S
        else:
            vertices = [v for v in A if anchor < v]
            adjacent = lambda x, y: anchor+abs(x-y) in S
        edges, bound, packing, finished = pack(vertices, adjacent)
        rows.append(dict(direction=direction, anchor=anchor, edges=edges,
                         lower_bound=bound, cliques=packing, finished=finished))

line_bound = sum(row["lower_bound"] for row in rows)
out = dict(input=str(INPUT), marks=A, corners=corners,
           diagonal_lower_bound=diagonal, row_column_lower_bound=line_bound,
           total_lower_bound=diagonal+line_bound,
           contradiction_margin=diagonal+line_bound-corners,
           line_graphs_processed=len(rows), expected_line_graphs=2*len(A),
           seconds=time.monotonic()-start, packings=rows,
           scope="Greedy discovery on one source; no universal source bound or optimum.")
(ROOT / "completion_cut_probe.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k not in ("marks", "packings")}))
