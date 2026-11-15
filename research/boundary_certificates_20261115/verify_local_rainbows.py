"""Verify exact small-triangle minima and neighborhoods around two larger examples."""
import argparse
import json
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def literal(n, rows):
    assert [len(r) for r in rows] == list(range(1, n))
    assert set("".join(rows)) <= set("012")
    counts = Counter(
        len({rows[x-1][y], rows[x+d-1][y], rows[x+d-1][y+d]})
        for x in range(1, n) for y in range(x) for d in range(1, n-x)
    )
    assert sum(counts.values()) == comb(n, 3) and counts[1] == 0
    return counts[3]


def tally(executable, n, word, k, edges, pool):
    def run(bounds):
        low, high = bounds
        run = subprocess.run([executable, str(n), word, str(k), str(low), str(high)],
                             capture_output=True, text=True, check=True)
        cases, visits, *hits = run.stdout.split()
        counts = {}
        for hit in hits:
            rain, number = map(int, hit.split(":"))
            counts[rain] = number
        return int(cases), int(visits), counts

    intervals = [(0, 0)] if not k else [(i, min(i+2, edges-1)) for i in range(0, edges, 3)]
    cases = visits = 0
    counts = Counter()
    for c, v, h in pool.map(run, intervals):
        cases += c
        visits += v
        counts.update(h)
    assert cases == comb(edges, k)
    if k == 0:
        # The first cell is fixed. The other two palette labels can still be exchanged.
        assert all(v % 2 == 0 for v in counts.values())
        counts = Counter({a: b // 2 for a, b in counts.items()})
    print(f"T{n}, {'global' if word == 'all' else 'fixed support'}, k={k}, "
          f"{cases:,} supports, {visits:,} nodes, palette classes {dict(counts)}", flush=True)
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("executable", help="compiled verify_rainbow_neighborhood.c")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--group", choices=("small", "neighbors", "all"), default="all")
    args = parser.parse_args()
    executable = str(Path(args.executable).resolve())
    small = json.loads((ROOT / "small_triangle_rainbows.json").read_text())
    refs = json.loads((ROOT / "triangle_literal_examples.json").read_text())
    for n, rows in small.items():
        n = int(n)
        assert literal(n, rows) == {9: 0, 10: 1, 11: 3, 12: 6}[n]
    with ThreadPoolExecutor(args.jobs) as pool:
        if args.group in ("small", "all"):
            for n, k, expected in [(9, 0, {0: 42}), (10, 0, {}), (10, 1, {1: 12}),
                                   (11, 0, {}), (11, 1, {}), (11, 2, {}), (11, 3, {3: 66})]:
                assert tally(executable, n, "all", k, comb(n, 3), pool) == expected
        if args.group in ("neighbors", "all"):
            for n, cost, rows in [(13, 11, [{11: 1}, {12: 3}, {12: 3, 13: 10}]),
                                  (14, 17, [{17: 2}, {18: 5}, {18: 16, 19: 7}])]:
                ref = refs[str(n)]
                assert literal(n, ref) == cost
                for k, expected in enumerate(rows):
                    assert tally(executable, n, "".join(ref), k, comb(n, 3)-cost, pool) == expected


if __name__ == "__main__":
    main()
