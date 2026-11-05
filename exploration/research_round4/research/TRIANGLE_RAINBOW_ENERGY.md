# Rainbow corners and line discrepancy on the full strict triangle

Root research derivation, R4-RESEARCH-0004. This gives a global identity and a conditional amplification criterion. Checkpoint 0006 subsequently excludes the proposed T_10 application through either maximum multiplicity or the positive-semidefinite refinement; see RAINBOW_PACKING_BARRIER.md and WEIGHTED_RAINBOW_ENERGY.md. The identity and conditional criterion themselves remain valid.

Let T_N={(v,u):0<=u<v<N}. It has M=binom(N,2) cells and T=binom(N,3) directed corners. A rainbow corner means that its three cells have three distinct colors. For a k-coloring, let R count rainbow corners and B count monochromatic corners. For every row, column, and slope-one diagonal ell of T_N, let n_{ell,i} be its number of cells of color i and let |ell| be its length. Define

    V=sum_ell sum_{i=1}^k (n_{ell,i}-|ell|/k)^2.

## Exact global identity

For every k>=2 and every coloring,

    V+2R-4B
       = N(N-1)[2(k-3)N+5k+3]/(6k).                 (1)

In particular, a corner-free three-coloring satisfies

    V+2R=N(N-1)=2M,                                  (2)

so R<=M and V<=2M. A corner-free four-coloring satisfies

    V+2R=N(N-1)(2N+23)/24.                           (3)

Proof. Every pair in a row, column, or slope-one diagonal belongs to exactly one directed corner of T_N. For a row pair (v,u),(v,w), with u<w<v, the third cell is (v-(w-u),u). Its row exceeds u because v>w. For a column pair (v,u),(w,u), with u<v<w, the third cell is (w,u+w-v), whose column is less than w because u<v. For a slope-one pair (u+d,u),(v+d,v), u<v, its completion is (v+d,u). All these cells belong to T_N. The direction of the pair identifies its role and its unique completion.

Consequently the total number P of equal-color pairs on the three families of lines counts each corner according to its color pattern: three for a monochromatic corner, one for a corner using exactly two colors, and zero for a rainbow corner. Thus

    P=T-R+2B.                                       (4)

Each of the three line families has one line of every length 1,...,N-1. Hence sum_ell |ell|=3M and

    sum_ell |ell|^2=N(N-1)(2N-1)/2.

Expanding V and using sum_i n_{ell,i}=|ell| gives

    P=V/2+N(N-1)(2N-1)/(4k)-3M/2.                   (5)

Equating (4) and (5), and inserting T=N(N-1)(N-2)/6, gives (1). Equations (2) and (3) follow by setting B=0 and k=3 or 4. Every pair count used in the proof is internal to the full strict triangle; the same complete-line argument is not valid for an arbitrary sparse T(A).

For three colors the cubic terms cancel exactly. The resulting quadratic budget constrains rainbow corners and the imbalances of all three line directions simultaneously. For four colors a cubic term remains; discarding it would be incorrect.

## A precise local-to-global forcing criterion

Let P be a specified finite collection of cells in T_m, together with a collection E of directed corners among those cells. Assume it has the following proved property:

    Every corner-free three-coloring of P has a rainbow
    corner belonging to E.                           (F)

Monochromatic corners are excluded everywhere in P, including corners outside E. Only the rainbow corners in E incur the incidence cost below. This stronger formulation is useful because the ambient grid already excludes every monochromatic corner. The property is a separate mathematical hypothesis, not an established conclusion for the candidate found by a solver. For N>=m>=3, define

    C(N,m)=sum_{d=1}^{floor((N-2)/(m-2))} binom(N-d(m-2),2),
    b_N(E)=max_{1<=h<=N-2} #{e in E: step(e) divides h}.

If C(N,m)>b_N(E) binom(N,2), then R3(L)<=N.

Proof. Represent a cell (v,u) of T_m by its nonnegative gap coordinates

    (u, v-u-1, m-1-v),

which sum to m-2. A corner of step j consists of three gap-coordinate vectors obtained by adding j to each of the three different coordinates of one common nonnegative vector. Thus coordinate permutations preserve the corner relation, and so do positive integral dilation followed by adding a common nonnegative vector.

For a fixed dilation d, choose nonnegative a,b,c with a+b+c=N-2-d(m-2). Such a choice maps gap coordinates into the simplex for T_N. In row-column coordinates the map is

    (v,u) -> (a+b+1-d+dv, a+du).

It preserves the corner shape and multiplies every step by d. There are exactly binom(N-d(m-2),2) choices of a,b,c, giving C(N,m) embeddings in total. This counts labeled embeddings; possible symmetries of P do not affect the incidence argument.

Suppose a three-coloring of T_N has no monochromatic corner. By (F), each embedding contains a rainbow image of at least one edge in E. A fixed host rainbow corner of step h can be the image of a given e only if step(e) divides h. In that event the dilation is determined, and the image of the first cell determines both translation coordinates; hence there is at most one such embedding. A host rainbow corner is therefore counted at most b_N(E) times. It follows that C(N,m)<=b_N(E)R. Equation (2) gives R<=binom(N,2), contradicting the criterion. Finally T_N is a subset of an N by N square, so its obstruction proves the stated grid bound.

The coarser bound b_N(E)<=|E| is always available. For the whole T_m, if every corner-free three-coloring has at least r rainbow corners, the same incidence argument gives

    r C(N,m)<=binom(m,3) binom(N,2).                 (6)

A strict reverse inequality would establish R3<=N.

## What would close the present R3 target

At N=464 and m=10,

    C(464,10)=2021068,       binom(464,2)=107416.

Thus a proved pattern satisfying (F) with b_464(E)<=18 would suffice: the strict margin is 2021068-18*107416=87580. A bound of 19 would not suffice in this particular comparison, since the margin would be -19836.

Using all 120 corners of T_10 instead would require the local hypothesis r>=7 in (6). That hypothesis is false: TEN_TRIANGLE_ONE_RAINBOW.md gives a complete corner-free coloring with exactly one rainbow corner. This rules out that simple local-density shortcut.

The bounded discovery found three-colorings of T_6 through T_9 with exactly two colors on every corner. A different SAT encoding returned a raw negative for that exact-two-colors condition on T_10. No pencil-and-paper proof of that negative is supplied, so it is not a premise here. The bounded corner-deletion experiment retained 107 candidate corners, with b_464=107; it does not approach the sufficient value 18 and does not prove that a smaller pattern is impossible.

The identity (1), embedding count, and conditional criterion are proved above. The later construction in RAINBOW_PACKING_BARRIER.md proves that every nonnegative local rainbow-forcing inequality on T_10 has exact maximum host multiplicity at least 24 at N=464. Thus the proposed small hitting-set route cannot meet the threshold, even after allowing fractional weights or exact boundary incidences. WEIGHTED_RAINBOW_ENERGY.md also excludes the associated positive-semidefinite trace refinement. A different local pattern or a stronger inequality using actual color compatibility remains possible. Neither the numerical negative nor the conditional criterion is a new Ramsey bound. The line-count identity uses elementary quadratic counting and carries no priority claim.
