#!/usr/bin/env python3
"""Literal independent checks for full-square zero-rainbow witnesses."""

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "kernel_results.json"
OUT = ROOT / "kernel_verification.json"


def check_matrix(matrix):
    m = len(matrix)
    assert m >= 1 and all(len(row) == m for row in matrix)
    assert all(color in (0, 1, 2, 3) for row in matrix for color in row)
    mono = []
    rainbow = []
    triangle_count = 0
    for x in range(m):
        for y in range(m):
            for d in range(1, m - max(x, y)):
                colors = (matrix[x][y], matrix[x + d][y], matrix[x + d][y + d])
                if len(set(colors)) == 1:
                    mono.append((x, y, d))
                if x > y:
                    triangle_count += 1
                    if len(set(colors)) == 3:
                        rainbow.append((x, y, d))
    return mono, rainbow, triangle_count


def normalized(matrix):
    renaming = {}
    next_color = 0
    result = []
    for row in matrix:
        for color in row:
            if color not in renaming:
                renaming[color] = next_color
                next_color += 1
            result.append(renaming[color])
    return result


def two_color_proper_exists(m):
    cells = [(x, y) for x in range(m) for y in range(m)]
    index = {cell: i for i, cell in enumerate(cells)}
    completed = [[] for _ in cells]
    for x in range(m):
        for y in range(m):
            for d in range(1, m - max(x, y)):
                ids = tuple(index[cell] for cell in
                            ((x, y), (x + d, y), (x + d, y + d)))
                completed[max(ids)].append(ids)
    colors = [-1] * (m * m)

    def visit(position):
        if position == m * m:
            return True
        choices = (0,) if position == 0 else (0, 1)
        for color in choices:
            if any(all(colors[i] == color for i in ids if i != position)
                   for ids in completed[position]):
                continue
            colors[position] = color
            if visit(position + 1):
                return True
            colors[position] = -1
        return False

    return visit(0)


def main():
    source = json.loads(SOURCE.read_text(encoding="ascii"))
    checked = []
    for row in source["orders"]:
        if row.get("rho_m") != 0:
            checked.append({"m": row["m"], "status": row["status"], "witness_check": "not applicable"})
            continue
        matrix = row["witness_matrix_row_x"]
        mono, rainbow, triangle_count = check_matrix(matrix)
        m = row["m"]
        assert not mono and not rainbow
        assert triangle_count == m * (m - 1) * (m - 2) // 6
        assert row["strict_triangle_Ls"] == triangle_count
        flat = [color for line in matrix for color in line]
        canonical = normalized(matrix)
        assert flat == canonical, "generator did not return first-appearance canonical witness"
        checked.append({"m": m, "status": "PASS", "proper_Ls_checked": row["all_Ls"],
                        "strict_triangle_Ls_checked": triangle_count,
                        "rainbow_Ls": 0, "rho_m": 0})

    # Independent pruned encoding checks reproduce R_2=5 at the square boundary.
    known = []
    for m, expected_proper in ((4, True), (5, False)):
        proper_exists = two_color_proper_exists(m)
        assert proper_exists == expected_proper
        known.append({"m": m, "two_color_proper_exists": proper_exists,
                      "zero_rainbow_when_proper": proper_exists,
                      "status": "PASS"})

    result = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "witnesses": checked,
        "known_answer_checks": known,
        "new_R4_bound": False,
        "scope": "Literal witness checks and known-answer encoding checks only",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
