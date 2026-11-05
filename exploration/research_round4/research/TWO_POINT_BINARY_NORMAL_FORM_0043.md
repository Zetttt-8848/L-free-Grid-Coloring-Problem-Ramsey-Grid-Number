# A two-pattern normal form for one-sided binary weak constraints

Root integration and additional derivation, continuation0043. The
complete two-point binary classification in
fibers/TWO_POINT_BINARY_OBSTRUCTION_TYPES_0043.md is used as an input.
Here the remaining direct-unit alternative is reduced to an exterior
doubling pattern. This gives a concise necessary-and-sufficient test
for the one-sided two-point binary subsystem, not for a full weak
extension with many marks in both classes.

Let B be Golomb and C={r,s}, r<s, be disjoint from B. Give B and C
their named diagonal colors. Same-class strict cells have the opposite
color. Normalize r=0,s=d>0 when displaying formulas.

## 1. An interior matching edge never has two B-unit endpoints

Take interior B marks p,q, possibly equal, with

    0<p,q<d,   p+q=d.

One matching edge has mixed variables

    X_(d,p) and X_(0,q),

both of interval length h=d-p=q. Let a<a+h be the unique B-pair
of length h, if it exists. The lower-oriented variable X_(d,p)
is a B-reflection unit only if a>p. The upper-oriented variable
X_(0,q) is a B-reflection unit only if a<0. These cannot both
hold, since p>0. If the difference is unsupported, neither
condition creates a unit in the first place.

The other interior matching edge is obtained by exchanging p,q.
The same proof includes the midpoint p=q=d/2. Therefore every
direct double-unit matching obstruction is exterior.

This argument uses the placement of the unique representing
difference, not merely the fact that the endpoints have equal
interval length. It is also the fixed-offset order separation of
the two orientations of B units written in two-point coordinates.

## 2. The exterior obstruction is exactly anchored doubling

At a B mark b define

    D_b^+={h>0:b+h in C,
                h in Delta(B intersect(b,infinity))},
    D_b^-={h>0:b-h in C,
                h in Delta(B intersect(-infinity,b))}.

The positive membership h in D_b^+ means precisely that the mixed
cell (b+h,b) is a B-reflection unit. The analogous upper mixed
cell (b,b-h) is a B unit for h in D_b^-.

If the lower exterior mark -d belongs to B, its matching edge is

    {(0,-d),(d,-d)}.

Both endpoints are B units exactly when d,2d belong to D_(-d)^+.
Equivalently there exist a,c>-d with

    -d, a,a+d, c,c+2d in B,
    0,d in C.                                      (1)

The fixed C-C cell (d,0) has color B, so the three displayed
mixed/fixed cells form a monochromatic B corner. The upper
exterior alternative is the reflected pattern with d,2d in
D_(2d)^-. Thus the direct-unit obstruction has the exact form

    {h,2h} subset D_b^+ or D_b^-.                   (2)

In an actual proper weak source the stronger supported-fan
sum-free theorem already excludes (2). The present derivation
identifies exactly its role in the complete two-point binary test.

## 3. The only remaining binary type is a reflected-middle core

The auxiliary classification proves that, after direct double-unit
edges are removed, a failure can only come from an exterior-to-
interior parent edge. Every such edge itself generates the
reflection event that forces its two opposite matching endpoints.
In normalized coordinates the upper and lower cores are

    B contains {x,d-x,d+x,2d},   C={0,d},            (3)
    B contains {-d,-x,x,d-x},   C={0,d},             (4)

with 0<x<d and the B-Golomb premise retained. Midpoint coincidences
are allowed as sets. No replacement x -> d-x is assumed to preserve
the extra witness d+x; all actual parameter values are retained.

For (3), the reflection (x,d+x,2d) outputs d and forces
z(d,x)=z(2d,d)=B. The C-C cell (d,0) has color B. Its two binary
corners force z(d-x,0)=z(2d,0)=C, contradicting the fixed C-colored
B-B cell (2d,d+x). This is the positive corner

    (d-x,0),(2d,0),(2d,d+x).

Formula (4) is the direction-preserving reflected version. These
are exactly the geometric mechanism in
REFLECTED_MIDDLE_HOLE_RULE_0042.md: the missing reflected extreme
would have been the second C mark.

## 4. Complete scope of the normal form

For a fixed Golomb B and opposite pair C={r,s}, the unit and binary
subsystem has a solution if and only if neither of the following
occurs after translation or direction-preserving reversal:

* the exterior anchored doubling pattern (1), equivalently (2);
* the reflected-middle core (3) or (4).

Necessity follows from the explicit forced corners. For sufficiency,
the auxiliary complete matching classification has at most three
choices. Its Golomb parent-witness restrictions eliminate every
alternating chain on two distinct parent edges. It leaves only a
direct double-unit matching edge or an exterior-to-interior forced
collision. Section1 excludes interior direct double units, Section2
identifies the exterior direct units, and Section3 identifies the
other collision. Hence no binary obstruction remains.

For larger C, applying this theorem to every selected pair in C
characterizes all the B-versus-two-C binary restrictions. Exchanging
the classes gives the symmetric set of restrictions. These
pairwise tests do not constitute a theorem that the complete
mixed system is satisfiable: the full system also has opposite
unit conflicts, implications using more anchors, and the shared-
difference three-variable clauses. Even for C of size two, its
possible ternary clause still requires the separate augmentation
test in TWO_POINT_TRANSVERSAL_GEOMETRY_0042.md.

The normal form makes a whole collection of local binary conditions
explicitly available for finite-span counting. No sufficient lower
count of these forbidden patterns, and no new Ramsey bound, has
yet been derived from it.
