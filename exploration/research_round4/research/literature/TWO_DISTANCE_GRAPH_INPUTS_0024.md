# Spherical two-distance graphs at squared-distance ratio two

## Exact spherical encoding

Let \(v_1,\ldots,v_N\) lie on a common sphere of radius \(r\), with squared
distances \(a\) and \(2a\).  After dividing by \(r\), their off-diagonal inner
products are

\[
\alpha=1-\frac{a}{2r^2},\qquad \beta=1-\frac{a}{r^2},\qquad \beta<\alpha.
\]

Take \(G\) to have an edge at the \(\beta\) inner product, equivalently at
squared distance \(2a\).  Then
\((1-\alpha)/(\alpha-\beta)=1\).

**Z. Jiang, J. Tidor, Y. Yao, S. Zhang and Y. Zhao, [*Spherical Two-Distance
Sets and Eigenvalues of Signed Graphs*](https://arxiv.org/abs/2006.06633),
Lemma 2.1.**  For \(-1\le\beta<\alpha<1\), a spherical
\(\{\alpha,\beta\}\)-code of size \(N\) in \(\mathbb R^d\) exists if and only
if there is a graph \(G\) with

\[
\lambda I-A_G+\mu J\succeq0,
\qquad \operatorname{rank}(\lambda I-A_G+\mu J)\le d,
\]

where \(\lambda=(1-\alpha)/(\alpha-\beta)\) and
\(\mu=\alpha/(\alpha-\beta)\).  Thus the ratio-two case gives

\[
I-A_G+\mu J\succeq0. \tag{1}
\]

This needs a common sphere and the two global distances; arbitrary centered
PSD data or a partial distance graph does not meet the lemma's hypotheses.

## What (1) does, and does not, imply

For \(x\perp\mathbf1\), (1) gives \(x^TA_Gx\le\lVert x\rVert^2\).  With
\(\bar A=J-I-A_G\), it follows that

\[
x^T\bar A x\ge-2\lVert x\rVert^2\qquad(x\perp\mathbf1). \tag{2}
\]

This bounds only the compression to \(\mathbf1^\perp\), not automatically
\(\lambda_{\min}(\bar A)\ge-2\): for an irregular graph,
\(\mathbf1^\perp\) need not be an invariant eigenspace.

If the realization is additionally centered at the origin
(\(\sum_i v_i=0\)), its Gram matrix annihilates \(\mathbf1\).  In the
ratio-two formula this forces \(A_G\mathbf1=(1+\mu N)\mathbf1\), so \(G\)
is regular.  Only with this centering/regularity input does (2) become the
usual least-eigenvalue statement for the nontrivial spectrum of \(\bar A\).
A common sphere alone does not imply this centering condition.

## Least-eigenvalue \(-2\) classification: conditional graph input

The classical Cameron--Goethals--Seidel--Shult classification is summarized
in this [two-distance graph overview](https://zilin.one/slides/forbidden_subgraphs_and_spherical_two_distance_sets/index.html): connected graphs with smallest adjacency eigenvalue at least \(-2\) are generalized line graphs together with a finite exceptional family.  Root systems enter through the positive-semidefinite matrix \(A+2I\).

**Scope limitation.**  The classification applies after proving the full
adjacency condition \(\lambda_{\min}(A)\ge-2\).  The ratio-two spherical
encoding directly gives only (1), hence the projected complement inequality
(2).  Applying the classification to the complement requires the extra
centering/regularity argument above, or another full least-eigenvalue proof.

## Further spherical graph characterizations

**I. Noman and Y. Yao, [*Spectral conditions for spherical two-distance
sets*](https://arxiv.org/abs/2211.12582).**  This work characterizes spherical
two-distance representations using both the adjacency spectrum and the
spectrum projected to \(\mathbf1^\perp\), and determines the least ambient
dimension.  It confirms that projected spectral data are essential in the
nonregular case and should not be replaced silently by a full least-eigenvalue
assertion.

## Bounded use

For an atom-incidence model that genuinely produces a common-sphere,
ratio-two set, Lemma 2.1 is the exact Gram/graph conversion.  If it also
supplies centroid zero, generalized-line-graph/root-system machinery may be
relevant to the complement graph.  Nothing here embeds general proper sources
or partial additive-parallelogram systems into that model.
