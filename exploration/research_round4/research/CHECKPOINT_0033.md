# Research checkpoint R4-RESEARCH-0033

Continuation of CHECKPOINT_0030.md, integrating the new work numbered
0031-0033. The goal remains active and incomplete. The working bounds
remain 21<=R3<=465 and R4<=21991300. S21, D(7/5), H10, and the requested
original superior method remain open. The general literature growth
bound is complete and unchanged. No unconditional small-color
improvement is asserted here.

The user requests invention and full derivations, with no separate
audits, repeated checking, review agents, or verification reports, and
no results summary until all objectives are met. All auxiliary tasks
and bounded executions below are terminal. No reset credit was used.

## 1. Main direction retained

Checkpoint 0030 proved that separate unlabeled overlap restrictions,
even every entire nonzero F_d Golomb, do not imply an absolute total
or single-band energy coefficient. Its balanced construction has no
proper source coloring. The new work therefore retains the colors of
physical cells shared by distinct completion blocks.

The positive full-product and dense-partial-product theorems from
0027-0028 remain available. They do not cover arbitrary sources.
The completed S21 and D(7/5) transfer calculations should be reused,
not recomputed. The next step is still a uniform source inequality.

## 2. Root: reflected triples compete with ordinary completions

REFLECTION_COMPLETION_COMPATIBILITY_0033.md derives a longer forcing
rule and its exact counting scope. If a<b<c are in the same signed
fiber F_d^s, put w=a+c-b. Their three pair outputs have color -s.
Whenever w is in A, a three-corner path forces

    z(c+d,w)=s.

Whenever w+d is in A, the row-mirror path forces

    z(w+d,a)=s.

Both target offsets exceed d. Each orientation needs only two seed
pair completions followed by one reflected corner. No unsupported
reflection is used.

Let H=sum_(d,s) binom(|F_d^s|,2), B=T-H. If w belongs to F_d, it has
the opposite signed-fiber color, by Golombness of F_d^s. The column
orientation maps the seed injectively to the bichromatic pair (w,c)
in F_d: the pair difference specifies the unique seed pair (a,b) of
that gap and sign. The row orientation similarly injects into (a,w).
Thus the number K of internally supported seed triples satisfies

    K<=B.

The two orientations have safe combined count 2K<=2B; disjointness
between their images is not assumed. If O counts supported reflections
with exactly one of w,w+d present, the complete transport count is

    J=2K+O<=2B+O.

An unlabeled separate-fiber bound gives only

    O<=2sum_d r_d(|A|-r_d)=2[(|A|-1)M-2T],

which is too large to close a linear energy inequality. When every
entire F_d is Golomb, K=0 and every supported reflection is open.

At a physical target q, H_q^s counts ordinary equally colored pair
endpoints of sign s and J_q^s counts reflected triples of sign s.
They force opposite and equal target colors, respectively. Therefore

    H_q^+H_q^-=J_q^+J_q^-=H_q^s J_q^s=0.

Writing h_q=H_q^+-H_q^-, j_q=J_q^+-J_q^-, and using unsigned totals,

    h_q=-z(q)H_q, j_q=z(q)J_q,
    h_q j_q=-H_qJ_q, |j_q-h_q|=H_q+J_q.

These are exact shared-color constraints, not a proved bound on H or T.
The new quantitative gap is to amortize O at its actual targets or to
force incompatible occupancy using these identities. An upper bound
on J cannot be inverted into an upper bound on T.

## 3. Root and auxiliary: rigid reconstruction within every fiber

fibers/FIBER_COLOR_RIGIDITY_0033.md proves an elementary sharp lemma.
Fix all pair-output colors for r input vertices. Form a graph whose
edges are the output-1 pairs. Valid input assignments are exactly its
partitions into a clique of input color 0 and an independent set of
input color 1. Any two valid assignments differ on at most one old-0
and at most one old-1 vertex. A set-family argument gives at most r+1
valid assignments, with equality for constant pair-output colors.
The empty, singleton, and two-input cases are included.

COMPLETION_PROFILE_RIGIDITY_0033.md applies this to actual offset
fibers. Their pair outputs have strictly greater offsets, so descending
processing gives the complete counting corollary

    N(A)<=product_(d=1)^L (r_d+1)<=(1+M/L)^L  (L>0),

where N(A) counts proper source colorings. The empty product handles
L=0. Induced output patterns 2K2, its complement C4, and C5 are explicit
local obstructions. These restrictions still apply when an entire F_d
is Golomb and its own strict triangle has no corners.

No lower bound on N(A) contradicting this product has been derived.
Independent local recoloring is invalid because inputs also act as
outputs for smaller offsets. The rigidity result provides a linked
constraint formulation, not nonexistence or canonicalization.

## 4. Auxiliary: ordered output injectivity does not ensure colorability

fibers/ORDERED_GROUP_HYPERGRAPH_0031.md settles a bounded abstract
question negatively. Every pair inside a group has exactly one output
in a higher group; at most one pair in a fixed lower group outputs
into any fixed higher group. Outputs can be shared across lower groups.

