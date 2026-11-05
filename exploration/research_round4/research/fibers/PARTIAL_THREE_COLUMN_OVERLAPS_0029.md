# Partial three-column overlaps

## 1. The sharp array bound

Consider a partially occupied array with \(b\) rows and three columns.
Every occupied entry is colored red or blue. Assume that no two rows
and two columns form a fully occupied monochromatic rectangle. Let

\[
 n_{\rm occ}=\text{number of occupied entries},
 \qquad
 f=\text{number of fully occupied rows}.               \tag{1}
\]

Then

\[
 \boxed{f\le6,\qquad n_{\rm occ}\le2b+f.}              \tag{2}
\]

Consequently

\[
 \boxed{n_{\rm occ}\le\min(3b,2b+6).}                 \tag{3}
\]

The second inequality in (2) is immediate once \(f\) is fixed: a row
that is not full contains at most two occupied entries.

To prove \(f\le6\), encode a full row by its word in
\(\{R,B\}^3\). Duplicate full words are forbidden. If neither constant
word \(RRR,BBB\) occurs, only the six nonconstant words are available.
If \(RRR\) occurs, it excludes all three words having exactly two red
entries. The remaining candidates are \(BBB\) and the three words with
exactly one red entry; moreover \(BBB\) cannot coexist with any of the
latter three, because they share blue in two columns. Thus a family
containing \(RRR\) has size at most four. The color-reversed argument
handles a family containing \(BBB\). This proves the first inequality
in (2).

Both bounds are sharp simultaneously. The six nonconstant binary words
are pairwise rectangle-free: two majority-red words share red in only
one position, two majority-blue words share blue in only one position,
and a word of each type cannot share either color twice. For any
\(0\le f\le\min(b,6)\), take any \(f\) of these full words. Fill every
remaining row in just two columns, once red and once blue, using the
same two-entry pattern repeatedly. Such a row has only one entry of
each color and therefore cannot participate in a monochromatic
rectangle. This gives exactly \(2b+f\) occupied entries. In particular,
the maximum in (3) is attained for every \(b\).

## 2. An actual source overlap array

Let \(B,C\) be finite integer sets, let

\[
 Q>2\operatorname{span}(B),
 \qquad
 A\subset B+QC,                                       \tag{4}
\]

and suppose the strict source triangle \(V(A)\) is properly
two-colored. For \(c\in C\), retain the actual support neighborhood

\[
 N_c=\{x\in B:x+Qc\in A\}.                            \tag{5}
\]

Fix \(\delta>0\), and choose three distinct starts
\(c_1,c_2,c_3\) satisfying

\[
 c_j,c_j+\delta\in C.                                 \tag{6}
\]

The starts in the source overlap of difference \(Q\delta\) associated
with representation \(j\) are exactly

\[
 S_j=N_{c_j}\cap N_{c_j+\delta}.                      \tag{7}
\]

Make a \(B\)-by-three partial array by occupying \((x,j)\) precisely
when \(x\in S_j\). Color that entry by the actual source-edge color

\[
 \chi(x,j)=
 \operatorname{col}(x+Q(c_j+\delta),x+Qc_j).           \tag{8}
\]

This is the diagonal coloring inherited by the translated weak
triangle on

\[
 F_{Q\delta}=A\cap(A-Q\delta).                         \tag{9}
\]

Its two diagonal color classes are Golomb. Therefore the partial array
has no monochromatic rectangle: such a rectangle on rows \(x\ne y\)
and columns \(j\ne k\) would put the two distinct pairs

\[
 \{x+Qc_j,y+Qc_j\},
 \qquad
 \{x+Qc_k,y+Qc_k\}                                    \tag{10}
\]

of the same difference \(|x-y|\) into one diagonal color class. All
four cells in this argument are actual overlap cells; no missing source
mark is filled.

Applying (2) gives the exact necessary inequalities

\[
 \boxed{
 \left|S_1\cap S_2\cap S_3\right|\le6,}               \tag{11}
\]

and

\[
 \boxed{
 |S_1|+|S_2|+|S_3|
 \le2|B|+|S_1\cap S_2\cap S_3|
 \le2|B|+6.}                                          \tag{12}
\]

Thus the full-row term is retained rather than discarded as a density
error.

## 3. Missing-cell form and an all-representation consequence

For each representation define its actual missing-overlap set

\[
 D_j=B\setminus S_j
 =(B\setminus N_{c_j})\cup(B\setminus N_{c_j+\delta}). \tag{13}
\]

Equations (11)-(12) are equivalently

\[
 \left|D_1\cup D_2\cup D_3\right|\ge |B|-6,            \tag{14}
\]

and

\[
 |D_1|+|D_2|+|D_3|
 \ge |B|-|S_1\cap S_2\cap S_3|
 \ge |B|-6.                                           \tag{15}
\]

In particular the six endpoint columns in (6) must collectively miss,
with multiplicity, at least \(|B|-6\) source marks:

\[
 \sum_{j=1}^3
 \bigl(|B\setminus N_{c_j}|+|B\setminus N_{c_j+\delta}|\bigr)
 \ge |B|-6.                                           \tag{16}
\]

Now let \(q=r_C(\delta)\ge3\), list all starts
\(c_1,\ldots,c_q\), and define \(S_j,D_j\) as above. Applying (12) to
every triple and summing, each \(|S_j|\) occurs
\({q-1\choose2}\) times. Hence

\[
 \boxed{
 \sum_{j=1}^q|S_j|
 \le\frac q3(2|B|+6),}                                \tag{17}
\]

or, in missing-incidence form,

\[
 \boxed{
 \sum_{j=1}^q|D_j|
 \ge\frac q3(|B|-6).}                                 \tag{18}
\]

The no-carry condition (4) makes the pieces
\(S_j+Qc_j\) disjoint and exhausts the actual overlap fiber. Therefore
(17) may also be written

\[
 \boxed{
 |F_{Q\delta}|
 \le\frac{r_C(\delta)}3(2|B|+6).}                     \tag{19}
\]

## 4. Scope

Equations (11)-(19) are necessary conditions on an actual overlap fiber
of a proper source contained in an incomplete direct product. They
retain the neighborhood intersections and count every missing overlap
cell explicitly. The abstract array extremizers prove sharpness of
(2)-(3), but they are not asserted to extend to proper colorings of an
entire source triangle. No global source-energy bound follows here
without an additional summation controlling how the missing sets
\(D_j\) are reused across different factor differences.
