# PROPERTY (formal)

For an integer `n>=1`, let the object universe be every total function
`chi:{0,...,n-1}^2->{1,2,3}`.  The labels of cells and colors are retained in
witness files; only the explicitly proved color-permutation normalization is
used in the SAT search.

For integers `x,y,d`, a mandated corner is

`C(x,y;d)=((x,y),(x+d,y),(x+d,y+d))`,

where `0<=x,y<n` and `1<=d<min(n-x,n-y)`.  A coloring is corner-free exactly
when the three values on every such `C(x,y;d)` are not all equal.

The fixed claim under investigation is whether a corner-free coloring exists
at `n=21`.  There are exactly

`sum_{d=1}^{20}(21-d)^2=sum_{m=1}^{20}m^2=20*21*41/6=2870`

mandated geometric corners.  A complete side-21 witness would prove
`R_3(L)>=22`; a certified exhaustive impossibility result, combined with the
inherited side-20 witness, would prove `R_3(L)=21`.  Timeout, interruption, raw
solver UNSAT, and an unverified trace do not prove impossibility.

