# No modular-affine construction through modulus 128

There is no proper three-coloring of the 21 by 21 square of the form
\[
 \chi(x,y)=f((ax+by)\bmod m),\qquad 1\le m\le128,
\]
for any integers \(a,b\) and any three-color map \(f\). An additive constant is absorbed into \(f\). This settles the [earlier unfinished scan through modulus 50](../../exploration/research_round3/lower/AFFINE_CONSTRUCTIONS.md) and extends it to 128.

**Reduction.** Let \(g=\gcd(a,b,m)\). Restricting \(f\) to multiples of \(g\) gives an equivalent map at primitive parameters \((a/g,b/g,m/g)\). When the resulting modulus is at most 20, step \(d=m/g\) sends the three cells of a directed L to the same residue. At larger primitive moduli, multiplying \(a,b\) by a common unit merely relabels the residues. Exchanging \(a,b\) preserves feasibility, since the grid symmetry \((x,y)\mapsto(20-y,20-x)\) exchanges them up to a common minus sign and an additive constant.

**Finite proof.** At each representative, project all 2,870 directed Ls onto the residues. One distinct residue precludes a coloring. Two distinct residues require different colors. Three distinct residues forbid a monochromatic triple. The checker colors the residues by propagating these restrictions. Whenever two residues get the same color, all third residues completing their projected triples lose it. The search branches on every remaining choice, using one representative when several colors are as yet unused. Palette symmetry fixes residue zero to color zero.

| Primitive modulus | Ordered primitive pairs | Representatives |
|---|---:|---:|
| 21–50 | 33,240 | 857 |
| 51–64 | 38,568 | 631 |
| 65–128 | 513,912 | 4,805 |
| **Total** | **585,720** | **6,293** |

Together with divisor reduction this covers all \(\sum_{m=1}^{128}m^2=707,264\) ordered parameter choices. An additional SAT encoding independently rejected all 2,092 symmetry representatives at primitive moduli 21 through 75. The exhaustive direct coloring checker supplies the full theorem.

Compile **verify_affine_128.c** with an optimizing GCC or Clang target that supports unsigned 128-bit integers. Run the executable with no arguments, or give an inclusive subrange such as **21 50**. Search order affects runtime. The proof concerns this construction family; the unrestricted side-21 problem remains open.
