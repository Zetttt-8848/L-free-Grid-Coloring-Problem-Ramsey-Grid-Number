# Structure of all targets reusing one transported pair

Let \(A\subseteq[0,L]\cap\mathbb Z\) carry one proper strict
two-coloring \(z\).  Fix

\[
a<a'=a+\delta,\qquad x>0,\qquad c\in\{+1,-1\},
\tag{1}
\]

and suppose \(a,a'\) occurred together in an incoming set
\(U_{(b,x,h)}\).  In particular,

\[
a,a+x,a',a'+x\in A,\qquad
z(a+x,a)=z(a'+x,a')=c.
\tag{2}
\]

The positive corner

\[
(a+x,a),\quad(a'+x,a),\quad(a'+x,a')
\]

therefore forces

\[
z(a'+x,a)=-c.
\tag{3}
\]

Thus the fixed pair produces the earlier opposite anchored arc
\(x\to x+\delta\) at \(a\).  The question here is how often that same
pair can be reused by later target arcs.

## 1. Exact parameterization of the reuse class

Define the common-row set

\[
K=\left\{
r\in A: r-x\in A, r-x>a',
\ z(r,a)=z(r,a')=c
\right\}.
\tag{4}
\]

Let \(\mathcal T\) be the set of all later targets \((b,x,h)\), with
\(b>a'\), for which \(a,a'\in U_{(b,x,h)}\).  Such a target has

\[
r=b+x,\qquad s=b+x+h.
\tag{5}
\]

Both \(r,s\) belong to \(K\), and the target arc colors are

\[
z(r,b)=-c,\qquad z(s,b)=c.
\tag{6}
\]

Conversely, if \(r<s\) lie in \(K\), put

\[
b=r-x,\qquad h=s-r.
\tag{7}
\]

If the two cells in (6) have the displayed colors, then \((b,x,h)\)
is an opposite target arc and all four reuse cells

\[
z(r,a),z(s,a),z(r,a'),z(s,a')
\tag{8}
\]

equal \(c\); hence \(a,a'\in U_{(b,x,h)}\).  Equations (4)--(8) are an
exact description of the full reuse class.  No target or incoming
anchor is inserted artificially.

## 2. A restriction shared by all targets

**Lemma 1.**  The common-row set has no pair at distance \(\delta\):

\[
\boxed{K\cap(K-\delta)=\varnothing.}
\tag{9}
\]

**Proof.**  If \(r,r+\delta\in K\), then

\[
(r,a),\qquad(r+\delta,a),\qquad(r+\delta,a')
\tag{10}
\]

is a positive corner of step \(\delta=a'-a\), and all three cells have
color \(c\) by (4).  \(\square\)

This couples different target arcs: the union of all their lower and
upper rows, not merely the two rows of one target, is
\(\delta\)-difference-free.

## 3. Every target excludes two shadow rows

**Lemma 2.**  For a target \((b,x,h)\in\mathcal T\),

\[
\boxed{a+x+h\notin K,\qquad a'+x+h\notin K.}
\tag{11}

\]

**Proof.**  Continue with \(r,s\) from (5).  The target and reuse
conditions give

\[
z(s,a)=z(s,a')=z(s,b)=c.
\tag{12}

Set \(q=a+x+h\).  Since

\[
s-q=b-a>0,
\]

membership \(q\in K\) would make

\[
(q,a),\qquad(s,a),\qquad(s,b)
\tag{13}

a monochromatic positive corner of step \(b-a\).  Hence \(q\notin K\).
Replacing \(a\) by \(a'\) gives a positive step \(b-a'>0\), using the
hypothesis that every target is later than \(a'\), and proves the
second exclusion.  \(\square\)

The conclusion permits all genuine defects.  A shadow row may be absent
from \(A\), its back-shift by \(x\) may be absent, or one of its two
cells over \(a,a'\) may have the other color.  The proof only says that
it cannot satisfy all conditions defining \(K\).

## 4. A global packing inequality for one reuse class

Let

\[
H=\{h:\text{some }(b,x,h)\in\mathcal T\}
\tag{14}
\]

be the set of distinct target steps, and let

\[
V=\bigcup_{(b,x,h)\in\mathcal T}\{b,b+h\}
\tag{15}
\]

be the set of target anchor endpoints.  From (4)--(5),

\[
V+x\subseteq K.
\tag{16}
\]

Lemma 1 and Lemma 2 give the simultaneous disjointness relations

\[
V\cap(V+\delta)=\varnothing,
\tag{17}
\]

and

\[
V\cap(a+H)=V\cap(a'+H)=\varnothing.
\tag{18}
\]

All numbers in these sets lie in \([0,L]\).  For example,
\(a'+h<b+h\le L\) because \(b>a'\).  The two translates \(a+H\) and
\(a'+H\) intersect once for every ordered pair of steps differing by
\(\delta\).  Define

\[
N_\delta(H)=|\{h\in H:h+\delta\in H\}|.
\tag{19}
\]

Counting the disjoint union of \(V\) and
\((a+H)\cup(a'+H)\) yields the span-sensitive bound

\[
\boxed{
|V|+2|H|-N_\delta(H)\le L+1.
}
\tag{20}
\]

The same count can be made at the actual row level, using the disjoint
sets

\[
V+x\subseteq K,\qquad
(a+x+H)\cup(a'+x+H)\subseteq[0,L]\setminus K.
\tag{21}
\]

To retain source holes explicitly, put

\[
D_{\rm hole}=
|((a+x+H)\cup(a'+x+H))\setminus A|.
\tag{22}
\]

The remaining

\[
2|H|-N_\delta(H)-D_{\rm hole}
\tag{23}
\]

shadow rows are actual source marks, but each fails either the required
back-shift support or one of the two color equalities in (4).  Thus (20)
does not silently fill missing source positions.

Lemma 1 alone also gives the coarse interval bound

\[
|V|\le
\left\lfloor\frac{L-a'+\delta}{2}\right\rfloor,
\tag{24}
\]

obtained by partitioning \(\{a'+1,\ldots,L\}\) into its \(\delta\)
residue chains and taking an independent set in each path.

## 5. Exact remaining multiplicity gap

Inequality (20) controls the distinct target steps and the distinct
target endpoints of one reuse class.  It does not control
\(|\mathcal T|\) linearly: many target edges may use the same endpoint
set \(V\), and many targets may have the same step in \(H\).  The exact
parameterization only gives the quadratic relaxation

\[
|\mathcal T|\le\binom{|V|}{2}.
\tag{25}
\]

Therefore an unweighted charge of one earlier arc per later target is
still unsupported.  A complete amortized bound would need one further
actual-color statement limiting the graph on \(V\) whose edges are the
target pairs \(\{b,b+h\}\), or it would need to charge repeated edges
to the supported or color-defective shadow rows in (23).  The present
lemmas supply cross-target exclusions and a span budget without assuming
that reuse is injective.
