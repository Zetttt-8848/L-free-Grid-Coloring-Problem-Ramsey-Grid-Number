# O1: ordered intersections and cap-sensitive overlap bounds

Author: root, Level3. UNVERIFIED pending required independent reviews.

Fix a monochromatic diagonal set A in a corner-free three-color grid,
and one other color blue. Write B_d for the starts u such that u,u+d
belong to A and their completing point is blue. The inherited completion
argument puts every point of Q_d={(v+d,u):u<v in B_d} in the third color.
Fix positive d<e and put Delta=e-d. Define

 C_de=B_d intersect B_e,
 D_de=B_e intersect(B_d-Delta).

Then the exact ordered intersection formula is

 |Q_d intersect Q_e|=sum_(q in D_de) |{u in C_de:u<q}|.       (O1)

Indeed equality of the two outputs (v+d,u)=(q+e,p) forces p=u and
v=q+Delta. Membership of both input pairs is precisely u in C_de,
q in D_de, and u<q. Conversely these conditions give valid pairs;
u<q also implies u<v because Delta>0. Distinct (u,q) produce distinct
outputs (q+e,u), so this is a bijection, not a charge with multiplicity.

To use only the source set define

 X_de=A intersect(A-d) intersect(A-e),
 Y_de=A intersect(A-Delta) intersect(A-e).

Then C_de subset X_de and D_de subset Y_de, and hence O1 is at most
J_de=#{(u,q) in X_de times Y_de:u<q}. Each of |X_de|,|Y_de| is at
most min(r_A(d),r_A(e),r_A(Delta)): use the three sides of each triple,
translating the start when needed. Thus if r_A(h)<=V_h,

 |Q_d intersect Q_e| <= min(binomial(|B_d|,2),binomial(|B_e|,2),
                            J_de,min(V_d,V_e,V_Delta)^2).     (O2)

The binomial terms follow because an intersection is contained in either
set and each single-shift map is injective. The term J_de retains the
ordered triple structure; replacing it by the square discards that input.
Summing any of these valid pair bounds gives Obar>=O. Therefore, for
M=sum_d binomial(|B_d|,2)>0, the inherited Cauchy identity gives

 |union Q_d|>=ceil(M^2/(M+2Obar)).                            (O3)

For an upper bound on this union, every output diagonal ell is a
monochromatic subset of the two-color completion-closed region T(A),
so its Golomb bound uses q(n-ell) positions. One can sum those capacities
over the output diagonals actually reached. A contradiction requires
this sum to be strictly below O3; O1 alone does not assert that happens.

Checks. Empty fibers give zero sums; d=e is excluded, as Delta must be
positive. There is no division when M=0. At d1 or adjacent shifts,
all translations above are integral and actual source membership fixes
the boundary. The formula is set-theoretic, valid even without coloring;
the third-color and Golomb conclusions require the stated three-color
corner-free hypothesis. For k1,2 those conclusions are only used after
the missing-color premises, never to force nonempty fibers. A one-color
grid with a corner is outside the hypothesis.

Failure mode. In the inherited closed-region witness A={1,4,8,14,18,21},
B3={1,18},B7={1,14}. Here C={1},D={14}, so O1=1 equals
min(|Q3|,|Q7|)=1. Both sets consist of the point(21,1), and M=2,
O=1 gives the sharp lower bound1. Thus no universal positive fraction
of improvement over this overlap maximum follows from local closure
and these triple intersections alone. This is a two-fiber obstruction,
not an impossibility proof for every full-grid many-fiber method.

Dependency graph: inherited completion geometry -> color of Q; elementary
endpoint bijection -> O1 -> O2; inherited Cauchy + O2 -> O3. Finite
tests check the set identity independently of color assertions.
