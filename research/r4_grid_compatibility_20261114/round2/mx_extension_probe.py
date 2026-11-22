"""MX stage 1, follow-up probe. This probe was NOT pre-registered: it was added after the
run to address the caveat that 21 is only a lower bound for the full square problem.

Question: take a diagonal word w that is feasible for the same-class relaxation. Does it
extend to a proper 3-coloring of the FULL n x n square with that diagonal?
- Only the diagonal is fixed.
- The same-class cells may be recolored within their two allowed colors, and every
  other cell is free.
If no relaxed-feasible diagonal extends, then the outside cells are what excludes these
words.

Each n uses diagonals from fresh relaxed witnesses: the class encoding of mx_stage1.py,
with a random clause blocking every earlier diagonal (exact clause on the class vector).
For each diagonal, the full-square CNF has one-hot colors per cell and three
not-all-equal clauses per L, and is solved with a conflict budget.
- SAT: the full coloring is re-checked against every L of the square.
- UNSAT: confirmed by a second solver.
- UNKNOWN: recorded as UNKNOWN.
Usage: python mx_extension_probe.py [seconds]
"""
import json
import sys
import time
from pathlib import Path

from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mx_stage1 as m1   # noqa: E402

K = 3


def full_cnf(n, diag):
    v = lambda x, y, c: (x * n + y) * K + c + 1   # noqa: E731
    cl = []
    for x in range(n):
        for y in range(n):
            cl.append([v(x, y, c) for c in range(K)])
            for a in range(K):
                for b in range(a + 1, K):
                    cl.append([-v(x, y, a), -v(x, y, b)])
    for i, c in enumerate(diag):
        cl.append([v(i, i, c)])
    for x in range(n):
        for y in range(n):
            for d in range(1, n - max(x, y)):
                for c in range(K):
                    cl.append([-v(x, y, c), -v(x + d, y, c), -v(x + d, y + d, c)])
    return cl, v


def check_full(n, model, v):
    pos = set(l for l in model if l > 0)
    col = [[next(c for c in range(K) if v(x, y, c) in pos) for y in range(n)] for x in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(1, n - max(x, y)):
                assert not (col[x][y] == col[x + d][y] == col[x + d][y + d])
    return True


def solve_limited(cl, name, conflicts):
    with Solver(name=name, bootstrap_with=cl) as s:
        s.conf_budget(conflicts)
        r = s.solve_limited()
        return r, (s.get_model() if r else None)


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 780
    t0 = time.time()
    out = {"rows": []}
    for n in (21, 24, 28, 34, 40):
        cnf, p, z = m1.encode(n)
        with Solver(name="cadical153", bootstrap_with=cnf.clauses) as rel:
            for trial in range(4):
                if time.time() - t0 > budget or not rel.solve():
                    break
                model = set(l for l in rel.get_model() if l > 0)
                diag = [next(c for c in range(K) if p[(i, c)] in model) for i in range(n)]
                rel.add_clause([-p[(i, diag[i])] for i in range(n)])     # block this word
                cl, v = full_cnf(n, diag)
                r, mdl = solve_limited(cl, "cadical153", 200000)
                row = {"n": n, "trial": trial, "diagonal": diag, "full_extension": r}
                if r is True:
                    row["checked"] = check_full(n, mdl, v)
                elif r is False:
                    r2, _ = solve_limited(cl, "glucose4", 10**7)
                    row["glucose4"] = r2
                    assert r2 is not True, "solvers disagree"
                out["rows"].append(row)
                print({k: x for k, x in row.items() if k != "diagonal"}, round(time.time() - t0), "s", flush=True)
                (HERE / "mx_extension_probe.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
