# A matrix energy bound retaining the positions of rainbow corners

Root derivation, R4-RESEARCH-0006. This supplies a conditional matrix amplification criterion after RAINBOW_PACKING_BARRIER.md excludes the ten-row maximum-multiplicity argument. An exact residue-class test then excludes this matrix refinement as well at (N,m)=(464,10). No new Ramsey bound is asserted here.

## 1. Weighted corner matrix

Let P=T_N, with one row of a real symmetric matrix Q for each cell. Assign a real weight a_e to each corner e. For distinct cells p,q on a common row, column, or slope-one diagonal, set Q_(p,q)=a_e, where e is their unique completing corner in T_N. Set Q_(p,q)=0 for other distinct cells, and let Q_(p,p)=D_p.

The completing corner is internal to T_N. Specifically, a row pair (v,u),(v,w) with u<w completes at (v-(w-u),u); a column pair (v,u),(w,u) with v<w completes at (w,u+w-v); and a slope-one pair (u+d,u),(v+d,v) with u<v completes at (v+d,u). Their respective inequalities ensure the new cell has column strictly less than row. The pair's direction determines which role it occupies, so the completion is unique. Thus every corner contributes exactly its three pairs to Q.

Assume Q is positive semidefinite. For a k-coloring c, put

    z_p=e_(c(p))-(1/k)*1  in R^k,

where e_i are the coordinate vectors and 1 is the all-ones vector. Then

    <z_p,z_q>=1{c(p)=c(q)}-1/k,
    ||z_p||^2=(k-1)/k.

For a corner e, let r_e and b_e be its rainbow and monochromatic indicators. The sum of its three pair-equality indicators is 1-r_e+2b_e: the three possible color patterns give 3,1,0 respectively. Expanding the matrix quadratic form therefore yields the exact identity

    sum_(p,q) Q_(p,q)<z_p,z_q>
      = (k-1)/k * sum_p D_p
        + 2*(1-3/k)*sum_e a_e
        - 2*sum_e a_e*r_e + 4*sum_e a_e*b_e.       (1)

The left side is nonnegative. Indeed it is the sum, over the k coordinates of z, of the corresponding quadratic form of Q. For a proper coloring, every b_e vanishes, so

    sum_(rainbow e) a_e
       <= (k-1)/(2k)*sum_p D_p
          +(1-3/k)*sum_e a_e.                     (2)

In particular,

    sum_(rainbow e) a_e <= (1/3)*sum_p D_p          (k=3),  (3)
    sum_(rainbow e) a_e <= (3/8)*sum_p D_p
                              +(1/4)*sum_e a_e   (k=4).  (4)

Weights a_e need not be nonnegative for this identity. Positive semidefiniteness is essential; merely specifying the diagonal entries does not prove it. The four-color term involving the total corner weight cannot be dropped.

## 2. Exact-incidence amplification

Suppose nonnegative local corner weights w_e on T_m have the proved property

    sum_(local rainbow e) w_e >= 1                 (5)

in every proper three-coloring of T_m. Count all integral positive homotheties into T_N, and let a_q be their exact weighted incidence at the host corner q. In gap coordinates, if q has step h and base t, then

    a_q=sum_(local e: s_e divides h)
          w_e * 1{t_i >= (h/s_e)*r_(e,i) for all i}, (6)

where s_e and r_e are the local step and base. This is the formula proved in RAINBOW_PACKING_BARRIER.md. The number of homotheties is

    C(N,m)=sum_(d=1)^floor((N-2)/(m-2))
                         binom(N-d*(m-2),2).

Summing (5) gives

    C(N,m)<=sum_(host rainbow q) a_q.              (7)

Build Q with the off-diagonal entries determined by these a_q. If diagonal values D_p can be proved to make Q positive semidefinite and satisfy

    sum_p D_p < 3*C(N,m),                          (8)

then (3) and (7) contradict each other. This proves R3<=N under the stated two mathematical inputs: the local forcing statement (5) and a positive-semidefinite matrix with the strict trace bound (8).

Unlike the scalar estimate using max_q a_q, condition (8) can retain the spatial pattern of the incidences. RAINBOW_PACKING_BARRIER.md proves that the scalar route fails at (N,m)=(464,10), even with arbitrary nonnegative local weights. That packing argument alone does not exclude (8); the additional residue-class argument in section 5 does.

Neither required input is supplied here for a strict improvement. In particular, the raw negative for a zero-rainbow coloring of T_10 is not a proof of (5), and an exploratory floating eigenvalue would not be a proof that Q is positive semidefinite. At the ten-row target, section 5 proves that no suitable trace bound exists in this framework.

## 3. Why separate local matrix bounds cannot suffice

The amplification must obtain a gain from the overlaps of the copies. This can be stated precisely.

