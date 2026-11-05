# Eight-mark routing reduction

Later result: the literal source obstruction is now proved in
`../EIGHT_MARK_PAIR_OBSTRUCTION_0014.md` by cancelling pair polynomials.
The eleven-word route below is retained as its earlier partial reduction;
the completed proof does not require finishing those eleven cases.

Let

```text
A={0,1,2,3,4,6,7,8}.
```

This note gives a bounded direct reduction for the observed
non-two-colorability of its strict completion triangle.  It does not
complete a human contradiction. The line-minimum values below are the
reported finite enumeration inputs from ROUTING_DUAL_DISCOVERY_0014.json;
this note does not supply a separate analytic derivation of those minima.
Using those inputs, the remaining problem is reduced to
eleven explicit offset-one cases with a three-unit line-slack budget and
nested ordered cuts.  No Ramsey-number improvement follows.

## 1. Exact budget forced by a hypothetical proper coloring

Write `z_d(x)` for the sign of `(x+d,x)`.  The nonempty difference fibers
have start-set sizes

```text
d       1  2  3  4  5  6  7  8
|F_d|   6  5  4  4  3  3  2  1.
```

Hence the number of corners is

```text
T=binom(6,2)+binom(5,2)+2binom(4,2)
    +2binom(3,2)+binom(2,2)=44.                           (1)
```

Every proper two-colored corner has exactly one equal-color pair.  The
independent minimum equal-pair counts on the difference, row, and column
line families are respectively `16,12,13`.  Therefore a hypothetical
proper coloring would have nonnegative integral excesses

```text
delta_D+delta_R+delta_C=44-(16+12+13)=3.                 (2)
```

This is stronger than merely saying that the independent line budget
does not contradict properness: every line family must be within a total
of three equal edges of all its separate maximum cuts.

For later use, the difference-fiber contributions alone imply:

* `F_1` has a `3+3` or `2+4` color split; the latter uses one unit of
  `delta_D`.
* `F_2` has a `2+3` or `1+4` split; the latter uses two units.
* Each of `F_3,F_4` has a `2+2` or `1+3` split; the latter uses one unit.
* A monochromatic `F_5` or `F_6` uses two units.

All other imbalance combinations whose displayed costs exceed three are
excluded before any row/column compatibility is used.

## 2. The eleven possible first-fiber words

The first fiber has ordered start set

```text
F_1={0,1,2,3,6,7}.
```

Each of its two actual color classes is Golomb.  Normalize by global
color reversal, and encode the two signs by bits so the first bit is 0.
The sign variables used in the formulas outside the word list still take
values -1,+1. Applying distinct-difference to the
repeated differences

```text
1: (0,1),(1,2),(2,3),(6,7)       4: (2,6),(3,7)
2: (0,2),(1,3)                   5: (1,6),(2,7)
3: (0,3),(3,6)                   6: (0,6),(1,7)
```

leaves exactly the following words, written in the order
`0,1,2,3,6,7`:

```text
001010   001011   001101   001110
010010   010011   010100   010101
010110   010111   011010.                                (3)
```

The words with two or four ones use one unit of `delta_D` on `F_1`;
the words with three ones use none.  List (3) is a direct finite
consequence of the six displayed repeated-difference restrictions; it
does not use a satisfiability result.

For any word in (3), every same-sign pair supplies the forced completion

```text
z_1(x)=z_1(y)=s, x<y
       implies z_{1+y-x}(x)=-s.                          (4)
```

Thus (3)--(4) fix a substantial part of the higher fibers before the
three units in (2) are allocated.

## 3. The first nested ordered cuts

Put

```text
a_x=z_1(x),
b_x=z_2(x),
c_x=z_4(x).
```

For `(d,e)=(1,2)`, the valid corner starts are

```text
G_{1,2}={0,1,2,6};
```

the inner endpoint pairs are

```text
(a_0,a_1), (a_1,a_2), (a_2,a_3), (a_6,a_7),              (5)
```

and their completion signs are `b_0,b_1,b_2,b_6`.  Fixing a completion
sign `s`, classify a start `x` as

```text
diagonal: a_x=a_{x+1}=-s,
column:   a_x=s,  a_{x+1}=-s,
row:      a_x=-s, a_{x+1}=s.                             (6)
```

There is at most one diagonal start of each completion sign.  More
strongly, among the starts having completion sign `s`, every column start
in (6) is smaller than every row start.  Hence (5) is split by one ordered
cut for each actual class of the `b` variables.

The next nontrivial cut is nested inside the same variables.  For
`(d,e)=(2,4)`,

```text
G_{2,4}={0,2,4};
```

the inner endpoint pairs and completions are

```text
(b_0,b_2)->c_0,
(b_2,b_4)->c_2,
(b_4,b_6)->c_4.                                         (7)
```

For each fixed value of `c_x`, the column cases in (7) again precede the
row cases, with at most one diagonal exception.  In particular the four
variables `b_0,b_2,b_4,b_6` must simultaneously serve as completion
colors in (5) and as the ordered inner word in (7).  This compatibility
is discarded by the separate line minima `16,12,13`.

There is also a bridge at `(d,e)=(1,4)`:

```text
(a_0,a_3)->c_0,       (a_3,a_6)->c_3,                    (8)
```

so the completion `c_0` in the first corner of (7) is already coupled to
the first-fiber word.  Equations (5)--(8), together with their
color-reversed forms, are the smallest nested routing subsystem isolated
here.

## 4. Product form of the shared-line constraint

For any corner with left, completion, and right signs `L,Q,R`, define

```text
I_C=(1+LQ)/2,     I_R=(1+RQ)/2,     I_D=(1+LR)/2.         (9)
```

Under properness these are zero-one variables satisfying

```text
I_C+I_R+I_D=1.                                           (10)
```

The signed route variable is

```text
rho=I_C-I_R=Q(L-R)/2.                                   (11)
```

After the possible diagonal exception is removed, the one-cut statement
says that `rho=+1` occurs before `rho=-1` within each fixed completion
class.  Thus the coupling needed for this example is already a coupling
of shared products `LQ` and `RQ`, rather than unary sign preferences.
For two starts `x<y` in the same `(d,e)` block, its forbidden inversion
has the exact form

```text
I_R(x) I_C(y) (1+Q_x Q_y)/2 = 0.                         (12)
```

This explains why independently optimizing each row and column graph
misses the constraint: it may choose `I_R(x)=I_C(y)=1` without retaining
that the two completion cells have the same actual sign.

## 5. Exact residual

A direct proof from this reduction must eliminate the eleven words in
(3) using all three of the following simultaneously:

```text
(i)   the forced completions (4),
(ii)  the nested one-cut systems (5)--(8),
(iii) the total line excess delta_D+delta_R+delta_C=3.    (13)
```

The bounded derivation did not close these eleven cases by a short forcing
chain.  The missing step is an inequality, preferably in the shared
products appearing in (9)--(12), showing that every extension of each
word in (3) spends at least four units above the independent line minima.
That would give at least `41+4=45` equal pair edges, contradicting the
exact proper-coloring total `44`.

Ordinary clique packing does not encode (12), and assigning unary sign
potentials cannot distinguish a coloring from its global reversal.  The
finite residual (13) therefore points specifically to cancelling
potentials on shared products or to an explicit eleven-case forcing
argument.  No assertion that such a potential or argument has been
completed is made here.
