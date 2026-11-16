#!/usr/bin/env python3
"""Verify the full O1 counterexample directly from the L definition."""

import json
from pathlib import Path


def main():
    path = Path(__file__).with_name("counterexample.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["witness"]
    assert rows is not None and len(rows) == 3
    assert all(len(row) == 3 for row in rows)
    assert all(color in range(4) for row in rows for color in row)
    checked = 0
    for x in range(3):
        for y in range(3):
            for d in range(1, 3):
                if x + d < 3 and y + d < 3:
                    colors = {rows[x][y], rows[x + d][y], rows[x + d][y + d]}
                    assert len(colors) > 1
                    checked += 1
    assert checked == 5
    assert rows[0][0] == rows[1][1] == 0
    assert rows[1][0] == rows[2][1] == 1
    assert rows[1][0] == 1
    # The off-diagonal pair has a different completion cell, (2,0), from the
    # main-diagonal pair's completion cell, (1,0).
    assert rows[2][0] != 1
    print(json.dumps({
        "status": "PASS",
        "checked_Ls": checked,
        "main_completion": [1, 0],
        "off_diagonal_completion": [2, 0],
        "conclusion": "O1 is refuted; no sixteen-class consumer is justified"
    }, indent=2))


if __name__ == "__main__":
    main()
