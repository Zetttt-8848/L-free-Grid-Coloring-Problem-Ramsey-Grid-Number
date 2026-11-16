# Two-diagonal product classes: refutation and surviving constraint

## Definitions

For a proper four-coloring `chi` of `[n]^2`, let
`W_c[y]=chi(y+c,y)` whenever `0<=c<n` and `0<=y<n-c`. For fixed `c>0` and
colors `a,b`, define

```text
J_(a,b)={y : W_0[y]=a and W_c[y]=b}.
```

## Candidate O1

The candidate asserted that for every lag `h>0` and every `u` with
`u,u+h in J_(a,b)`, the main-diagonal completion `chi(u+h,u)` avoids both `a`
and `b`. If true, it would split these starts into at most two Golomb classes
when `a!=b`, and at most three when `a=b`.

## Coordinate obstruction

The main-diagonal pair at indices `u,u+h` belongs to the L

```text
(u,u), (u+h,u), (u+h,u+h).
```

Properness excludes color `a` only at `chi(u+h,u)=W_h[u]`.

The off-diagonal pair on `W_c` at the same indices belongs to the different L

```text
(u+c,u), (u+h+c,u), (u+h+c,u+h).
```

Properness excludes color `b` at `chi(u+h+c,u)=W_(c+h)[u]`, not at
`chi(u+h,u)`. For `c>0`, these completion cells are distinct. Thus the proposed
palette reduction does not follow.

## Complete counterexample

**O1 is REFUTED.** The following zero-based row matrix is a proper four-coloring
of the full 3 by 3 square:

```text
0 0 0
1 0 1
0 1 1
```

Set `c=h=1`, `a=0`, `b=1`, and `u=0`. Then

```text
W_0[0]=chi(0,0)=0,
W_0[1]=chi(1,1)=0,
W_1[0]=chi(1,0)=1,
W_1[1]=chi(2,1)=1.
```

Therefore `0,1 in J_(0,1)`, but the main completion is
`chi(1,0)=1=b`, contrary to O1. The off-diagonal exclusion instead applies at
`chi(2,0)=0`, a different cell. `verify_counterexample.py` checks all five Ls
in the square and every prescribed entry directly from the definition.

The generator examined 18 assignments before returning this first witness from
the prescribed 1024-assignment domain. This number documents the run only; the
full witness, not the early stop, is the mathematical evidence.

## Surviving single-lag restriction

A weaker statement remains true and is already implicit in the usual source
restriction. If `u,u+c in J_(a,a)`, then the main-diagonal L of lag `c` would be
monochromatic because its completion is

```text
chi(u+c,u)=W_c[u]=a.
```

Hence `F_c(J_(a,a))` is empty. For `a!=b`, no analogous exclusion of `b` from
that completion follows. For `h!=c`, even the equality of the completion with
`W_c[u]` disappears.

This single-lag restriction does not supply the proposed sixteen-class fiber
capacity and is not claimed as a new numerical mechanism.

## Status

- O1: REFUTED by a complete full-square witness, independently checked.
- Sixteen-class capacity consumer: not executed because its premise is false.
- R_3 and R_4 numerical bounds: unchanged.
- Other cross-lag couplings using shared completion cells: not addressed by this
  counterexample, but they must be checked against existing cross-source work
  before use.
