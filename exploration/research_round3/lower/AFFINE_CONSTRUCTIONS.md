# Restricted affine and circulant construction channel

## Difference-circulant family — PROVED exact ceiling

Fix any integer modulus `m>=1` and any total map
`f:Z_m->{1,2,3}`.  Consider

`chi(x,y)=f((y-x) mod m)`.

If this coloring is corner-free on side `n`, then `n<=3`.  Indeed, take any
`0<=i<j<n`, set `x=i`, `y=0`, and `d=j-i`.  The mandated corner

`((i,0),(j,0),(j,j-i))`

has difference residues `-i,-j,-i` modulo `m`.  Its first and third colors are
equal, so corner-freeness forces `f(-i) != f(-j)`.  Thus the `n` values
`f(0),f(-1),...,f(-(n-1))` are pairwise distinct.  Their codomain has size
three, proving `n<=3`.  This argument also handles repeated residues: a repeat
would demand a color differ from itself.

Equality is attained at `n=m=3` with `f(r)=r+1` on residues `0,1,2`.  The full
matrix is in `difference_circulant_n3.txt`; the independent direct verifier
checks all five mandated geometric corners and all entries in `{1,2,3}`.

This theorem closes only the one-dimensional difference-circulant premise.  It
does not constrain general grid colorings and is weaker than the inherited
side-20 construction.

## Modular-affine finite scan — UNDECIDED

The broader searched family is

`chi(x,y)=f((a*x+b*y) mod m)`

for all `2<=m<=50`, all ordered `(a,b) in Z_m^2`, and all total three-color
maps `f`, normalized by `f(0)=1` under color permutation.  SAT instances encode
the map `f` directly and include every literal side-21 corner induced by the
parameters.  The intended range contains exactly
`sum_{m=2}^{50}m^2=42924` parameter pairs.

The three bounded epochs attempted deterministic pair indices `0..26102`.
All 26103 calls returned raw UNSAT and none reached its 100000-conflict cap;
16821 pairs remain unattempted after R3-R5-E4 and R3-R5-E6.  No negative proof traces were
retained, so even the attempted portion carries solver telemetry only.  No
side-21 witness was found.  The broader family and the side-21 instance both
remain UNDECIDED.
