"""Lane B round 2, pilot 2: completeness of the catalogued conflicts on small translate pairs.

See PREREGISTRATION_PILOT2.md. For each instance (A, B = A+t) this reports:
- colorability (complete search, imported from ntsd_search, with colorings re-checked);
- C-collisions (Lemma C);
- type I and type II conflicts (Proposition 2G), computed from the definitions;
- whether plain unit propagation from the fixed A-pairs and B-pairs alone gives a contradiction;
- the number of branch decisions a complete search needs to refute the instance.

Usage: python conflict_check.py [seconds]
"""
import json
import random
import sys
import time
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ntsd_search as ns  # noqa: E402


# ---------- Bose sets ----------
def bose(q):
    """Bose Sidon set {k in [0,q^2-2] : g^k - g in GF(q)} for a primitive g of GF(q^2)."""
    nr = next(x for x in range(2, q) if pow(x, (q - 1) // 2, q) == q - 1)  # non-residue

    def mul(a, b):  # (a0 + a1 w)(b0 + b1 w), w^2 = nr
        return ((a[0] * b[0] + nr * a[1] * b[1]) % q, (a[0] * b[1] + a[1] * b[0]) % q)

    N = q * q - 1
    for c0 in range(q):
        for c1 in range(1, q):
            g = (c0, c1)
            x, order = g, 1
            while x != (1, 0):
                x = mul(x, g)
                order += 1
            if order == N:
                A, x = [], (1, 0)
                for k in range(N):
                    if ((x[0] - g[0]) % q, (x[1] - g[1]) % q)[1] == 0:
                        A.append(k)
                    x = mul(x, g)
                return A, N
    raise ValueError("no primitive element")


def make_instance(q, t, rng):
    A0, N = bose(q)
    while True:
        u = rng.randrange(1, N)
        if gcd(u, N) == 1:
            break
    s = rng.randrange(N)
    A = sorted((u * a + s) % N for a in A0)
    assert ns.is_sidon(A), "Bose image not Sidon in Z"
    # greedy deletion of points carrying differences in [1, 2t]
    A = list(A)
    while True:
        cnt = {x: 0 for x in A}
        for i, x in enumerate(A):
            for y in A[i + 1:]:
                if y - x <= 2 * t:
                    cnt[x] += 1
                    cnt[y] += 1
        worst = max(cnt.values())
        if worst == 0:
            break
        cands = [x for x in A if cnt[x] == worst]
        A.remove(rng.choice(cands))
    B = [x + t for x in A]
    assert not set(A) & set(B) and ns.is_sidon(B)
    return A, B, (u, s)


# ---------- catalogue ----------
def analyse(A, B):
    sA, sB = set(A), set(B)
    U = sorted(sA | sB)
    S = set(U)
    M = U[-1] - U[0]
    alphaA = {y - x: x for i, x in enumerate(A) for y in A[i + 1:]}
    alphaB = {y - x: x for i, x in enumerate(B) for y in B[i + 1:]}
    mixed = lambda x, y: not ((x in sA and y in sA) or (x in sB and y in sB))
    phi = {}           # (g, p) -> 0/1
    collisions = []
    for g in range(1, M + 1):
        aA, aB = alphaA.get(g), alphaB.get(g)
        for p in U:
            if p + g not in S:
                continue
            vals = set()
            if p in sA and p + g in sA:
                vals.add(0)
            elif p in sB and p + g in sB:
                vals.add(1)
            elif p in sA:                      # AB start
                if aA is not None and aA > p:
                    vals.add(1)
                if aB is not None and aB < p:
                    vals.add(0)
            else:                              # BA start
                if aB is not None and aB > p:
                    vals.add(0)
                if aA is not None and aA < p:
                    vals.add(1)
            if len(vals) == 2:
                collisions.append((g, p))
            elif vals:
                phi[(g, p)] = vals.pop()
    forced = {}        # mixed cell -> set of (value, lag)
    direct = []        # forcing contradicting a fixed in-set pair
    for g in range(1, M + 1):
        starts = [p for p in U if (g, p) in phi]
        for i, p in enumerate(starts):
            for qq in starts[i + 1:]:
                f = phi[(g, p)]
                if phi[(g, qq)] != f:
                    continue
                x, y = p, qq + g
                if mixed(x, y):
                    forced.setdefault((x, y), set()).add((1 - f, g))
                else:
                    fixed = 0 if x in sA else 1
                    if fixed != 1 - f:
                        direct.append((x, y, g))
    type1 = [(x, y, v, g) for (x, y), fs in forced.items() for (v, g) in fs
             if (y - x, x) in phi and phi[(y - x, x)] == 1 - v]
    type2 = [(x, y) for (x, y), fs in forced.items() if len({v for v, _ in fs}) == 2]
    return {"C_collisions": len(collisions), "type_I": len(type1), "type_II": len(type2),
            "direct_fixed_conflicts": len(direct),
            "type_I_example": type1[:1], "type_II_example": type2[:1]}


def propagation_and_search(A, B):
    """Unit propagation from fixed values alone, then complete search with a decision counter."""
    U = sorted(set(A) | set(B))
    sA, sB = set(A), set(B)
    pairs = [(x, y) for i, x in enumerate(U) for y in U[i + 1:]]
    idx = {p: i for i, p in enumerate(pairs)}
    val = [-1] * len(pairs)
    for (x, y), i in idx.items():
        if x in sA and y in sA:
            val[i] = 0
        elif x in sB and y in sB:
            val[i] = 1
    S = set(U)
    cons = []
    for i, u in enumerate(U):
        for v in U[i + 1:]:
            for g in range(1, U[-1] - u + 1):
                if u + g in S and v + g in S:
                    cons.append((idx[(u, u + g)], idx[(v, v + g)], idx[(u, v + g)]))
    occ = [[] for _ in pairs]
    for j, c in enumerate(cons):
        for x in c:
            occ[x].append(j)

    def propagate(queue, trail):
        while queue:
            j = queue.pop()
            a, b, c = cons[j]
            vs = (val[a], val[b], val[c])
            if vs[0] == vs[1] == vs[2] != -1:
                return False
            if vs.count(-1) == 1:
                kn = [w for w in vs if w != -1]
                if kn[0] == kn[1]:
                    x = (a, b, c)[vs.index(-1)]
                    val[x] = 1 - kn[0]
                    trail.append(x)
                    queue.extend(occ[x])
        return True

    ok = propagate(list(range(len(cons))), [])
    if not ok:
        return {"refuted_by_propagation": True, "decisions": 0, "colorable": False}
    decisions = [0]

    def search():
        free = [i for i in range(len(pairs)) if val[i] == -1]
        if not free:
            return True
        x = max(free, key=lambda i: len(occ[i]))
        for bit in (0, 1):
            decisions[0] += 1
            trail = [x]
            val[x] = bit
            if propagate(list(occ[x]), trail) and search():
                return True
            for y in trail:
                val[y] = -1
        return False

    col = search()
    return {"refuted_by_propagation": False, "decisions": decisions[0], "colorable": col}


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 780
    t0 = time.time()
    rng = random.Random(20261122)
    rows = []
    plan = [(q, t) for q in (13, 17, 19) for t in (1, 2, 3)]
    per = budget / len(plan)
    for q, t in plan:
        tend = time.time() + per
        n = 0
        while time.time() < tend and n < 25:
            A, B, us = make_instance(q, t, rng)
            n += 1
            c = ns.colorable(A, B)
            if c is not None:
                assert ns.check_tsd(A, B, c)
            an = analyse(A, B)
            if c is not None:  # soundness: a certificate of uncolorability must not fire
                assert an["C_collisions"] == an["type_I"] == an["type_II"] == an["direct_fixed_conflicts"] == 0
            row = {"q": q, "t": t, "u_s": us, "size": len(A), "colorable": c is not None, **an}
            if c is None:
                ps = propagation_and_search(A, B)
                assert ps["colorable"] is False
                row.update(ps)
                row["A"] = A
            rows.append(row)
        print(q, t, "instances", n, flush=True)
    unc = [r for r in rows if not r["colorable"]]
    uncovered = [r for r in unc if r["C_collisions"] == 0 and r["type_I"] == 0 and r["type_II"] == 0
                 and r["direct_fixed_conflicts"] == 0]
    out = {"elapsed_s": round(time.time() - t0, 1), "instances": len(rows),
           "colorable": sum(r["colorable"] for r in rows), "uncolorable": len(unc),
           "uncolorable_with_C_collision": sum(r["C_collisions"] > 0 for r in unc),
           "uncolorable_with_type_I_or_II": sum((r["type_I"] + r["type_II"]) > 0 for r in unc),
           "uncolorable_not_covered": len(uncovered),
           "not_covered_refuted_by_propagation": sum(r["refuted_by_propagation"] for r in uncovered),
           "not_covered_max_decisions": max((r["decisions"] for r in uncovered), default=None),
           "rows": rows}
    (HERE / "conflict_check_results.json").write_text(json.dumps(out, indent=1) + "\n")
    print({k: v for k, v in out.items() if k != "rows"})
    for r in uncovered:
        print("NOT COVERED:", r["q"], r["t"], r["size"], "propagation", r["refuted_by_propagation"], "decisions", r["decisions"])


if __name__ == "__main__":
    main()
