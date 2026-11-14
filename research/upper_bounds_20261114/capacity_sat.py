"""Exact finite relaxations of the directed L-grid problem, encoded as SAT.

Forbidden configuration in an n x n grid: cells (x, y), (x+d, y), (x+d, y+d),
d > 0, one color.  A cell (v, u) with u < v is identified with the pair {u, v}.
In this pair language a forbidden L inside the strict source V(A) of a set A is

    u < v, d > 0, u, u+d, v, v+d in A, and z{u,v} = z{u,v+d} = z{u+d,v+d}.

(Cell (v,u) -> pair {u,v}; cell (v+d,u) -> {u,v+d}; cell (v+d,u+d) -> {u+d,v+d}.)

Two problems are encoded.

partition(n, k): is there a map a: {0..n-1} -> {0..k-1} (diagonal classes) and a
    map z on pairs {u<v} with a(u) = a(v) to {0..k-1} such that
      (i)  z{u,v} != a(u) whenever a(u) = a(v)      (diagonal exclusion), and
      (ii) no forbidden L as above with u, u+d, v, v+d all in one class?
    A proper k-coloring chi of the n x n square yields such a pair
    (a(i) = chi(i,i), z{u,v} = chi(v,u)), so UNSAT implies R_k <= n.

capacity(L, j, s): is there A in {0..L} with |A| >= s and a proper j-coloring of
    V(A)?  UNSAT means f_j(L) < s.

Symmetry breaking for partition: simultaneous relabelling of classes and colors
by one permutation of {0..k-1} maps solutions to solutions, so we may require
the classes to appear in first-occurrence order 0, 1, 2, ... (a standard
value-symmetry break; sound because every solution has a relabelled image
satisfying it).  No other symmetry is used.  The capacity problem uses no
symmetry breaking.
"""
import argparse
import itertools
import json
import sys
import time

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool


def l_configs(n):
    """All (u, v, d) with u < v, d >= 1, v + d <= n - 1."""
    for u in range(n):
        for v in range(u + 1, n):
            for d in range(1, n - v):
                yield u, v, d


def exactly_one(cnf, lits):
    cnf.append(list(lits))
    for p, q in itertools.combinations(lits, 2):
        cnf.append([-p, -q])


def encode_partition(n, k, symmetry=True):
    pool = IDPool()
    cnf = CNF()
    A = lambda i, c: pool.id(("a", i, c))
    Z = lambda u, v, e: pool.id(("z", u, v, e))
    for i in range(n):
        exactly_one(cnf, [A(i, c) for c in range(k)])
    for u in range(n):
        for v in range(u + 1, n):
            # at least one color and at most one color for every pair (harmless
            # for pairs whose endpoints lie in different classes)
            exactly_one(cnf, [Z(u, v, e) for e in range(k)])
            for c in range(k):
                cnf.append([-A(u, c), -A(v, c), -Z(u, v, c)])
    for u, v, d in l_configs(n):
        pts = sorted({u, u + d, v, v + d})
        for c in range(k):
            for e in range(k):
                if e == c:
                    continue  # already excluded by diagonal exclusion
                cnf.append([-A(p, c) for p in pts]
                           + [-Z(u, v, e), -Z(u, v + d, e), -Z(u + d, v + d, e)])
    if symmetry:
        # first-occurrence order: class c may occur at i only if class c-1 occurs before i
        cnf.append([A(0, 0)])
        for c in range(2, k):
            for i in range(n):
                cnf.append([-A(i, c)] + [A(j, c - 1) for j in range(i)])
    return cnf, pool


def encode_grid(n, k, symmetry=True):
    """Full problem: proper k-coloring of the n x n grid (cells (x, y), 0-based).

    Symmetry breaking (optional): colors appear in first-occurrence order along
    the main diagonal (0,0), (1,1), ...; sound because color permutations map
    proper colorings to proper colorings.
    """
    pool = IDPool()
    cnf = CNF()
    C = lambda x, y, e: pool.id(("c", x, y, e))
    for x in range(n):
        for y in range(n):
            exactly_one(cnf, [C(x, y, e) for e in range(k)])
    for x in range(n):
        for y in range(n):
            for d in range(1, n - max(x, y)):
                for e in range(k):
                    cnf.append([-C(x, y, e), -C(x + d, y, e), -C(x + d, y + d, e)])
    if symmetry:
        cnf.append([C(0, 0, 0)])
        for e in range(2, k):
            for i in range(n):
                cnf.append([-C(i, i, e)] + [C(j, j, e - 1) for j in range(i)])
    return cnf, pool


def encode_triangle(n, k, symmetry=True):
    """Weak lower triangle {(x, y): 0 <= y <= x <= n-1} of the n x n grid.

    Every forbidden L of the square whose three cells satisfy x >= y lies in
    this triangle, and conversely every L with corner (x, y), x >= y, has all
    three cells in it (x+d >= y and x+d >= y+d).  A proper k-coloring of the
    square restricts to a proper k-coloring of the triangle, so UNSAT implies
    R_k <= n.  Symmetry breaking as in encode_grid (colors in first-occurrence
    order along the diagonal).
    """
    pool = IDPool()
    cnf = CNF()
    C = lambda x, y, e: pool.id(("c", x, y, e))
    for x in range(n):
        for y in range(x + 1):
            exactly_one(cnf, [C(x, y, e) for e in range(k)])
    for x in range(n):
        for y in range(x + 1):
            for d in range(1, n - x):
                for e in range(k):
                    cnf.append([-C(x, y, e), -C(x + d, y, e), -C(x + d, y + d, e)])
    if symmetry:
        cnf.append([C(0, 0, 0)])
        for e in range(2, k):
            for i in range(n):
                cnf.append([-C(i, i, e)] + [C(j, j, e - 1) for j in range(i)])
    return cnf, pool


