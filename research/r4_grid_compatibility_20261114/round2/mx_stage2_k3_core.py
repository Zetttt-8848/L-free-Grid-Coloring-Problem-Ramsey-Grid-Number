"""MX stage 2, part 2 (k = 3): an UNSAT core for the relaxed diagonal that has no full
extension at n = 21 (mx_extension_probe.json, trial 2).

There is one selector variable per L. CaDiCaL is solved under the assumption that every
selector is true, and the core is read off. The core is then shrunk by re-solving under
the core alone, up to a time budget. Removal of single L's is tried while the budget
lasts. This gives a small core, not a guaranteed minimum.

Each core cell is classified as D (diagonal), S (same-class lower cell), M (mixed lower
cell) or U (upper cell). The final core is confirmed UNSAT by Glucose 4 on the
restricted formula: the fixed diagonal, one-hot cells, and the core L's only.
Usage: python mx_stage2_k3_core.py [seconds]
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

from pysat.solvers import Solver

HERE = Path(__file__).resolve().parent
K = 3


def build(n, diag, Ls):
    v = lambda x, y, c: (x * n + y) * K + c + 1   # noqa: E731
    base = []
    for x in range(n):
        for y in range(n):
            base.append([v(x, y, c) for c in range(K)])
            for a in range(K):
                for b in range(a + 1, K):
                    base.append([-v(x, y, a), -v(x, y, b)])
    for i, c in enumerate(diag):
        base.append([v(i, i, c)])
    top = n * n * K
    sel, groups = [], []
    for L in Ls:
        top += 1
        sel.append(top)
        groups.append([[-top] + [-v(*cell, c) for cell in L] for c in range(K)])
    return base, sel, groups


def ctype(c, diag):
    x, y = c
    if x == y:
        return "D"
    if x < y:
        return "U"
    return "S" if diag[x] == diag[y] else "M"


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 600
    t0 = time.time()
    probe = json.loads((HERE / "mx_extension_probe.json").read_text())
    row = next(r for r in probe["rows"] if r["full_extension"] is False)
    diag, n = row["diagonal"], row["n"]
    Ls = [((x, y), (x + d, y), (x + d, y + d)) for x in range(n) for y in range(n)
          for d in range(1, n - max(x, y))]
    base, sel, groups = build(n, diag, Ls)
    s = Solver(name="cadical153", bootstrap_with=base)
    for g in groups:
        for cl in g:
            s.add_clause(cl)
    assert s.solve(assumptions=sel) is False
    core = sorted(set(s.get_core()))
    history = [len(core)]
    while time.time() - t0 < budget / 2:
        assert s.solve(assumptions=core) is False
        new = sorted(set(s.get_core()))
        history.append(len(new))
        if len(new) >= len(core):
            break
        core = new
    # deletion pass under the remaining budget (conflict-limited checks)
    i = 0
    while i < len(core) and time.time() - t0 < budget:
        trial = core[:i] + core[i + 1:]
        s.conf_budget(20000)
        r = s.solve_limited(assumptions=trial)
        if r is False:
            core = sorted(set(s.get_core()) & set(trial))
        else:
            i += 1
    idx = {sv: j for j, sv in enumerate(sel)}
    coreL = [Ls[idx[sv]] for sv in core]
    # confirm with a second solver on the restricted formula
    with Solver(name="glucose4", bootstrap_with=base) as g:
        for sv in core:
            for cl in groups[idx[sv]]:
                g.add_clause(cl[1:])
        confirmed = g.solve() is False
    cells = {c for L in coreL for c in L}
    out = {"n": n, "diagonal": diag, "class_sizes": dict(Counter(diag)),
           "core_size_history": history, "core_size": len(coreL),
           "confirmed_unsat_glucose4": confirmed,
           "deletion_pass_complete": i >= len(core),
           "cell_types": dict(Counter(ctype(c, diag) for c in cells)),
           "L_types": dict(Counter("".join(ctype(c, diag) for c in L) for L in coreL)),
           "uses_upper_cells": any(ctype(c, diag) == "U" for c in cells),
           "core": [[list(c) for c in L] for L in coreL],
           "elapsed_s": round(time.time() - t0, 1)}
    (HERE / "mx_stage2_k3_core.json").write_text(json.dumps(out, indent=1) + "\n")
    print({k: v for k, v in out.items() if k not in ("core", "diagonal")})


if __name__ == "__main__":
    main()
