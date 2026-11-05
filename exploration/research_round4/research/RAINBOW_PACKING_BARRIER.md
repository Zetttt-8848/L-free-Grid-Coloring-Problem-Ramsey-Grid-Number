# Disjoint rainbow sets exclude the ten-row scalar amplification route

Root derivation, R4-RESEARCH-0006. This is a limitation theorem for a precisely specified proof method. It is not a Ramsey upper bound. It supersedes the unresolved hope that a more efficient nonnegative rainbow hitting inequality on T_10 alone could close side 464 through the maximum-multiplicity criterion.

Write T_N={(v,u):0<=u<v<N}. A proper coloring has no monochromatic directed L. Let R(chi) be the set of rainbow corners in a proper three-coloring chi.

## 1. Statements

There exist thirty proper three-colorings of T_10 whose rainbow sets are pairwise disjoint. Every rainbow in these colorings has step in {1,2,3,4,5}. Moreover, twenty-four of these colorings have all their rainbow steps in {1,2,3,4}.

Consequently, suppose nonnegative weights w_e on the corners of T_10 satisfy

    sum_(e in R(chi)) w_e >= 1                       (1)

for every proper three-coloring chi of T_10. Then:

* the divisibility-only multiplicity b_464(w) is at least 30;
* the exact maximum multiplicity kappa_464(w), which retains the positions and boundaries of every embedding, is at least 24.

In particular, no such inequality can establish R3<=464 by counting all positive integral homothetic copies of T_10 and then using only the scalar budget R<=binom(464,2). This includes ordinary hitting sets, fractional weights, and local lower bounds normalized to have right side one. It also includes patterns supported on a subset of T_10, since every full proper coloring restricts to a proper coloring of that subset.

The conclusion concerns this particular amplification scheme. It does not rule out larger local patterns, additional constraints on the positions of host rainbows, joint line-discrepancy inequalities, or other methods for the Ramsey bound.

## 2. Five explicit proper colorings

The five colorings A through E are given below. Row v lists the colors at columns u=0,...,v-1.

| row v | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 10 | 20 | 01 | 01 | 20 |
| 3 | 120 | 022 | 101 | 110 | 001 |
| 4 | 0002 | 2212 | 1010 | 1001 | 2110 |
| 5 | 01111 | 11010 | 22222 | 22222 | 02222 |
| 6 | 222210 | 122010 | 202120 | 020021 | 102021 |
| 7 | 0021102 | 2211002 | 0020122 | 0201022 | 0020122 |
| 8 | 01022111 | 00000202 | 02201021 | 10022211 | 10210021 |
| 9 | 200120122 | 020102102 | 100222210 | 101020200 | 220220200 |

Here is a complete arithmetic proof of their corner properties. In F3, a triple sums to zero exactly when it is monochromatic or rainbow: a triple with repeated label a and distinct label b has sum 2a+b=b-a, which is nonzero.

For each displayed coloring define

    G_d(v,u)=c(v,u)+c(v+d,u)+c(v+d,u+d) in F3.

For each d, the next table gives all its G_d rows in the order v=1,...,9-d, with u increasing within each row. A slash separates successive rows. These additions cover every directed corner of T_10.

