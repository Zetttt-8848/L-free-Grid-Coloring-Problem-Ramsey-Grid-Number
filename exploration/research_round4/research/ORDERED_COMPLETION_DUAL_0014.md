# A joint inequality for lines and ordered completion blocks

Root derivation, checkpoint R4-RESEARCH-0014. Base: R4-RESEARCH-0013 and
the subsequent terminal product experiments, as consolidated in
`handoff_20260912/RESEARCH_HANDOFF.md` (SHA256
`614A721B10ADEE968767A51D2F3CFB30A877BB9DD1BE57919D68E3F63E11754F`).
There is no Git repository or mathematical ledger at this base.

This is an auxiliary obstruction framework, called **ordered completion
duality** in this note. It incorporates the newly derived one-cut routing
constraint into a valid global inequality. It does not prove S11, a new
Ramsey bound, or superiority to the inherited small-color method. The
optimization operations themselves are standard dual decomposition; the
additional mathematical input is the ordered source-completion constraint.

## 1. Geometry and the exact budget

Let A be a finite subset of the integers. Put

    V(A)={(v,u):u,v in A, u<v},
    F_d={x:x,x+d in A},              d>0.

All corners have positive equal step. Parameterize them uniquely as

    L_x=(x+d,x),  Q_x=(x+e,x),  R_x=(x+e,x+e-d),
    0<d<e,       x in G_{d,e}:=F_d intersect (F_d-(e-d)).       (1)

Thus the corner step is e-d. Let E be this set of corners and let
P be the graph consisting of their three pair edges. A pair edge belongs
to precisely one corner: its direction specifies whether it is the row,
column, or offset-diagonal pair, after which the missing cell is unique.
Write e(f) for the corner belonging to a pair edge f.

For signs z:V(A)->{-1,+1}, put

    X_f(z)=(1+z_p z_q)/2,                   f={p,q}.          (2)

If z is proper, each corner has exactly one equal-color pair. Therefore,
for arbitrary nonnegative corner weights w_e,

    sum_{f in P} w_{e(f)} X_f(z) = sum_{e in E} w_e.         (3)

The row, column, and offset-diagonal graphs are the exact graphs from
`COMPLETION_CUT_BUDGET.md`; missing row or column edges are not filled in.
They partition P. The sets E_{d,e} of corners in (1) also partition E.
Consequently the pair edges of distinct completion blocks do not overlap.
Their endpoint cells do overlap, and their actual colors must agree.

This distinction matters: summing arbitrary direction-dependent costs
does not give (3). Equal corner weights on all three pair directions are
what make (3) a fixed budget.

## 2. The local states retained in a completion block

Let U_{d,e} be the union of the cells of corners in E_{d,e}. For a sign
assignment sigma on U_{d,e}, and s in {-1,+1}, define

    B_s={x in G_{d,e}:sigma(Q_x)=s},
    J_s={x in B_s:sigma(L_x)=sigma(R_x)=-s},
    C_s={x in B_s:sigma(L_x)=s, sigma(R_x)=-s},
    R_s={x in B_s:sigma(L_x)=-s, sigma(R_x)=s}.              (4)

Call sigma admissible for this block if every corner in the block is
nonmonochromatic, |J_s|<=1 for each sign, and

    x<y whenever x in C_s and y in R_s.                    (5)

Denote this finite set of local assignments by Bcal_{d,e}. Repeated
occurrences of a cell in the block have one sign, not independent signs.

Every globally proper coloring restricts to an element of Bcal_{d,e}.
Here is the derivation, including the part that uses corners outside the
block. Properness gives the exhaustive three cases in (4). Each signed
fiber is Golomb, so two members of J_s would give two pairs of difference
e-d in the same signed fiber F_d^{-s}. This proves |J_s|<=1.

For the ordering, suppose y in R_s, x in C_s, and y<x. Then y belongs to
F_d^{-s} intersect F_e^s, and x belongs to
F_e^s intersect (F_d^{-s}-(e-d)). The same-sign pair of starts y,x in
F_e^s forces (x+e,y) to sign -s. The same-sign pair of starts
y,x+(e-d) in F_d^{-s} forces exactly that cell to sign s. Both steps are
positive, and all endpoints are source marks. This is a contradiction.
The two routing sets are disjoint, so equality of x and y is impossible.
This proves (5).

These are necessary local states, not an assertion that every collection
of such states glues to a proper coloring. In particular, taking their
minima separately is an explicitly stated relaxation.

## 3. Edge prices and shared-pair potentials

Choose nonnegative numbers a_f and b_f for each pair edge such that

    a_f+b_f <= w_{e(f)}.                                  (6)

The a price is assigned to the unique line graph containing f, and the b
price to its unique completion block. Let I be any chosen collection of
unordered pairs {p,q} of distinct physical cells. These pairs need not be
edges of P. Choose arbitrary real potentials eta_{H,pq} for pairs contained
in line graphs H, and theta_{d,e,pq} for pairs contained in completion
blocks, satisfying cancellation at each physical pair {p,q}:

    sum_{H containing p,q} eta_{H,pq}
      + sum_{(d,e):p,q in U_{d,e}} theta_{d,e,pq}=0.       (7)

