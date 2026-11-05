# The Cartesian three-halves target

**Status update.**  A subsequent finite search recorded a raw (59/36) countercandidate; that stored assignment remains discovery input rather than the proof here.  The separate explicit construction in `PERIODIC_CARTESIAN_DERIVATION_0017.md` now proves that the (3/2) estimate is false, and in fact that no universal constant (c) can bound (U/(|B||C|)) for arbitrary proper Cartesian products.  The identities and collision reduction below remain valid, but their proposed capacity inequality does not.

## 1. Exact forms of the target

Let (N=|B||C|), and for each numerical diagonal (delta) put

\[
D_\delta=\{(b,c)\in B\times C:b-c=\delta\},
\qquad n_\delta=|D_\delta|.
\]

Two Cartesian cells lie on the same numerical diagonal exactly when their two coordinate differences agree.  Consequently

\[
U(B,C)=\sum_\delta {n_\delta\choose2},
\qquad
N+2U(B,C)=\sum_\delta n_\delta^2.
\tag{1}
\]

Thus the proposed estimate

\[
U(B,C)\le \frac32N
\tag{2}
\]

is equivalent to the mixed-energy bound

\[
\sum_\delta n_\delta^2\le4N.
\tag{3}
\]

Equivalently, a cell chosen uniformly from (B\times C) must see average diagonal-fiber size at most (4).  This gives a first unconditional regime: (2) holds whenever every (n_\delta\le4).  More generally, (2) is exactly

\[
\sum_{n_\delta\ge5}n_\delta(n_\delta-4)
\le
\sum_{n_\delta\le3}n_\delta(4-n_\delta).
\tag{4}
\]

Hence only the excess mass of diagonals of size at least five needs a coloring argument; fibers of size four are neutral and fibers of size at most three supply the exact deficit in (4).

Now use the fixed-offset routing from `CARTESIAN_CUT_LEMMA_0016.md`.  Let (S) be the number of monochromatic diagonal pairs.  Route every bichromatic diagonal pair to the endpoint whose color agrees with the corner completion.  For a cell (p), let (lambda(p)) be its total routed load over all offsets, and put

\[
P=|\{p:\lambda(p)>0\}|,
\quad Z=N-P,
\quad E=\sum_p(\lambda(p)-1)_+.
\]

Then

\[
U=S+P+E=S+N-Z+E.
\tag{5}
\]

Therefore the three-halves conjecture is exactly the following routing-capacity inequality:

\[
\boxed{\quad S+E\le \frac N2+Z.\quad}
\tag{6}
\]

This is sharper and more informative than asking separately for bounds on (S) and (E).  A nearly extremal configuration with almost every cell used by the routing ((Z\approx0)) must have (S+E\lesssim N/2).  If many cells are unused, each unused cell contributes one full extra unit of capacity.

## 2. Collision-forest lemma

There is a direct conversion of every unit of cross-offset excess (E) into an incidence with a monochromatic diagonal pair.

Fix a cell (p).  Every diagonal pair routed to (p) is bichromatic, so its other endpoint has color (-z_p).  All these other endpoints lie on the same numerical diagonal as (p).  Denote their set by (O_p); fixed-offset injectivity ensures that the routed edges are distinct, and hence

\[
|O_p|=\lambda(p).
\]

If (lambda(p)\ge2), choose any tree (T_p) on vertex set (O_p).  Each edge of (T_p) joins two same-colored cells on one numerical diagonal, so it is one of the (S) monochromatic diagonal pairs.  Moreover

\[
|E(T_p)|=\lambda(p)-1.
\]

Taking the union as a multiset over all centers (p) gives the exact identity

\[
E=\sum_{e\in\mathcal M}\mu(e),
\tag{7}
\]

where (mathcal M) is the set of monochromatic diagonal pairs and (mu(e)) is the number of chosen center-trees containing (e).  In particular, routing overload cannot occur without monochromatic diagonal structure.

The choice of tree can be made ordered: list (O_p) along its diagonal and join consecutive elements.  Then (mu(e)) counts cells (p) of the opposite color for which the endpoints of (e) are consecutive among the endpoints routed to (p).  This removes artificial long chords from the collision certificate.