def encode_capacity(L, j, s, card=EncType.seqcounter):
    pool = IDPool()
    cnf = CNF()
    X = lambda i: pool.id(("x", i))
    Z = lambda u, v, e: pool.id(("z", u, v, e))
    n = L + 1
    for u in range(n):
        for v in range(u + 1, n):
            if j == 1:
                continue
            exactly_one(cnf, [Z(u, v, e) for e in range(j)])
    for u, v, d in l_configs(n):
        pts = sorted({u, u + d, v, v + d})
        if j == 1:
            cnf.append([-X(p) for p in pts])
            continue
        for e in range(j):
            cnf.append([-X(p) for p in pts]
                       + [-Z(u, v, e), -Z(u, v + d, e), -Z(u + d, v + d, e)])
    xs = [X(i) for i in range(n)]
    enc = CardEnc.atleast(lits=xs, bound=s, top_id=pool.top, encoding=card)
    cnf.extend(enc.clauses)
    return cnf, pool


def solve(cnf, solver_name="cadical195", time_limit=None):
    from pysat.solvers import Solver
    t0 = time.time()
    with Solver(name=solver_name, bootstrap_with=cnf.clauses) as s:
        res = s.solve()
        model = s.get_model() if res else None
    return res, model, time.time() - t0


def decode_partition(model, pool, n, k):
    pos = set(l for l in model if l > 0)
    cls = [next(c for c in range(k) if pool.id(("a", i, c)) in pos) for i in range(n)]
    z = {}
    for u in range(n):
        for v in range(u + 1, n):
            if cls[u] == cls[v]:
                z[(u, v)] = next(e for e in range(k) if pool.id(("z", u, v, e)) in pos)
    return cls, z


def check_partition(n, k, cls, z):
    for (u, v), e in z.items():
        if e == cls[u]:
            return False
    for u, v, d in l_configs(n):
        pts = {u, u + d, v, v + d}
        if len({cls[p] for p in pts}) == 1:
            if z[(u, v)] == z[(u, v + d)] == z[(u + d, v + d)]:
                return False
    return True


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("partition")
    p.add_argument("--n", type=int, nargs="+", required=True)
    p.add_argument("--k", type=int, default=3)
    p.add_argument("--solver", default="cadical195")
    p.add_argument("--dimacs", default=None, help="write CNF for the single n given")
    g = sub.add_parser("grid")
    g.add_argument("--n", type=int, nargs="+", required=True)
    g.add_argument("--k", type=int, default=3)
    g.add_argument("--solver", default="cadical195")
    g.add_argument("--dimacs", default=None)
    t = sub.add_parser("triangle")
    t.add_argument("--n", type=int, nargs="+", required=True)
    t.add_argument("--k", type=int, default=3)
    t.add_argument("--solver", default="cadical195")
    t.add_argument("--dimacs", default=None)
    c = sub.add_parser("capacity")
    c.add_argument("--L", type=int, required=True)
    c.add_argument("--j", type=int, default=2)
    c.add_argument("--s", type=int, required=True)
    c.add_argument("--solver", default="cadical195")
    c.add_argument("--dimacs", default=None)
    args = ap.parse_args()
    if args.cmd == "partition":
        for n in args.n:
            cnf, pool = encode_partition(n, args.k)
            if args.dimacs:
                cnf.to_file(args.dimacs)
            res, model, dt = solve(cnf, args.solver)
            out = {"problem": "partition", "n": n, "k": args.k, "vars": cnf.nv,
                   "clauses": len(cnf.clauses), "sat": res, "seconds": round(dt, 3)}
            if res:
                cls, z = decode_partition(model, pool, n, args.k)
                out["checked"] = check_partition(n, args.k, cls, z)
                out["classes"] = "".join(map(str, cls))
            print(json.dumps(out), flush=True)
    elif args.cmd in ("grid", "triangle"):
        enc = encode_grid if args.cmd == "grid" else encode_triangle
        for n in args.n:
            cnf, pool = enc(n, args.k)
            if args.dimacs:
                cnf.to_file(args.dimacs)
            res, model, dt = solve(cnf, args.solver)
            print(json.dumps({"problem": args.cmd, "n": n, "k": args.k, "vars": cnf.nv,
                              "clauses": len(cnf.clauses), "sat": res,
                              "seconds": round(dt, 3)}), flush=True)
    else:
        cnf, pool = encode_capacity(args.L, args.j, args.s)
        if args.dimacs:
            cnf.to_file(args.dimacs)
        res, model, dt = solve(cnf, args.solver)
        out = {"problem": "capacity", "L": args.L, "j": args.j, "s": args.s,
               "vars": cnf.nv, "clauses": len(cnf.clauses), "sat": res, "seconds": round(dt, 3)}
        if res:
            pos = set(l for l in model if l > 0)
            out["set"] = [i for i in range(args.L + 1) if pool.id(("x", i)) in pos]
        print(json.dumps(out), flush=True)


if __name__ == "__main__":
    sys.exit(main())
