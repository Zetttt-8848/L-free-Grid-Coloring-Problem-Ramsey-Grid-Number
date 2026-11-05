# A supported-difference condition in every weak source

Root derivation, continuation 0039. The positive-fan rule has a direct
form inside a proper weak two-color source W(S), where diagonal cells
are present. It applies at every actual diagonal mark and requires just
one membership test in S. This provides a new structural input for weak
fiber capacity questions, but no numerical capacity is established here.

Write

    W(S)={(v,u):u,v in S, u<=v}

and fix one proper two-coloring z. Choose a in S and put c=z(a,a).
Let P be the positive labels of the later diagonal marks having color c:

    P={p>0:a+p in S, z(a+p,a+p)=c}.

Let

    D=Delta P intersect (S-a),
    Delta P={q-p:p,q in P, p<q}.                     (1)

Only positive differences enter D. The diagonal color classes of a
proper weak source are Golomb, so P union {0} is Golomb.

## 1. Difference support fixes two actual colors

Take h=q-p in D, p<q in P. The two diagonal c-cells at a+p and a+q
force

    z(a+q,a+p)=-c.

The diagonal c-cells at a and a+q similarly force z(a+q,a)=-c.
By (1), a+h is an actual source mark. The three cells

    (a+h,a), (a+q,a), (a+q,a+p)

form a positive corner of step p, and its last two cells are -c.
Therefore z(a+h,a)=c. Finally the positive corner

    (a,a), (a+h,a), (a+h,a+h)

has its first two cells c, so its last cell must be -c. Thus every
supported difference satisfies the simultaneous conclusion

    z(a+h,a)=c,
    z(a+h,a+h)=-c.                                  (2)

In particular a+D lies in the opposite diagonal class. This proves
that D is Golomb without selecting a new coloring for it.

## 2. The supported difference set is sum-free

Suppose h,d,h+d all belong to D. Their diagonal cells have color -c
by (2). The two such cells at a+h and a+h+d force

    z(a+h+d,a+h)=c.

But (2) also gives z(a+d,a)=z(a+h+d,a)=c. The three cells

    (a+d,a), (a+h+d,a), (a+h+d,a+h)

are a monochromatic positive corner of step h. This contradiction proves

    h,d in D imply h+d not in D.                     (3)

The argument includes h=d. It uses only cells in W(S) and does not
require that W of the original strict source be present.

## 3. The resulting graph and its exact missing-support count

Join p<q in P when a+q-p belongs to S. The graph's distinct edge labels
are exactly D. It is triangle-free by (3): the gaps of a triangle are
h,d,h+d. It also has common-neighbor count at most two, with at most one
interior and one exterior common neighbor for any fixed pair of vertices.
This follows from Golombness of P and D by the complete geometric
difference argument in POSITIVE_FAN_DIFFERENCE_BUDGET_0039.md, Section 3.

Consequently, with t=|P|>0,

    |D| <= (t/4)[1+sqrt(8t-7)].                      (4)

Since the positive differences of P are distinct, the exact number of
missing numerical supports supplied by its pairs is

    |{h in Delta P:a+h not in S}|=binom(t,2)-|D|.    (5)

Equations (4)-(5) are a local exclusion budget. Different choices of a
may exclude the same integer, so their right sides cannot be summed as
disjoint missing positions. Reversing source order through the
anti-diagonal gives the corresponding statement at the right side of a.

For example, if t>=3, not every positive difference of P can be
supported at a: any three labels would otherwise make a triangle in the
graph. This is a complete implication under the stated support premise,
not a global density theorem.

## 4. Relation to the finite fiber targets

For an original proper strict source V(A), its actual translated weak
triangle on a difference fiber F_d may be used as W(S) here. The theorem
then holds for each a in that fiber, with the two diagonal classes fixed
by the actual offset-d cell colors. It retains colors of the weak
triangle's first-column cells as well as its diagonal classes through
(2). Merely splitting F_d into two arbitrary Golomb sets does not supply
those first-column colors or the sum-free conclusion (3).

The remaining finite-capacity question is whether these simultaneous
conditions at all diagonal marks, together with the known ruler span
inputs, exclude the profiles needed for R3. There is no bound on the
overlap multiplicity of the missing positions in (5) in this note.
The C46/45(463), S21, and small-color objectives remain open.

The sharp local limitation from
fibers/POSITIVE_FAN_CYCLE_CONSTRUCTION_0039.md also applies here. Restrict
its cross-layer cells to the translated W(S), for the nine-mark S listed
there, and use a=0. Its same-color positive diagonal labels are exactly
P={1000,1001,1011,1111}; its supported differences are
D={1,10,100,111}. Thus this weak-source graph is the same four-cycle
and attains two common neighbors. The weak formulation does not remove
that limitation.