Suppose T_m admits at least one proper three-coloring and the local weights satisfy (5). If Q_local is any positive-semidefinite matrix with those corner weights and diagonal D_local, applying (3) to that proper coloring gives

    1 <= sum_(its rainbows e) w_e
      <= (1/3)*sum_p D_(local,p).

Thus every such local matrix has trace at least three. Summing one independently embedded local matrix for each of the C(N,m) copies gives trace at least 3*C(N,m), so it cannot satisfy the strict inequality (8). A successful application needs a global matrix construction that does better than adding independent local bounds. The displayed proper colorings of T_10 ensure that this limitation applies at m=10.

## 4. The four-color cost in this same framework

If (5) is instead assumed for every proper four-coloring, formula (7) still holds. Let W=sum_e w_e. Since each embedding contributes all its local corner weights exactly once,

    sum_(host corners q) a_q=C(N,m)*W.

Combining (4) and (7), a contradiction through this same argument would require

    (3/8)*sum_p D_p < C(N,m)*(1-W/4).              (9)

A positive-semidefinite matrix has D_p>=0, by applying its quadratic form to the coordinate vector at p. Consequently W<4 is necessary for this specific criterion. For m=10, the thirty proper three-colorings in RAINBOW_PACKING_BARRIER.md are also proper colorings using at most four colors. Their disjoint rainbow sets force W>=30 under the four-color version of (5). Thus m=10 cannot supply (9). This is another precise limitation of this local-rainbow scheme, not a limitation on all four-color methods.

## 5. An exact residue-class obstruction to the ten-row matrix refinement

Let p be an odd prime larger than m-2. To each host cell (v,u) assign a unit vector determined by the residue of v+u modulo p:

    z_(v,u)=sqrt(p/(p-1))*(e_r-(1/p)*1),
    r=(v+u) modulo p.

Two such vectors have inner product 1 if their residues agree and -1/(p-1) otherwise. For a step-h corner, the three pair differences in v+u are h,h,2h. Since p is odd, all three inner products are 1 when p divides h, and all three are -1/(p-1) otherwise.

Apply the positive-semidefinite matrix Q to the coordinates of these vectors and sum. This gives

    0 <= tr(Q) + 6*A_div_p - 6/(p-1)*A_not_div_p,

where tr(Q) is the sum of the diagonal entries, A_div_p is the sum of the host corner weights a_q with p dividing the step, and A_not_div_p is the sum over the other steps. Hence

    tr(Q) >= 6/(p-1)*(A_total-p*A_div_p).           (10)

This argument uses the definition of positive semidefiniteness directly; no spectral computation is needed.

Every local step s satisfies 1<=s<=m-2<p. Thus p divides the image step d*s exactly when it divides the dilation d. Put

    C_p(N,m)=sum_(1<=d<=floor((N-2)/(m-2)), p divides d)
                                binom(N-d*(m-2),2).

Each homothety contributes total local weight W=sum_e w_e, so

    A_total=C(N,m)*W,    A_div_p=C_p(N,m)*W.

Substitution into (10) yields the universal trace obstruction

    tr(Q) >= [6/(p-1)]*W*[C(N,m)-p*C_p(N,m)].      (11)

Now take N=464, m=10 and p=11. The admissible dilations divisible by eleven are 11,22,33,44,55. Therefore

    C_11(464,10)
      =binom(376,2)+binom(288,2)+binom(200,2)
         +binom(112,2)+binom(24,2)
      =70500+41328+19900+6216+276
      =138220.

Together with C(464,10)=2021068, this gives

    C-11*C_11=500648,
    tr(Q) >= (1501944/5)*W.                        (12)

Any nonnegative local weights satisfying the three-color forcing condition (5) have W>=30 by the thirty disjoint rainbow sets in RAINBOW_PACKING_BARRIER.md. Consequently every positive-semidefinite Q with the exact incidence off-diagonal entries has

    tr(Q) >= 9011664 > 6063204 = 3*C(464,10).       (13)

This contradicts the trace requirement (8). Thus the ten-row matrix criterion cannot establish R3<=464, even with arbitrary nonnegative local weights, arbitrary diagonal choices, exact boundary incidences, and a global matrix construction exploiting the overlaps of copies.

The test vectors have eleven residue classes, rather than the three labels of an actual coloring. This is permitted because a positive-semidefinite matrix must have a nonnegative quadratic form on every real vector. It pinpoints what the relaxation discards: constraints specific to the actual three-color vectors could be stronger, but they would need a new argument beyond positive semidefiniteness alone. The obstruction does not concern a different local size or a different family of host embeddings.

## Research status

The identity (1), conditional criteria, and obstruction (13) have full derivations above. The latter closes the suggested ten-row positive-semidefinite refinement; it should not trigger a larger numerical matrix search for the same hypotheses. A different local pattern, a different embedding family, or stronger use of the actual color labels remains possible. The framework uses elementary quadratic forms and the unique-completion geometry. It is not a superior method and carries no claim of historical priority.
