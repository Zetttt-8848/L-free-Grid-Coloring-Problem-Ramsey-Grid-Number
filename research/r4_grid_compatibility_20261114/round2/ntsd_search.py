"""Lane B round 2, pilot 1: search for near-maximal TSD instances (see PREREGISTRATION.md).

A TSD instance: disjoint Sidon sets A, B inside an interval of m+1 integers, and a proper
2-coloring c of V(U), U = A ∪ B, with c = 0 on A-pairs and c = 1 on B-pairs. Only the
mixed pairs are free. Colorability is decided by a complete backtracking search, and
every reported coloring is re-checked by check_tsd(), which is independent of the
search code.

Candidate families:
  (ii)  translate and reflected-translate pairs of Golomb rulers G recalled from memory
        (each is verified Sidon here), trimmed greedily until colorable;
  (iii) random greedy growth: add points to A or B while both stay Sidon and the
        instance stays colorable. This is a direct lower-bound search for max rho.

Q(m) uses the optimal Golomb ruler lengths for up to 28 marks, cited from memory.
The elementary upper bound on Q (verify_four_rank) is also reported, giving a
conservative rho.

Usage: python ntsd_search.py [seconds]
"""
import json
import random
import sys
import time
from bisect import bisect_right
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "boundary_certificates_20261115"))
import verify_four_rank as vr  # noqa: E402

OGR_LEN = {1: 0, 2: 1, 3: 3, 4: 6, 5: 11, 6: 17, 7: 25, 8: 34, 9: 44, 10: 55, 11: 72, 12: 85,
           13: 106, 14: 127, 15: 151, 16: 177, 17: 199, 18: 216, 19: 246, 20: 283, 21: 333,
           22: 356, 23: 372, 24: 425, 25: 480, 26: 492, 27: 553, 28: 585}  # cited from memory
RULERS = {  # recalled from memory; each is verified Sidon below, so only its length matters
    10: [0, 1, 6, 10, 23, 26, 34, 41, 53, 55],
    11: [0, 1, 4, 13, 28, 33, 47, 54, 64, 70, 72],
    12: [0, 2, 6, 24, 29, 40, 43, 55, 68, 75, 76, 85],
    13: [0, 2, 5, 25, 37, 43, 59, 70, 85, 89, 98, 99, 106],
    14: [0, 4, 6, 20, 35, 52, 59, 77, 78, 86, 89, 99, 122, 127],
}
G_EL = vr.golomb_spans()


def Q_ogr(m):
    return max(k for k, L in OGR_LEN.items() if L <= m)


def Q_el(m):
    return bisect_right(G_EL, m) - 1


def is_sidon(X):
    seen = set()
    X = sorted(X)
    for i, a in enumerate(X):
        for b in X[i + 1:]:
            if b - a in seen:
                return False
            seen.add(b - a)
    return True


def colorable(A, B):
    U = sorted(set(A) | set(B))
    inA, inB = set(A), set(B)
    pairs = [(x, y) for i, x in enumerate(U) for y in U[i + 1:]]
    idx = {p: i for i, p in enumerate(pairs)}
    val = [-1] * len(pairs)
    for (x, y), i in idx.items():
        if x in inA and y in inA:
            val[i] = 0
        elif x in inB and y in inB:
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
    for a, b, c in cons:   # constraints violated by the fixed values alone
        if val[a] == val[b] == val[c] != -1:
            return None

    def assign(i, bit, trail):
        stack = [(i, bit)]
        while stack:
            x, bx = stack.pop()
            if val[x] != -1:
                if val[x] != bx:
                    return False
                continue
            val[x] = bx
            trail.append(x)
            for j in occ[x]:
                a, b, c = cons[j]
                vs = (val[a], val[b], val[c])
                if vs[0] == vs[1] == vs[2] != -1:
                    return False
                if vs.count(-1) == 1:
                    kn = [w for w in vs if w != -1]
                    if kn[0] == kn[1]:
                        stack.append(((a, b, c)[vs.index(-1)], 1 - kn[0]))
        return True

    # initial propagation from fixed values
    trail0 = []
    for j, (a, b, c) in enumerate(cons):
        vs = (val[a], val[b], val[c])
        if vs.count(-1) == 1:
            kn = [w for w in vs if w != -1]
            if kn[0] == kn[1]:
                if not assign((a, b, c)[vs.index(-1)], 1 - kn[0], trail0):
                    return None
    free = sorted((i for i in range(len(pairs)) if val[i] == -1), key=lambda i: -len(occ[i]))

    def search(k):
        while k < len(free) and val[free[k]] != -1:
            k += 1
        if k == len(free):
            return True
        x = free[k]
        for bit in (0, 1):
            tr = []
            if assign(x, bit, tr) and search(k + 1):
                return True
            for y in tr:
                val[y] = -1
        return False

    sys.setrecursionlimit(10000)
    if search(0):
        return {p: val[i] for p, i in idx.items()}
    return None


