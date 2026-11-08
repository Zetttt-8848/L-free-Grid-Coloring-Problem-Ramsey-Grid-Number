#!/usr/bin/env python3
"""Check a full positive directed-L coloring using only integer arithmetic.

JSON must explicitly specify domain, k and rows. Square row x lists y in
increasing order, starting at zero. Source rows follow increasing mark order;
strict sources omit the empty first row, weak sources include the diagonal.
This checks a supplied coloring; it performs no search and proves no minimum.
"""

import argparse
from collections import Counter, defaultdict
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    return type(value) is int


def check(data):
    require(isinstance(data, dict), "Expected a JSON object")
    domain, k, rows = data.get("domain"), data.get("k"), data.get("rows")
    require(domain in ("square", "strict-source", "weak-source"), "Unknown domain")
    require(integer(k) and k >= 1, "k must be a positive integer")
    require(isinstance(rows, list), "rows must be a list")
    if domain == "square":
        n = data.get("n")
        require(integer(n) and n >= 1, "n must be a positive integer")
        row_marks = list(range(n))
        columns = [list(range(n)) for _ in row_marks]
        marks = None
    else:
        marks = data.get("marks")
        require(isinstance(marks, list) and all(integer(a) for a in marks),
                "marks must be a list of integers")
        require(marks == sorted(set(marks)), "marks must be strictly increasing")
        row_marks = marks[1:] if domain == "strict-source" else marks
        columns = [[u for u in marks if u < v or (domain == "weak-source" and u == v)]
                   for v in row_marks]
    require(len(rows) == len(row_marks), "Missing or extra rows")
    colors = {}
    for v, us, row in zip(row_marks, columns, rows):
        if isinstance(row, str):
            require(k <= 10 and all(c in "0123456789" for c in row),
                    "String rows require decimal color digits and k <= 10")
            row = [int(c) for c in row]
        require(isinstance(row, list) and len(row) == len(us), f"Wrong row length at {v}")
        require(all(integer(c) and 0 <= c < k for c in row), f"Invalid color at row {v}")
        for u, c in zip(us, row):
            colors[v, u] = c

    # Start from horizontal pairs, independent of fiber or SAT auxiliary data.
    horizontal = defaultdict(list)
    for x, y in colors:
        horizontal[y].append(x)
    total = mono = rainbow = mixed = 0
    examples = []
    for y, xs in sorted(horizontal.items()):
        for x, v in combinations(sorted(xs), 2):
            p, q, r = (x, y), (v, y), (v, y + v - x)
            if r not in colors:
                continue
            total += 1
            count = len({colors[p], colors[q], colors[r]})
            rainbow += count == 3
            mixed += colors[p] != colors[r]
            if count == 1:
                mono += 1
                if len(examples) < 8:
                    examples.append([list(p), list(q), list(r)])
    report = dict(domain=domain, k=k, cells=len(colors), corners=total,
                  monochromatic=mono, rainbows=rainbow, mixed_parallel_inputs=mixed,
                  proper=mono == 0, first_monochromatic_corners=examples)
    if domain == "square":
        expected = sum(t * t for t in range(1, n))
        require(total == expected, "Square corner enumeration is incomplete")
        report.update(n=n, implied_Rk_lower_bound=n + 1 if mono == 0 else None)
    else:
        m = len(marks)
        M = m * (m - 1) // 2
        pair_sums = Counter(a + b for a in marks for b in marks)
        energy = sum(t * t for t in pair_sums.values())
        T = total - (M if domain == "weak-source" else 0)
        require(energy == 2 * m * m - m + 4 * T, "Source energy identity failed")
        report.update(mark_count=m, M=M, T=T, E=energy,
                      span=marks[-1] - marks[0] if marks else 0)
        if domain == "strict-source" and k == 2 and mono == 0:
            fibers = defaultdict(list)
            for (v, u), c in colors.items():
                fibers[v - u].append(c)
            phi = sum(sum(1 - 2 * c for c in cs) ** 2 for cs in fibers.values())
            H = total - mixed
            require(4 * H == 2 * T - M + phi, "Forcing identity failed")
            report.update(Phi=phi, forcing_corners=H, forcing_edges=2 * H)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = args.input.read_bytes()
        report = check(json.loads(raw.decode("utf-8-sig")))
        report["input_sha256"] = hashlib.sha256(raw).hexdigest()
        report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    except (OSError, ValueError, TypeError, KeyError) as error:
        report = dict(proper=False, error=str(error))
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if report.get("proper", False) else 1


if __name__ == "__main__":
    sys.exit(main())
