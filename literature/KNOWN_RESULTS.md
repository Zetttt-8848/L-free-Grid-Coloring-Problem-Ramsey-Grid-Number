# The relationship between existing achievements in academia and this project

Verification date: 2026-11-05. The following is a map of the core original literature that has been verified and is not an exhaustive survey of the entire literature. Numerical bounds updates must have verifiable original source, version, and proven location.

## First unify the problem agreement

This project fixes the positive step length and the orientation L of two legs of equal length:

```math
\mathcal L(x,y;d)=\{(x,y),(x+d,y),(x+d,y+d)\},\qquad d>0.
```

Some documents are written in another orientation, and the coordinate transposition corresponds to the two, so the number of positive steps L is the same. Generally, three-point right angles, angles that allow arbitrary length and width, density versions and three-dimensional corners cannot be directly confused. For the proof of direction conversion, see the Transposition Lemma in the main text of this project.

## 1. Two-Color Exact Value: Solved Benchmark

```math
R_2(\mathcal L)=5.
```

Source: Maria Axenovich and Jacob Manske, *On monochromatic subsets of a rectangular grid*, Integers 8 (2008), A21. [Journal original text](https://math.colgate.edu/~integers/i21/i21.pdf). It can also be cross-checked with Theorem 2.2 of Canakci et al.'s literature below.

Purpose: Verifying direction, indexing, and small-scale implementations. The two-color proof cannot be viewed directly as a three-color answer.

## 2. Three-color lower bound and early upper bound

[2023 preprint v1 by Canakci, Christenson, Fleischman, Gasarch, McNabb, Smolyak](https://arxiv.org/html/2312.01159v1)Theorem 2.3 gives an upper bound of 2593, and Theorem 3.1 gives the interval 21 to 2593. The lower bound comes from the full 20×20 normal tricolor, rather than from searching for no counterexamples found.

```math
21\le R_3(\mathcal L)\le2593.
```

Research value: diagonal achromaticity, forced relations, and SAT constructs. 2593 is a historical upper bound that has been improved by the next project and should not be marked as the current benchmark upper bound on the project homepage.

## 3. Three-color verified stronger upper bound

Mammel,Smith,Yerger,*Ramsey Theory on the Integer Grid: The “L” Problem*,Integers 25 (2025), A21,Theorem 6:

```math
R_3(\mathcal L)\le493.
```

[Journal original text](https://math.colgate.edu/~integers/z21/z21.pdf);[arXiv version](https://arxiv.org/abs/2502.05162). The method uses interval counting and Golomb ruler constraints. The paper acknowledgments attribute the proofs of 772 and 493 to the reviewers. There are differences in the representation of intermediate values ​​between the journal version and the preprint version. This library only uses the final Theorem 6 value of 493 as the benchmark for comparison. The arXiv version also discusses lower bounds and search strategies.

Merging the checked upper and lower bounds, the unconditional numerical starting point for collaboration is:

```math
21\le R_3(\mathcal L)\le493.
```

The range is still not equal to the exact value. This directed search did not verify the stronger subsequent unconditional bound, and it cannot be concluded based on this that there is no subsequent literature. The 22×22 normal coloring prediction proposed in this article should not become an existing structure.

## 4. General density tools: quasi-polynomial corners theorem

Jaber, Liu, Lovett, Ostuni, Sawhney, *Quasipolynomial bounds for the corners theorem*, [Full version v2, Theorem 1.1](https://arxiv.org/html/2504.07006v2). For the finite square subset of the Abelian group with no non-zero step size standard corner, there is an absolute constant c>0, such that

```math
|A|\le |G|^2\exp\!\left(-c(\log |G|)^{1/600}\right).
```

Standard angles are (x,y), (x+d,y), (x,y+d). The theorem itself is not a numerical bound on small color numbers for the orientation L of this project. Positive step processing, reflection, paired colors and wraparound-free embedding require additional certification. The appendix of this project provides a transformation to derive a general growth bound for the number of colors, but does not directly change 493 to a smaller value.

## 5. Related math input and reading order

- Graham–Solymosi, *Monochromatic equilateral right triangles on the integer grid* (2006): Important background on this grid coloring problem. [Publisher DOI](https://doi.org/10.1007/3-540-33700-8_7). Its entire quantitative derivation was not re-audited in this round.
- Classic corners work by Ajtai–Szemerédi: background input for density routes, see AS74 in bibliography for a specific version.
- Sidon/Golomb theory: for monochromatic fiber constraints; binary Sidon input and Wood's no-carry transformation are relevant to the cube discussion. [Wood original entry](https://arxiv.org/abs/math/0509455). The specific capacity and weight assumptions must be returned to the project text and its references, and the global source boundary cannot be automatically derived from ordinary Sidon definitions.

It is recommended to read two numerical literature on the L problem first, and then read the background along the two directions of "global completion lattice compatibility" and "density/structure increment". Existing theories are the benchmark for testing new mechanisms, which does not mean that the use of previous theorems is prohibited.

## 6. Project conclusions that must not be mixed into industry numerical benchmarks

Source counting, Golomb union counting, six-label classification, and structured source bounds for this project are provided in the Current Mathematics text. Their priority is not automatically confirmed by this import.

379 and 98777 under S21 and 361 under existential G9 are all conditional inferences that retain unproven assumptions. The five-dimensional cube exclusion is only a necessary condition. F11(5), F12(7), F13(17) have been negated by the full tinting certificate in the project. Neither the above numbers nor the failed premise can replace the unconditional interval in academia.
