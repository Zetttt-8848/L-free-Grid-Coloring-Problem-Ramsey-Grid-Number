# R3 finite-cap input map (checkpoint 0034)

## Conventions retained by the inherited transfer

The R3 grid parameter \(n=464\) counts **positions**. A diagonal coordinate
class is consequently a set \(A\subseteq\{0,\ldots,463\}\), so its span is
at most \(463\), not 464. The three diagonal colors force one class of size
at least \(\lceil464/3\rceil=155\). That monochromatic grid diagonal supplies
a **strict** two-color source triangle \(V(A)\): its diagonal cells retain
the excluded third color. Each difference fiber \(F_d\) instead supplies a
translated **weak** two-color triangle \(W(F_d)\). These are distinct
premises.

For \(d>0\), the cap files use \(r_A(d)=|\{x:x,x+d\in A\}|\). The labels
“through distance 27” and “first three distances” are statements about
these *translation distances*, not about the rank positions of marks in
\(A\).

## One finite lemma sufficient for the inherited strict improvement

The required new input can be stated cleanly as the following conditional
finite interval lemma.

> **C46/45(463) strict-source capacity lemma.** Every set
> \(A\subseteq\{0,\ldots,463\}\) of size 155 whose strict two-color
> source triangle \(V(A)\) is proper obeys
> \[
> r_A(d)\le46\quad(1\le d\le27),\qquad
> r_A(d)\le45\quad(d=1,2,3).
> \]

An eventual proof may additionally use the translated weak triangles
\(W(F_d)\); it must not replace the strict premise on \(A\) by \(W(A)\).
This is a requested finite lemma, not a claim established by this map.

## Existing transfer and its scope

`research_round3/cap/PREDICTIONS.md`, CAP-P4, records this exact profile as
the finite capacity input: “46-cap through 27 plus 45-caps at distances
1,2,3.” It says that, together with window-13 spacing, the profile excludes
155 marks at \(n=464\). Root located the complete existing mixed-profile
conditional calculation in `research_round3/round3_report.tex`, beginning
at line 403: it uses s=155,c=10, distance lower sum 25110 and endpoint
upper sum 25091. Those recorded quantities establish the conditional
implication, not its cap premise, and were reused without recomputation.
In contrast, `research_round3/cap/conditional_descent.json` uses the stronger
profile `45 through27 and inherited elsewhere, plus window13`; it is not
the mixed-profile citation.

The spacing half of the transfer is `research_round3/cap/endpoint_neighbor.md`.
It uses a set of \(s\) ordered marks of span at most \(L\), lower bounds
on contiguous-block spans \(\ell_i\), and the sum of the \(H\) smallest
distances with their allowed multiplicities. Distinct integer positions give
the base \(\ell_i=i\); the inherited window profile strengthens these
minimum lengths. This is why the final application has position count 464,
span 463, and cardinality 155 as separate quantities.

## What the cap route already uses

* The cap mechanism includes its recorded \(H_j\) position-minimum inputs in
  the \(q(n-d)\) capacity profile, alongside signed-fiber Golomb restrictions.
  This map does not identify or replace the source basis of those \(H_j\)
  minima.
* The endpoint lemma also uses the window-13 spacing profile on \(A\), plus
  valid split lower bounds \(\ell_{i+j}\ge\ell_i+\ell_j\). These are source
  spacing inputs, separate from the fiber caps.
* `research_round3/cap/ap5_uniqueness.md` records a further candidate
  geometric restriction: every \(F_d\) is five-AP-free. It explicitly says
  this does not itself establish the 45-cap. It is therefore an available
  refinement input, not part of the recorded C46/45 transfer.

The old literal two-ruler pair search is not a joint-ruler theorem: its raw
negative solver results were quarantined in `pair_audit_prediction.md`.
Nothing in the conditional transfer may be read as proving a universal
disjoint-pair capacity from that experiment.

## Unpursued simultaneous-color-class refinement

The existing cap reduction aggregates the two signed subclasses into the
single number \(r_A(d)\). A sharper finite lemma could retain, at once, that
the two subclasses of \(F_d\) are disjoint, that each has its own Golomb and
position-minimum constraints, and that both are induced by one common strict
coloring of \(V(A)\), with the weak fiber triangles \(W(F_d)\) as additional
local support. The AP5 fiber condition is another already-recorded possible
joint restriction. No such simultaneous two-class finite inequality is
presently transferred by the cited files.
