# A two-Golomb partition of the three-axis binary fiber

## 1. Statement and construction

Let

\[
 F=\{\pm a_i,\ E\pm a_i:1\le i\le3\},                 \tag{1}
\]

where \(E,a_1,a_2,a_3\) admit no nonzero integer relation whose
coefficients have absolute value at most four. Then \(F\) is the
disjoint union of the following two Golomb sets:

\[
\begin{aligned}
 R={}&\{a_1,-a_1,a_3,\ E+a_2,E-a_2,E-a_3\},\\
 B={}&\{a_2,-a_2,-a_3,\ E+a_1,E-a_1,E+a_3\}.
                                                               \tag{2}
\end{aligned}
\]

Equivalently, in the bottom layer the three signed axes have color
patterns

\[
 (RR),\quad(BB),\quad(RB)                              \tag{3}
\]

when the entries are ordered \((+a_i,-a_i)\). Translation by \(E\)
complements every color, giving the top patterns

\[
 (BB),\quad(RR),\quad(BR).                             \tag{4}
\]

## 2. Exhaustion of repeated differences

The dissociation assumption means that two differences between members
of \(F\) are equal only when their formal \(E,a_1,a_2,a_3\)
coefficient vectors are equal. Indeed, subtracting two such differences
produces coefficients of absolute value at most two on \(E\) and at
most four on each \(a_i\). It is therefore enough to inspect the formal
difference fibers listed below.

### Horizontal fibers

For a fixed axis, the difference \(2a_i\) has one representation in
each layer. For \(i=1\), the bottom representation is red and its
translate is blue; for \(i=2\), the colors are reversed; and for
\(i=3\), both representations are bichromatic. Thus no color occurs
monochromatically twice in a \(2a_i\)-fiber.

For distinct axes \(i,j\), each root difference

\[
 \pm a_i\pm a_j                                       \tag{5}
\]

has two representations in the bottom layer and their two translates
in the top layer. The bottom signed-axis patterns (3) give:

\[
\begin{array}{c|c}
 \text{axis support}&
 \text{monochromatic representations in a fixed fiber (5)}\\ \hline
 \{1,2\}&\text{none},\\
 \{1,3\}&\text{exactly one red and no blue},\\
 \{2,3\}&\text{exactly one blue and no red}.
\end{array}                                             \tag{6}
\]

The translated representations have all colors complemented. Hence a
fiber supported on \(\{1,3\}\) has at most one monochromatic red
representation and at most one monochromatic blue representation; the
same conclusion holds for \(\{2,3\}\). The \(\{1,2\}\) fibers remain
entirely bichromatic. No horizontal repeated difference occurs twice
inside either color class.

### Vertical and slanted fibers

The pure difference \(E\) has the six representations

\[
 (E+\sigma a_i)-(\sigma a_i),
 \qquad i\in\{1,2,3\},\quad \sigma\in\{+,-\}.
\]

Every one is bichromatic by the complement rule (4), so this largest
fiber causes no collision in either color.

The differences \(E\pm2a_i\) have only one representation each. For
distinct \(i,j\), a slanted root difference \(E\pm a_i\pm a_j\) has
exactly two representations. For example,

\[
 E+a_i-a_j
  =(E+a_i)-a_j
  =(E-a_j)-(-a_i),                                    \tag{7}
\]

and the other sign patterns are obtained in the same way. The colors
of the four endpoints of these two representations have the following
form:

\[
\begin{array}{c|c}
 \text{axis support}&\text{endpoint-color multiset}\\ \hline
 \{1,2\}&2R+2B,\\
 \{1,3\}&3R+B\text{ or }R+3B,\\
 \{2,3\}&3R+B\text{ or }R+3B.
\end{array}                                             \tag{8}
\]

In particular the four endpoints are never monochromatic. Therefore
the two representations in (7), or in any of its sign variants, cannot
both lie in \(R\) and cannot both lie in \(B\).

The horizontal, pure vertical, and slanted cases exhaust all formal
difference vectors: the coefficient of \(E\) is zero or \(\pm1\), and
the remaining support uses either one axis or two. Thus every nonzero
difference has at most one representation inside \(R\) and at most one
inside \(B\). Both sets in (2) are Golomb.

## 3. Scope

The construction settles the three-axis binary fiber positively. It
uses the simultaneous presence of one red-monochromatic axis, one
blue-monochromatic axis, and one split axis in the bottom layer, followed
by color complementation in the top layer. It does not give a partition
for four or more axes and does not assert that an arbitrary proper
source decomposes into fibers of this form.
