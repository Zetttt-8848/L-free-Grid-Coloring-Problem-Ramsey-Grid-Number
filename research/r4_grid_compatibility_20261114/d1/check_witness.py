"""Independent checker for D1 witnesses. It shares no code with d1_search.py.

For a witness (D, chi, h[, e]) it recomputes from the definitions:
  * that chi colors every cell (v,u), u<v in D, with a color in {0,1,2};
  * that no directed L (x,y),(x+t,y),(x+t,y+t), t>0, with all three cells in
    V(D), is monochromatic (every triple of cells is tested);
  * S_e(d), F_h(D), m_{e,h}(u), N_e(h) and sum_u m^2;
  * the U1 and UW(1) inequalities of D1_PREREGISTRATION.md.
Usage: python check_witness.py <results.json>
"""
import itertools
import json
import sys
from fractions import Fraction


def verify(D, chi_list):
    D = sorted(D)
    chi = {(v, u): c for v, u, c in chi_list}
    cells = {(v, u) for u in D for v in D if u < v}
    assert set(chi) == cells, "coloring domain"
    assert all(c in (0, 1, 2) for c in chi.values()), "palette"
    # Brute force over all ordered triples of cells in the L shape.
    for (x, y) in cells:
        for (x2, y2) in cells:
            t = x2 - x
            if y2 != y or t <= 0:
                continue
            third = (x2, y + t)
            if third in cells and chi[(x, y)] == chi[(x2, y)] == chi[third]:
                raise AssertionError(f"monochromatic L at {(x, y)}, {(x2, y)}, {third}")
    return chi


def stats(D, chi, h, e):
    S = set(D)
    cls = lambda d: {u for u in D if u + d in S and chi[(u + d, u)] == e}
    F = [u for u in D if u + h in S]
    m = {}
    for d in range(1, h):
        X = cls(d)
        for u in X:
            if u + (h - d) in X:
                m[u] = m.get(u, 0) + 1
    N = sum(m.values())
    E2 = sum(v * v for v in m.values())
    return len(F), N, E2, m


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    w = data["U1_witness"]
    chi = verify(w["D"], w["chi"])
    F, N, E2, m = stats(w["D"], chi, w["h"], w["e"])
    rhs = Fraction(3, 2) * (N + Fraction(N * N, F))
    print(f"U1 witness: |D|={len(w['D'])}, h={w['h']}, e={w['e']}, |F_h|={F}, N={N}, "
          f"sum m^2={E2}, (3/2)(N+N^2/|F|)={rhs}  -> U1 {'VIOLATED' if E2 > rhs else 'holds'}")
    w = data["UW1_witness"]
    chi = verify(w["D"], w["chi"])
    Ns, Fh = [], None
    for e in range(3):
        F, N, _, _ = stats(w["D"], chi, w["h"], e)
        Fh = F
        Ns.append(N)
    print(f"UW(1) witness: |D|={len(w['D'])}, h={w['h']}, |F_h|={Fh}, N_e={Ns} "
          f"-> UW(1) {'VIOLATED' if min(Ns) > Fh else 'holds'}")


if __name__ == "__main__":
    main(sys.argv[1])
