#!/usr/bin/env python3
"""Crop a self-contained 6-square witness without modifying its source."""

import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = args.source.read_bytes()
    source = json.loads(raw.decode("utf-8"))
    assert source["domain"] == "square" and source["n"] == 20
    assert source["k"] == 3 and len(source["rows"]) == 20
    rows = [row[:6] for row in source["rows"][:6]]
    assert len(rows) == 6 and all(len(row) == 6 for row in rows)
    assert all(type(c) is int and 0 <= c < 4 for row in rows for c in row)
    checked_ls = 0
    for x in range(6):
        for y in range(6):
            for d in range(1, 6):
                if x + d < 6 and y + d < 6:
                    checked_ls += 1
                    assert len({rows[x][y], rows[x + d][y],
                                rows[x + d][y + d]}) > 1
    assert checked_ls == 55
    result = {
        "domain": "square",
        "k": 4,
        "n": 6,
        "rows": rows,
        "coordinate_convention": "rows[x][y] is the color of cell (x,y)",
        "proper": True,
        "checked_geometric_Ls": checked_ls,
        "provenance": {
            "source_file": args.source.name,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "operation": "crop to x=0..5 and y=0..5; no recoloring",
            "source_colors": 3,
            "external_theorem_used": False,
        },
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "n": 6, "cells": 36,
                      "checked_geometric_Ls": checked_ls,
                      "source_sha256": result["provenance"]["source_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
