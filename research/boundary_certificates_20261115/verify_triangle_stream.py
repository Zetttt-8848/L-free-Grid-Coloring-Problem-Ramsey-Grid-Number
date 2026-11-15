"""Reconstruct the archived order-13 minimizers and the empty catalogs through order 15."""
import argparse
import lzma
import json
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from pathlib import Path
from tempfile import TemporaryFile

from verify_triangle_boundary import cost, orbit


def enumerate_shard(task):
    search, extend, first, target, final_budget, save_from, side, prefix = task
    budget = final_budget - (target-side)
    mode = "free" if side == first else "shell"
    with TemporaryFile() as stats:
        with subprocess.Popen([search, str(side), mode, str(budget), "0", "0", "stream", prefix],
                              stdout=subprocess.PIPE, stderr=stats) as process:
            with process.stdout:
                result = subprocess.run([extend, str(side), str(budget), str(target), str(save_from)],
                                        stdin=process.stdout, capture_output=True)
            if process.wait() or result.returncode:
                stats.seek(0)
                raise RuntimeError((side, prefix, stats.read(), result.stderr))
    counts = Counter()
    for row in result.stderr.splitlines():
        n, k, count = map(int, row.split())
        counts[n, k] += count
    return counts, result.stdout.splitlines()


def reconstruct(search, extend, first, target, budget, save_from, jobs):
    if not (5 <= first <= target <= 15 and first <= save_from <= target and budget >= target-first):
        raise ValueError("Invalid side, budget, or first saved order")
    tasks = [(search, extend, first, target, budget, save_from, n, "".join(prefix))
             for n in range(first, target+1) for prefix in product("012", repeat=3 if n>=10 else 2)]
    tasks.sort(key=lambda row: (sum(map(int, row[-1])), -row[-2], row[-1]))
    totals = Counter()
    words = {n: set() for n in range(save_from,target+1)}
    with ThreadPoolExecutor(jobs) as pool:
        for counts, rows in pool.map(enumerate_shard, tasks):
            totals.update(counts)
            for row in rows:
                side, score, word = row.split()
                n = int(side)
                assert word not in words[n] and cost(n, word) == int(score)
                words[n].add(word)
    for n in range(first,target+1):
        by_cost = {k:c for (side,k),c in sorted(totals.items()) if side == n}
        print(f"T{n} through {budget+n-target} rainbows: {sum(by_cost.values()):,} orbits, {by_cost}.")
        if n in words:
            assert len(words[n]) == sum(by_cost.values())
            print(f"  {sum(orbit(n,w) for w in words[n]):,} classes up to palette permutations.")
    return totals, words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("search", type=Path)
    parser.add_argument("extend", type=Path)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--order-13-through-12", action="store_true",
                        help="rebuild all order-13 colorings through twelve rainbows and order 14 through thirteen")
    args = parser.parse_args()
    if args.order_13_through_12:
        counts, words = reconstruct(str(args.search.resolve()), str(args.extend.resolve()),
                                    6, 14, 13, 13, args.jobs)
        archived = set(lzma.decompress(Path(__file__).with_name("triangle_13_through_12.txt.xz").read_bytes()).splitlines())
        assert len(archived)==488 and archived==words[13] and not words[14]
        assert counts[13,11]==21 and counts[13,12]==467
        assert sum(orbit(13,w) for w in archived)==2928
        return
    counts, words = reconstruct(str(args.search.resolve()), str(args.extend.resolve()),
                                6, 15, 13, 13, args.jobs)
    archived = json.loads(Path(__file__).with_name("triangle_13_minimizers.json").read_text())
    assert {w.decode() for w in words[13]} == set(archived)
    assert counts[13,11] == len(archived) == 21 and not words[14] and not words[15]
    assert sum(orbit(13,w) for w in words[13]) == 126


if __name__ == "__main__":
    main()
