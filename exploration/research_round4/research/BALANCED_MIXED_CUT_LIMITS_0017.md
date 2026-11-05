# Two limitations of a mixed-energy shortcut at a balanced cut

Root exploratory derivation, checkpoint R4-RESEARCH-0017. These examples
concern proposed intermediate inequalities, not new Ramsey bounds.

For separated finite sources B<C write b=|B|, c=|C|,

    q(h)=#{(u,v) in B x C:v-u=h},
    U=sum_(h>0) r_B(h)r_C(h),
    V=sum_(h>0) [r_B(h)+r_C(h)]q(h).

The exact identity from CARTESIAN_SOURCE_TRANSFER_0016.md is

    T(B union C)-T(B)-T(C)=2U+V.                    (1)

Thus a bound for V would help convert a Cartesian bound on U into a
source-energy bound. The two tempting shortcuts below have different
scopes, and both fail.

## 1. V<=bc fails even on a balanced cut of a proper source

Use the literal proper ten-mark source already derived in
SOURCE_ENERGY_BOTTLENECK.md:

    B={0,1,3,4,6},       C=B+7,
    A=B union C.

The existing displayed coloring and its derivation are reused as an input;
they are not rechecked here. Both children have five marks. Their common
positive-difference profile, at h=1,...,6, is

    r_B=r_C=(2,2,3,1,1,1).

For the same six positions, q(h)=r_B(7-h), so

    (q(1),...,q(6))=(1,1,1,3,2,2).

Consequently the new mixed-cut quantity is

    V=2(2+2+3+3+2+2)=28>25=bc.                     (2)

This rules out the proposed balanced-cut V<=bc statement even with actual
proper source colors. The failure is not an unbalanced-endpoint effect.

## 2. V<=bc+U fails as a purely additive balanced-cut statement

This example is uncolored. It does not exclude a properness-specific
version of the inequality.

Let t>=1, m=6t, and take

    B={-2i:0<=i<m},      C={3j:1<=j<=m}.

These two sets are separated and both have m marks. A common positive
internal difference is 6h, with multiplicities m-3h and m-2h. Hence

    U=sum_(h=1)^(2t-1) (6t-3h)(6t-2h)
      =28t^3-18t^2+2t.                              (3)

For a difference 2h contributing to r_B, a cross representation is
3j+2i=2h. Write j=2k, so i=h-3k and k ranges from 1 to floor(h/3).
For 1<=h<m the upper constraints on i and j introduce no other bound.
The B part of V is therefore

    V_B=sum_(h=1)^(m-1)(m-h) floor(h/3)
       =sum_(k=0)^(2t-1) 3k(m-3k-1)
       =12t^3-6t^2.                                 (4)

For a difference 3h contributing to r_C, write i=3k. Then
j=h-2k>=1 and 0<=k<=2t-1. Thus

    q(3h)=min(ceil(h/2),2t),       1<=h<m.

Pairing h=2k-1,2k through h=4t, and summing the remaining tail, gives

    V_C=sum_(k=1)^(2t)(2m-4k+1)k + 2t^2(2t-1)
       =(52t^3)/3+4t^2-t/3.                         (5)

Equations (3)--(5) use only finite sums of first and second powers.
In particular,

    V-U-bc=t(4t^2-60t-7)/3.                          (6)

At t=16 this equals 304>0. The corresponding two 96-mark sets satisfy

    U=110112,       V=119632,       bc=9216,
    V-(U+bc)=304.

This is a direct counterexample to the uncolored V<=bc+U shortcut. Both
sets contain long common-step progressions, so this construction is not
presented as a proper two-color Cartesian example or a proper source.

Wolfram Language expanded the three defining finite sums once during the
new derivation. No subsequent checking pass was run.

## 3. Remaining scope

Neither example refutes a joint color-dependent bound on 2U+V, a suitable
choice of cut, or a transfer that retains the unused cut capacities.
In particular, the source-size target cannot be obtained merely by
asserting either shortcut above. The actual shared coloring must enter
any replacement beyond these purely additive calculations.
