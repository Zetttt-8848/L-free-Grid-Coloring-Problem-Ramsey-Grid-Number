# Interlaced shared pairs: exclusive continuation and two missing positions

Root derivation, continuation0044. This joins the reflected-middle rule to
the shared-difference and unit budgets of the actual weak coloring. It
improves the earlier pair-hole charge: one shared difference can activate
at most one seed, even after both diagonal classes are counted. The
result is a structural and moment constraint, not a source-size theorem.

Let W(S) have a proper two-coloring, and let S=B disjoint union C be its
diagonal partition. Both classes are Golomb. Write b=|B|, c=|C|,
n=b+c, ell=span(S), and rho=|Delta B intersect Delta C|. Colors named B
and C refer to the diagonal colors. A strict cell with two B endpoints
has color C, and one with two C endpoints has color B.

For a shared length h, the two classes each have a unique h-pair. Call
the shared pair interlaced if their lower endpoints differ by p with
0<p<h. After exchanging the class names if necessary, write it as

    {r,r+h} subset C,
    {r+p,r+h+p} subset B,       0<p<h.                 (1)

The letters B,C in a use of (1) are local names for the left and right
pair classes; the set of shared lengths is counted without choosing
an additional class role. Let I be the number of interlaced shared
lengths. In particular I<=rho.

## 1. Four candidate positions

Associate with (1) the outer positions

    q_-=r+p-h,                 q_+=r+2h

and the interior positions

    v_-=r+2p,                  v_+=r+h-p.             (2)

The two outer positions are strictly outside the four-mark span:

    q_-<r<r+p<r+h<r+h+p<q_+.

The interiors satisfy r+p<v_-<r+h+p and r<v_+<r+h.
They can coincide with each other, or with an already occupied mark;
no generic-position assumption will be used.

**Exclusive-continuation theorem.** With f=1_S, the following three
inequalities hold for every interlaced shared pair:

    f(q_-)+f(q_+) <= 1,
    f(q_-)+f(v_-) <= 1,
    f(q_+)+f(v_+) <= 1.                               (3)

First, if q_+ is present, its diagonal color must be B. Otherwise the
three C marks r,r+h,r+2h repeat the difference h. Likewise, if q_-
is present its diagonal color must be C, since the B marks
r+p-h,r+p,r+p+h would repeat h.

Suppose both outer positions are present. Put t=h-p>0 and consider
the three cells of the same positive-offset fiber

    e_0=(r,r+p-h),
    e_1=(r+h,r+p),
    e_2=(r+2h,r+h+p).                                (4)

Their lower endpoints increase strictly, and all three offsets equal t.
The endpoint classes give color(e_0)=B and color(e_2)=C. The completion
of e_0,e_1 is (r+h,r+p-h), with two C endpoints and hence color B.
Properness forces color(e_1)=C. But the completion of e_1,e_2 is
(r+2h,r+p), with two B endpoints and hence color C. It forces
color(e_1)=B. This proves the first inequality of (3).

If q_+ is present, the five starts in (1), together with that outer
continuation, are exactly the upper reflected-middle seed:

    C contains r,r+h;
    B contains r+p,r+h+p,r+2h.

The completed reflected-middle rule in
fibers/BINARY_CORE_FIBER_TRANSFER_0044.md forces v_+ absent from all
of S. This proves the third inequality of (3). If q_- is present,
exchange the class roles and use the lower seed based at r+p, with
parameter p. Its three opposite-class marks are q_-,r,r+h, and it
forces v_- absent. This proves the second inequality. All these cells
and steps belong to the original positive weak triangle.

Consequently

    f(q_-)+f(q_+)+f(v_-)+f(v_+) <= 2.                 (5)

Equation (5) counts the two interior positions with their indicated
labels if they coincide. More geometrically, at least two DISTINCT
positions among (2) are absent: if both outer positions are absent,
use those two; otherwise exactly one outer position is present, and
the other outer position and the forced interior position are distinct
holes. Thus coincidence of the interior candidates does not remove
the two-hole conclusion.

For example, if p=h/2, both interior candidates coincide with occupied
marks in (1). Both outer positions must then be absent. This degenerate
case is covered by (3); it is not an admissible activated seed.

## 2. One seed per shared difference, across both class roles

Let K_seed count every upper and lower reflected-middle seed, allowing
both choices of its opposite-class pair. A seed determines an
interlaced shared pair. Conversely, in the normalization (1), its two
possible seeds are exactly the occupied q_+ and occupied q_- cases.
Golombness specifies their colors as above, so

    K_seed = sum_(interlaced h) [f(q_-)+f(q_+)]
           <= I <= rho.                            (6)

The first inequality requires actual weak properness. Golomb uniqueness
alone only says that a specified class h-pair has at most one seed:
it does not by itself exclude the two opposite class roles. The
two-completion contradiction (4) is what closes that multiplicity.

## 3. An independent injection into internal-reflection units

For a Golomb class D and a mark s in the other diagonal class, let
mu_D(s) count triples a<m<q in D with

    s=a+q-m.                                         (7)

Such an output is strictly between a and q. Define

    K_ref=sum_(s in C)mu_B(s)+sum_(s in B)mu_C(s).

The internal-reflection unit theorem, recorded in
WEAK_MIXED_CELL_REDUCTION_0041.md, assigns two distinct mixed-cell
units to every such reflection; units from different reflections
cannot coincide in a proper weak coloring. Its complete count gives

    2K_ref <= bc.                                    (8)

Every activated shared pair maps to one of these reflections. If q_+
is present in (1), take

    (a,m,q)=(r+p,r+h+p,r+2h) in B,
    s=r+h in C.

