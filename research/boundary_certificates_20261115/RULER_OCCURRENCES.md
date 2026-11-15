# At most two optimal completion classes on the entire 461 diagonal

A proper three-color square of side at most 461 has **at most two completion classes of size 24 and span exactly 425 in total over all positive shifts**. Each orientation supplies at most one. This strengthens the earlier bound of 56 at comparable sides. The proof uses the external uniqueness of the optimal 24-mark Golomb ruler and a finite binary-source certificate covering 595 placement patterns. The subsequent [single-class exclusion](NO_OPTIMAL_461.md) and [35-letter certificate](THREE_COLOR_461.md) give the three-color upper bound 461. [Earlier occurrence-count argument](../../research/global_counting_20261108/multiscale/THEOREM.md) · [OGR-24 completion announcement](https://blogs.distributed.net/2004/11/)

## Occurrences in one diagonal word

Write $Q$ for the 24-mark optimal ruler, normalized with endpoints 0 and 425. Its marks are

```
0 9 33 37 38 97 122 129 140 142 152 191
205 208 252 278 286 326 332 353 368 384 403 425
```

For either orientation $P=Q$ or $P=425-Q$, let $T_P$ be the set of starts $s$ for which $s+P$ has one color on the main diagonal. In a square of side at most 461 the largest possible start is 35. Every difference from 1 to 35 occurs between two marks of $P$. Thus any two of its translates with these starts intersect, and all the occurrences of this orientation share one diagonal color.

Suppose three starts occur. Translating the least to zero gives starts $0,a,b$ for some $1\le a<b\le35$. Their union $A=P\cup(a+P)\cup(b+P)$ lies in one diagonal color. In a proper square each strict cell $(x,y)$ with $x,y\in A$ and $x>y$ must avoid that color, because $(y,y),(x,y),(x,x)$ is a directed L. The strict source on $A$ must therefore admit a proper binary coloring.

For $P=Q$, the certificate rules out this binary coloring in **all 595 cases**. For the reflected orientation, reflect integer positions by $z\mapsto425+b-z$. This maps the marked union for starts $0,a,b$ to the forward union for starts $0,b-a,b$. On the strict cells the map $(x,y)\mapsto(425+b-y,425+b-x)$ preserves the strict order and takes each directed L to another directed L of the same positive step. Therefore $|T_P|\le2$ for both orientations.

## From occurrences to completion classes

At lag $d$, a size-24 class of span 425 is $s+P$ by the uniqueness of the optimal ruler. The two diagonal projections of its completion cells give monochromatic occurrences of $P$ at both $s$ and $s+d$. A class determines the ordered pair of these starts. Conversely, an ordered pair fixes $d$, all the class positions and their original color. The physical completion cells cannot simultaneously have two different completion colors. Hence at most one such class can use that pair. With at most two starts per orientation, there is at most one ordered pair of increasing starts for each orientation. At most two classes survive across the entire diagonal. A 24-mark class of greater span is outside this count.

## Finite certificate

The compressed file **ruler_triple_proofs.json.xz** contains one record for every increasing pair $a,b$. Each record supplies a subset of the corresponding union and a RUP trace for the binary strict source on that subset. In every case the checker validates containment, builds all source cells and directed triples, and pins the first binary cell by color interchange. For each triple the two complementary clauses forbid all-zero and all-one. A single refuted subset excludes the entire union by restriction.

Run **python verify_ruler_occurrences.py /path/to/drat-trim**. The verifier enumerates triples from their leftmost cell and checks the proof in RUP-only mode. The producer enumerated pairs of starts at each positive step and used Glucose and drat-trim. The decompressed data have SHA-256 **95a25a08857751ba51260e1c2b67d195c016b27913bb7ead3409c70be8e2d715**. [Proof-checker source](https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985)
