# Kempe-component probe of the \(T_{13}\) witness

**Status:** the \(21\)-rainbow seed has no nontrivial Kempe exchange of
the specified type.  This is a statement about its Kempe orbit, not
about all proper \(T_{13}\) colorings.

## 1. Seed

The seed is the literal proper coloring from
`LARGER_TRIANGLE_RAINBOW_PROBE.md`.  Its row strings are

| row \(v\) | colors |
|---:|:---|
| 1 | `0` |
| 2 | `11` |
| 3 | `101` |
| 4 | `2112` |
| 5 | `20120` |
| 6 | `020101` |
| 7 | `2211222` |
| 8 | `11022000` |
| 9 | `000202111` |
| 10 | `2220010122` |
| 11 | `11002121000` |
| 12 | `101021021020` |

It has \(28,26,24\) cells of colors \(0,1,2\), respectively, and
exactly \(21\) rainbow corners.

## 2. Component construction

For a color pair \(\{a,b\}\), take all cells colored \(a\) or \(b\).
For every corner whose three cells all have colors in \(\{a,b\}\),
join its three vertices into one hyperedge.  The connected components
are the transitive closure of these hyperedges.

The seed is proper, so every such hyperedge uses both \(a\) and \(b\).
The exact component counts are:

| color pair | vertices | two-color corner hyperedges | components | component sizes |
|:---:|---:|---:|---:|:---|
| \(\{0,1\}\) | 54 | 98 | 1 | 54 |
| \(\{0,2\}\) | 52 | 89 | 1 | 52 |
| \(\{1,2\}\) | 50 | 78 | 1 | 50 |

The hyperedge counts sum to

\[
98+89+78=265
=\binom{13}{3}-21,
\]

as they should: all \(286\) corners are either one of the \(21\)
rainbow corners or use exactly one of the three color pairs.

## 3. Induced component-flip problems

For each color pair there is only one component.  Hence there are only
two flip assignments:

1. leave the component unchanged;
2. swap the two colors on every cell having either color.

The second assignment is a global transposition of two color labels.
It preserves the color pattern of every corner, including whether that
corner is rainbow.  Equivalently, for each pair the signed component
cut problem has one vertex, no cross-component terms, and constant
rainbow score \(21\).

After any such transposition, the three named pair hypergraphs are
merely relabeled versions of the three connected hypergraphs above.
Consequently every finite sequence of permitted Kempe exchanges is a
global permutation of the seed's color labels.  Its entire reachable
orbit has at most six labeled colorings, all with the same \(21\)
rainbow positions.

## 4. Terminal scope

No coloring with at most \(16\) rainbow corners is reachable from this
seed by the specified Kempe-component exchanges, because the only
available moves leave the rainbow count equal to \(21\).  This does not
exclude another proper \(T_{13}\) coloring with at most \(16\)
rainbows, nor does it give a lower bound on the \(T_{13}\) minimum.
The refined \(17\)- or \(18\)-rainbow amplification thresholds
therefore remain unresolved by this probe.