Unused potentials can all be zero. For each exact line graph H define

    L_H = min_{sigma:V(H)->{-1,+1}}
          [sum_{f in E(H)} a_f X_f(sigma)
             + sum_{{p,q} in I, p,q in V(H)}
                         eta_{H,pq} sigma(p)sigma(q)].    (8)

For each nonempty completion block define

    K_{d,e} = min_{sigma in Bcal_{d,e}}
          [sum_{f:e(f) in E_{d,e}} b_f X_f(sigma)
             + sum_{{p,q} in I, p,q in U_{d,e}}
                       theta_{d,e,pq} sigma(p)sigma(q)]. (9)

An empty local state set is already a source obstruction, by Section 2;
there is then no need to assign an artificial finite value to its minimum.

**Joint inequality.** If V(A) has a proper two-coloring, then every choice
of prices and potentials above satisfies

    sum_H L_H + sum_{0<d<e} K_{d,e} <= sum_{e in E} w_e.  (10)

**Derivation.** Restrict the one actual coloring z to every line and
block. It is allowed in (8) and, by Section 2, in (9). Their minima are
therefore at most their values on these restrictions. Summing those
values counts each pair edge with coefficient a_f+b_f. Every shared-pair
potential cancels by (7), giving

    sum_H L_H + sum_{d<e} K_{d,e}
      <= sum_f (a_f+b_f) X_f(z)
      <= sum_f w_{e(f)} X_f(z)
       = sum_e w_e.

The second inequality uses (6) and X_f(z)>=0; the last is (3). This proves
(10). Strict reversal in any explicitly derived instance excludes A.

The pair potentials retain agreement of the relative colors of shared
cells. They may have either sign because they cancel exactly. Nonnegative
edge prices preserve the comparison with the fixed corner budget. For
example, two completion blocks with the same outer offset e may share two
outer cells (x+e,x) and (y+e,y). Their product of signs has one value in an
actual coloring. Equal and opposite potentials on that shared pair permit
the two local minima to be coupled in (10). The pair need not itself be
an edge belonging to either block's own corners.

### Why unary sign potentials cannot supply this coupling

There is an exact symmetry obstruction to substituting unary sign prices
for the pair prices in this construction. For any one factor, let S be
its allowed sign assignments and let c(sigma) be its edge-price cost.
Both satisfy sign-reversal symmetry: -sigma belongs to S whenever sigma
does, and c(-sigma)=c(sigma). If sigma_0 minimizes c, then for arbitrary
real unary prices h_q,

    min_{sigma in S} [c(sigma)+sum_q h_q sigma(q)]
       <= min(c(sigma_0)+sum_q h_q sigma_0(q),
              c(sigma_0)-sum_q h_q sigma_0(q))
        = c(sigma_0)-|sum_q h_q sigma_0(q)|
       <= min_{sigma in S} c(sigma).                    (11)

Consequently every factor's lower value is at most its value with all
unary prices zero. Summing shows that cancelling unary potentials can
never improve this dual lower bound for fixed edge prices. This conclusion
applies to both the unrestricted line factors and the one-cut block
factors, since their definitions allow exchange of the two color names.
Pair products are unchanged by that exchange, so argument (11) does not
apply to the shared-pair potentials in (7)--(9). This is why the proposed
global coupling uses relative colors, not individual color labels.

## 4. Relation to the inherited line bound

Set w_e=1, a_f=1, b_f=0, and all potentials to zero. Formula (8) is the
minimum equal-color edge count tau(H), and every nonempty block has cost
zero. Formula (10) becomes exactly

    sum_d floor((|F_d|-1)^2/4)
       + sum_v tau(R_v) + sum_u tau(C_u) <= |E|.

Thus the earlier exact line criterion is a special case. This is an
inclusion statement, not a claim that the new factors yield a strictly
larger obstruction score for any particular source.

At the other extreme, if a_f=0, all potentials vanish, and each of the
three b prices of a corner is its common weight w_e, every admissible
block state pays exactly sum_{e in E_{d,e}}w_e. Equation (10) is then an
equality. Simply adding one-cut bounds with identical per-corner weights
cannot improve a Ramsey bound.

To obtain a gain, line prices must leave useful direction-dependent
residual prices in (9), or nonzero cancelling pair potentials must couple
the local color choices. Either way, a numerical obstruction needs actual
lower derivations of (8) and (9). A solver's optimal-value report alone is
not the requested mathematical derivation.

## 5. Explicit one-dimensional lower bounds inside a block

Conditional on the actual outer signs, and after its possible exception
j_s has been removed, list B_s\{j_s} as x_1<...<x_m. The routing lemma
makes the column routes a prefix x_1,...,x_k and the row routes a suffix.
If c_i and r_i are the residual prices on the column and row pairs at
x_i, the residual equal-pair cost is

    sum_{i<=k}c_i + sum_{i>k}r_i.                         (12)

