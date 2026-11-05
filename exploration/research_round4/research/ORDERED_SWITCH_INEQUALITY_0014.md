# A quadratic ordered-switch inequality

Root derivation extending the ordered routing lemma in checkpoint 0014.
This is a properness-specific local inequality and a conditional transfer
to certain reflected corners. It does not assert that negative-step or
reflected corners are forbidden everywhere, and it gives no new Ramsey
number by itself.

Let V(A)={(v,u):u,v in A,u<v} have a proper two-coloring z in {-1,+1}.
For a pair of cells p,q write X(p,q)=(1+z_p z_q)/2. Thus X is one exactly
when the two cells have the same color.

Fix d,h>0, put e=d+h, and take two distinct starts x<y such that

    x,x+d,x+h,x+e,y,y+d,y+h,y+e all belong to A.          (1)

Repeated marks in this list are allowed. Define

    L_t=(t+d,t), Q_t=(t+e,t), R_t=(t+e,t+h), t=x,y.

These give two positive corners, of step h. The following is necessary:

    X(Q_x,R_x)+X(Q_y,L_y)+X(Q_x,Q_y) <= 2.               (2)

Equivalently,

    z_{Q_x}z_{R_x}+z_{Q_y}z_{L_y}+z_{Q_x}z_{Q_y} <= 1. (3)

**Derivation.** If the three X terms were one, the four cells
R_x,Q_x,Q_y,L_y would all have a common color s. Properness of the corner
at x gives z_{L_x}=-s. Properness of the corner at y gives z_{R_y}=-s.
The cells L_x,R_y lie on offset d, their positive displacement is
y+h-x, and their completion is Z=(y+e,x). Thus they force z_Z=s.
On the other hand, Q_x,Q_y lie on offset e, with positive displacement
y-x, and force exactly the same Z to color -s. All three cells in each
of these last two corners belong to V(A); in particular its outer row
y+e and column x belong to A and y+e>x. The contradiction proves (2).
Substituting the definition of X gives (3).

This is a quadratic consequence of the ordered routing condition. The
forbidden inversion can also be written as a product of three indicators,
but no higher-degree monomial is needed for the upper inequality (2).
Its three pairs are genuine source pair edges: the first is a row pair,
the second a column pair, and the third an offset-e pair. Their original
corners are generally different. Thus (2) retains actual compatibility
that separate minima on these three lines need not retain.

## An exact identity when the switches meet

Suppose y=x+h. Then R_x=L_y=:S, and (2) concerns the three pairs of the
three cells Q_x,S,Q_y. These cells form the reflected corner

    (x+d+h,x), (x+d+h,x+h), (x+d+2h,x+h).                (4)

Their source hypothesis is exactly

    x,x+h,x+2h,x+d,x+d+h,x+d+2h in A.                   (5)

For any two-colored triple, its number of equal-color pairs is one or
three. Inequality (2) excludes three. Consequently, under (5),

    X(Q_x,S)+X(S,Q_y)+X(Q_x,Q_y)=1,                     (6)
    z_{Q_x}z_S+z_S z_{Q_y}+z_{Q_x}z_{Q_y}=-1.           (7)

Thus this particular reflected corner cannot be monochromatic. The proof
uses the two supporting marks x+d and x+2h as well as the marks of (4).
It is invalid to drop (5) and declare every reflected corner forbidden.
The argument is specific to two colors: the forced opposite sign at the
first two corners is essential.

For example, in the eight-mark development source, (d,h,x)=(1,1,0)
gives the reflected triple (2,0),(2,1),(3,1), while (d,h,x)=(2,2,0)
gives (4,0),(4,2),(6,2). Both are legitimate because their full lists
in (5) lie in A. These are local identities, not numerical obstruction
claims.

## Use in the joint dual

Nonnegative combinations of inequalities (3), together with identities
(7) and the original corner sign-product identities, can give explicit
lower bounds for a completion-block pair polynomial. Weighted clique
inequalities supply corresponding line-polynomial bounds. When the
physical-pair coefficients cancel across the factors, their constant
terms yield a source obstruction by ORDERED_COMPLETION_DUAL_0014.md.

This is a route for converting the saved finite pair-potential candidate
into algebraic derivations, rather than treating a feasibility status as
a theorem. A uniform estimate sufficient for S11 remains open.
