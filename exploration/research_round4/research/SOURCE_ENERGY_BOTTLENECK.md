# A source-energy implication sufficient for both small-color targets

Root derivation, R4-RESEARCH-0009, continuing R4-RESEARCH-0008.

**The energy hypothesis in this note is unproved.** The proved results are
its conditional consequences and the explicit construction in section 4.
No numerical Ramsey improvement is asserted.

Checkpoint-0011 priority: FINITE_SOURCE_SIZE_TARGET.md states the weaker
finite-span size assertion actually used by the transfers below. A proof
of that assertion would suffice without proving global H(5).
PROPERNESS_ESSENTIAL.md refutes universal arbitrary-sign row/column
correlation bounds and all universal linear supersaturation inequalities
B>=aT-bM with a>0. The examples are not proper and do not refute H(5).

Checkpoint-0010 additions: CONSTANT_WEIGHT_SOURCES.md and
fibers/WEIGHT_TWO_LAYER.md prove a uniform properly two-colored family
with T/M=2-8/(r+1). Thus any constant in (H) must be at least 2,
strengthening the finite lower constraint in section 4. Neither H(2)
nor H(5) is proved. SQUARE_ENERGY_GROWTH.md proves that square sources
have T/M tending to infinity, but their uniform two-colorability is
unresolved. That result is a stress test, not a counterexample to (H).

## 1. The precise missing statement

For a finite integer set A define

    m=|A|,  M(A)=binom(m,2),
    r_A(d)=|A intersect (A-d)|,       d>0,
    T(A)=sum_(d>0) binom(r_A(d),2).

Here T(A) is the number of directed corners in the strict completion
triangle on A, regardless of color. To distinguish this number from the
region, write V(A)={(v,u):u,v in A, u<v} in this note.

For a real kappa>=0, consider the following hypothesis:

    H(kappa): if V(A) has a proper two-coloring, then
              T(A)<=kappa M(A), for every finite integer A.      (H)

Neither H(2) nor H(5) is proved here. H(5) alone would be sufficient for
both requested strict small-color improvements. Proving (H) is the hard
step; the elementary deductions below do not replace that step. For the
specific H(5) application, it would suffice to prove the assertion for
sources of span at most 91998. This finite-range variant is also unproved.

The additive energy in ordered-quadruple notation is

    E(A)=#{(a,b,c,d) in A^4:a-b=c-d}
        =m^2+2 sum_(h>0)r_A(h)^2
        =2m^2-m+4T(A).

Thus (H) is equivalent to

    E(A)<=(2+2kappa)m^2-(1+2kappa)m.                    (1)

It is a uniform bound on total additive energy, not a bound on the
largest individual difference fiber or on the number of corners forced
at one cell. The latter quantities may be large.
UNBOUNDED_COMPLETION_LOAD.md proves a uniform construction with forcing
load 2q-2 at one cell and total ratio T(A)/M(A)<1/2. Thus no fixed
pointwise load bound can be substituted for the global hypothesis.

## 2. A proved consequence for the size of a two-color source

**Proposition 1 (conditional on H(kappa)).** Put b=2kappa+1. If A has
span L and V(A) is properly two-colored, then

    binom(|A|,2)<=b L,                                  (2)
    |A|<=1+sqrt(2bL).                                   (3)

For L=0, A has at most one element, so both statements hold. For L>0,
there are at most L positive distance positions and

    sum_(d=1)^L r_A(d)=M(A),
    sum_(d=1)^L r_A(d)^2=2T(A)+M(A)<=bM(A).

Cauchy--Schwarz gives M(A)^2<=L bM(A). For M(A)>0, division proves
(2); for M(A)=0 it is immediate. Finally, writing m=|A|, the inequality
m(m-1)<=2bL and (m-1)^2<=m(m-1) prove (3).

## 3. Complete conditional transfer to R3 and R4

A monochromatic main-diagonal set A in a proper k-color grid forces
every cell (v,u), u<v in A, to avoid that diagonal color: otherwise
(u,u),(v,u),(v,v) is a monochromatic directed corner. Thus V(A) has a
proper coloring in at most k-1 colors.

**Proposition 2.** H(5) implies

    R3<=201,            R4<=92000.                      (4)

**Proof for R3.** Suppose a proper three-color grid has side 201. One
main-diagonal color occurs at least 67 times. Its source A has span at
most 200 and a proper two-color strict triangle. Proposition 1, with
kappa=5 and b=11, would give

    binom(67,2)=2211 <= 11*200=2200,

which is a contradiction.

**Proof for R4.** Suppose a proper four-color grid has side N, and let
A be a main-diagonal color class of size at least ceil(N/4). Its strict
triangle uses at most three colors. For each d>0 partition F_d=A
intersect (A-d) according to the color of the cells (u+d,u).

For each such color class B, all cells (v+d,u), u<v in B, avoid that
color. They form a translated proper two-color copy of V(B). Translation
of the first coordinate by d preserves directed corners. The starts in
B lie in an interval of span at most N-1-d. Under H(kappa), (3) therefore
gives

    r_A(d)<=3[1+sqrt(2b(N-1-d))].                      (5)

This upper bound is permitted even when a color class is empty. Summing
(5), and using that sqrt(x) is increasing, yields

    M(A)<=3(N-1)+3sqrt(2b) sum_(l=0)^(N-2) sqrt(l)
         <=3(N-1)+2sqrt(2b)(N-1)^(3/2)
         =(N-1)[3+2sqrt(2b(N-1))].                     (6)

