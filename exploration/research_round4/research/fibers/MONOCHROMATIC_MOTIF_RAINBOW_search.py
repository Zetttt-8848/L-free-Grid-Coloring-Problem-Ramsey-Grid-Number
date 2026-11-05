"""Bounded discovery search for a monochromatic-C four-edge forcing motif."""

from itertools import combinations
from collections import deque


def search(n=13, sizes=(4, 5)):
    cells = [(v, u) for v in range(1, n) for u in range(v)]
    idx = {x: i for i, x in enumerate(cells)}
    corners = []
    completion = {}
    for j, i, k in combinations(range(n), 3):
        tri = ((i, j), (k, j), (k, i))
        ids = tuple(idx[x] for x in tri)
        corners.append(ids)
        for p, q, r in ((ids[0], ids[1], ids[2]),
                        (ids[0], ids[2], ids[1]),
                        (ids[1], ids[2], ids[0])):
            completion[tuple(sorted((p, q)))] = r

    corner_sets = {frozenset(t) for t in corners}

    def examine(C):
        Cset = set(C)
        X = set()
        witnesses = {}
        for p, q in combinations(C, 2):
            x = completion.get(tuple(sorted((p, q))))
            if x is not None and x not in Cset:
                X.add(x)
                witnesses.setdefault(x, (p, q))
        if len(X) < 5:
            return None

        graph = {x: set() for x in X}
        labels = {}
        for x, y in combinations(X, 2):
            z = completion.get(tuple(sorted((x, y))))
            if z in Cset:
                graph[x].add(y)
                graph[y].add(x)
                labels[tuple(sorted((x, y)))] = z

        # Test every corner among X.  A connected set on five vertices and
        # four edges containing its terminals is the desired forcing tree.
        for terminals in corners:
            T = set(terminals)
            if not T <= X:
                continue
            for extra in combinations(X - T, 2):
                V = T | set(extra)
                induced_edges = [
                    tuple(sorted((x, y)))
                    for x, y in combinations(V, 2)
                    if y in graph[x]
                ]
                # Any spanning tree on V works; check connectivity using
                # the induced graph, then recover one BFS tree.
                seen = {next(iter(V))}
                queue = deque(seen)
                tree = []
                while queue:
                    x = queue.popleft()
                    for y in graph[x] & V:
                        if y not in seen:
                            seen.add(y)
                            queue.append(y)
                            tree.append(tuple(sorted((x, y))))
                if len(seen) == 5:
                    return {
                        "C": [cells[x] for x in C],
                        "X": [cells[x] for x in sorted(X)],
                        "pair_witness": {
                            str(cells[x]): [cells[p] for p in witnesses[x]]
                            for x in sorted(X)
                        },
                        "terminals": [cells[x] for x in terminals],
                        "vertices": [cells[x] for x in sorted(V)],
                        "tree": [
                            {
                                "edge": [cells[x], cells[y]],
                                "label": cells[labels[(x, y)]],
                            }
                            for x, y in tree
                        ],
                        "induced_edge_count": len(induced_edges),
                    }
        return None

    for size in sizes:
        for number, C in enumerate(combinations(range(len(cells)), size), 1):
            # C itself must be corner-free.
            Cset = frozenset(C)
            if any(t <= Cset for t in corner_sets):
                continue
            result = examine(C)
            if result is not None:
                result["n"] = n
                result["size"] = size
                result["combination_number"] = number
                return result
    return None


if __name__ == "__main__":
    from pprint import pprint
    pprint(search())

