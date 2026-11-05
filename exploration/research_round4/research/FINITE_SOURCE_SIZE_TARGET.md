# The weaker finite-span target actually needed for the small colors

Root research target, continuing R4-RESEARCH-0010. The size assertion
below is unproved. This note distinguishes it from a stronger global
energy conjecture, so work can target the required implication directly.

For a finite integer source A, write L=max A-min A and
M(A)=binom(|A|,2). For empty A set L=0. Consider

    S_11: if V(A) has a proper two-coloring and L<=91998,
          then M(A)<=11 L.                           (S)

S_11 implies R3<=201 and R4<=92000. Both are conditional numbers.

The H(5) conjecture from SOURCE_ENERGY_BOTTLENECK.md would imply
(S) by Cauchy--Schwarz applied to the positive difference counts.
The proofs transferring to the grid need only (S), not H(5).

Here are the transfers explicitly. From (S),

    |A|<=1+sqrt(22L),                                (1)

For nonempty A this follows from (|A|-1)^2<=|A|(|A|-1)<=22L;
the empty case is immediate. A putative proper three-color
grid of side 201 has a main-diagonal color class A with |A|>=67.
Its strict triangle avoids that color and has two colors, with L<=200.
But M(A)>=binom(67,2)=2211>11*200=2200, contrary to (S).

For a putative proper four-color grid of side N=92000, a main-diagonal
class A has at least 23000 marks. On V(A) there are at most three
remaining colors. Partition every difference fiber A intersect (A-d)
by its cell color. Each part B forces a translated proper two-color
triangle on B and has span at most N-1-d<=91998. Formula (1) gives

    |A intersect (A-d)|<=3[1+sqrt(22(N-1-d))].

Summing over d=1,...,N-1 and bounding the increasing square-root sum
by its integral gives

    M(A)<=(N-1)[3+2sqrt(22(N-1))].                    (2)

At N=92000, 22*91999=2023978<1423^2=2024929. Thus the right side
of (2) is less than 91999*2849=262105151. On the other hand,
M(A)>=binom(23000,2)=264488500, a contradiction.

This proof uses (S) only in its stated finite range. A source-size
estimate with a different formula could also suffice if substituted
into the same fiber sum; (S) is not claimed necessary or optimal.

## What the recent counterexamples do and do not change

The square-source corner/energy ratio tends to infinity, but its
size-to-span ratio remains small: for A_m={1^2,...,m^2}, m>=2,

    M(A_m)/span(A_m)=m/[2(m+1)]<1/2.

Consequently these sources satisfy the numerical conclusion of (S)
irrespective of their colorability. They stress-test global H(kappa)
but cannot refute (S).

The Boolean-cube signs in PROPERNESS_ESSENTIAL.md refute universal
arbitrary-color sign bounds and linear supersaturation estimates.
They are not proper, and do not refute (S) either. Conversely, none
of these limitations supplies a proof of (S).

The next hard implication should use source span and the actual local
properness restrictions together. Proving a global energy bound on
all spans, or classifying every square-source coloring, is stronger
than what is required for the stated small-color transfer.
