"""Sanity check of the same-class relaxation at two colors (exact, small).

Relaxation: keep the main diagonal and the same-class cells (v,u), u<v, diag(u)=diag(v),
together with every L lying inside them. These L's never mix diagonal color classes, so
the relaxed problem decomposes by color class. With two colors, each class must be a
Sidon set (including no 3-term progressions). n_rel(2) is the largest n such that
[0,n) splits into two Sidon sets. It is compared with the full problem: the largest
n with a proper 2-coloring of the n x n square (complete SAT check).
Usage: python relaxation_k2.py
"""
from itertools import product, combinations
from pysat.solvers import Cadical153
def sidon(S):
    ds=[b-a for a,b in combinations(sorted(S),2)]; return len(ds)==len(set(ds))
def rel2(n):
    return any(sidon([i for i in range(n) if m>>i&1]) and sidon([i for i in range(n) if not m>>i&1]) for m in range(1<<(n-1)))
def full(n,k):
    v=lambda x,y,c:(x*n+y)*k+c+1; s=Cadical153()
    for x in range(n):
        for y in range(n): s.add_clause([v(x,y,c) for c in range(k)])
    for x in range(n):
        for y in range(n):
            for d in range(1,n):
                if x+d<n and y+d<n:
                    for c in range(k): s.add_clause([-v(x,y,c),-v(x+d,y,c),-v(x+d,y+d,c)])
    return s.solve()
print("n_rel(2):", max(n for n in range(2,14) if rel2(n)), [ (n,rel2(n)) for n in range(5,12)])
print("full k=2:", [(n,full(n,2)) for n in range(3,7)])
