# A support correlation forced by the larger source triangle

Root auxiliary derivation, R4-RESEARCH-0003. The notation is that of fibers/DERIVATIONS.md. A is one monochromatic diagonal class in a three-color corner-free grid; its strict completion triangle has signs + and -. Translations of the entire geometry allow us to write the source diagonal with offset zero. Put F_d=A intersect (A-d), and let F_d^eps contain the starts of sign-eps cells on offset d. Write r_d=|F_d|, r_d^eps=|F_d^eps|, and U_eps={h>0:r_h^eps>0}.

The two translated triangles on F_d do not record all the cells available in T(A). Keeping the additional cells yields the following pointwise statement.

## Two alternative supporting cells

If u<v belong to F_d^eps, and h=v-u, then

    u in F_h^eps  or  u+d in F_h^eps,                 (1)
    u in F_{d+h}^{-eps}.                             (2)

Proof. The two sign-eps cells (u+d,u) and (v+d,v) force their completion Q=(v+d,u) to sign -eps. The three cells

    P=(v,u), Q=(v+d,u), R=(v+d,u+d)

form a corner of step d. All belong to T(A): u,v,u+d,v+d are source marks, and v>u. Since Q has sign -eps, P and R cannot both have that sign. At least one has sign eps. P has offset h and start u; R has offset h and start u+d. This proves (1); the offset and start of Q give (2).

In particular, the positive differences of F_d^eps must be supported by the same sign at the smaller offset and by the opposite sign at the larger offset:

    Diff^+(F_d^eps) subset U_eps intersect (U_{-eps}-d).  (3)

The known Golomb property of F_d^eps makes its positive pair differences distinct. Hence

    binom(r_d^eps,2)
        <= sum_{h>0} 1_{h in U_eps} 1_{h+d in U_{-eps}}. (4)

Dropping the first indicator recovers the earlier one-sided support-transfer inequality. Statement (1) also retains where a supporting cell must be, which (4) discards.

## A color-free necessary profile inequality

Let s_h=1_{h in U_+}+1_{h in U_-}, extended by zero to offsets outside the source span. Adding (4) for the two signs gives

    floor((r_d-1)^2/4)
      <= sum_{h>0} [1_{h in U_+}1_{h+d in U_-}
                    +1_{h in U_-}1_{h+d in U_+}]
      <= sum_{h>0} min(s_h,s_{h+d})
      <= sum_{h>0} min(2,r_h,r_{h+d}).                 (5)

The first left side is the minimum of binom(b,2)+binom(r_d-b,2) over integral b. For the second inequality, the bracket counts the colors present at offset h whose opposite is present at h+d, and thus is at most the number of colors present at either offset. Finally s_h<=min(2,r_h) at every h.

This improves the logical content of the tail-support constraint by requiring both offsets to be occupied. No improved R3 or R4 bound follows from (5) here.

## Exact retention of the signs on singly occupied offsets

Define t_h=1_{h in U_+}-1_{h in U_-}. The middle sum in (5) is exactly

    (1/2) sum_{h>0} (s_h s_{h+d} - t_h t_{h+d}).       (6)

This follows by substituting 1_{U_+}=(s+t)/2 and 1_{U_-}=(s-t)/2 and expanding the two products. The variable t_h vanishes at empty offsets and at offsets carrying both signs. On an offset carrying exactly one sign it equals that sign. Thus (6) retains the coupling between the actual signs of different singly occupied offsets; these signs cannot be selected separately for each d.

The unresolved quantitative task is an upper estimate for these coupled correlations or their pointwise form (1) that contradicts an actual small-color source size. Merely maximizing each correlation separately loses the shared sign information and does not complete that task.
