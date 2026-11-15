"""D1 bounded falsification search for the pre-registered candidates U1 and UW(1).

See ../D1_PREREGISTRATION.md for the candidates, written before this search.
Domain: finite D, proper 3-colorings chi of V(D) = {(v,u): u<v, u,v in D},
found by randomized min-conflict local search. Every coloring that is used is
re-checked against every L of V(D) by check_proper(), independently of the
search code. This is a falsification search only. It gives no completeness
claim and no evidence at the R4 scale.

Usage: python d1_search.py [seconds] [seed]
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ells(D):
    """All L's of V(D): cells (v,u),(v+t,u),(v+t,u+t) with u<v, t>0, all in D."""
    S = set(D)
    out = []
    for u in D:
        for v in D:
            if v <= u:
                continue
            for t in range(1, max(D) - v + 1):
                if (u + t) in S and (v + t) in S:
                    out.append(((v, u), (v + t, u), (v + t, u + t)))
    return out


def check_proper(D, chi):
    """Independent check from the definition: no monochromatic directed L."""
    S = sorted(D)
    Sset = set(S)
    for (v, u) in chi:
        assert u < v and u in Sset and v in Sset
    assert len(chi) == len(S) * (len(S) - 1) // 2
    for i, u in enumerate(S):
        for v in S[i + 1:]:
            for t in range(1, S[-1] + 1):
                if (u + t) in Sset and (v + t) in Sset:
                    if chi[(v, u)] == chi[(v + t, u)] == chi[(v + t, u + t)]:
                        return False
    return True


def color(D, rng, max_steps=200000):
    cells = [(v, u) for u in D for v in D if u < v]
    L = ells(D)
    by_cell = {c: [] for c in cells}
    for i, tri in enumerate(L):
        for c in tri:
            by_cell[c].append(i)
    chi = {c: rng.randrange(3) for c in cells}

    def bad(i):
        a, b, c = L[i]
        return chi[a] == chi[b] == chi[c]
    viol = {i for i in range(len(L)) if bad(i)}
    for _ in range(max_steps):
        if not viol:
            return chi
        i = rng.choice(tuple(viol)) if len(viol) < 64 else rng.sample(sorted(viol), 1)[0]
        best = None
        for c in L[i]:
            old = chi[c]
            for col in range(3):
                if col == old:
                    continue
                chi[c] = col
                score = sum(1 for j in by_cell[c] if bad(j)) - sum(
                    1 for j in by_cell[c] if j in viol)
                if best is None or score < best[0] or (score == best[0] and rng.random() < 0.3):
                    best = (score, c, col)
            chi[c] = old
        if rng.random() < 0.1:
            c = rng.choice(L[i])
            col = rng.choice([x for x in range(3) if x != chi[c]])
        else:
            _, c, col = best
        chi[c] = col
        for j in by_cell[c]:
            if bad(j):
                viol.add(j)
            else:
                viol.discard(j)
    return None


def statistics(D, chi):
    S = set(D)
    top = max(D) - min(D)
    cls = {}
    for d in range(1, top + 1):
        for e in range(3):
            cls[(e, d)] = set()
        for u in D:
            if u + d in S:
                cls[(chi[(u + d, u)], d)].add(u)
    rows = []
    for h in range(2, top + 1):
        F = [u for u in D if u + h in S]
        if not F:
            continue
        per = []
        for e in range(3):
            m = {}
            for d in range(1, h):
                X = cls[(e, d)]
                for u in X:
                    if u + h - d in X:
                        m[u] = m.get(u, 0) + 1
            N = sum(m.values())
            E2 = sum(x * x for x in m.values())
            denom = N + (N * N) / len(F)
            per.append({"e": e, "N": N, "sum_m2": E2, "union": len(m),
                        "u1_ratio": (E2 / denom) if N else 0.0})
            assert set(m) <= set(F)                       # R_e(h) inside F_h(D)
            assert not (set(m) & {u for u in F if chi[(u + h, u)] == e})   # S_e(h) avoids R_e(h)
        cover = sum(p["union"] for p in per)
        assert cover <= 2 * len(F)                        # double-cover bound
        rows.append({"h": h, "F": len(F), "per": per,
                     "uw_ratio": min(p["N"] for p in per) / len(F), "cover": cover})
    return rows


def main():
    seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 600
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261114
    rng = random.Random(seed)
    t0 = time.time()
    best_u1, best_uw = None, None
    tried = found = 0
    log = []
    while time.time() - t0 < seconds:
        if rng.random() < 0.5:
            m = rng.randrange(6, 19)
            D = list(range(m))
        else:
            L = rng.randrange(10, 40)
            k = rng.randrange(6, min(L, 22))
            D = sorted(rng.sample(range(L + 1), k))
            D = [x - D[0] for x in D]
        tried += 1
        chi = color(D, rng, max_steps=40000)
        if chi is None:
            continue
        assert check_proper(D, chi), "local search returned an improper coloring"
        found += 1
        for row in statistics(D, chi):
            for p in row["per"]:
                if best_u1 is None or p["u1_ratio"] > best_u1[0]:
                    best_u1 = (p["u1_ratio"], D, chi, row["h"], p, row["F"])
            if best_uw is None or row["uw_ratio"] > best_uw[0]:
                best_uw = (row["uw_ratio"], D, chi, row["h"], row)
    def pack(D, chi):
        return {"D": D, "chi": [[v, u, c] for (v, u), c in sorted(chi.items())]}
    out = {"seed": seed, "seconds": seconds, "instances_tried": tried, "proper_colorings": found,
           "U1_max_ratio": best_u1[0] if best_u1 else None,
           "U1_violated": bool(best_u1 and best_u1[0] > 1.5),
           "UW1_max_ratio": best_uw[0] if best_uw else None,
           "UW1_violated": bool(best_uw and best_uw[0] > 1.0)}
    if best_u1:
        out["U1_witness"] = dict(pack(best_u1[1], best_u1[2]), h=best_u1[3], e=best_u1[4]["e"],
                                 F=best_u1[5], N=best_u1[4]["N"], sum_m2=best_u1[4]["sum_m2"])
    if best_uw:
        out["UW1_witness"] = dict(pack(best_uw[1], best_uw[2]), h=best_uw[3],
                                  F=best_uw[4]["F"], N=[p["N"] for p in best_uw[4]["per"]])
    (HERE / f"d1_search_seed{seed}.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print({k: v for k, v in out.items() if not k.endswith("witness")})


if __name__ == "__main__":
    main()