| coloring | step d | corner-sum rows |
|---|---|---|
| A | 1 | 1 / 12 / 122 / 1221 / 12212 / 212122 / 1112121 / 21121212 |
| A | 2 | 1 / 12 / 212 / 1101 / 22121 / 221212 / 2112122 |
| A | 3 | 2 / 22 / 222 / 1122 / 21211 / 212122 |
| A | 4 | 1 / 12 / 221 / 2212 / 11212 |
| A | 5 | 2 / 12 / 211 / 2122 |
| A | 6 | 2 / 22 / 112 |
| A | 7 | 1 / 22 |
| A | 8 | 1 |
| B | 1 | 2 / 11 / 122 / 1020 / 12221 / 221112 / 2211221 / 22112211 |
| B | 2 | 2 / 21 / 112 / 2112 / 11122 / 122211 / 2211122 |
| B | 3 | 1 / 11 / 121 / 2122 / 11212 / 211211 |
| B | 4 | 1 / 12 / 212 / 2111 / 12122 |
| B | 5 | 1 / 11 / 221 / 1212 |
| B | 6 | 1 / 22 / 111 |
| B | 7 | 2 / 21 |
| B | 8 | 2 |
| C | 1 | 1 / 12 / 212 / 2121 / 11221 / 221221 / 2111212 / 12112122 |
| C | 2 | 2 / 21 / 212 / 2121 / 12212 / 122121 / 1211221 |
| C | 3 | 1 / 12 / 120 / 1122 / 22111 / 221222 |
| C | 4 | 1 / 11 / 222 / 2221 / 21121 |
| C | 5 | 2 / 20 / 111 / 1222 |
| C | 6 | 2 / 21 / 111 |
| C | 7 | 1 / 21 |
| C | 8 | 1 |
| D | 1 | 1 / 22 / 211 / 2112 / 11212 / 211112 / 1222121 / 21111101 |
| D | 2 | 1 / 12 / 221 / 1222 / 22221 / 112121 / 2201121 |
| D | 3 | 2 / 12 / 121 / 2221 / 21122 / 111211 |
| D | 4 | 1 / 21 / 122 / 1211 / 22221 |
| D | 5 | 1 / 22 / 121 / 2211 |
| D | 6 | 2 / 22 / 111 |
| D | 7 | 2 / 11 |
| D | 8 | 1 |
| E | 1 | 2 / 21 / 022 / 1221 / 11112 / 121122 / 1221112 / 22122211 |
| E | 2 | 1 / 21 / 212 / 2121 / 22212 / 111112 / 2112221 |
| E | 3 | 2 / 11 / 121 / 2222 / 22120 / 212111 |
| E | 4 | 2 / 21 / 122 / 0122 / 11111 |
| E | 5 | 2 / 12 / 121 / 1212 |
| E | 6 | 2 / 21 / 121 |
| E | 7 | 2 / 12 |
| E | 8 | 2 |

All the zero positions, and the actual three labels there, are as follows. The notation (v,u;d) means the corner with cells (v,u),(v+d,u),(v+d,u+d).

| coloring | zero position | three labels | step and sorted base gaps |
|---|---|---|---|
| A | (4,2;2) | 021 | (2;1,2,3) |
| B | (4,1;1) | 210 | (1;1,2,4) |
| B | (4,3;1) | 210 | (1;0,3,4) |
| C | (3,2;3) | 120 | (3;0,2,3) |
| C | (2,1;5) | 102 | (5;0,1,2) |
| D | (8,6;1) | 120 | (1;0,1,6) |
| D | (7,2;2) | 012 | (2;0,2,4) |
| E | (3,0;1) | 021 | (1;0,2,5) |
| E | (5,4;3) | 201 | (3;0,1,4) |
| E | (4,0;4) | 210 | (4;0,1,3) |

Each zero position has three distinct labels. Every other corner has nonzero sum and therefore cannot be monochromatic. This proves that all five colorings are proper and that their complete rainbow sets are exactly those in the last table. No assertion of nonexistence from a search is used in this proof.

## 3. Six symmetries turn the five arrays into a disjoint packing

Identify a cell of T_10 with its three gap coordinates

    (u, v-u-1, 9-v),

which are nonnegative and sum to eight. A step-s corner has a unique base vector

    r=(u, v-u-1, 9-v-s),

and consists of r+s*e_1, r+s*e_2, r+s*e_3. Here e_i are the three coordinate unit vectors. Permuting the coordinates therefore preserves corners and their steps. Pulling back a coloring by any of the six permutations preserves its properness.

The orbit of a corner is specified exactly by its step and the sorted coordinates of r. If the three coordinates of r are distinct, its orbit has six members: a permutation fixing the corner must fix r, and a vector with distinct coordinates has only the identity stabilizer.

The ten entries in the final column of the last table are all different. Each has three distinct base coordinates. Thus no two of the ten displayed rainbow corners lie in the same symmetry orbit. It follows that the six images of any one of A,...,E have pairwise disjoint rainbow sets: within each corner orbit the six images are six different corners. Images belonging to different arrays are disjoint because the arrays use different corner orbits.

This supplies thirty proper colorings with pairwise disjoint, nonempty rainbow sets. Discarding the six images of C leaves twenty-four colorings, derived from A,B,D,E. Their rainbows all have steps in {1,2,3,4}. This proves the packing assertions.

## 4. A general weighted packing obstruction

If proper colorings chi_j have pairwise disjoint rainbow sets, summing (1) gives

    number of colorings <= sum_(e in union R(chi_j)) w_e.  (2)

