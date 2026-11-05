# Refined energy bound for complete progression products

Root derivation, continuation 0040. The new two-Golomb mixed-pair bound
improves the complete progression-product theorem from T<=5M and
M<=11L to T<=7M/2 and M<=8L. The full-product premise remains essential;
this is not a universal source theorem or a new small-color Ramsey bound.

Let B be a nonempty finite integer set, b=|B|, let t>=2 be an integer,
and let Q>2 span(B). Set

    A=B+Q{0,...,t-1}, n=tb, M=binom(n,2), L=span(A).

Assume V(A) has one proper two-coloring. The inherited weak-source
argument gives a two-Golomb partition of

    F_Q=B+Q{0,...,t-2}.

The exact no-carry energy factorization from
PROPER_PROGRESSION_PRODUCT_ENERGY_0027.md is

    E(B+Q{0,...,s-1})=e_s E(B),
    e_s=s(2s^2+1)/3.                                 (1)

It follows by equality of the two coordinate differences and includes
the zero coordinate difference. We reuse this established factorization.

TWO_GOLOMB_MIXED_ENERGY_0040.md now supplies

    E(F_Q)<=6[(t-1)b]^2-5(t-1)b.                    (2)

Write D_t=2(t-1)^2+1 and R_t=(2t^2+1)/D_t. Taking the ratio of the
two identities (1) and substituting (2) yields

    E(A)<=6[(t-1)/t]R_t n^2-5R_t n.                 (3)

The estimate holds also when (t-1)b=1, since the new energy bound
includes singleton sets.

## Uniform coefficient and the linear term

Put lambda_t=6[(t-1)/t]R_t. The exact difference satisfies

    9-lambda_t
      =3(t-2)(2t^2-4t-1)/(tD_t)>=0                 (4)

for every t>=2. We claim that (3) is at most 9n^2-8n. Their difference
is n[(9-lambda_t)n+5R_t-8]. Since n=tb>=t and (4) is nonnegative,
the bracket is at least

    (9-lambda_t)t+5R_t-8
      =[6t^3-30t^2+53t-13]/D_t.                    (5)

The numerator is 21,38,103 at t=2,3,4, respectively. For t>=5,
its first two terms are 6t^2(t-5)>=0, and 53t-13>0. Thus (5) is
positive for all required t. We have derived

    E(A)<=9n^2-8n.                                  (6)

Subtracting 2n^2-n in the exact energy identity gives

    T(A)<=7(n^2-n)/4=(7/2)M(A).                     (7)

Finally sum_d r_A(d)=M and sum_d r_A(d)^2=M+2T<=8M. The usual
positive-difference Cauchy estimate gives M^2<=8LM; dividing by
M>0 proves

    M(A)<=8 span(A).                                (8)

The statement continues to hold whenever F_Q admits a two-Golomb
partition, even if that premise is supplied without a full source
coloring. It says nothing about filling missing layers or completing
an arbitrary partial product. The general S21 and small-color goals
remain open despite this improvement on the complete class.
