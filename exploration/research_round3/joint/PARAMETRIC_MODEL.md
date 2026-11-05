# Compact model for the uniform block obstruction

This is an exact encoding of the already certified two-parameter family;
it is not an extra mathematical assumption. Let h be a positive integer.
For each start i, define indicators

    L_(i,h) = AND_{j in {0,1,2,4,5,6}} x_(i+jh),
    K_(i,h) = AND_{j in {0,3,4,5}} x_(i+jh),
    J_(i,h) = AND_{j in {0,1,2,5}} x_(i+jh).

Each start is restricted so every displayed position is in [n]. A
forward forbidden copy is exactly a pair L_(i,h)=K_(z,h)=1 with
z>i+6h. Its parameter b is z-i and satisfies b>6h.

Under position reflection t->n+1-t, an L-start i becomes an L-start
n+1-i-6h; a J-start y becomes a K-start n+1-y-5h. Applying the forward
inequality to the reflected set therefore gives the second condition:
forbid J_(y,h)=L_(i,h)=1 whenever i>y+5h. Equivalently, if the relevant
start sets are nonempty, require

    max K - min L <= 6h,
    max L - min J <= 5h.

The smallest possible forward span is 11h+1. Thus h>(n-2)//11 cannot
produce a forbidden copy in [n]. At n=464 only h=1,...,42 is relevant.

The search implementation maintains one Fenwick tree for each of L,K,J
and each h. Inserting an L-start i creates exactly
|{z in K:z>i+6h}|+|{y in J:y<i-5h}| forbidden start pairs. Inserting a
K-start z creates |{i in L:i<z-6h}| pairs; inserting a J-start y creates
|{i in L:i>y+5h}| pairs. Deletions negate these changes. Every change
updates its own tree after counting its partners. Sequential changes
therefore count cross-interactions exactly once. Rejected swaps undo
these changes in reverse order. A separate random-toggle check compares
every tree update with direct start-pair enumeration.

An exact CP/SAT alternative needs no ten-point copy list. For each h,
let P^L_t=OR_{i<=t} L_(i,h) and P^J_t=OR_{y<=t} J_(y,h). Prefix ORs
are defined recursively, with empty prefixes false. Add

    NOT K_(z,h) OR NOT P^L_(z-6h-1),
    NOT L_(i,h) OR NOT P^J_(i-5h-1).

The definitions of the block indicators and prefix ORs must be exact
equivalences. These clauses are equivalent to excluding every forward
and reflected forbidden start pair. This formulation is specified for
the next proof-producing solver iteration; the current run uses the
exact score and independent literal-set checker instead.

The checker uses a different method: materialize all actual L,K,J starts
from the saved set, then test every pair in the two displayed relations.
It does not import or reuse the Fenwick implementation.
