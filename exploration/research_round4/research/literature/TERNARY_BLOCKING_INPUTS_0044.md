# Ternary blocking/code inputs for the T11 corner normals (0044)

## Exact translation

Use the 53 free signature coordinates in fibers/T11_FIVE_RAINBOW_LEMMA_0043.md, and write the 165 reconstructed corner-sum forms as

    g_e(s)=a_e dot s,     a_e in F_3^53.

Let G be the 53-by-165 matrix with columns a_e and let C={s^T G:s in F_3^53}. For every signature s,

    #{e:g_e(s)=0}=165-wt(s^T G).

Thus the stronger arbitrary-signature statement “every signature has at least five zero corner sums” is exactly

    A_w(C)=0 for w=161,162,163,164,165,

where A_w(C) is the ternary code weight distribution. The actual T11 target is weaker because the signature also has to pass the divisible-step and excluded-slope proper-lift conditions. The projective cap property of the prescribed normals is retained as an input, but is not replaced by a cardinality-only statement.

## 1. Exact applicable technique: Greene’s weight-enumerator theorem

C. Greene, [Weight Enumeration and the Geometry of Linear Codes](https://doi.org/10.1002/sapm1976552119), *Studies in Applied Mathematics* 55 (1976), 119--128, proves that the weight distribution of a linear code is an evaluation of the Tutte (generalized dichromatic) polynomial of its associated combinatorial geometry.

Applied here, the represented ternary column matroid M(G) is the prescribed 165-normal configuration. A computation or structural determination of the relevant Tutte specialization gives the complete list of A_w(C), so it is capable in principle of proving the five-zero statement by showing that the five top-weight coefficients vanish. This is an exact matroid/code route, not a generic blocking bound.

Mismatch/remaining work: Greene’s theorem does not estimate those coefficients from “cap” alone, nor does it use the sparse three-support geometry or the proper-lift conditions. It supplies a finite invariant to calculate or control; it does not itself yield A_161=...=A_165=0.

## 2. Blocking/minimal/trifferent framework: wrong blocking strength

A. Bishnoi, J. D'haeseleer, D. Gijswijt, and A. Potukuchi, [Blocking sets, minimal codes and trifferent codes](https://arxiv.org/abs/2301.09457), proves that a projective strong (s-1)-blocking set is equivalent to a corresponding affine s-blocking set (Lemma 1.2), and over F_3 relates strong blocking sets, minimal codes, and linear trifferent codes. Their strong blocking condition requires the intersection with every specified codimension subspace to *span* that subspace.

The T11 claim concerns a fixed point set { [a_e] } and asks that every dual hyperplane contain at least five of these points. Ordinary blocking would only require one point; strong blocking asks for a spanning intersection. Neither hypothesis is known for the corner-normal cap, and neither is implied by capness or by each normal having three nonzero entries. The asymptotic size bounds in that paper therefore do not give a five-fold hyperplane-intersection bound for this prescribed configuration.

## Bounded conclusion

The direct source-dependent route is a ternary weight-enumerator/Tutte calculation for the actual 165-column matroid, potentially refined by the reconstruction identities and proper-lift filter. The located blocking-set results do not apply merely from the cap property and cannot be used as a cardinality-only proof of five zeros. No theorem located in this bounded search handles a prescribed sparse ternary cap while forcing a fixed hyperplane intersection multiplicity of five.
