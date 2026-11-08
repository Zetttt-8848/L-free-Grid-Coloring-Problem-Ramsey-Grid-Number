# Colored boundary minima and adjacent-layer paths

This package gives a second counting improvement beyond the six-disjoint-
Golomb minima bound. It retains the **diagonal color** of each charged
boundary pair and couples neighboring shifts. All statements through
Section 4 have direct proofs; Section 5 is a finite diagnostic.

## 1. Colored boundary-minimum charging

Use coordinates 0,...,n-1. Let A_c be the positions of color c on the main
diagonal of an L-free three-color square. At distance d, each
F_d(A_c)={u:u,u+d in A_c} splits into two disjoint Golomb sets, according
to the actual color of the completion cell (u+d,u). Across c=0,1,2 these
are six disjoint sets of starting positions. The geometric reduction is
proved in the preceding checkpoint's `numeric_upper/THEOREM.md`.

Assume n<=481 and the established span lower bounds G(24)>=425,
G(25)>=480. Every one of the six sets has at most24 marks. Put b=n-425.
For 1<=d<b, its possible positions are 0,...,n-d-1. A24-mark set must
have minimum at most n-d-426=b-d-1, since otherwise its span is at most424.
Thus every24-mark set has a minimum in the first b-d starting positions.

Let L be the actual prefix diagonal word of length b, and define

`m_c(d,L)=#{u:0<=u<b-d, L_u=L_(u+d)=c}`.

For a fixed original diagonal color c there are only two completion-color
sets. The minima of distinct sets are distinct, and each such minimum is
counted by m_c(d,L). Therefore the number of24-mark sets of original color
c is at most `min(2,m_c(d,L))`. Every remaining set has at most23 marks.
Writing R_d=sum_c |F_d(A_c)| gives the universal bound

`R_d <= 138 + sum_c min(2,m_c(d,L)).`                         (1)

The same argument using maxima gives (1) with the suffix word on positions
425,...,n-1. In fact one may use the stronger sum of
`min(2,m_c(d,L),m_c(d,right))`. The present proof only needs the prefix.

Discarding the color information gives the earlier scalar bound
`R_d<=138+min(6,b-d)`. Keeping colors matters: six matches of a single
diagonal color can pay for only two large Golomb sets, not all six.

## 2. Adjacent match layers form a path

Fix q with 2q<=b and take X to be the first q letters of L, and Y the
last q letters. For 1<=k<=q put

`m_c(k)=#{i:0<=i<k, X_i=Y_(q-k+i)=c}`,
`t_k=sum_c min(2,m_c(k))`.

Then (1) says `R_(b-k)<=138+t_k`. In particular
`0<=t_k<=min(6,k)`.

**Path lemma.** For 2<=k<=q,

`t_(k-1)+t_k <= B_k := max_(r=1,2,3) min(4r,2k-r).`         (2)

To prove this, place the k vertices X_0,...,X_(k-1) on one side and the k
vertices Y_(q-k),...,Y_(q-1) on the other. The match comparisons at layer k
are edges X_i--Y_(q-k+i), while those at layer k-1 are
X_i--Y_(q-k+1+i). Together they form one alternating path with2k vertices
and2k-1 edges. If r distinct colors occur on its vertices, at least r-1
edges have endpoints of different colors: traverse the path and account
for the first appearance of each new color. Consequently the number of
same-color edges is at most2k-r. Capping each color's contribution at two
per layer can only reduce this count, and also bounds the contribution
of each color across the two layers by four. This proves both bounds in
the minimum and then (2).

The values for k=2,...,8 are

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| B_k | 3 | 4 | 6 | 8 | 9 | **11** | 12 |

The value at k=7 is11, not10. An early inter-agent arithmetic message
contained10; it is corrected here and is not used in any result.

This lemma controls different shifts simultaneously by their shared
colored endpoints. Its proof does not enumerate square colorings or
assume any unproved source-budget conjecture.

## 3. A weighted deficit that needs no optimization solver

Write `delta_k=min(6,k)-t_k`. From (2), respectively at k=4,6,7,

`delta_3+delta_4>=1`,
`delta_5+delta_6>=2`,
`delta_6+delta_7>=1`.

Suppose `0<=v_1<=...<=v_q` and q>=7. Multiply these three inequalities
by v_3, v_5 and v_6-v_5. The resulting coefficient of delta_3 is v_3;
of delta_4 is v_3<=v_4; of delta_5 is v_5; of delta_6 is v_6; and of
delta_7 is v_6-v_5<=v_7. All remaining deficits are nonnegative. Hence

`sum_(k=1)^q v_k delta_k >= v_3+v_5+v_6.`                   (3)

This is an explicit double-counting certificate: its multipliers and
every resource coefficient are displayed. No floating LP dual is needed.

## 4. Application to the new464 certificate

For a nonnegative weight sequence w supported on at most n consecutive
positions, let a_d=sum_i w_i*w_(i+d). Only d<n contributes. The joint
three-color convolution argument gives the necessary condition

`sum_(d>0) (n-d-3U_d)*a_d <= n*a_0`

whenever R_d<=U_d. Use the six-class bound
`U_d=138+min(6,max(0,n-d-425))` on the support of the following weights:

`w_i=i(86-i), 1<=i<=85`, zero elsewhere.

The exact a_d are nonnegative and decreasing, so v_k=a_(b-k) are
nondecreasing. Formula (3) improves the contradiction expression by

`3*(a_(b-3)+a_(b-5)+a_(b-6))`.

The independent integer checker reconstructs all a_d by literal products.

| n | Six-class contradiction gap | Boundary weighted deficit | New gap |
|---|---:|---:|---:|
| 464 | 477965143 | 240395555 | **1199151808** |
| 463 | -3527580772 | 249859659 | **-2778001795** |

The positive464 value is another complete proof of exclusion, using a
stronger shared-boundary count. The463 value is negative, so this particular
explicit inequality does not exclude463. It is not a coloring witness or
a proof that the larger boundary-counting program must fail.

## 5. A finite clue beyond adjacent paths

For arbitrary two words X,Y of length6 on three colors, exact enumeration
gives `sum_(k=1)^6 t_k<=14`, whereas independent layer capacities sum to21.
After using only the safe global color relabeling X_0=0, all177147 word
pairs were checked. There are two normalized maximizers:

`X=001111, Y=000011`, and its exchange of colors1 and2.

Their profile is `(0,0,2,4,4,4)`. The standard-library checker records this
complete finite domain and all maxima. This is **FINITE-CHECKED local
evidence**, distinct from the direct universal proofs above. No general
formula for arbitrary word length is asserted. The neighboring package
contains further bounded diagnostics; they must retain their own scopes.

The next mathematical task is to prove a sharp multi-layer charging rule
for these capped colored comparisons. It could force a substantially
larger weighted loss than (3), potentially addressing463. This package
does not complete that step and does not claim global novelty priority.
