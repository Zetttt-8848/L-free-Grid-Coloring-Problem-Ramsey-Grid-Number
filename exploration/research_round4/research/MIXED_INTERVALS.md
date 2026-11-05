# Ordered mixed-interval obstruction

Base R4-RESEARCH-0002. Root original-research derivation. This is a universal necessary condition, not yet a new global upper bound. No priority claim is made before comparison with the literature.

Write W(S)={(v,u):u,v in S, u<=v}. Suppose W(S) has a corner-free two-coloring. Let B and C partition S according to the two diagonal colors, named blue and green.

## Six-mark forcing theorem

For every h>0 there cannot be p<u<q with

p,p+h,u+h in C, and u,q,q+h in B.                    (1)

The statement with B and C exchanged also holds. Distinctness of all six marks is not an extra hypothesis: if coinciding marks demand opposite diagonal colors then (1) is already impossible; the argument covers every remaining overlap.

Proof. Put v=u+h. The cell E=(v,u) exists because u,v belong to S and h>0. Diagonal green pairs force both (p+h,p) and (v,p) blue. Their coordinates exist in W(S), and v>p+h because u>p. They are the first and middle vertices of the positive corner

{(p+h,p), (v,p), (v,u)}

of step u-p. Hence E must be green.

On the other hand, diagonal blue pairs force both (q+h,u) and (q+h,q) green. They lie in W(S), since u<q<q+h. They are the middle and third vertices of

{(v,u), (q+h,u), (q+h,q)}

of step q-u>0. Hence E must be blue, a contradiction. Exchanging the two colors proves the other assertion.

The proof uses only four diagonal-pair completions and two further corners. It eliminates the unknown off-diagonal colors and leaves a restriction entirely on the colored diagonal.

## Difference-profile form

For h>0 define B_h={b:b,b+h in B}, C_h={c:c,c+h in C}, and X_h={u:u in B,u+h in C}. Then

sum_(p in C_h) sum_(q in B_h) #{u in X_h:p<u<q}=0.       (2)

The analogous expression with B,C exchanged is zero as well. Every summand is nonnegative; a positive summand gives precisely (1). Thus the identity is equivalent to the forbidden family.

Both B and C are Golomb sets, as follows from the usual two-color completion argument. Therefore B_h and C_h each have at most one point. When both are nonempty and their starts satisfy p_C<p_B, (2) states

X_h intersect (p_C,p_B)=empty.                           (3)

This retains the order of the unique monochromatic intervals of a shared difference. Separate Golomb cardinality caps do not retain the intervening mixed-color intervals.

## Relation to source fibers in a three-color grid

If A is one monochromatic diagonal class and F_d=A intersect (A-d), the cells {(v+d,u):u,v in F_d,u<=v} form a translate of W(F_d). Every such cell lies in T(A), because u and v+d belong to A and v+d>u. Hence they use only the other two colors and are corner-free. Their diagonal colors are exactly the signed fiber partition F_d^+,F_d^-.

The theorem therefore applies with S=F_d and B=F_d^+, C=F_d^- at every d>0. It is a condition on the two-ruler splitting of each actual source fiber, not a condition on arbitrary independent ruler pairs.

## First discriminator

The script mixed_interval_probe.py examines the two literal rulers from the previous research, their disjoint reflected/unreflected translations within the stated span, and reports one six-mark obstruction whenever it finds one. Its role is to determine whether this short analytic rule detects the near-threshold configurations previously requiring longer forcing chains. It does not enumerate all rulers or prove a universal numerical cap. A found instance is explained by the theorem above; failure to find an instance does not establish a triangle coloring.

The completed probe found an instance in every one of the 60 specified pairs (four unreflected order-23 pairs, 38 reflected order-23 pairs, and 18 reflected order-24 pairs). For example, the reflected order-24 pair at shift 2 has p=24,u=122,q=384,h=19: the three green marks are 24,43,141 and the three blue marks are 122,384,403. The theorem forces the cell (141,122) to both colors. This gives a short analytic explanation for that formerly longer forced-color refutation. The finite coverage is a property of these literal inputs only.

## A useful specialization for translated copies

Let C=B+t, t>0, with B and C disjoint. If B contains four ordered marks b<a<c<e satisfying

t=(a-b)+(e-c),

then its prescribed blue/green coloring cannot extend to W(B union C).

Proof. Put h=c-a and p=a. The green interval of length h starts at q=a+t. The green point u=b+t lies strictly between p and q: u-a=e-c>0 and q-u=a-b>0. Moreover u+h=e is blue. Thus the color-reversed six-mark obstruction has a blue interval first, a green-to-blue mixed interval in the middle, and a green interval last. All steps are positive because the four marks are strictly ordered.

This criterion uses the sum of two separated end gaps, not just a repeated difference. It can rule out a disjoint translation even though each copy individually remains Golomb.

## This rule is not a complete characterization

The next bounded discriminator found the following smaller literal pair:

B={0,8,11,13,17}, C={3,9,19}.

Its positive difference sets are

Delta(B)={2,3,4,5,6,8,9,11,13,17},
Delta(C)={6,10,16}.

All differences in each list occur once, so both sets are Golomb. Their only common positive difference is 6. Its green interval begins at 3 and its blue interval begins at 11. The only blue mark strictly between those starts is 8, and 8+6=14 is not green. Thus neither orientation of the six-mark rule occurs.

Nevertheless this prescribed diagonal coloring does not extend to W(B union C). A complete short proof is the special case s=8,t=3,r=6 of BRANCHED_FORCING.md. Thus Golomb splitting plus the entire six-mark family is still insufficient. The failure was discovered by a bounded candidate experiment and is established by the explicit difference lists and the pencil-and-paper forcing argument, not by a solver verdict.