The equality of the right side with the sum of the individual contributions uses disjointness. Its comparison with any larger edge set uses w_e>=0.

More generally, the same argument permits nonnegative multipliers lambda_j: if each corner belongs to rainbow sets of total lambda-weight at most one, then the right side for their union is at least sum_j lambda_j. The disjoint construction above takes every lambda_j=1.

Define the earlier divisibility bound by

    b_N(w)=max_(1<=h<=N-2) sum_(e: step(e) divides h) w_e.

All thirty rainbow sets lie at steps dividing 60. Since 60<=462, using h=60 and (2) proves b_464(w)>=30. In particular, an ordinary hitting set satisfying (1) must have divisibility multiplicity at least 30, not at most 18.

## 5. Exact incidence formula, including boundary positions

The preceding divisibility bound can overcount embeddings. The obstruction survives when that loss is removed.

For a local pattern T_m, let e have step s and base vector r with nonnegative coordinates summing to m-2-s. Let a host corner in T_N have step h and base vector t, whose coordinates sum to N-2-h. A positive integral homothety sends e to that host corner exactly when

    s divides h,   d=h/s,   and t_i>=d*r_i for i=1,2,3.  (3)

Proof. An embedding acts on the gap coordinates by z -> a+d*z, where a has nonnegative integer coordinates. Matching the corner determines d=h/s and a=t-d*r. If these coordinates are nonnegative, their sum is N-2-d*(m-2), exactly the sum required for the embedding of the full T_m. Conversely every embedding must satisfy these equations. Thus the embedding is unique when (3) holds and does not exist otherwise.

The exact weighted multiplicity of that host corner is consequently

    m_w(h,t)=sum_(e: s_e divides h)
                w_e * 1{t_i >= (h/s_e)*r_(e,i) for every i}.  (4)

Let kappa_N(w) be the maximum of (4) over host corners. There are

    C(N,m)=sum_(d=1)^floor((N-2)/(m-2)) binom(N-d*(m-2),2)

embeddings: for fixed d, the three coordinates of a sum to N-2-d*(m-2). Summing the local inequality over these embeddings gives, for any proper host coloring,

    C(N,m) <= sum_(host rainbow corners q) m_w(q)
            <= kappa_N(w)*R.                         (5)

This is the exact maximum-multiplicity version of the earlier scalar criterion.

Now set N=464 and choose the host corner with step 12 and base vector (150,150,150), namely

    {(301,150),(313,150),(313,162)}.

Every corner of T_10 with step s in {1,2,3,4} satisfies (3) for this host corner. Indeed s divides 12, each local base coordinate is at most 8-s, and

    (12/s)*(8-s) <= 84 < 150.

In particular, all the rainbow corners of the twenty-four colorings derived from A,B,D,E occur in (4). Equation (2) therefore gives

    kappa_464(w) >= m_w(12,(150,150,150)) >= 24.      (6)

This uses a specified host corner where all the required embeddings actually exist. It does not substitute the coarser divisibility count for the boundary conditions.

## 6. Consequence for the proposed R3 improvement

For m=10 and N=464 the embedding count can be evaluated directly:

    C(464,10)=sum_(j=1)^57 binom(8j,2)
             =32*sum_(j=1)^57 j^2 - 4*sum_(j=1)^57 j
             =2021068.

Also binom(464,2)=107416. The scalar rainbow-energy bound for a proper three-coloring of T_464 is R<=107416. To obtain a contradiction from (5) and only that bound would require

    2021068 > kappa_464(w)*107416.

But (6) makes the right side at least 24*107416=2577984, which is larger by 556916. Therefore no choice of the nonnegative local weights in (1) can make this proof scheme close side 464. The conclusion remains valid when all monochromatic-corner exclusions on the local triangle are retained for free.

A stronger argument could use the location-dependent expression in the middle of (5) together with additional restrictions on the host rainbow set. It could also use other local sizes or combine the actual corner labels with line discrepancy. Those possibilities are outside this limitation theorem; no general impossibility of a rainbow method is asserted.

## Scope and provenance

The arrays were discovered by a bounded search. The mathematical evidence used here is the explicitly displayed arrays, their complete finite-field additions, and the symmetry and incidence proofs above. No solver negative, optimality assertion, or exhaustive enumeration is a premise. The use of a disjoint packing to bound a nonnegative covering inequality is elementary. The concrete construction changes the research route, but it is not the requested original superior method and carries no claim of universal priority.
