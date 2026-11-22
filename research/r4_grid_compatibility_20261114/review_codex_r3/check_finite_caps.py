"""Independent exhaustive check of the finite binary-source caps used by Codex round 3.

Claim under review (codex/r4-local-capacity-round3-20261114, THEOREM.md section 1):
    C(4)=4, C(8)=7, C(12)=9, C(16)=11, C(20)<=14,
where C(n) is the largest |A|, A subset {0..n-1}, whose strict source
V(A) = {(v,u): u<v, u,v in A} has a proper 2-coloring, i.e. one with no
monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t>0, with all three cells in V(A).

Method (shares no code with Codex): for each (n,k), enumerate every k-subset A of
{0..n-1} with 0 in A. Translation preserves properness, so this loses nothing.
Decide 2-colorability of V(A) with a complete backtracking search (a not-all-equal
constraint per L, unit propagation, exhaustive branching). Upper bounds need every
subset to be UNSAT. Lower bounds need one explicit coloring, re-checked against every L.

Heredity: a proper coloring of V(A) restricts to every subset of A. So "no k-subset
of {0..n-1} is colorable" also excludes every larger subset.

Usage: python check_finite_caps.py [time_limit_seconds]
"""
import itertools
import json
import sys
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


def witness(n, k):
    for rest in itertools.combinations(range(1, n), k - 1):
        A = (0,) + rest
        chi = colorable(A)
        if chi is not None:
            assert check_proper(A, chi)
            return A, chi
    return None


def main():
    limit = float(sys.argv[1]) if len(sys.argv) > 1 else 840
    t0 = time.time()
    deadline = t0 + limit
    out = {"claims": "C(4)=4, C(8)=7, C(12)=9, C(16)=11, C(20)<=14", "checks": []}
    # (n, k_upper_excluded, k_witness)
    plan = [(4, None, 4), (8, 8, 7), (12, 10, 9), (16, 12, 11), (20, 15, 12)]
    for n, kex, kw in plan:
        rec = {"n": n}
        if kw is not None:
            w = witness(n, kw)
            rec["witness_size"] = kw
            rec["witness_found"] = w is not None
            if w:
                rec["witness_A"] = list(w[0])
        if kex is not None:
            res, cnt = none_colorable(n, kex, deadline)
            rec["excluded_size"] = kex
            rec["subsets_checked"] = cnt
            rec["all_uncolorable"] = res  # True, False, or None (time limit)
        rec["elapsed_s"] = round(time.time() - t0, 1)
        out["checks"].append(rec)
        print(rec, flush=True)
    Path(__file__).with_name("finite_caps_check.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
