#!/usr/bin/env python3
"""Search complete squares for zero-rainbow proper four-color witnesses."""

import json
import sys
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent / "kernel_results.json"
COLORS = 4
ORDER_BUDGET = 120.0
TOTAL_BUDGET = 300.0


def geometry(m):
    cells = [(x, y) for x in range(m) for y in range(m)]
    index = {cell: i for i, cell in enumerate(cells)}
    completed = [[] for _ in cells]
    triangle_ls = []
    all_ls = []
    for x in range(m):
        for y in range(m):
            for d in range(1, m - max(x, y)):
                triple = ((x, y), (x + d, y), (x + d, y + d))
                ids = tuple(index[cell] for cell in triple)
                all_ls.append(ids)
                if all(a > b for a, b in triple):
                    triangle_ls.append(ids)
                completed[max(ids)].append(ids)
    return cells, completed, all_ls, triangle_ls


def zero_search(m, deadline):
    cells, completed, all_ls, triangle_ls = geometry(m)
    colors = [-1] * len(cells)
    stats = {
        "nodes": 0,
        "monochromatic_prunes": 0,
        "rainbow_prunes": 0,
        "zero_leaves": 0,
    }
    timed_out = False

    def visit(position, highest):
        nonlocal timed_out
        stats["nodes"] += 1
        if stats["nodes"] % 4096 == 0 and time.monotonic() > deadline:
            timed_out = True
            return None
        if position == len(cells):
            stats["zero_leaves"] += 1
            return colors.copy()
        largest_allowed = min(COLORS - 1, highest + 1)
        for color in range(largest_allowed + 1):
            rejected_mono = False
            rejected_rainbow = False
            for ids in completed[position]:
                used = {colors[i] for i in ids if i != position}
                used.add(color)
                if len(used) == 1:
                    rejected_mono = True
                    break
                ids_tuple = tuple(cells[i] for i in ids)
                if len(used) == 3 and all(a > b for a, b in ids_tuple):
                    rejected_rainbow = True
                    break
            if rejected_mono:
                stats["monochromatic_prunes"] += 1
                continue
            if rejected_rainbow:
                stats["rainbow_prunes"] += 1
                continue
            colors[position] = color
            witness = visit(position + 1, max(highest, color))
            colors[position] = -1
            if witness is not None or timed_out:
                return witness
        return None

    witness = visit(0, -1)
    return witness, stats, timed_out, cells, all_ls, triangle_ls


def literal_witness_check(witness, cells, all_ls, triangle_ls):
    assert witness is not None
    assert set(witness) <= set(range(COLORS))
    assert all(color >= 0 for color in witness)
    assert all(len({witness[i] for i in ids}) > 1 for ids in all_ls)
    assert all(len({witness[i] for i in ids}) < 3 for ids in triangle_ls)
    matrix = []
    m = int(len(cells) ** 0.5)
    for x in range(m):
        matrix.append([witness[x * m + y] for y in range(m)])
    return matrix


def main():
    started = time.monotonic()
    rows = []
    for m in (3, 4, 5):
        remaining = TOTAL_BUDGET - (time.monotonic() - started)
        if remaining <= 0:
            rows.append({"m": m, "status": "UNDECIDED", "reason": "total budget exhausted"})
            continue
        deadline = time.monotonic() + min(ORDER_BUDGET, remaining)
        witness, stats, timed_out, cells, all_ls, triangle_ls = zero_search(m, deadline)
        row = {"m": m, "cells": len(cells), "all_Ls": len(all_ls),
               "strict_triangle_Ls": len(triangle_ls), "search": stats}
        if witness is not None:
            matrix = literal_witness_check(witness, cells, all_ls, triangle_ls)
            row.update({
                "status": "COUNTEREXAMPLE TO POSITIVE LOCAL MINIMUM",
                "rho_m": 0,
                "coverage": "one complete proper witness; exact zero minimum",
                "witness_matrix_row_x": matrix,
            })
            standard = {
                "domain": "square",
                "k": COLORS,
                "n": m,
                "rows": matrix,
                "coordinate_convention": "rows[x][y] is the color of cell (x,y)",
                "strict_triangle_rainbow_Ls": 0,
            }
            (OUT.parent / f"kernel_{m}.json").write_text(
                json.dumps(standard, indent=2) + "\n", encoding="ascii")
        elif timed_out:
            row.update({"status": "UNDECIDED", "coverage": "incomplete canonical search",
                        "rho_m": "undecided"})
        else:
            row.update({"status": "NO ZERO WITNESS; POSITIVE MINIMUM NOT OPTIMIZED",
                        "coverage": "complete canonical zero-witness search",
                        "rho_m": ">=1; exact value undecided"})
        rows.append(row)
        if timed_out:
            break
    result = {
        "date": "2026-11-15",
        "python": sys.version.split()[0],
        "palette": 4,
        "symmetry": "first-appearance canonical renaming in row-major (x,y) cell order",
        "order_budget_seconds": ORDER_BUDGET,
        "total_budget_seconds": TOTAL_BUDGET,
        "pruning": "only a completed monochromatic L or a completed strict-triangle rainbow L",
        "orders": rows,
        "new_R4_bound": False,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"status": "PASS" if all(row.get("rho_m") == 0 for row in rows) else "CHECK REPORT",
                      "output": str(OUT), "orders": [
                          {"m": row["m"], "status": row["status"], "rho_m": row.get("rho_m")}
                          for row in rows], "new_R4_bound": False}, indent=2))


if __name__ == "__main__":
    main()
