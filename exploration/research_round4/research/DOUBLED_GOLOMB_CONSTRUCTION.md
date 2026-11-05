# An explicit two-color weak triangle from a doubled Golomb ruler

Root construction, R4-RESEARCH-0003. This is a limitation on possible uniform fiber estimates, not a new upper bound. No priority claim is made.

Let A be any finite integer Golomb set with m marks and span L. Define

    S={2a,2a+1:a in A}.

There is a corner-free two-coloring of W(S). Consequently a universal upper bound for the number of diagonal marks in a two-color weak triangle of span 2L+1 must allow at least 2m marks.

Every element of S has a unique expression 2a+alpha, with a in A and alpha in {0,1}. Write a cell as (2b+beta,2a+alpha). On its diagonal assign color alpha. On an internal block cell (2a+1,2a), assign color 0. For b>a assign colors as follows:

| alpha (column parity) | beta (row parity) | color |
|---|---|---|
| 0 | 0 | 1 |
| 1 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 if b-a=1, and 0 otherwise |

These cases give every cell of W(S) a color. The exceptional entry in the last row is needed when A itself has consecutive marks.

## Proof of corner-freeness

Every directed L in W(S) has two distinct endpoints on a common slope-one diagonal of some offset d>=0. If these endpoints are (u+d,u) and (v+d,v), with u<v, the completion is (v+d,u). It is enough to prove that every equal-color endpoint pair has the opposite-color completion.

At d=0, equal-color endpoints have the same parity alpha. They belong to different blocks of A. Their completion has color 1-alpha by the first two rows of the table.

At d=1, there is one color-0 cell (2a+1,2a) for each a in A. There can also be an interblock cell (2a+2,2a+1) for a pair a,a+1 in A. There is at most one such pair by the Golomb property, and the exceptional entry assigns this cell color 1. Hence all equal-color pairs at this offset are pairs of internal block cells. Their completion is (2b+1,2a), with b>a, and the third row of the table assigns it color 1.

At d=2h>0, an endpoint must have equal row and column parity and satisfy b-a=h. There is at most one pair a,b by the Golomb property. The two possible cells have colors 1 and 0 respectively, so there is no equal-color pair.

At an odd offset d>=3, there is at most one cell with alpha=0,beta=1, from a pair of A of difference (d-1)/2; it has color 1. There is at most one with alpha=1,beta=0, from a pair of difference (d+1)/2; this difference is at least two, so that cell has color 0. There are no other cells at this offset. Again there is no equal-color pair.

All nonnegative offsets are covered, proving the construction. The set S has 2m marks and span 2L+1 directly from its definition.

The result applies to every literal Golomb ruler, with no appeal to a solver or to an asymptotic ruler-existence theorem. It allows a substantial number of diagonal marks even after all weak-triangle compatibility conditions are imposed. It does not decide whether a stronger bound than two separate ruler caps holds at the span needed for R3.
