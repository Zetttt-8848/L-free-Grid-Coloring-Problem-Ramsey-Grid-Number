# Integer cut budgets for source completion triangles

Root derivation, R4-RESEARCH-0008, continuing R4-RESEARCH-0007.
The statements below are necessary conditions and sufficient obstruction
criteria. They do not establish an improved Ramsey number. Their role is to
retain actual two-color constraints that the earlier unweighted spectral
criterion discards.

## 1. The three graphs attached to a source set

Let A be a finite set of integers and

    V = T(A) = {(v,u): u,v in A, u<v}.

A corner is the ordered triple

    (v,u), (v+t,u), (v+t,u+t),       t>0,

when all three cells belong to V. Write E for the set of corners and
T=|E|. For d>0 put F_d=A intersect (A-d) and r_d=|F_d|. Then

    T = sum_(d>0) binom(r_d,2).                         (1)

Indeed, the first and third cells of a corner lie on the same offset d.
Conversely, any two different starts u<w in F_d have the unique completion
(w+d,u), which belongs to V.

Replace every corner with the three pairs of its cells. No pair is used
twice: a pair on a column determines the third cell by its row difference;
a pair on a row determines it by its column difference; and a pair on an
offset diagonal determines it by its common offset. These three pair types
are distinct for two different cells. Thus the resulting graph has exactly
3T edges, partitioned into the following line graphs.

* D_d is the complete graph on {(u+d,u):u in F_d}.
* R_v has vertices {(v,u):u in A, u<v}. Its vertices indexed by u<w
  are adjacent exactly when v-(w-u) belongs to A. Their completing cell is
  (v-(w-u),u). Its row exceeds u because v>w.
* C_u has vertices {(v,u):v in A, u<v}. Its vertices indexed by v<w
  are adjacent exactly when u+(w-v) belongs to A. Their completing cell is
  (w,u+(w-v)). Its row exceeds its column because v>u.

In particular, each corner gives one edge to each of the three line
directions. The row and column graphs are generally not complete. Filling
their missing edges would incorrectly impose corners outside T(A).

## 2. The exact two-color budget

For a finite graph H, let tau(H) be the minimum number of edges whose
endpoints receive the same color in a two-coloring of its vertices. Thus
tau(H)=|E(H)|-MaxCut(H), with both quantities unweighted here. Put

    phi(r) = binom(r,2)-floor(r^2/4)
           = floor((r-1)^2/4),      r>=1,
    phi(0) = 0.

The value phi(r) is tau(K_r). To prove this, if b vertices have one color,
the cut has b(r-b) edges. Completing the square gives
b(r-b)<=floor(r^2/4), with equality when b is one of the two integers
nearest r/2.

**Theorem 1.** If T(A) has a corner-free two-coloring, then

    sum_d phi(r_d) + sum_(v in A) tau(R_v)
                       + sum_(u in A) tau(C_u) <= T.     (2)

Equivalently,

    sum_v tau(R_v) + sum_u tau(C_u)
                       <= sum_d floor(r_d^2/4).          (3)

**Proof.** A nonmonochromatic triple in two colors has one equal-color
pair and two unequal-color pairs. Consequently every corner contributes
exactly one equal-color edge to the graph of all corner pairs. The
uniqueness of the pair completions proves that the total equal-color edge
count is exactly T, without multiplicity. Restrict the same coloring to
each line graph. Its equal-color edge count there is at least tau of that
graph. The line graphs partition the edges, so adding their lower bounds
gives (2). Subtracting the diagonal terms and using (1) gives (3).

Thus any proved lower bounds on the row and column cut deficits whose sum
exceeds the right side of (3) exclude that source. These lower bounds must
hold for every coloring of each graph; a proposed cut or a heuristic
maximum cut does not give them.

## 3. Explicit lower bounds from cliques and odd cycles

A nonnegative fractional packing of cliques in a graph H consists of
numbers lambda_K>=0, one for each selected complete subgraph K, such that

    sum_(K containing e) lambda_K <= 1

for every edge e. Then

    tau(H) >= sum_K lambda_K phi(|K|).                  (4)

For any fixed coloring, each selected clique has at least phi(|K|)
equal-color edges. After multiplying and adding, an equal-color edge of H
is counted with total coefficient at most one. This proves (4) for that
coloring and hence for the minimum.

An odd cycle can be included in the same packing with lower bound one:
traversing a cycle, a change of color toggles a bit, so the number of color
changes on a closed walk is even. An odd cycle therefore has at least one
equal-color edge. If a clique and an odd cycle overlap, their combined
coefficients still have to obey the edge capacity condition above. No
edge-disjointness of their vertices is needed.

Here is a direct triangle estimate requiring no optimization. Let t(H) be
the number of triangles of H and let mu(H) be the largest number of
triangles containing one edge. If t(H)>0, weighting every triangle by
1/mu(H) gives

    tau(H) >= t(H)/mu(H).                               (5)