Combining (6) and (7), the remaining assertion is

\[
\sum_{e\in\mathcal M}(1+\mu(e))\le \frac N2+Z.
\tag{8}
\]

The left side consists of one unit for the monochromatic pair itself and one unit for every selected routing collision supported on it.  Formula (8) is a concrete color-dependent capacity statement; proving it for a suitable choice of the ordered trees would prove (2).

## 3. Why the present mechanism stops at pair congestion

For a pair of routed edges meeting at (p), let their other endpoints be (a,d).  Both have color (-z_p), so (ad) is the monochromatic diagonal pair supplied by the collision-forest lemma.  If the two routed edges lie on opposite sides of (p), their offsets add; if they lie on the same side, the offset of (ad) is their positive difference.  Both are legal equal-step diagonal pairs, so no unequal-step substitution is used.

A fixed monochromatic pair (ad), however, can be selected in the trees of more than one opposite-colored center (p) on the same diagonal.  The signed-Golomb property only says that another monochromatic pair of the same color cannot repeat the difference (d-a); it does not bound the number of opposite-colored centers incident with this one pair.  Thus it controls distinct pair labels, while (8) needs control of the multiplicity (mu(e)).

Full Cartesian availability does impose completion colors for every such incidence, but the immediate forced cells have unequal legs when two centers use different offsets.  No legal corner follows without a further relation among those offsets.  The precise unresolved step is therefore:

> Choose the ordered trees (T_p), or redistribute their edge units, so that the total weighted monochromatic-pair load in (8) is paid by half a unit per Cartesian cell plus one unit per unused routed cell.

This is narrower than the original (U\le3N/2) statement: fixed-offset collisions have already been eliminated, every remaining collision has been converted into a genuine same-color diagonal pair, and only the congestion of those pair certificates remains.

## 4. Ratio-preserving amplification of any finite Cartesian pattern

There is a simple amplification lemma relevant to counterexample searches.  It shows that any single finite proper example above (3/2) would automatically yield a parametric counterfamily; no new large SAT instances would be needed.

Let ((B_0,C_0,\chi_0)) be any finite proper Cartesian coloring.  Choose finite integer offset sets (R,S) such that

\[
(R-R)\cap(S-S)=\{0\}.
\tag{9}
\]

Choose an integer (W>2(\operatorname{span}R+\operatorname{span}S)), and set

\[
B'=WB_0+R,\qquad C'=WC_0+S.
\]

Every equality of differences in (B') and (C') separates uniquely into equality of the coarse (W)-multiples and equality of the offset differences.  By (9), the latter equality forces the two row offsets to be equal and the two column offsets to be equal.  Therefore every common positive difference is (Wh), where (h) is a common positive difference of (B_0,C_0), and

\[
r_{B'}(Wh)=|R|r_{B_0}(h),\qquad
r_{C'}(Wh)=|S|r_{C_0}(h).
\]

Color by copying the coarse cell,

\[
\chi'(Wb+r,Wc+s)=\chi_0(b,c).
\]

Every corner in the amplified product projects to a corner of the seed, so this is proper.  Furthermore

\[
U(B',C')=|R||S|U(B_0,C_0),
\quad |B'||C'|=|R||S||B_0||C_0|,
\tag{10}
\]

and hence the ratio (U/(|B||C|)) is preserved exactly.

Offset sets of arbitrarily large prescribed sizes satisfying (9) are easy to obtain: take (R=\{0,1,\ldots,r-1\}) and (S=2r\{0,1,\ldots,s-1\}), then enlarge (W) accordingly.  Thus a finite proper seed with ratio (>3/2) would refute (2) parametrically.  Conversely, amplification of a seed below (3/2) approaches no larger ratio; it cannot decide the threshold by itself.

## 5. Scope

The concrete reduction in this note is the exact capacity reformulation (6) together with the collision-forest identity (7): all cross-offset excess is supported on actual monochromatic diagonal pairs.  The later periodic construction shows that the proposed congestion estimate (8), and hence (2), fails in general.  The diagonal-energy form (4) still localizes every violation to excess mass on fibers of size at least five.
