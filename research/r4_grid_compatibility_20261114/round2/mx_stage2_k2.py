"""MX stage 2, part 1 (k = 2, exact): which outside-cell L's kill relaxed diagonals.

Setting: 2 colors, n x n square, L = (x,y),(x+d,y),(x+d,y+d), d > 0.
- A diagonal word w in {0,1}^n is RELAXED-FEASIBLE if both classes are Sidon sets
  (no repeated positive difference, which includes 3-term progressions). That is the
  same-class relaxation at k = 2 (relaxation_k2.py).
- Since R_2 = 5, no such word extends to a proper full coloring when n >= 5.

For every relaxed-feasible word with n in {5, 6, 7} (up to swapping the two colors),
this script finds:
- a minimum-cardinality set of L's whose not-all-equal constraints, together with the
  fixed diagonal, are already unsatisfiable. This is a smallest MUS over L-groups,
  computed by pysat.examples.optux.OptUx;
- the cell type of each cell in the core:
  D  diagonal cell (i,i);
  S  same-class lower cell (v,u), u<v, w(u)=w(v);
  M  mixed lower cell (v,u), u<v, w(u)!=w(v);
  U  upper cell (x,y) with x<y.
A core containing only D and S cells would contradict relaxed feasibility, so every core
must contain M or U cells.
Every reported core is re-checked: it is UNSAT (complete enumeration of its free cells),
and removing any single L makes it SAT. Smallest-ness relies on OptUx.
Usage: python mx_stage2_k2.py
"""
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path

from pysat.examples.optux import OptUx
from pysat.formula import WCNF

HERE = Path(__file__).resolve().parent


def sidon(S):
    ds = [b - a for a, b in combinations(sorted(S), 2)]
    return len(ds) == len(set(ds))


def ells(n):
    return [((x, y), (x + d, y), (x + d, y + d)) for x in range(n) for y in range(n)
            for d in range(1, n - max(x, y))]


def cell_type(c, w):
    x, y = c
    if x == y:
        return "D"
    if x < y:
        return "U"
    return "S" if w[x] == w[y] else "M"


def var(n, c):
    return c[0] * n + c[1] + 1


def satisfiable(Ls, n, w):
    """Complete check by enumeration over the free cells of the given L's."""
    cells = sorted({c for L in Ls for c in L if c[0] != c[1]})
    idx = {c: i for i, c in enumerate(cells)}
    for bits in product((0, 1), repeat=len(cells)):
        def col(c):
            return w[c[0]] if c[0] == c[1] else bits[idx[c]]
        if all(len({col(c) for c in L}) == 2 for L in Ls):
            return True
    return False


def smallest_core(n, w):
    Ls = ells(n)
    wc = WCNF()
    for i, c in enumerate(w):
        wc.append([var(n, (i, i)) if c else -var(n, (i, i))])        # hard
    top = n * n
    sel = []
    for L in Ls:
        top += 1
        s = top
        sel.append(s)
        a = [var(n, c) for c in L]
        wc.append([-s] + a)
        wc.append([-s] + [-x for x in a])
    for s in sel:
        wc.append([s], weight=1)                                        # soft selectors
    with OptUx(wc, verbose=0) as o:
        core = o.compute()
    return [Ls[i - 1] for i in core]   # OptUx returns 1-based soft indices


def main():
    out = {"words": []}
    summary = Counter()
    for n in (5, 6, 7):
        for w in product((0, 1), repeat=n):
            if w[0] != 0:
                continue                                  # color swap symmetry
            A = [i for i in range(n) if w[i] == 0]
            B = [i for i in range(n) if w[i] == 1]
            if not (sidon(A) and sidon(B)):
                continue
            core = smallest_core(n, w)
            assert not satisfiable(core, n, w)
            for j in range(len(core)):
                assert satisfiable(core[:j] + core[j + 1:], n, w), "core not minimal"
            types = ["".join(cell_type(c, w) for c in L) for L in core]
            cells = {c for L in core for c in L}
            tc = Counter(cell_type(c, w) for c in cells)
            rec = {"n": n, "word": "".join(map(str, w)), "core_size": len(core),
                   "core": [[list(c) for c in L] for L in core], "L_types": types,
                   "cell_type_counts": dict(tc)}
            out["words"].append(rec)
            summary[(n, len(core), tuple(sorted(tc.items())))] += 1
            print(n, rec["word"], len(core), types, dict(tc), flush=True)
    out["summary"] = [{"n": k[0], "core_size": k[1], "cell_types": dict(k[2]), "words": v}
                      for k, v in sorted(summary.items())]
    (HERE / "mx_stage2_k2.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
