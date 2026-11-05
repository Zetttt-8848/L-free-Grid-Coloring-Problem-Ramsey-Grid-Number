# CAP1 — uniqueness of five-term progressions at each step

Author: root, GPT-6 Astra ultra, Level3. BaseR3-CP0.
Status: UNVERIFIED candidate with complete proof; final independent reviews pending.
This is new geometric input beyond the inherited six-AP exclusion.

## Statement

Let A be the coordinate set of a monochromatic slope-one diagonal class
in a corner-free three-color square. For every integer a>=1, there is
at mostone x for which {x,x+a,x+2a,x+3a,x+4a} is contained inA.
Equivalently, for every d>=1, F_d={u:u,u+d inA} contains no five-termAP.

## Proof

Suppose two distinct starts x andx+d, d>0, yield five-term progressions
of stepa inA. All15 points

 Q_ij=(x+j*a+d+sigma, x+i*a), 0<=i<=j<=4,

lie in the original square; sigma is the source diagonal offset.
Their row coordinates come from the second source progression, and their
column coordinates from the first. For each i<=j, the corresponding two
source diagonal points have coordinate difference d+(j-i)a>0. Therefore
Q_ij lies in the completing triangle T(A) and avoids A's color.

The map (j,i) -> (x+j*a+d+sigma,x+i*a) is a common positive scaling by a
followed by a translation. Thus the Q_ij form an affine copy of the weak
triangle W5={(j,i):0<=i<=j<=4}. Translating W5 by(1,0) gives exactly
T6={(r,s):0<=s<r<=5}. Translation preserves every corner and its positive
step, so the inherited two-color obstruction onT6 also holds onW5.
AllQ_ij use at mosttwo colors, contradiction.

The equivalent fiber statement follows in both directions: a five-termAP
in F_d supplies the two source progressions; two distinct source starts
can be ordered to give positive d and hence such a fiberAP.

## Exact linear encoding

For each admissible five-termAP P_(x,a), introduce a binaryy_(x,a) and impose

 sum_(i=0)^4 x_(x+i*a) <=4+y_(x,a),
 sum_x y_(x,a) <=1 for everyfixeda.

If an AP is fullyoccupied its y is forcedto1, so these inequalities imply
the stated multiplicity restriction. Conversely assigny=1 exactly to fully
occupiedAPs: every feasible set satisfies allinequalities. Thus this is
an exact existential encoding, despite not imposing an unnecessary reverse
implication on every auxiliaryvariable.

At n464 the number of AP5 occurrences is
sum_(a=1)^115(464-4a)=26680, with115 at-most-one groups.

## Immediate three-step audit

Definitions: x,d,a are integers; d,a>0; the two starts are distinct; every
row andcolumn is between source endpoints. The positive completionstep is
d+(j-i)a, includingd wheni=j. The affine common scaling is a in both
coordinates, not unrelated horizontal/vertical scales.

Boundaries: k3 is essential because T(A) has at mosttwo colors; no claim
is made for fourcolors. k1,2 cannot be counterexamples when considered as
three-color colorings. For n<6 the premise of two distinctAP5 is impossible.
At n6,a=d1 it reduces to the inherited monochromaticAP6 obstruction. A
single AP5 is allowed. A fiber with fewer thanfive points is outside the
forbidden antecedent; no extra positions are fabricated. A monochromatic
grid alreadyviolates cornerfreeness.

Counterexample audit: the literal weaktriangle is a translated copy of
the fullycertified inheritedT6, so its20 corners and all2^15 assignments
are covered by that proof. Separate finite scripts below reconstruct the
map and its cornerlist. The original155-set is tested directly for the
new condition; any violations demonstrate the condition is not implied
by the earlier one-class necessary system, not a counterexample to this
grid-dependent lemma.

Dependency graph: source monochromaticity + gridcornerfreeness -> colors
excluded onQ; exact affine identification + inheritedT6 -> contradiction.
No general-k result, numerical optimization, or negative solver run enters.
Confidence in this derivation: high; current publicationstatus remains
UNVERIFIED pending the mandated external-to-author subagentreviews.

The lemma does not by itself prove r_A(d)<=45. It supplies a stronger
fiberrestriction whose global quantitative impact requires a separate proof
or certificate.
