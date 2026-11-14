# Moving an argument between three and four colors

For a `k`-coloring of the square, a diagonal color class `D` has a strict
source `V(D)` colored with the remaining `k - 1` colors. At lag `h`, the
fiber `F_h(D)` is partitioned by the color of `(u+h, u)` into `k - 1` sets,
each of whose own strict source avoids two colors and so carries `k - 2`.

| Object | `k = 3` | `k = 4` |
|---|---|---|
| `V(D)` | binary | ternary |
| Parts of `F_h(D)` | 2 Golomb sets | 3 sets with binary sources |
| Parts of fibers of those parts | (none) | 2 Golomb sets each |
| Classes per lag at top level, over all diagonal colors | 6 | 12 |

## Transfer test

For each step of a three-color argument, answer in writing:

1. Does the step use that a completion color is **forced** (only one color
   left)? Then it is binary-only. The ternary version has a list of two
   colors per cell; state what replaces forcing (a list constraint, a
   counting inequality over the two choices, or nothing).
2. Does it use that a class is **Golomb**? At the top level of a four-color
   argument the classes are not Golomb. The property reappears one level
   down. State at which level the step is being applied.
3. Does it use `G(24)`, `G(25)`, OGR uniqueness, or any small-span table?
   These are inputs about Golomb sets in a few hundred positions. The
   four-color regime has spans in the millions; check both the level and
   the span.
4. Does it use signs, squared imbalance, or a bipartite graph? Re-derive
   with color vectors or a three-part structure; do not assume the identity
   survives.
5. Do the constants depend on the number of classes (2, 6) or colors? Redo
   the count (3, 12) and the accounting of shared positions.

A step that passes the test transfers as a **new statement to be proved**,
not as a corollary. Record it on the candidate card with `k = 4` scope.

## What does transfer (with proofs on record)

- Diagonal exclusion and the fiber partition, for every `k`
  (`manuscript/main.tex`, `lem:restriction`, proof of `thm:s21four`).
- The shift count `lem:shift`, which needs only multiplicity caps.
- The abstract joint packing lemma for `q` disjoint classes with a monotone
  capacity function (`SIX_CLASS_LEMMA.md`); its gain at four-color scale is
  expected to be negligible unless the capacity function has cliffs.
- Joint Cauchy over the diagonal partition, with `k` classes.

## What does not transfer without new work

- The six-class cap `U(p)` and everything derived from OGR inputs.
- Signed completion, forcing graphs, G9-type statements, repair and balance
  arguments.
- Conditional figures: `98777` is a consequence of S21, which is a statement
  about binary sources at spans up to `98775`; it is neither a four-color
  theorem nor evidence for one.

## Direction of use

Four-color work can also feed back: a binary-source bound proved for large
spans with a crude constant is a statement about exactly the sources the
three-color problem needs, in a regime where asymptotic tools apply. Check
whether its small-span specialization says anything at span 450.
