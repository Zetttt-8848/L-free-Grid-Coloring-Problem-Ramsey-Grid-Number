# A single-exponential general bound from the 2025 corners theorem

Base: R4-RESEARCH-0001. Author: root. This is a complete deduction from a cited published theorem, not a claim of an original corners-density theorem. All logarithms are natural.

## External input

Jaber, Liu, Lovett, Ostuni and Sawhney, *Quasipolynomial bounds for the corners theorem*, arXiv:2504.07006v1 (9 April 2025), Theorem 1.1, prove that an absolute constant c>0 exists such that, for every finite abelian group G and every set S in G^2 without a triple (a,b),(a+d,b),(a,b+d), d nonzero in G,

|S| <= |G|^2 exp(-c (log |G|)^(1/600)).

Primary source: https://arxiv.org/html/2504.07006v1 . The theorem is in Section 1 immediately before the paragraph discussing integer embeddings and positive steps. The argument below supplies its own elementary orientation and embedding steps; it does not need the additional positive-step result mentioned there. The input theorem's proof is credited to those authors and is not re-proved here.

## Proposition: two orientations can be handled by paired colors

Suppose f:[N]^2 -> [k] has no positive standard corner, meaning no monochromatic {(a,b),(a+d,b),(a,b+d)} with d>0. Define J(a,b)=(N+1-a,N+1-b), and give each point p the ordered pair of colors (f(p),f(Jp)). Then every class of this coloring is free of standard corners with either sign of a nonzero integer d.

Proof. A positive corner in a paired-color class would be monochromatic for its first component f. If d<0, apply J to the three points. Their images are (N+1-a,N+1-b), (N+1-a-d,N+1-b), and (N+1-a,N+1-b-d). They form a positive corner of step -d. They have equal f-colors because the original points have equal second components. Each conclusion contradicts the hypothesis. J preserves the square, so no boundary extension is involved.

## Proposition: an embedding without wraparound

Let S be a signed-standard-corner-free subset of [N]^2. Its coordinatewise image in G^2, for G=Z/(2N)Z, is corner-free in the group sense.

Proof. The coordinate map is injective on [N]. Suppose a group corner lies in the image. Equality of its second coordinates identifies two representatives as (a,b),(a',b); equality of its first coordinates identifies the third as (a,b'). Let h=a'-a and t=b'-b. Then h and t lie between -(N-1) and N-1, and h=t modulo 2N. Since |h-t|<=2N-2<2N, they are equal integers. The group step is nonzero, so h is nonzero. These representatives are a forbidden signed corner in S.

## Theorem: directed L bound

For every integer k>=1, with c any constant valid in the external input, put

B(k) = ceil(exp((c^(-1) log(8k^2))^600)).

Then R_k(L) <= B(k), where L is {(x,y),(x+d,y),(x+d,y+d)}, d>0.

Proof. Set N=B(k), and suppose a corner-free k-coloring chi of [N]^2 exists. The reflection H(x,y)=(N+1-x,y) sends an L of step d to a positive standard corner: its three images are (N+1-x,y), (N+1-x-d,y), and (N+1-x-d,y+d), with base (N+1-x-d,y). Conversely a positive standard corner reflects to an L. Thus f=chi composed with H has no positive standard corner.

The paired-color proposition gives a coloring with at most k^2 classes, each signed-corner-free. One class S has |S|>=N^2/k^2. Embed it in G^2 with |G|=2N by the preceding proposition. The external theorem yields

N^2/k^2 <= |S| <= 4N^2 exp(-c(log(2N))^(1/600)).

The definition of N implies log(2N)>=(c^(-1)log(8k^2))^600. Hence the rightmost expression is at most 4N^2/(8k^2)=N^2/(2k^2), strictly below the leftmost expression. This is a contradiction.

## Required growth form and comparison

Because 8k^2 <= (2k)^3 for k>=1, the same proof gives

R_k(L) <= ceil(exp(C (log(2k))^600)), where C=(3/c)^600.

This exponent has no exponential dependence on k. If a literal polynomial exponent is desired, log(2k)<=k for k>=1: the function t-log(2t) has derivative 1-1/t>=0 on [1,infinity), and its value at 1 is positive. Consequently

R_k(L) <= ceil(exp(C k^600)) <= exp((C+log 2) k^600).

The final inequality uses ceil(x)<=2x for x>=1 and k^600>=1. Thus it is also a bound of the requested form D^(k^600), with D=exp(C+log 2) an absolute constant.

This is asymptotically strictly smaller than the prior [k(k-2)-1]^(2^(k-1)) bound. Its logarithm is at most C(log(2k))^600+log 2, whereas the old logarithm is 2^(k-1)log(k(k-2)-1). For k>=6 the latter is at least 2^(k-1). Also log(2k)<=k and k^600/2^k tends to zero: the ratio of consecutive terms is (1+1/k)^600/2, which tends to 1/2 and is eventually less than 3/4. The ratio of the new logarithmic upper bound to the old logarithm therefore tends to zero.

## Scope and originality

The general growth target is established as a corollary of the 2025 theorem with the complete transfer proof above. The absolute constant is not numerically specified in Theorem 1.1, so this deduction supplies no usable numerical improvement for R3 or R4. It must not be advertised as an explicit small-color bound or as an original replacement for the authors' method. The paired-color orientation argument is elementary, and no priority claim is made for it. The original-method and small-color objectives remain open in this campaign.
