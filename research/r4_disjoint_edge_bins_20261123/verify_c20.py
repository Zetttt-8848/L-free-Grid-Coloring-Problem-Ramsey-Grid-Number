"""Exhaustively check the binary-source capacity C(20)=13."""

import itertools
import json
from math import comb
import time
from pathlib import Path


def ells(A):
    S = set(A)
    out = []
    for u in A:
        for v in A:
            if v <= u:
                continue
            for t in range(1, max(A) - v + 1):
                if u + t in S and v + t in S:
                    out.append(((v, u), (v + t, u), (v + t, u + t)))
    return out


def colorable(A):
    """Return a proper 2-coloring dict of V(A), or None if none exists (complete search)."""
    cells = [(v, u) for u in A for v in A if u < v]
    idx = {c: i for i, c in enumerate(cells)}
    cons = [tuple(idx[c] for c in L) for L in ells(A)]
    occ = [[] for _ in cells]
    for j, c in enumerate(cons):
        for x in c:
            occ[x].append(j)
    order = sorted(range(len(cells)), key=lambda i: -len(occ[i]))
    val = [-1] * len(cells)

    def assign(i, b, trail):
        stack = [(i, b)]
        while stack:
            x, bx = stack.pop()
            if val[x] != -1:
                if val[x] != bx:
                    return False
                continue
            val[x] = bx
            trail.append(x)
            for j in occ[x]:
                a, b2, c = cons[j]
                vs = (val[a], val[b2], val[c])
                if vs[0] == vs[1] == vs[2] != -1:
                    return False
                if vs.count(-1) == 1:
                    known = [w for w in vs if w != -1]
                    if known[0] == known[1]:
                        free = (a, b2, c)[vs.index(-1)]
                        stack.append((free, 1 - known[0]))
        return True

    def undo(trail):
        for x in trail:
            val[x] = -1

    def search(pos):
        while pos < len(order) and val[order[pos]] != -1:
            pos += 1
        if pos == len(order):
            return True
        x = order[pos]
        for b in (0, 1):
            trail = []
            if assign(x, b, trail) and search(pos + 1):
                return True
            undo(trail)
        return False

    if not cons:
        return {c: 0 for c in cells}
    # Color permutation symmetry: fix the first branching variable to 0 (sound).
    trail = []
    if not assign(order[0], 0, trail):
        return None
    if search(1):
        return {c: val[idx[c]] for c in cells}
    return None


def check_proper(A, chi):
    S = set(A)
    for u in A:
        for v in A:
            if v <= u:
                continue
            for t in range(1, max(A) + 1):
                if u + t in S and v + t in S:
                    if chi[(v, u)] == chi[(v + t, u)] == chi[(v + t, u + t)]:
                        return False
    return True


def none_colorable(n, k, deadline):
    count = 0
    for rest in itertools.combinations(range(1, n), k - 1):
        if time.time() > deadline:
            return None, count
        A = (0,) + rest
        count += 1
        if colorable(A) is not None:
            return False, count
    return True, count


def main():
    archive = json.loads(Path(__file__).with_name("c20_witness.json").read_bytes())
    marks = archive["k13_witness_A"]
    coloring = {(x, y): c for x, y, c in archive["k13_witness_coloring"]}
    assert len(marks) == 13 and 0 == min(marks) <= max(marks) < 20
    assert set(coloring) == {(v, u) for u in marks for v in marks if u < v}
    assert set(coloring.values()) <= {0, 1}
    assert check_proper(marks, coloring)
    excluded, count = none_colorable(20, 14, float("inf"))
    assert excluded and count == comb(19, 13)
    print(f"C(20)=13; all {count} normalized 14-subsets fail and the 13-mark witness is proper.")


if __name__ == "__main__":
    main()
