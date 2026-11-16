# Contract: two-diagonal product classes

Date: 2026-11-15. Author: Kimi. Branch:
`kimi/r4-off-diagonal-20261115`. Base: Kimi round 1 at
`252bdcfb9da09eb149a7e5c0505d512fbd907405`.

## Object and coordinates

A proper four-coloring `chi` of a full zero-based square. For `0<=c<n` and
`0<=y<n-c`, define the diagonal word `W_c[y]=chi(y+c,y)`. The forbidden L is
`(x,y),(x+d,y),(x+d,y+d)` with integer `d>0`.

For fixed `c>0` and colors `a,b`, consider product positions

```text
J_(a,b)={y : W_0[y]=a and W_c[y]=b}.
```

## Information retained

The incumbent uses the main-diagonal color classes and treats other diagonal
words only as completion colors. The candidate retains joint membership in a
main-diagonal class and an off-diagonal class.

## Exact candidate statement to falsify

O1. For every lag `h>0`, the main-diagonal completion colors
`chi(u+h,u)` at starts `u in F_h(J_(a,b))` avoid both `a` and `b`.
Consequently these starts would split by completion color into at most two
Golomb sets when `a!=b`, and at most three when `a=b`, enabling a sixteen-class
capacity consumer.

## Cheapest discriminating test and stop condition

Expand the two relevant Ls coordinate by coordinate. Search a complete proper
3 by 3 four-coloring with `c=h=1`, `a=0`, `b=1`, `u=0`, and prescribed word
entries `W_0[0]=W_0[1]=0`, `W_1[0]=W_1[1]=1`, but `chi(1,0)=1`.
Such a witness directly refutes O1.

If found, stop O1 and do not run the sixteen-class capacity computation. Record
which weaker cross-lag constraints survive. If no witness occurs in the complete
finite assignment search, prove the exclusion before any consumer calculation.

## Consumer if successful

Only a valid O1 would justify sixteen joint capacities and a full-square shift
count. Without O1 there is no consumer and no numerical claim.

## Evidence

A counterexample requires the full matrix and an independent check of every L
and every prescribed entry. Any solver failure or incomplete enumeration would
be UNDECIDED. No Ramsey bound is claimed by this contract.
