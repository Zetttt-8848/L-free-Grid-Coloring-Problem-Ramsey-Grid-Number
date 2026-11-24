"""Enumerate low-rainbow triangles by deleting a boundary line."""
import argparse
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import permutations
from math import comb
from pathlib import Path
from tempfile import TemporaryFile


def listed(args):
    with TemporaryFile() as out:
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=out, check=True)
        cases = int(result.stdout.split()[0])
        out.seek(0)
        words = set()
        for line in out:
            tag, word = line.split()
            assert tag == b"witness"
            words.add(word)
        return cases, words


def seed(executable, n, budget, jobs):
    edges = comb(n, 3)
    catalog = set()
    with ThreadPoolExecutor(jobs) as pool:
        for k in range(budget+1):
            bounds = [(0, 0)] if not k else [(i, min(i+3, edges-1)) for i in range(0, edges, 4)]
            commands = [[executable, str(n), "all", str(k), str(i), str(j), "list"] for i, j in bounds]
            cases = 0
            for size, words in pool.map(listed, commands):
                cases += size
                catalog.update(words)
            assert cases == comb(edges, k)
    return catalog


def extend(executable, n, budget, words):
    with TemporaryFile() as source, TemporaryFile() as dest:
        source.writelines(w+b"\n" for w in words)
        source.seek(0)
        subprocess.run([executable, str(n), str(budget)], stdin=source, stdout=dest, check=True)
        dest.seek(0)
        return {line.split()[1] for line in dest}


def cost(n, w):
    def i(x, y):
        return x*(x-1)//2+y
    c = Counter(len({w[i(x,y)], w[i(x+d,y)], w[i(x+d,y+d)]})
                for x in range(1,n) for y in range(x) for d in range(1,n-x))
    assert len(w) == comb(n,2) and c[1] == 0
    return c[3]


def orientations(n, w):
    forms = set()
    for p in permutations(range(3)):
        b = bytearray()
        for x in range(1,n):
            for y in range(x):
                t = (x-y-1, y, n-x-1)
                yy, xx = t[p[1]], 1+t[p[0]]+t[p[1]]
                b.append(w[xx*(xx-1)//2+yy])
        labels = {}
        forms.add(bytes(labels.setdefault(c, 48+len(labels)) for c in b))
    assert w == min(forms)
    return forms


def orbit(n, w):
    return len(orientations(n, w))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("search", help="compiled verify_rainbow_neighborhood.c")
    parser.add_argument("extend", help="compiled verify_triangle_extensions.c")
    parser.add_argument("--target", type=int, default=12)
    parser.add_argument("--budget", type=int, default=5)
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()
    first = args.target-args.budget+3
    assert 5 <= first <= args.target <= 14
    search, extender = str(Path(args.search).resolve()), str(Path(args.extend).resolve())
    words = seed(search, first, 3, args.jobs)
    print(f"T{first}, budget 3, {len(words):,} geometric and palette orbits", flush=True)
    for n in range(first+1, args.target+1):
        bound = 3+n-first
        next_words = extend(extender, n-1, bound, words)
        _, shell = listed([search, str(n), "shell", str(bound), "0", "0", "list"])
        n_ext = len(next_words)
        next_words.update(shell)
        words = next_words
        print(f"T{n}, budget {bound}, extensions {n_ext:,}, interior-only {len(shell):,}, "
              f"union {len(words):,} orbits", flush=True)
    by_cost = Counter()
    for w in words:
        r = cost(args.target, w)
        assert r <= args.budget
        by_cost[r] += orbit(args.target, w)
    print("Palette classes at target:", dict(sorted(by_cost.items())), flush=True)
    if (args.target, args.budget) == (12, 5):
        assert not by_cost


if __name__ == "__main__":
    main()
