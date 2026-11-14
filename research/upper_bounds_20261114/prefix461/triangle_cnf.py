"""CNF for a proper three-coloring of an initial region of the square with a fixed diagonal.

Coordinates: cell (x, y), 0 <= x, y <= m-1, x = column, y = row; the forbidden
shape is (x,y), (x+d,y), (x+d,y+d), d > 0.  The diagonal cell (i,i) has color
word[i] for i < len(word).

Regions:
  'tri'   : cells with y <= x <= m-1 (weak lower triangle in this convention).
  'block' : all cells with 0 <= x, y <= m-1.
Every directed L whose three cells lie in the region gives, for each color c,
the clause (-v1c | -v2c | -v3c).  Every cell gets an at-least-one clause.
Dropping at-most-one clauses is sound: from any model choose one true color per
cell; all L clauses stay satisfied.  Hence UNSAT of this CNF implies that no
proper coloring of the region with this diagonal exists.
"""
import hashlib


def build(word, m=None, region="tri"):
    b = len(word)
    m = b if m is None else m
    cells = {}
    if region == "tri":
        for y in range(m):
            for x in range(y, m):
                cells[(x, y)] = len(cells)
    elif region == "block":
        for y in range(m):
            for x in range(m):
                cells[(x, y)] = len(cells)
    else:
        raise ValueError(region)
    var = lambda cell, c: 3 * cells[cell] + c + 1
    clauses = []
    for cell in cells:
        clauses.append([var(cell, c) for c in range(3)])
    for i in range(min(b, m)):
        clauses.append([var((i, i), int(word[i]))])
    nL = 0
    for (x, y) in cells:
        for d in range(1, m):
            p2, p3 = (x + d, y), (x + d, y + d)
            if p2 in cells and p3 in cells:
                nL += 1
                for c in range(3):
                    clauses.append([-var((x, y), c), -var(p2, c), -var(p3, c)])
    nvars = 3 * len(cells)
    return nvars, clauses, nL


def dimacs(nvars, clauses):
    lines = [f"p cnf {nvars} {len(clauses)}"]
    lines += [" ".join(map(str, cl)) + " 0" for cl in clauses]
    return "\n".join(lines) + "\n"


def sha(nvars, clauses):
    return hashlib.sha256(dimacs(nvars, clauses).encode()).hexdigest()
