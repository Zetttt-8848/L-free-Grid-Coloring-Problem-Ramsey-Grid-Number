"""MX stage 1 (pre-registered in NEXT_TARGETS.md section 2): exact n_rel(3).

n_rel(3) is the largest n such that [0, n) splits into three sets D_1, D_2, D_3, each a
binary source: V(D) = {(v,u) : u < v in D} has a 2-coloring with no monochromatic L
(x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D).
This is the same-class relaxation of the three-color square problem. The L's of the
square that lie inside the diagonal and the same-class cells never mix classes. The
diagonal-corner L's only say that a same-class cell avoids the class color, which leaves
two colors.

Encoding (CNF):
- p[i][c]: position i lies in class c, with exactly one class per position. Symmetry
  breaking: p[0][0], which is valid because the classes are interchangeable.
- z[v,u]: one color bit for every pair u < v. A pair is used only when u and v share a
  class, and then its bit selects one of that class's two colors.
- For every L (x,y,t) with y < x, x+t < n and every class c: if x, y, x+t, y+t all lie
  in class c, the bits of (x,y), (x+t,y), (x+t,y+t) are not all equal (two clauses).
Splittability is hereditary in n (restrict to a prefix), so n is scanned upward until
the first UNSAT.

Evidence:
- SAT: the witness is re-checked against every L by direct code. Each class is also
  re-decided colorable by the independent backtracking solver
  ../review_codex_r3/check_finite_caps.colorable.
- UNSAT: confirmed by two different solvers (CaDiCaL 1.5.3 and Glucose 4), as
  pre-registered. No DRAT check was done.
Usage: python mx_stage1.py [seconds] [start_n]
Results are written after every row, so an interrupted run keeps its rows.
"""
import json
import sys
import time
from itertools import combinations
from pathlib import Path

from pysat.formula import CNF
from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "review_codex_r3"))
import check_finite_caps as cfc   # noqa: E402

K = 3


def encode(n):
    cnf = CNF()
    p = {(i, c): i * K + c + 1 for i in range(n) for c in range(K)}
    top = n * K
    z = {}
    for u, v in combinations(range(n), 2):
        top += 1
        z[(v, u)] = top
    for i in range(n):
        cnf.append([p[(i, c)] for c in range(K)])
        for a, b in combinations(range(K), 2):
            cnf.append([-p[(i, a)], -p[(i, b)]])
    cnf.append([p[(0, 0)]])
    for y in range(n):
        for x in range(y + 1, n):
            for t in range(1, n - x):
                pts = sorted({x, y, x + t, y + t})
                cells = [z[(x, y)], z[(x + t, y)], z[(x + t, y + t)]]
                for c in range(K):
                    guard = [-p[(i, c)] for i in pts]
                    cnf.append(guard + cells)
                    cnf.append(guard + [-a for a in cells])
    return cnf, p, z


def solve(cnf, name):
    with Solver(name=name, bootstrap_with=cnf.clauses) as s:
        ok = s.solve()
        return ok, (s.get_model() if ok else None)


def check_witness(n, model, p, z):
    pos = set(l for l in model if l > 0)
    cls = [[i for i in range(n) if p[(i, c)] in pos] for c in range(K)]
    assert sorted(sum(cls, [])) == list(range(n))
    col = {cell: (z[cell] in pos) for cell in z}
    for D in cls:
        S = set(D)
        for y in D:
            for x in D:
                if x <= y:
                    continue
                for t in range(1, n - x):
                    if x + t in S and y + t in S:
                        vals = {col[(x, y)], col[(x + t, y)], col[(x + t, y + t)]}
                        assert len(vals) == 2, ("monochromatic L", x, y, t)
        if len(D) >= 2:
            base = [d - D[0] for d in D]
            assert cfc.colorable(base) is not None, "independent solver disagrees"
    return cls


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 840
    t0 = time.time()
    out = {"rows": []}
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    out["start_n"] = n
    last_sat = None
    while time.time() - t0 < budget:
        cnf, p, z = encode(n)
        t1 = time.time()
        ok, model = solve(cnf, "cadical153")
        row = {"n": n, "clauses": len(cnf.clauses), "cadical153": ok,
               "seconds": round(time.time() - t1, 2)}
        if ok:
            row["classes"] = check_witness(n, model, p, z)
            row["witness_checked"] = True
            last_sat = n
        else:
            ok2, _ = solve(cnf, "glucose4")
            row["glucose4"] = ok2
            assert ok2 is False, "solvers disagree"
        out["rows"].append(row)
        print({k: v for k, v in row.items() if k != "classes"}, flush=True)
        out["n_rel_3_lower"] = last_sat
        (HERE / "mx_stage1_results.json").write_text(json.dumps(out, indent=1) + "\n")
        if not ok:
            break
        n += 1
    out["n_rel_3_lower"] = last_sat
    out["n_rel_3_exact"] = last_sat if out["rows"] and out["rows"][-1].get("cadical153") is False else None
    out["elapsed_s"] = round(time.time() - t0, 1)
    (HERE / "mx_stage1_results.json").write_text(json.dumps(out, indent=1) + "\n")
    print("n_rel(3) exact:", out["n_rel_3_exact"], "largest SAT:", last_sat)


if __name__ == "__main__":
    main()