For a triangle-free graph use the lower bound zero. A stronger explicit
packing assigns to each triangle K the weight

    lambda_K = 1 / max_(e in K) mu_e,

where mu_e is the number of triangles containing e. For every fixed edge
e, each incident triangle has weight at most 1/mu_e, and there are mu_e
of them, so this is a valid packing. These formulas make (2) a concrete
source condition in terms of fully specified subgraph counts. A
quantitative estimate uniform over the source sets needed for R3 has not
been obtained here.

## 4. A weighted version, with every color count retained

Give each corner e a nonnegative weight a_e. Assign that same weight to
each of its three pair edges; the unique-completion property makes the
edge weights well-defined. Write W=sum_e a_e.

For a k-coloring let B_a and R_a be the total weights of monochromatic
and rainbow corners, respectively. Let U_a be the total weight of
equal-color edges in all the line graphs. A monochromatic corner has
three equal-color pairs, a rainbow corner has none, and a corner using
exactly two colors has one. It follows that

    U_a = W + 2 B_a - R_a.                              (6)

For k>=2 and r=kq+s with integers q>=0 and 0<=s<k, define

    phi_k(r) = k binom(q,2) + s q.                      (7)

This is the minimum number of equal-color pairs on a k-colored clique
of r vertices. If class sizes n_i and n_j differ by at least two, moving
one vertex from the larger to the smaller decreases the sum of their
binomial coefficients by n_i-n_j-1>0. Repeating this operation terminates
with all sizes equal to q or q+1, with exactly s larger classes, which
gives (7).

In the line graphs, choose any nonnegative clique weights lambda_K with

    sum_(K containing edge f) lambda_K <= a_(e(f)),     (8)

where e(f) is the unique corner containing f. Adding the clique lower
bounds with (6) proves the general necessary inequality

    sum_K lambda_K phi_k(|K|) <= W+2B_a-R_a.            (9)

For a proper coloring this right side is W-R_a<=W. In two colors R_a=0,
so it is exactly W; odd cycles can then be added to the packing, each
with lower bound one. The two-color odd-cycle lower bound is not valid
for arbitrary k and must not be inserted into the k-color statement.

Every term in (9) is derived from the same vertex coloring. Taking
separate minima over line graphs relaxes that shared-color condition,
which is why the resulting obstruction is sufficient rather than a
characterization of colorability.

## 5. The first integer improvement over the old spectral test

For A={0,1,2,3,4,5}, each row, column, and offset diagonal graph is a
clique, with nonzero sizes 1,2,3,4,5 in each direction. Formula (1) gives

    T = 0+1+3+6+10 = 20.

But the lower bound in (2) is

    3[phi(1)+phi(2)+phi(3)+phi(4)+phi(5)]
      = 3(0+0+1+2+4) = 21.

This proves that this six-mark strict triangle is not two-colorable.
The contradiction is the single integer inequality 21>20.

The previously derived unweighted spectral criterion does not detect
this source: SIGNED_COMPLETION.md exhibits least eigenvalue -2 while
that criterion requires a value exceeding -5/3. Thus retaining integer
clique deficits supplies strength missing from that particular spectral
test. The six-mark exclusion itself was already known; this calculation
is not a new Ramsey bound or a claim to a historically new cut inequality.

## 6. Bounded discovery on the saved dense source

The script completion_cut_probe.py applies a deterministic greedy
edge-disjoint clique packing to the row and column graphs of the literal
source in research_round3/joint/witness_464_parametric.json. It starts a
clique at a maximum-degree vertex of the remaining graph, extends within
the common neighborhood, and deletes the clique edges. This operation
preserves the invariant that every recorded clique is complete in the
original graph and that different recorded cliques have no common edge.
Only cliques with at least three vertices contribute a positive bound.

The completed discovery run processed all 310 line graphs and returned

    corners                         187358,
    diagonal lower count             90752,
    row and column packing count    102349,
    sum of lower counts             193101,
    sum minus corner budget           5743.

The full literal packings are retained in completion_cut_probe.json.
These are integer outputs on one specified source, not an optimum, a
universal source-size estimate, or a Ramsey certificate. The source was
already known to fail the full triangle constraints; the useful discovery
is that this particular global counting criterion detects it. No
additional verification pass or new all-source exclusion was performed.

## 7. Remaining research implication

The exact next task for this route is to bound the row and column
deficits, or to construct explicit valid packings, uniformly over the
possible source sets at an improved grid side. The construction in
fibers/GOLOMB_SUMSET_CONSTRUCTION.md and the separated binary cube in
fibers/THREE_CUBE_SOURCE.md show that repeated translates and a generic
three-dimensional cube cannot by themselves force such a bound.

The present argument uses elementary cut counting, integer balancing,
and the established unique-completion geometry. No claim of universal
priority or superiority to the prior interval-Golomb method is made.
Neither R3<465 nor R4<100000 follows from these criteria alone.
