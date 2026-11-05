# Strict equal-gap source condition: bounded extremal-source search

## Exact source condition

For \(A\subset\mathbb Z\), color each ordered edge \((v,u)\), \(u<v\),
in two colors. The forbidden triple is
\[
(b,a),\quad(d,a),\quad(d,c)
\]
when \(a<c\), \(b<d\), and \(b-a=d-c>0\). The three edges form a
three-edge path on the four source vertices, but only those copies whose
two outer edges have the stated equal integer gap are constrained.

The existing edge-source notes `EDGE_COLORED_SOURCE_INPUTS_0016.md` and
`SOURCE_ENERGY_INPUTS_0019.md` were read first. This search did not repeat
their locally-additive, grid-rectangle, vertex-Sidon, anti-Ramsey-Sidon, or
general-corners inputs.

## Closest exact edge-color framework: ordered Ramsey, but it omits arithmetic support

**David Conlon, Jacob Fox and Choongbum Lee, [*Ordered Ramsey
Numbers*](https://people.math.ethz.ch/~sudakovb/ordered-ramsey.pdf), Journal
of Combinatorial Theory B 122 (2017), 353--383.** The paper defines
\(r_{<}(H)\) as the least \(N\) such that every red/blue coloring of all
edges of the ordered complete graph on \([N]\) contains a monochromatic,
order-preserving copy of a fixed ordered graph \(H\) (pages 1--2). It
records the exact monotone-path value
\[
r_{<}(P_n;2)=(n-1)^2+1.
\]

This is a genuine quantitative, two-edge-color theorem on complete ordered
graphs, and its quadratic scale superficially resembles the desired
\(|A|=O(\sqrt{\operatorname{span} A})\) outcome.

**Exact mismatch.** A monochromatic ordered \(P_4\) is forbidden by the
ordered-Ramsey problem for every order-preserving four-vertex placement. The
strict source condition forbids only placements satisfying
\(b-a=d-c\). The theorem's host is the full rank order \([N]\), whereas
the source has an arbitrary integer subset and the equality depends on its
actual numerical gaps. There is no implication from avoiding the sparse
equal-gap family to avoiding all ordered \(P_4\)'s, so the exact path value
does not transfer.

There is a further ordering distinction: the monotone path in the quoted
formula does not have the source path order \(b-a-d-c\). Also, when
\(b=c\), the source corner uses three source vertices and is an arithmetic-
progression instance, not a four-vertex path. These differences reinforce
the lack of a direct theorem transfer.

## Search scope and outcome

Three query batches were used: (1) edge-colored additive quadruples/equal
sums; (2) Ramsey-Sidon and additive edge colorings; and (3) ordered-edge
Ramsey with arithmetic progressions/equal-sum paths. One primary source was
read in full-source form. The remaining returns were either ordinary ordered
Ramsey results for fixed graphs, vertex-colored Sidon results, or generic
edge-color Ramsey results; none had both edge variables and the same-gap
arithmetic support.

Within that scope, no published extremal theorem was found that bounds
\(|A|\) by \(O(\sqrt{\operatorname{span}A})\) or
\(O(\sqrt{\operatorname{span}A\log\operatorname{span}A})\) for this exact
strict source condition, and no exact translation to a known ordered
equal-sum path theorem was located. This is a scoped gap, not a novelty
claim or a proof that no such theorem exists.
