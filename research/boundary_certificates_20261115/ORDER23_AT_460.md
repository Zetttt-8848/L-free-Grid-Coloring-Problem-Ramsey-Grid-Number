# An order-23 completion shape excluded at side 460

In a proper three-color square of side 460, no completion class can be a translate or reflection of the following 23 marks:
~~~
0 3 7 17 61 66 91 99 114 159 171 199
200 226 235 246 277 316 329 348 350 366 372
~~~
This is the listed optimal order-23 ruler. The finite assertion here is about this explicit shape. The order-24 and order-25 span bounds are used for diagonal color frequencies. [Ruler table](https://www.feiri.de/ogr/nearopt.html) · [Frequency argument](NO_OPTIMAL_461.md)

For a shift \(1\le d\le87\), let \(Q\) be the given set and suppose the completion class starts at \(s+Q\). Every position of \(s+Q\) and \(s+d+Q\) belongs to its original diagonal color. Every cell \((s+x+d,s+x)\) for \(x\in Q\) has the same completion color. This supplies a binary strict source with prescribed cells. For each additional prospective mark \(u\) relative to the start, impose the same conditions on \(Q\cup(Q+d)\cup\{u\}\) and propagate monochromatic-pair implications. If a triple demands both colors at one cell, exclude \(u\).

At 82 shifts those exclusions alone give a strict contradiction. At shifts 4, 9, 11, 12 and 15, 57 extra very short proofs exclude additional individual positions. The checker enumerates all admissible placements \(0\le s\le87-d\), with physical positions in \([-s,459-s]\). The largest upper bound on the size of the original color is 133. Recomputing the one-color Cauchy inequality gives at most 163 of each color, hence at least \(460-2\cdot163=134\). Reflection of the square in the anti-diagonal takes the reverse ruler to the forward one and preserves directed Ls. This proves the stated exclusion.

Run **python verify_order23.py**. It uses the standard library. For each lag it computes unit implications on the compulsory marks once and activates the extra triples separately for each tested \(u\). It rebuilds the full coordinate clauses independently for the short proofs in **order23_short_proofs.json**.