For the integral estimate, sqrt(l)<=integral_l^(l+1) sqrt(x) dx;
adding and evaluating the integral gives the displayed bound.

Take b=11 and N=92000. Since

    22*91999=2023978 < 1423^2=2024929,

the right side of (6) is less than

    91999*(3+2*1423)=262105151.

But |A|>=23000 gives

    M(A)>=binom(23000,2)=264488500.

The difference is 2383349, so the two inequalities contradict each
other. This proves the conditional R4 statement.

For comparison, the stronger unproved hypothesis H(2), with b=5,
would imply

    R3<=93,             R4<=41200.                     (7)

For R3 use binom(31,2)=465>5*92=460. For R4 use (6) and

    10*41199=411990<642^2=412164,
    41199*(3+2*642)=53023113
      <binom(10300,2)=53039850.

All numerical statements (4) and (7) remain explicitly conditional.
The general polynomial-exponent growth bound already established from
the cited density theorem does not prove either energy hypothesis.

## 4. A literal counterexample to smaller energy constants

Let

    A={0,1,3,4,6,7,8,10,11,13}.

In the following full coloring, each row lists its colors at all smaller
source marks, in increasing order. The row label is its first coordinate.

| row | colors |
|---:|:---|
| 1 | 0 |
| 3 | 00 |
| 4 | 100 |
| 6 | 1100 |
| 7 | 01111 |
| 8 | 010101 |
| 10 | 0010011 |
| 11 | 10101010 |
| 13 | 111100001 |

Here is a complete proof that the coloring is proper. For each nonempty
group of at least two equal-color cells on offset d, the table lists their
starts and the colors of their completions. Within a start list, use the
lexicographic order of its increasing pairs. The completion of starts
u<v is (v+d,u).

| d | endpoint color | starts | completion colors |
|---:|---:|:---|:---|
| 1 | 0 | 0,3,10 | 1,1,1 |
| 1 | 1 | 6,7 | 0 |
| 2 | 0 | 1,4,6 | 1,1,1 |
| 2 | 1 | 8,11 | 0 |
| 3 | 0 | 0,1,3,10 | 1,1,1,1,1,1 |
| 3 | 1 | 4,7,8 | 0,0,0 |
| 4 | 0 | 6,7 | 1 |
| 4 | 1 | 0,3,4 | 0,0,0 |
| 5 | 0 | 3,8 | 1 |
| 5 | 1 | 1,6 | 0 |
| 6 | 0 | 4,7 | 1 |
| 6 | 1 | 0,1 | 0 |
| 7 | 0 | 0,4,6 | 1,1,1 |
| 7 | 1 | 1,3 | 0 |
| 10 | 0 | 0,1 | 1 |

At offsets 8 and 9 the two endpoint colors differ. At offsets 11,12,13
there is just one cell; at offset 10 the remaining color occurs once.
The table and those singleton statements list every possible equal-color
endpoint pair. Every completion has the opposite color, so every directed
corner is nonmonochromatic.

The complete positive-distance profile, for d=1,...,13, is

    (5,5,7,5,4,4,5,2,2,3,1,1,1).

Its sum is 45=binom(10,2). Therefore the corner count is

    T(A)=4*binom(5,2)+binom(7,2)+2*binom(4,2)
          +2*binom(2,2)+binom(3,2)
        =40+21+12+2+3=78.

Consequently any valid universal kappa in (H) must satisfy

    kappa>=78/45=26/15.                                (8)

In particular, H(1) and H(3/2) are false. This is a full literal
construction proof, not an inference from a negative search status.

## 5. What the executed searches do and do not show

source_energy_probe.py discovered the preceding coloring. Its returned
objective and optimality status are not used to assert an extremal
optimum. The explicit array and proof above are the evidence for (8).

The coefficient-two CP runs at sides 22 and 30 ended with only a
one-mark incumbent and positive unresolved objective bounds. They did
not settle H(2), even on those intervals. The separate
source_energy_sampling run made 338 high-energy coloring calls among
1000 sampled sources and found no positive witness. The cube_energy_probe
made 832 high-energy calls among 1500 sampled subsets of separated cubes
and also found none. Their raw negatives are not theorems and give no
uniform energy bound. No separate verification process was opened.

A small preliminary cube call found a coloring at dimension four and
raw negatives at dimensions five and six. Those outcomes were used only
to choose the subsequent subset experiment; no universal cube exclusion
or dimension-four construction theorem is claimed here.

The known product construction is analyzed exactly in
fibers/PRODUCT_CUT_STRUCTURE.md. Its row and column graphs are bipartite
subdivisions, so a positive lower bound for their cut deficits cannot be
inferred from the number of source marks alone. Density or a different
global invariant must enter. That construction does not refute (H).
The same product graph contains induced stars of arbitrarily large
degree. The explicit Rayleigh vector in that note proves that even
properly two-colored sources have unboundedly negative least adjacency
eigenvalues. Thus a constant unweighted spectral shift cannot prove
(H); an energy proof must retain the actual sign assignments or use a
different, justified inequality.

## 6. The next mathematical task

The strongest useful next step is a proof or an explicit counterexample
to H(5), with H(2) a stronger optional target. Repeating failed finite
searches is not evidence for either statement. A purported proof must
control total source energy while keeping the completion colors shared
between different fibers; isolated Golomb caps do not supply (1).

The conditional reduction makes the requested R3 and R4 thresholds
depend on one common implication. It does not constitute the requested
original superior method until that implication has a complete proof.