The explicit three-layer construction has nine top singleton groups.
For every five-subset of them, five intermediate triples send their
pair outputs to three distinct top groups in that subset. For every
transversal of the five triples, a bottom five-vertex group sends its
cycle pairs to the five top vertices and its complementary-cycle
pairs to the selected intermediate vertices, all in distinct groups.

Any top coloring has a monochromatic five-subset of color c. Each
associated intermediate triple supplies a vertex of color 1-c. The
bottom group for that transversal has C5 output labels of color c and
the complementary C5 labels of color 1-c. Each input color then has
at most two vertices, impossible on five vertices. This is a complete
abstract obstruction with no asserted integer realization.

It prevents using ordered output injectivity as a general greedy
coloring theorem. It does not refute a size inequality for actual
proper integer sources.

## 5. Auxiliary: actual reflected path and the remaining forcing gap

fibers/CROSS_BLOCK_COLOR_CONFLICT_0031.md gives a ten-edge abstract
NAE obstruction: six Fano lines with one signal line deleted force
three signals equal, three further pair outputs force three new cells
opposite, and their final triple is monochromatic. A direct four-corner
shell sharing one bridge between endpoint offsets d<f forces e=2f-d,
placing a three-term progression in F_d. Thus that particular shell
cannot be realized in a cube-free source. No shortest-gadget claim is
made.

fibers/CUBE_FREE_SOURCE_FORCING_0032.md derives the one-sided reflection
rule in a source with every F_d Golomb. For the reduced source in the
next section it uses d=76, starts 0,15,20, and reflected mark 5. A
monochromatic seed triple

    (76,0), (91,15), (96,20)

of color c forces Z=(96,5) to color c. The absent mirror mark is 81.
The same target Z is an ordinary completion for the endpoint pairs

    (19,5), (96,82);
    (32,5), (96,69);
    (69,5), (96,32);
    (82,5), (96,19).

Any one of these pairs being monochromatic c gives a contradiction.
The exact remaining gap is to force the seed triple monochromatic and
one listed pair to the same color. The displayed local corners alone
do neither. This is not a paper proof of the raw negative source.

## 6. New finite lead, with bounded computational status retained

fibers/CUBE_FREE_COLOR_DISCOVERY_0031.py/json generated new random-greedy
sources with every nonzero overlap Golomb and supplied each candidate
one full-corner call capped at two seconds. The stated maximum was
80 sources; execution stopped after the third source produced a raw
UNSAT lead. The earlier 12- and 17-mark sources gave raw SAT outputs
with their literals retained. No independent checking pass was run.

The third source had 27 marks, span 124, 605 directed corners and 350
used cell variables. Its raw UNSAT call terminated in about 0.155 s.

fibers/CUBE_FREE_OBSTRUCTION_REDUCTION_0032.py/json then explored only
new proper subsets, without rerunning the parent. Each candidate was
distinct and received at most one capped full-corner call. The run
stopped at its cap of 50 calls. Removing 118 was the sole retained
raw-UNSAT deletion, leaving

    {0,4,5,15,19,20,24,29,32,37,44,48,58,59,62,65,
     66,67,69,76,82,91,92,96,114,124}.

The saved result reports 556 complete corner constraints, 324 used
cell variables, and a raw UNSAT time about 0.181 s. Used-variable
counts refer to cells occurring in corners, not every cell of V(A).
The JSON retains every candidate/status and the final used cell and
corner lists. The call cap does not establish deletion minimality.

No solver status here is a paper noncolorability proof, a universal
source inequality, or a Ramsey certificate. Do not rerun these terminal
calls as checks. A further computation must investigate a genuinely
new bounded question and preserve its distinction from a derivation.

## 7. Existing offset-path obstacle and next root work

fibers/OFFSET_PATH_DEPENDENCY_MAP_0032.md maps the existing cloud, fan,
and band notes without redoing them. Decreasing offsets do not bound
fan-in: same-sign predecessor anchors give only a square-root bound,
and supported closure charges have safe multiplicity 2r_A(delta).
When both boundary translates are missing, there need not be a forced
lower-scale corner at all. The new reflection rule above addresses
some configurations through other actual cells, but has its own
explicit open term O.

A tentative finite-span logarithmic energy inequality was considered
as an alternative to a universal constant-energy claim; no derivation
was obtained. The inspected notes do not refute T<=(log_2 L)M/2, but
their one-charge-per-cell-per-scale argument does not prove it. The
existing five-mark calibration refutes the stronger raw per-band
coefficient one half. This remains only an optional idea, not a new
premise or the current sufficient target.

The next root attack should combine actual split-profile obstructions
with reflected/ordinary target incompatibility to force a quantitative
finite-span exclusion. In parallel, a bounded symbolic continuation
of the 26-mark lead may reveal an actual geometric obstruction, but
that lead remains auxiliary to the uniform S21/R4 task. Do not replace
the full objective with abstract gadget classification or another
separate-overlap energy estimate. All three child agents are now
terminal and may be reactivated with bounded independent tasks.
