# Exact diagnostic: image weight is not parameter multiplicity

Source: [Wijaya, arXiv:2606.08890v1, Sections 2–4](https://arxiv.org/html/2606.08890v1#S4), accessed 2026-11-08. The weight definition and Fourier formula were also checked in the [primary PDF](https://arxiv.org/pdf/2606.08890v1), pp. 5–6, so the issue is not inferred solely from HTML rendering. This note is our independent derivation of a narrow issue. It does not refute the main density theorem or the displayed U³ inequality.

For a nonconstant P:Fₚ→Fₚ, write S=P(Fₚ), N(t)=#{z:P(z)=t}, and w(t)=p·1_S(t)/|S|. Both N and w have mean one, but they need not be the same function. For every test function F,

```math
\frac1p\sum_z F(P(z))=\frac1p\sum_t N(t)F(t).
```

The right side cannot generally use w instead of N. This is the implicit substitution needed if the parameter-average polynomial-corner operator is written with the paper's normalized image weight. The proof's displayed Fourier equality for f=w−1 also equates its Fourier coefficient at a nonzero frequency with |S|⁻¹Σ_z exp(−2πirP(z)/p); that change of variables counts preimages.

## A degree-three instance within p>d²

Take p=103 and P(z)=z³. The cyclic group F₁₀₃× has order 102, hence every nonzero cube has three preimages, whereas zero has one. Consequently |S|=1+102/3=35, N(1)=3, w(1)=103/35.

Choose f₀=1_{(0,0)}, f₁=1_{(1,0)}, and f₂=1_{(0,1)}. These are 1-bounded functions. Their corner product forces x=y=0 and step 1. Thus the parameter average equals 3/103³, whereas the uniform-image weighted average equals 1/(35·103²). Their exact difference is 2/(35·103³), which is nonzero. The step is nonzero, so excluding degenerate steps does not remove this example.

This disproves the **replacement equality**, not a bound between the two averages. Counting only existence of a polynomial step can sometimes use the image weight; doing so requires changing the counting operator consistently. Alternatively, using N restores the exact parameter identity, but then N−1 needs the appropriate norm estimate. Neither repair is completed here.

## Exact Fourier test

Let ζ be a primitive p-th root of unity. Encode each proposed coefficient as a rational polynomial in ζ. Since the minimal polynomial is Φₚ(X)=1+X+⋯+X^(p−1), a polynomial of degree at most p−1 vanishes at ζ exactly when all its coefficients coincide. The script subtracts the final coefficient from all earlier coefficients, computing the exact remainder modulo Φₚ. Nonzero remainders occur for (p,degree)=(5,2),(101,2),(103,3).

For the hand-checkable p=5 case, S={0,1,4}. At r=1 the correct coefficient is (1+ζ+ζ⁴)/3, while the displayed expression is (1+2ζ+2ζ⁴)/3. Their difference is −(ζ+ζ⁴)/3=−(√5−1)/6≠0.

The quadratic issue persists for every odd prime: the difference is −|S|⁻¹Σ_{t nonzero square}ζ^(−t). Its degree-at-most-p−1 coefficient vector has both zero and nonzero entries, so the cyclotomic criterion proves nonvanishing. Thus no “sufficiently large prime” cutoff repairs this exact equality. This observation still says nothing against a potentially valid asymptotic inequality with a different argument.

## Reproduction and scope

```text
python -X utf8 research/boundary_extension_20261108/literature/check_polynomial_weight.py --output /path/to/fresh/results.json
```

Recorded execution: `weight_run/results.json`, with provenance and input/output SHA-256 in `weight_run/manifest.json`. Only standard-library integer/rational arithmetic is used; no floating-point comparison or SAT solver enters. The degree-three multiplicity argument and p=5 cyclotomic calculation are independent hand derivations supporting the program.

Status: **COUNTEREXAMPLE** to the stated Fourier equality and to the indicated implicit weight substitution; **UNVERIFIED** for importing the paper's final density theorem as a project dependency. Other source steps, including the claimed geometric component factorization, were not resolved by this diagnostic. No L-grid Ramsey bound changes.
