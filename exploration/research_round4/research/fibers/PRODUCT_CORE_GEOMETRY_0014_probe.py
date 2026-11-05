"""Independent geometry/proof-table checker for PRODUCT_CORE_GEOMETRY_0014.

It does not invoke SAT. It checks that the saved discovery core projects to
an ordinary weak-triangle corner hypergraph and checks the two branches of the
human special-diagonal-pattern proof from the NAE rule itself.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "product_obstruction_discovery.json").read_text())
EDGES = {tuple(e) for e in DATA["edges"]}
COORD = {
    v["id"]: (v["scalar"][0] - 7, v["scalar"][1]) for v in DATA["vertices"]
}
ID = {cell: v for v, cell in COORD.items()}


def is_corner(cells: tuple[tuple[int, int], ...]) -> bool:
    (y, x), (v, x2), (v2, u) = cells
    return x == x2 and v == v2 and v - y == u - x > 0


def force(colors: dict[int, int], cells: tuple[tuple[int, int], ...]) -> None:
    """Check one displayed NAE forcing step and insert its missing color."""
    edge = tuple(ID[cell] for cell in cells)
    assert edge in EDGES
    assert is_corner(cells)
    missing = [v for v in edge if v not in colors]
    assert len(missing) == 1
    known = [colors[v] for v in edge if v in colors]
    assert known[0] == known[1]
    colors[missing[0]] = 1 - known[0]


def check_branch(assumed_color: int, steps, final_corner) -> None:
    diagonal = {
        0: 1, 1: 0, 3: 1,
        21: 0, 22: 1, 24: 1,
        63: 0, 64: 1, 66: 0,
        84: 1, 85: 0, 87: 0,
    }
    colors = {ID[(x, x)]: color for x, color in diagonal.items()}
    colors[ID[(63, 0)]] = assumed_color
    for cells in steps:
        force(colors, cells)
    edge = tuple(ID[cell] for cell in final_corner)
    assert edge in EDGES
    assert is_corner(final_corner)
    assert len({colors[v] for v in edge}) == 1


if __name__ == "__main__":
    assert len(COORD) == 56 and len(EDGES) == 75
    assert all(y >= x for y, x in COORD.values())
    assert all(is_corner(tuple(COORD[v] for v in edge)) for edge in EDGES)

    branch_zero = [
        ((0, 0), (84, 0), (84, 84)),
        ((63, 0), (84, 0), (84, 21)),
        ((21, 21), (85, 21), (85, 85)),
        ((84, 21), (85, 21), (85, 22)),
        ((1, 1), (66, 1), (66, 66)),
        ((1, 1), (87, 1), (87, 87)),
        ((66, 1), (87, 1), (87, 22)),
        ((21, 21), (87, 21), (87, 87)),
        ((84, 21), (87, 21), (87, 24)),
    ]
    check_branch(0, branch_zero, ((85, 22), (87, 22), (87, 24)))

    branch_one = [
        ((1, 1), (85, 1), (85, 85)),
        ((1, 1), (87, 1), (87, 87)),
        ((85, 1), (87, 1), (87, 3)),
        ((0, 0), (84, 0), (84, 84)),
        ((84, 0), (87, 0), (87, 3)),
        ((63, 0), (87, 0), (87, 24)),
        ((66, 3), (87, 3), (87, 24)),
        ((3, 3), (24, 3), (24, 24)),
        ((3, 3), (84, 3), (84, 84)),
        ((24, 3), (84, 3), (84, 63)),
        ((63, 63), (85, 63), (85, 85)),
        ((84, 63), (85, 63), (85, 64)),
        ((24, 3), (85, 3), (85, 64)),
        ((1, 1), (66, 1), (66, 66)),
        ((66, 1), (87, 1), (87, 22)),
        ((85, 22), (87, 22), (87, 24)),
    ]
    check_branch(1, branch_one, ((66, 3), (85, 3), (85, 22)))
    print("PASS: 56 projected cells, 75 positive-step corners, both proof branches")