Then (7) holds and m>s. If q_- is present, take

    (a,m,q)=(r+p-h,r,r+h) in C,
    s=r+p in B.

Now (7) holds and m<s.

The map is injective. Given a reflection triple and its output, m=s
would make a,m,q an arithmetic progression, contrary to Golombness.
If m>s, only the first orientation is possible, and its parameters
are recovered by

    h=q-s=m-a,        p=m-s,        r=2s-q.

If m<s, only the second orientation is possible, recovered by

    h=q-m=s-a,        p=s-m,        r=m.

These formulas recover both class roles and all five seed starts.
Therefore

    K_seed <= min(rho,K_ref) <= min(rho,floor(bc/2)). (9)

The condition for the recovered seed still includes its additional
opposite-class mark. An arbitrary internal reflection is not asserted
to have that mark or to be a seed.

## 4. Counting actual holes without a constant-reuse assumption

Translate S so its hull is [0,ell]. Let I_int count those interlaced
shared lengths for which both q_- and q_+ lie in this hull. All four
candidates in (2) then lie in the hull. Put H=ell+1-n.

For a hole x in [0,ell]\S, count its appearances as an outer candidate
and as an interior candidate, retaining the candidate labels.

An outer appearance specifies a same-class pair at distances h,2h
on one side of x. For each diagonal class and each side, these pairs
are edges in the graph t -> 2t on the positive distances from x to
that class. Every component is a path. The unique pair in the other
class, if it exists, is determined by h, so one such arithmetic pair
gives at most one candidate appearance. Since an interior hull hole
has marks on both sides, the four path forests have at least two
nonempty components in total. Hence

    outer multiplicity at x <= n-2.                 (10)

For an interior appearance x=v_+, the identity is

    x+(r+p)=r+(r+h);

for x=v_-, it is

    x+(r+h)=(r+p)+(r+h+p).                           (11)

In each case choose the displayed opposite-class mark a on the left
side of the equality. An unordered same-class pair of sum x+a is
unique by Golombness, so it determines h and its two endpoints.
The other class has at most one h-pair; thus a cannot give a second
appearance by changing from the lower to the upper endpoint role.
Both occurrences in (11) place a strictly between the matched
same-class pair's endpoints. In particular a is neither extreme
mark of S. Charging to a proves

    interior multiplicity at x <= n-2.              (12)

This counts two coincident interior labels correctly: their charges
are to different-class marks. Combining (10)-(12) with (5),

    2 I_int <= sum_(x in [0,ell]\S)
                         [outer multiplicity+interior multiplicity]
              <= (2n-4)H,

and consequently, for n>=2,

    I_int <= (n-2)(ell+1-n).                         (13)

One may retain the first sum instead of the coarse closed form.
Interlaced pairs with an outer candidate outside the hull are not
included in I_int. Neither these boundary positions nor repeated
bare holes are silently counted as distinct interior resources.

## 5. Simultaneous consequence for a proper strict source

Now let A have a proper two-color strict V(A). Use its actual weak
fibers F_d=B_d disjoint union C_d, with r_d=b_d+c_d, and put

    M=binom(|A|,2),       T=sum_d binom(r_d,2),
    s_d=b_d-c_d,         K_A=sum_d K_seed(F_d).

Applying (9) inside every actual weak fiber gives

    K_A <= sum_d rho_d,
    2K_A <= sum_d b_d c_d.                           (14)

Since 4b_dc_d=r_d^2-s_d^2 and sum_d r_d^2=2T+M,

    8K_A + sum_d s_d^2 <= 2T+M.                     (15)

The exact mixed decomposition T(F_d)=2rho_d+N_d+Q_d also yields

    2K_A <= sum_d T(F_d)=K_3(A).                    (16)

Here K_3 counts positive ordered three-generator cubes, as defined in
WEAK_FIBER_CUBE_BALANCE_0041.md. These inequalities retain the actual
fiber colors, not independently chosen Golomb partitions.

They admit exact window localization. Let t>=1 and write A_u for
A intersect[u,u+t-1]. A seed in F_d uses five starts spanning 2h;
including their d-translates gives whole source span d+2h. Hence

    sum_u K_(A_u)=sum_(seeds in A)(t-d-2h)_+.

Summing (15) on the restrictions A_u gives

    8 sum_(seeds)(t-d-2h)_+
       + sum_u sum_d s_(u,d)^2
       <= 2K_2^(t)(A)+K_1^(t)(A),                  (17)

where K_j^(t) are the already defined whole-span cube window counts.
Similarly (16) gives

    2 sum_(seeds)(t-d-2h)_+ <= K_3^(t)(A).           (18)

The variances in (17) use the signed counts in the restricted fibers.
They are not obtained by multiplying the full-fiber s_d^2 by an
arbitrary direction weight.

## 6. Remaining implication

The new constraints pay every activated interlaced pair by both a
unique shared length and a unique internal-reflection event, and every
interlaced pair has a two-position completion deficit. They supersede
using the much larger ambient missing-edge ledger as the only upper
bound for these seeds.

They do not force seeds or interlaced shared pairs to be numerous in
an arbitrary high-energy strict source. In particular, fibers with
rho_d=0 contribute no such events while still contributing to T(A).
Nor does (13) have the constant bare-hole reuse that would make it a
quadratic source-span lower bound. A general finite-span or energy
estimate still needs to control the sources with few activated pairs,
or connect those sources to a different actual-color resource.
S21, the local R3 lower lemmas, and the R4 target remain open;
unconditional small-color bounds do not change here.
