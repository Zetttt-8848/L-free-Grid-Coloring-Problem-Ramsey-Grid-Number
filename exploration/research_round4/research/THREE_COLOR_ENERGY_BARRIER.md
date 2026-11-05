# Actual three-color tests also obstruct universal ten-row energy bounds

Root derivation, R4-RESEARCH-0007. The test in WEIGHTED_RAINBOW_ENERGY.md used eleven-dimensional residue vectors to exclude a positive-semidefinite matrix criterion. The argument below uses actual three-colorings and excludes a wider, but still precisely scoped, class of universal energy bounds. It does not exclude estimates that use the absence of monochromatic corners in an essential way.

## 1. The statistic controlled by pair energy

For every corner e and every coloring, let r_e and b_e be its rainbow and monochromatic indicators. If P_e is the number of equal-color pairs among its three cells, then

    r_e-2*b_e=1-P_e.                               (1)

This follows by considering the three color patterns: monochromatic, exactly two colors, and rainbow give P_e=3,1,0 and r_e-2*b_e=-2,0,1 respectively.

Let nonnegative local weights w_e on T_m have total W, and let a_q be the exact weighted incidences of all positive integral homothetic copies of T_m in T_N, as defined in RAINBOW_PACKING_BARRIER.md. Define the host statistic

    S(c)=sum_(host corners q) a_q*(r_q(c)-2*b_q(c)). (2)

If the local inequality sum_(local rainbow e) w_e>=1 holds in every proper three-coloring of T_m, then a proper host coloring must satisfy S(c)>=C(N,m). Therefore one conceivable argument would prove a universal upper bound

    S(c)<=K<C(N,m) for every three-coloring c.      (3)

The theorem below shows that this argument cannot work at (N,m)=(464,10), for any choice of the nonnegative local weights satisfying the forcing condition.

## 2. A residue test using three actual colors

Let q>m-2 be an odd prime with q not divisible by three. Partition the q residues into three labeled color classes as equally as possible, uniformly over all partitions with those three prescribed sizes. Color each host cell (v,u) by the class containing v+u modulo q. This is a probability distribution on actual three-colorings of T_N.

For two distinct residues, the probability of receiving the same color is

    rho=[sum_(i=1)^3 n_i*(n_i-1)]/[q*(q-1)],

where n_i are the three class sizes. Balanced sizes give

    sum_i n_i^2=(q^2+2)/3,
    rho=(q-2)/(3q).

To see the square-sum formula, write q=3t+1 or q=3t+2. The class sizes are respectively (t+1,t,t) or (t+1,t+1,t); squaring and adding gives the displayed expression in both cases.

At a corner of step h not divisible by q, the three residues are r,r+h,r+2h and are distinct, because q is odd and prime. Each of the three pairs therefore has same-color probability rho. Equation (1) gives

    E[r_e-2*b_e]=1-3*rho=2/q.

If q divides h, all three residues agree, so the corner is always monochromatic and the same statistic equals -2.

Put

    C_q(N,m)=sum_(1<=d<=floor((N-2)/(m-2)), q divides d)
                                  binom(N-d*(m-2),2).

Every local step s lies strictly between zero and q, so q divides the image step d*s exactly when q divides d. Each embedding contributes total local weight W. By summing expectations over all embeddings and all local corners, we obtain the exact formula

    E[S(c)]
      =(2/q)*W*(C(N,m)-C_q(N,m))-2*W*C_q(N,m)
      =(2W/q)*[C(N,m)-(q+1)*C_q(N,m)].             (4)

Hence at least one actual three-coloring has S(c) at least the right side of (4). This is a finite averaging proof. It does not require a search for the maximizing partition, nor does it assert that any of these colorings is proper.

## 3. Exact consequence at side 464

Use m=10, N=464, and q=13. The dilation count is C=2021068. The dilations divisible by thirteen are 13,26,39,52, giving

    C_13=binom(360,2)+binom(256,2)
                       +binom(152,2)+binom(48,2)
        =64620+32640+11476+1128
        =109864.

It follows that

    C-14*C_13=482972,
    E[S(c)]=(965944/13)*W.                         (5)

The thirty proper T_10 colorings with disjoint rainbow sets in RAINBOW_PACKING_BARRIER.md prove that every nonnegative local forcing vector has W>=30. Thus there is an actual three-coloring of the host satisfying

    S(c)>=28978320/13
          =C+2704436/13 > C.                      (6)

Consequently no universal inequality of the form (3) can hold for these incidences. The conclusion is stronger than excluding a positive-semidefinite proof of (3): it excludes any proof of that universal upper bound, since (6) supplies a mathematical existence proof of a violating three-coloring.

## 4. What this does and does not exclude

The residue colorings contain monochromatic corners at step thirteen. Therefore they are not counterexamples to the desired Ramsey bound. They refute only a proposed upper bound on S(c) that is claimed for every three-coloring before properness is used to set all b_e to zero.

An estimate proved specifically for proper colorings could still be stronger. It might retain individual monochromatic-corner exclusions, use additional terms with different monochromatic penalties, exploit the shared affine parameter from CORNER_SUM_COORDINATES.md, or use a different local pattern or embedding family. None of those possibilities is decided here.

This theorem explains why replacing the eleven-dimensional matrix test by the mere fact that there are three actual colors is insufficient for the current universal pair-energy scheme. The next mathematical step must use properness more deeply than substituting B=0 in an otherwise universal inequality. No new value of R3 or R4 is claimed, and the construction carries no universal originality claim.
