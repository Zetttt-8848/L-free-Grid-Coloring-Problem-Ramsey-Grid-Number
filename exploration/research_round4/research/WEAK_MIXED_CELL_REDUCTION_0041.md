# The complete mixed-cell system of a weak two-color source

Root derivation, continuation0041. This isolates all extension constraints
for prescribed Golomb diagonal classes. There is exactly one genuinely
three-variable corner for each common positive difference of the classes.
The remaining nontrivial constraints have one or two variables. The
reflection-shadow holes from this continuation arise when such a
three-variable corner has all its variables already forced alike.

This is an exact mathematical reduction and counting identity, not a
solver certificate, a new capacity bound, or a claim that the resulting
system is always satisfiable.

## 1. Fixed cells and the free variables

Let S=B disjoint union C be two finite integer Golomb sets. Prescribe
diagonal color B at the marks of B and color C at the marks of C.
Every proper weak extension must color

    z(v,u)=C for u<v in B,
    z(v,u)=B for u<v in C.                            (1)

These values are forced by corners with diagonal endpoints. Every mixed
unordered pair {b,c}, b in B and c in C, has one strict cell
(max(b,c),min(b,c)). Let its color be a free variable. There are bc
variables. Diagonal corners between different diagonal colors impose
no further condition; those within one class are already satisfied by
(1).

It remains to impose every positive-offset corner. For d>0, let

    beta_d=1_(d in Delta B), gamma_d=1_(d in Delta C),
    x_d=|{u in B:u+d in C}|,
    y_d=|{u in C:u+d in B}|.

The endpoint cells on offset d fall into four types: a unique B-B cell
of fixed color C when beta_d=1; a unique C-C cell of fixed color B
when gamma_d=1; x_d mixed B-to-C cells; and y_d mixed C-to-B cells.
Any pair of different endpoint cells has its unique outer completion
inside W(S).

## 2. Complete classification by the endpoint types

The following list exhausts the unordered pairs on every positive
offset.

* A B-B and a C-C endpoint have opposite fixed colors. Their corner is
  automatically proper. There are beta_d gamma_d such pairs.

* A fixed within-class endpoint paired with a mixed endpoint has a
  completion either within that same class or mixed. In the first
  case the two fixed cells have the same color, so the mixed endpoint
  is forced to the opposite color. In the second case precisely two
  cells are mixed variables. They may not both equal the fixed color.
  These are, respectively, a unit constraint and a binary constraint.
  There are (beta_d+gamma_d)(x_d+y_d) such corners in total.

* Two mixed endpoints with opposite orientations have a within-class
  completion. Their two variables may not both equal its fixed color.
  There are x_d y_d such binary constraints. This includes a
  three-term progression whose middle mark is the sole mark of its
  diagonal color; no distinct-four-mark hypothesis is imposed here.

* Two mixed endpoints of the same orientation have a mixed completion.
  Their three actual variables may not all have the same color. There
  are binom(x_d,2)+binom(y_d,2) such three-variable constraints.

There is no pair of distinct B-B endpoints, or of distinct C-C
endpoints, at the same d, because each diagonal class is Golomb.

For clarity, in the second item an available homogeneous completion
cannot have the other diagonal class: it shares one of its source
endpoints with the fixed homogeneous endpoint. Thus it has the same
fixed color. This is why that case is a unit constraint rather than
another automatically satisfied corner.

Every displayed constraint is just the nonmonochromaticity requirement
for its actual positive corner. Conversely, satisfying all these
constraints, and filling in (1) and the prescribed diagonal, makes
every corner proper. The classification is therefore necessary and
sufficient for extension of the prescribed diagonal colors.

## 3. Exactly one three-variable constraint per shared difference

Put rho=|Delta B intersect Delta C|. The two-Golomb collision identity
from0037 gives

    sum_d [binom(x_d,2)+binom(y_d,2)] = rho.          (2)

Here is the full geometric dictionary in the present system. Choose
the unique B-pair p,p+h and C-pair q,q+h at a common length h. Their
starts are different. If p<q, the two mixed edges

    p -> q,  p+h -> q+h

are both B-to-C and have the same positive length q-p. They and their
outer completion give exactly one three-variable corner. If q<p,
exchange the classes. Conversely any two mixed endpoints of the same
orientation recover these two within-class pairs at the difference
between their starts. Golombness makes the dictionary injective.