Thus its lower envelope is the minimum of (12) over 0<=k<=m, with the
diagonal price at j_s added when the exception is present. Minimizing over
the possible exception locations gives the formula in the auxiliary note
`fibers/ORDERED_CLOUD_AMORTIZATION_0014.md`.

For use in (9), the outer signs are not fixed free inputs: one must retain
their cell assignments, the pair-potential costs, and all repeated endpoint
cells. Formula (12) by itself is only the edge-price part of (9).
Allowing extra independent choices only gives a lower bound for K_{d,e},
which is legitimate but can lose the intended gain. In particular, two
different values of d with the same e cannot select incompatible signs
for (x+e,x) in a claimed global coloring; the dual can address the loss
through shared-pair potentials without asserting that independently
optimal blocks glue.

## 6. The remaining root implication

The principal requested source statement is still

    V(A) properly two-colored, span(A)<=91998
        => binom(|A|,2)<=11 span(A).                     (S11)

To derive it from (10), it remains to give explicit source-dependent
prices, potentials, and local lower derivations such that

    binom(|A|,2)>11 span(A), span(A)<=91998
       => sum_H L_H + sum_{d<e} K_{d,e} > sum_e w_e.

No such uniform construction is proved here. In particular, replacing all
local costs by separately optimal values without a common budget is not
an argument for S11. A bounded finite separation would establish only the
scope of that literal example until an all-source estimate is supplied.

The working bounds remain 21<=R_3(L)<=465 and R_4(L)<=21991300. The
literature-derived general bound in GENERAL_BOUND.md is unchanged.

## 7. Exact meaning of the shared-pair relaxation

There is a useful finite-dimensional characterization of the remaining
coupling, which does not require a solver or a claimed numerical optimum.
Let F range over all the line and completion-block factors above. For each
factor let S_F be its allowed assignments (unrestricted on a line, and
Bcal_{d,e} on a block). Assume these sets are nonempty. Choose I to include
every physical pair that occurs in at least two factors. In factor F form
the vector

    v_F(sigma)=(sigma(p)sigma(q))_{{p,q} in I, p,q in F}.

Let K_F be the convex hull of these finitely many vectors. A **consistent
pair-marginal model** is a choice k_F in K_F for every factor such that all
copies of each physical pair have the same coordinate value. This means a
probability distribution on each factor's assignments with consistent
pair expectations; it does not assert a global distribution or coloring.

**Alternative.** Exactly one of the following occurs:

* a consistent pair-marginal model exists;
* there are real pair potentials r_{F,pq}, with sum_F r_{F,pq}=0 for each
  physical pair, such that

      sum_F min_{sigma in S_F}
          sum_{{p,q} in F} r_{F,pq} sigma(p)sigma(q) > 0.  (13)

**Direct derivation.** Work in the Euclidean space with one coordinate for
each factor-copy of a pair. Let K be the Cartesian product of the K_F,
and let D be the linear subspace where copies of every physical pair
agree. K is compact and convex. If k in K intersect D and the potentials
cancel, their value on k is zero, so the sum of independent minima in
(13) is at most zero. Thus the alternatives are incompatible.

If K and D are disjoint, choose k_* in K minimizing its squared distance
to D, and put r=k_*-proj_D(k_*). Then r is nonzero and orthogonal to D.
For any k in K, the segment k_*+t(k-k_*), 0<=t<=1, lies in K. The
right derivative at zero of its squared distance to D is nonnegative,
so

    2 r dot (k-k_*) >= 0.

Since r is orthogonal to proj_D(k_*), this gives

    r dot k >= r dot k_* = ||r||^2 > 0.

Orthogonality to D says precisely that r's coefficients sum to zero over
the copies of each physical pair. Minimizing r dot k over the Cartesian
product K separates over factors, and a linear function has the same
minimum on a finite set and its convex hull. This proves (13).

Taking all w_e,a_f,b_f to be zero in (10) shows that (13) is already a
certificate within the joint inequality. Conversely, a consistent model
prevents every version of (10), with arbitrary allowed edge prices and
pair potentials, from giving a contradiction. To see this, evaluate every
local cost on its marginal distribution. The shared pair products have
common expectations, so all pair potentials cancel. Every pair edge
appears in both its line and its corner block, so its equal-pair
expectation also agrees. In each block every supported assignment is
proper, and hence the expected three-pair sum of every corner is one.
The same calculation as in Section 3 then bounds the sum of local minima
by sum_e w_e. This establishes the stated converse for the whole price
framework, not only its zero-edge-price case.

Thus a bounded marginal-feasibility experiment is a meaningful development
test. Infeasibility suggests a separating potential that still needs an
explicit derivation; feasibility suggests that additional shared moments
or larger source blocks are required to exclude that particular source.
A floating LP status by itself proves neither mathematical alternative.

Finally, the sign-reversal argument (11) also applies to any additional
potential odd under simultaneous sign reversal, even after pair potentials
have been included: the remaining local cost is still even. Such odd
potentials cannot improve a fixed even-potential lower bound. Higher even
products, such as a product of four shared cell signs, are not ruled out by
this symmetry argument; no quantitative theorem for them is asserted here.
