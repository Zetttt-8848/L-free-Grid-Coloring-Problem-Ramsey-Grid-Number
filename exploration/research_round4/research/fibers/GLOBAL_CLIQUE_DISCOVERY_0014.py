"""One-source fractional clique-packing discovery for the global corner-pair graph.

This script deliberately performs one LP only.  It is not a certificate or an
all-source statement: HiGHS floating output is retained solely as discovery
data for the specified eight-mark source.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import networkx as nx
from scipy.optimize import linprog


A = [0, 1, 2, 3, 4, 6, 7, 8]
OUT = Path(__file__).with_name("GLOBAL_CLIQUE_DISCOVERY_0014.json")


def phi(size: int) -> int:
    return (size - 1) ** 2 // 4


def main() -> None:
    source = set(A)
    graph = nx.Graph()
    corners = []
    for d in range(1, A[-1] - A[0] + 1):
        starts = [u for u in A if u + d in source]
        for u, v in itertools.combinations(starts, 2):
            corner = ((u + d, u), (v + d, u), (v + d, v))
            corners.append(corner)
            graph.add_edges_from(itertools.combinations(corner, 2))
    cliques = [tuple(sorted(clique)) for clique in nx.find_cliques(graph) if len(clique) >= 3]
    cliques.sort(key=lambda clique: (-len(clique), clique))
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    edge_index = {edge: i for i, edge in enumerate(edges)}
    incidence = [[0.0 for _ in cliques] for _ in edges]
    for j, clique in enumerate(cliques):
        for edge in itertools.combinations(clique, 2):
            incidence[edge_index[tuple(sorted(edge))]][j] = 1.0
    values = [phi(len(clique)) for clique in cliques]
    result = linprog(
        c=[-value for value in values], A_ub=incidence, b_ub=[1.0] * len(edges),
        bounds=(0, None), method="highs",
    )
    support = []
    if result.success:
        for clique, value, weight in zip(cliques, values, result.x):
            if weight > 1e-9:
                support.append({
                    "vertices": [list(vertex) for vertex in clique],
                    "size": len(clique),
                    "phi": value,
                    "weight_float": float(weight),
                    "weight_small_fraction_guess": str(Fraction(float(weight)).limit_denominator(10000)),
                })
    output = {
        "purpose": "single-source floating LP discovery; not a certificate or verification pass",
        "marks": A,
        "corners": len(corners),
        "pair_graph_vertices": graph.number_of_nodes(),
        "pair_graph_edges": graph.number_of_edges(),
        "maximal_cliques_size_at_least_3": len(cliques),
        "clique_size_histogram": {str(size): sum(len(clique) == size for clique in cliques)
                                 for size in sorted({len(clique) for clique in cliques})},
        "solver": "scipy.optimize.linprog(method=highs)",
        "status": result.message,
        "objective_float": float(-result.fun) if result.success else None,
        "objective_exceeds_corner_budget_44": bool(result.success and -result.fun > 44.0 + 1e-8),
        "positive_support": support,
        "scope": "One global-clique packing LP on one source. Fraction strings are display guesses from floating weights.",
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: output[key] for key in (
        "corners", "pair_graph_vertices", "pair_graph_edges", "maximal_cliques_size_at_least_3",
        "clique_size_histogram", "objective_float", "objective_exceeds_corner_budget_44",
    )}))


if __name__ == "__main__":
    main()