def check_tsd(A, B, c):
    A, B = set(A), set(B)
    assert not (A & B) and is_sidon(A) and is_sidon(B)
    U = sorted(A | B)
    S = set(U)
    for (x, y), b in c.items():
        if x in A and y in A:
            assert b == 0
        if x in B and y in B:
            assert b == 1
    for i, u in enumerate(U):
        for v in U[i + 1:]:
            for g in range(1, U[-1] + 1):
                if u + g in S and v + g in S:
                    if c[(u, u + g)] == c[(v, v + g)] == c[(u, v + g)]:
                        return False
    return True


def trim_until_colorable(A, B, rng, tries=20):
    best = None
    for _ in range(tries):
        a, b = list(A), list(B)
        while True:
            c = colorable(a, b)
            if c is not None:
                break
            if len(a) >= len(b):
                a.pop(rng.randrange(len(a)))
            else:
                b.pop(rng.randrange(len(b)))
        if best is None or min(len(a), len(b)) > min(len(best[0]), len(best[1])):
            best = (a, b, c)
    return best


def record(rows, kind, A, B, c):
    U = sorted(set(A) | set(B))
    m = U[-1] - U[0]
    assert check_tsd(A, B, c)
    k = min(len(A), len(B))
    rows.append({"kind": kind, "m": m, "A": sorted(A), "B": sorted(B), "min_size": k,
                 "Q_ogr": Q_ogr(m), "Q_el": Q_el(m),
                 "rho_ogr": k / Q_ogr(m), "rho_el": k / Q_el(m)})


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 780
    t0 = time.time()
    rng = random.Random(20261122)
    rows = []
    for k, G in RULERS.items():
        assert is_sidon(G) and G[-1] == OGR_LEN[k], ("ruler", k)
    # (ii) translate / reflected-translate pairs, trimmed
    for k, G in RULERS.items():
        L = G[-1]
        for kind, base in (("translate", G), ("reflect", [L - x for x in G])):
            for t in range(1, 30):
                Bset = [x + t for x in base]
                if set(G) & set(Bset):
                    continue
                best = trim_until_colorable(G, Bset, rng, tries=8)
                record(rows, f"{kind}-k{k}-t{t}", best[0], best[1], best[2])
                break
        if time.time() - t0 > budget / 2:
            break
    # (iii) random greedy growth at fixed spans
    spans = [50, 100, 150, 200, 300]
    per = (budget - (time.time() - t0)) / len(spans)
    for m in spans:
        tend = time.time() + per
        best = None
        while time.time() < tend:
            A, B = [], []
            order = list(range(m + 1))
            rng.shuffle(order)
            for x in order:
                if time.time() > tend:
                    break
                for side in ((A, B) if len(A) <= len(B) else (B, A)):
                    other = B if side is A else A
                    if x in other or not is_sidon(side + [x]):
                        continue
                    side.append(x)
                    if colorable(A, B) is None:
                        side.pop()
                        continue
                    break
            if len(A) and len(B) and (best is None or min(len(A), len(B)) > min(len(best[0]), len(best[1]))):
                c = colorable(A, B)
                if c is not None:
                    best = (list(A), list(B), c)
        if best:
            record(rows, f"greedy-m{m}", best[0], best[1], best[2])
        print(rows[-1] if rows else None, flush=True)
    out = {"budget_s": budget, "elapsed_s": round(time.time() - t0, 1), "instances": rows,
           "max_rho_ogr_m_ge_100": max((r["rho_ogr"] for r in rows if r["m"] >= 100), default=None),
           "max_rho_el_m_ge_100": max((r["rho_el"] for r in rows if r["m"] >= 100), default=None)}
    (HERE / "ntsd_search_results.json").write_text(json.dumps(out, indent=1) + "\n")
    for r in rows:
        print(r["kind"], "m", r["m"], "min", r["min_size"], "Q_ogr", r["Q_ogr"], "rho", round(r["rho_ogr"], 3))
    print("max rho (m>=100):", out["max_rho_ogr_m_ge_100"], "elapsed", out["elapsed_s"])


if __name__ == "__main__":
    main()
