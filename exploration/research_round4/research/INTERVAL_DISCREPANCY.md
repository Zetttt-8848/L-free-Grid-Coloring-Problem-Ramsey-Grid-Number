# Integer interval discrepancy and a periodicity penalty

Root derivation, R4-RESEARCH-0004. This is a quantitative necessary inequality for a colored word. Its evaluation with the inherited diagonal caps does not improve the current Ramsey bound.

Let chi:[N]->[k], with k>=2, and put

    M_d=#{i:1<=i<=N-d, chi(i)=chi(i+d)}.

Assume M_d<=U_d, where U_d are any valid upper bounds. Let t be a positive multiple of k with t<N. Then

    (k-1)Nt + 2 sum_{d=1}^{t-1}(t-d)(k U_d-(N-d))
      >= k max(0,N-t-U_t) + t(k^2-1)/3.               (1)

The right side retains two sources of discrepancy: boundary intervals with lengths not divisible by k, and the color changes forced at lag t.

## Proof

For i in [N], define v_i=e_{chi(i)}-(1/k)1 in R^k, and extend v_i by zero outside [N]. For every integer x, put g_x=sum_{i=x}^{x+t-1}v_i, and V=sum_x ||g_x||^2. All these sums are finite. An individual point lies in t such intervals; a pair at distance d<t lies in t-d of them. Since ||v_i||^2=(k-1)/k and <v_i,v_j>=1_{chi(i)=chi(j)}-1/k, expansion gives

    kV=(k-1)Nt+2 sum_{d=1}^{t-1}(t-d)(kM_d-(N-d)).    (2)

Replacing M_d by U_d in (2) gives the left side of (1) as an upper bound for kV.

For the full intervals x=1,...,N-t+1, the coordinates of g_x are integers summing to zero, because t/k is an integer. Any nonzero such vector has squared norm at least two: at least one coordinate is a positive integer and another is a negative integer.

For 1<=x<=N-t,

    g_{x+1}-g_x=v_{x+t}-v_x.

If chi(x+t) differs from chi(x), this difference is nonzero, so at least one of g_x,g_{x+1} is nonzero. Therefore

    2 1_{chi(x+t)!=chi(x)} <= ||g_x||^2+||g_{x+1}||^2.

Summing over x counts each full-interval norm at most twice. It follows that

    sum_{x=1}^{N-t+1}||g_x||^2 >= N-t-M_t
                               >= max(0,N-t-U_t).     (3)

There are two boundary intervals of each occupied length ell=1,...,t-1. If ell=kq+r with 0<=r<k, the smallest possible squared norm of its color-count vector minus (ell/k)1 is r(k-r)/k. To see this, two counts differing by at least two can be brought one unit closer, reducing their sum of squares. The minimum is attained by k-r counts q and r counts q+1, and substitution gives the formula.

Because t is divisible by k, each nonzero residue r=1,...,k-1 occurs t/k times among 1,...,t-1. Thus the boundary contribution is at least

    (2t/k^2) sum_{r=1}^{k-1} r(k-r)
        = t(k^2-1)/(3k).                              (4)

The finite sum in (4) follows from the formulas for the sums of consecutive integers and their squares. Adding (3) and (4), multiplying by k, and comparing with (2) proves (1).

This argument couples neighboring interval vectors. It is stronger than using only the pointwise minimum of each squared norm. A purely real quadratic estimate would allow both vectors to be half of the color-change vector with opposite signs; the integer coordinates exclude that possibility.

## Three-color specialization and executed discriminator

On the main diagonal of a corner-free three-color grid, the inherited signed-Golomb bound gives M_d<=6q(N-d). One may also use M_d<=N-d. Substituting any of these valid caps into (1) is legitimate.

The exact discovery evaluation considered the listed side lengths in interval_discrepancy_probe.json and every positive multiple of three below each side length. At N=464 no tested t gives a contradiction. The largest unnormalized lower-minus-upper value is -1641 after multiplying the variance comparison by three; it occurs at t=3. The more informative normalized comparison at t=66 still has upper 6170 and lower 956 in those multiplied units. Thus this particular interval penalty does not bridge the gap. The calculation evaluates the proved inequality; it does not decide whether a compatible word or grid exists.

The same inequality applies to k=4 with any valid aggregate four-color diagonal profile, but it does not supply the substantially smaller profile required for R4<100000. No new numerical Ramsey upper bound is asserted.
