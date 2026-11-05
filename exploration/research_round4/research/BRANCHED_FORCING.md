# A branched forcing family beyond the mixed-interval rule

Base R4-RESEARCH-0002. Root derivation from the first survivor of the mixed-interval discriminator. This is an auxiliary forbidden family, not yet a global Ramsey improvement.

Let W(S)={(v,u):u,v in S,u<=v} have a corner-free two-coloring. Denote the two diagonal color classes by B (blue) and C (green).

## Theorem

Let x,s,t,r be integers with s,t>0 and 0<r<s. The following memberships cannot all hold:

x+{0,s,s+t,s+t+r} subset B,
x+{t,t+r,2s+t} subset C,
x+2s+t-r in S.                                        (1)

The last mark need not have a specified diagonal color. If a choice of parameters identifies marks prescribed different colors, the antecedent is already impossible. No other distinctness assumptions are required. The color-reversed family is also forbidden.

## Proof

Translate x to zero; common translation preserves all corners. Write

b=s, c=s+t, f=t, g=t+r, e=s+t+r, h=2s+t, i=2s+t-r.

The inequalities give 0<b<c<e<h, 0<f<g<c, and c<i<h. The relative order of e and i is immaterial.

1. The blue diagonal pairs {0,b} and {0,c} force the cells (b,0) and (c,0) green. The corner {(b,0),(c,0),(c,f)} has step c-b=t>0. Hence (c,f) is blue.

2. The green diagonal pairs {f,g} and {f,h} force (g,f) and (h,f) blue. Their corner, of step h-g, forces (h,i) green, because f+h-g=i. All three cells belong to W(S), including (h,i) by the last membership in (1).

3. The blue cells (c,f) and (h,f) form a corner of step h-c=s>0 whose third cell is (h,c), since f+h-c=c. Thus (h,c) is green.

4. The blue diagonal pair {c,e} forces (e,c) green. The three green cells

{(e,c),(h,c),(h,i)}

form a corner, since h-e=s-r>0 and i-c=s-r. This contradiction proves the theorem. Exchanging blue and green proves the reversed statement.

Every forced cell has its row and column among the prescribed marks; no missing grid cell is silently filled in. The inequalities above ensure the correct order and strictly positive steps at each stage.

## Concrete consequence and separation of necessary systems

For x=0,s=8,t=3,r=6, the required sets are

B0={0,8,11,17}, C={3,9,19}, and the extra mark i=13.

Taking the extra mark blue gives B={0,8,11,13,17}. The proof forces the following seven cells in order:

(8,0) green; (11,0) green; (11,3) blue;
(9,3) blue; (19,3) blue; (19,13) green; (19,11) green.

The blue diagonal pair {11,17} also forces (17,11) green, yielding the corner {(17,11),(19,11),(19,13)} of step 2.

MIXED_INTERVALS.md shows by complete difference lists that these B,C are Golomb and satisfy every instance of the six-mark family. Therefore the present family adds information that is not implied by those earlier necessary conditions. It is not merely a different inequality for the same six-mark pattern.

## Application and unresolved quantitative step

For a monochromatic diagonal class A in a three-color grid, each translated weak triangle on F_d=A intersect (A-d) is two-colored. The theorem applies to its actual signed diagonal partition exactly as explained in MIXED_INTERVALS.md. Thus this is a uniform three-parameter family of additional necessary fiber constraints.

It remains to show that these constraints, or a general principle accounting for their repeated use, force a sufficiently small fiber size. No such size bound is claimed here. Adding finitely many local patterns alone is not a proof that all large fibers are impossible.
