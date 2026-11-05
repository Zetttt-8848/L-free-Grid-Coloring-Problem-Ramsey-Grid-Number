# A reflected-middle hole rule from a binary implication chain

Root derivation, continuation0042. This is a further necessary condition
on a proper weak source. It uses one internal reflection together with
one reflected middle mark. Unlike the common-output shadow rule, it
does not require two reflection triples at the selected output.

Let S=B disjoint union C have a proper two-coloring of W(S), with B,C
the prescribed diagonal classes. They are Golomb. Name the two colors
B,C. All strict B-B cells have color C and all strict C-C cells color B.

## 1. The upper-middle rule

Suppose

    a<p<q are in B,   r=a+q-p is in C,   r<p,
    y=2r-p is in B.

Then

    x=2r-q is absent from S.                         (1)

Here r lies strictly between a and q. The extra condition r<p says
that both p and q are above the selected output r. Its reflected
points satisfy x<y<r and x<a<r. Also

    y-x=q-p=r-a>0,   y=x+r-a.                       (2)

First x cannot belong to B. Otherwise the B-pairs (x,y) and (p,q)
would represent the same positive difference q-p. They are distinct
because x<a<p, contrary to Golombness.

Suppose instead that x belongs to C. The reflection triple forces

    z(r,a)=B,   z(q,r)=B.                            (3)

For completeness, the first force uses the positive corner
(r,a),(q,a),(q,p), whose last two cells are B-B of color C. Its
step is q-r=p-a. The second uses (p,a),(q,a),(q,r), whose first
two cells are B-B of color C, with step q-p=r-a.

Since x,r belong to C, z(r,x)=B. The corner

    (y,x), (r,x), (r,a)

has positive step r-y=p-r=a-x, so (3) forces z(y,x)=C.
The corner

    (r,x), (q,x), (q,r)

has positive step q-r=r-x, so it forces z(q,x)=C. Finally,

    (y,x), (q,x), (q,p)

is a positive corner: its step is q-y>0 and

    x+q-y=p.

All three cells have color C, the last because p,q are in B. This
contradiction excludes x from C too, proving (1). The proof retains
the original positive orientation in every corner.

## 2. The reflected lower-middle rule

There is an order-reversed counterpart. If

    a<p<q are in B,   r=a+q-p is in C,   p<r,
    2r-p is in B,

then

    2r-a is absent from S.                          (4)

To derive it from Section1, replace every mark t by -t and every
cell (v,u) by (-u,-v). A corner
(v,u),(v+d,u),(v+d,u+d) is carried, after reversing its three
displayed positions, to a corner of the same positive step d.
The reversed triple is -q<-p<-a and its reflected output is -r.
Now -r<-p. Formula (1) gives the missing mark -2r+a, which returns
to 2r-a in the original coordinates. This is an explicit direction-
preserving transfer, not a negative-step substitution.

Thus reflecting the middle mark of an internal reflection across its
opposite-color output back into B forces the reflected extreme on
that same side to be a hole.

## 3. A local and global charge

Let kappa_B(r) count the reflection triples in Sections1 and2 for
which 2r-p belongs to B. Then

    0<=kappa_B(r)<=2.                               (5)

Indeed, p and 2r-p are two distinct B marks, since r is not in B.
The unordered pair with sum 2r is unique by Golombness. There are
therefore at most two possible middle marks p. For a fixed middle
p, the extremes obey a+q=r+p, so their unordered B-pair is also
unique. Hence at most one reflection triple occurs for each p.

If there are two such triples, one middle is below r and the other
above r. Their holes in (1) and (4) lie on opposite sides of r, so
they are distinct. Consequently the kappa_B(r) holes are distinct
at each output. Define kappa_C analogously.

For S contained in [0,L], some of these new holes can lie outside
[0,L]. They must not be charged to the finite interior hole budget.
Let kappa_B^in(r) count just the generated holes in [0,L], and put

    J_in=sum_(r in C) kappa_B^in(r)
         +sum_(r in B) kappa_C^in(r).

With n=|S| and H=L+1-n, the output-hole pairs give

    J_in<=nH,   J_in<=2n.                           (6)

The first bound uses uniqueness at a fixed output; the second uses
(5). No bounded multiplicity of the bare hole is assumed. A local
interval version counts only the output-hole pairs lying in the
chosen interval. We do not add these charges to the old shadow
charges without first accounting for possible coincidences.

## 4. The six-mark family and the remaining capacity question

The auxiliary TWO_POINT_TRANSVERSAL_GEOMETRY_0042.md derives the
uniform binary obstruction

    C={0,d},  B={p,d-p,d+p,2d},
    0<p<d/2,   p not equal to d/4 or d/3.            (7)

The six B-differences are d-2p,d,2d-p,2p,d+p,d-p; under the displayed
conditions they are distinct, so B is Golomb. For example d=7,p=2
gives B={2,5,9,14}, C={0,7}.

Section1 applies with the reflection triple (p,d+p,2d), output d,
and reflected middle d-p in B. It demands that 0 be absent, in
contradiction with C. The two-point derivation also identifies why
the binary obstruction is longer than a matching clause having both
endpoints directly forced B: two separate matching clauses transmit
the one reflection event to an all-C corner.

At the same time, the Golomb pair-sum argument reduces the complete
two-point matching to at most three edges. Although a distinct
interior pair supplies two edges, both exterior marks have the same
sum as that interior pair and therefore cannot occur together with
it. Thus the abstract four-edge crossed-path obstruction has no
integer realization in this two-point geometry.

These are new arithmetic restrictions on simultaneous weak colors.
They do not yet give a large enough count of interior holes or a
uniform source-size inequality. In particular (6) alone proves no
new R3 or R4 upper bound. The next needed step is a finite-span
lower bound for the relevant reflected-middle incidences, or a way
to combine their actual binary implications with the other shared
fiber constraints without charging the same hole repeatedly.