The same four marks also supply the automatically proper corner with
the B-B and C-C endpoints at offset h. Thus the rho automatically
proper corners and the rho three-variable corners are paired by
rotating the same four-mark parallelogram. The rotation preserves
positive orientation after ordering its endpoints.

This pairing applies to both disjoint and interleaved equal-length
intervals. It does not assume the two color classes are separated.

## 4. Exact number of unit and binary corner constraints

For r outside B let mu_B(r) count a<p<q in B with r=a+q-p, and define
mu_C analogously. Put

    K=sum_(r in C) mu_B(r)+sum_(r in B) mu_C(r),
    N=sum_d(beta_d+gamma_d)(x_d+y_d),
    Q=sum_d x_d y_d.

Every internal reflection a<p<q in B, r=a+q-p in C, forces precisely
the two mixed cells

    z(r,a)=B,  z(q,r)=B.                              (3)

The first follows from the corner (r,a),(q,a),(q,p), of step p-a;
the second from (p,a),(q,a),(q,r), of step q-p. The other two cells
in each corner are B-B cells of fixed color C. Conversely every unit
case in Section2 has two B-B or two C-C fixed cells and recovers one
such internal reflection and one of its two extremes. Thus there are
exactly 2K unit corner constraints, counted before possible duplicate
variables are identified.

The positive-offset corner inventory is exactly

    automatically proper: rho,
    three-variable:       rho,
    unit:                 2K,
    binary:               N+Q-2K.                    (4)

Its sum is the earlier exact energy decomposition

    T(S)=2rho+N+Q.                                   (5)

In particular N>=2K. The counts in (4) count actual corners, so two
constraints with the same logical content are not silently merged.
Three-term progressions are included in the binary inventory; they
cannot be unit cases since a Golomb class has no three-term progression.

## 5. Forced mixed cells and their possible conflicts

For one fixed B and one mixed cell incident with r in C, at most one
internal reflection of B can force (3) at that cell. If the B endpoint
is below r, it fixes the difference q-p=r-a; if it is above r, it
fixes p-a=q-r. Golombness fixes the remaining pair in either case.
The corresponding statement holds for forces of color C.

Thus a mixed variable can carry at most one force of each color. If
both occur, the prescribed diagonal has no extension. In a proper
extension, all 2K unit occurrences in (4) therefore concern distinct
mixed variables. This gives the actual-cell interpretation

    2K <= bc.                                       (6)

The positional theorem in0040 independently supplies this numerical
upper bound for two disjoint Golomb classes. The present argument
additionally identifies the forced physical cells and the exact
contradiction when opposite units meet.

As a simple consequence of the complete system, if C consists of one
mark then setting every mixed variable to B satisfies all constraints:
there are no shared differences, no three-variable constraints, and
all remaining fixed cells participating in a constraint have color C.
This recovers the one-point weak extension by the reduced system.

## 6. Why nested shadow holes are a joint constraint

Suppose r in C has two internal B-reflections with anchors a<a'.
Let t=r-(a'-a). If t belongs to B, the later reflection also supplies
the internal B-reflection t=a+q'-p', contradicting Golombness. If t
belongs to C, tail nesting supplies the three unit forces

    z(t,a)=z(r,a)=z(r,a')=B.

These three variables form exactly the three-variable corner paired
with the common length a'-a=r-t of B and C. Hence this one clause in
(2) is violated. Therefore t must be absent from S. Reflection gives
the upper shadows in NESTED_REFLECTION_HOLE_BUDGET_0041.md.

This makes the relation between the two new formulations precise:
reflection units cannot be treated separately from the rho rotated
parallelogram constraints. The shadow graph records a particular
family of three-variable clauses that would already be entirely fixed
to one color if their shadow output were present.

## 7. The remaining finite-capacity problem

The reduction uses bc mixed variables and exactly rho three-variable
corner constraints, coupled to the explicit unit/binary system.
The three-variable constraints are not independent choices, and a
solution of the binary part is not asserted to extend over them.
Nor does merely knowing their number force a contradiction.

A numerical source-capacity theorem still needs a global geometric
restriction on this particular shared-variable system, or expansion
of the reflection-shadow graph at the relevant finite span. The
classification supplies that system with no omitted corner types;
it does not establish S21, the finite R3 caps, or a Ramsey improvement.
