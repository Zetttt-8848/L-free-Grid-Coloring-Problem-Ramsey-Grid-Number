# Energy of a source with a perfect translation matching

Root derivation, continuing CHECKPOINT_0033. This extends the earlier
complete-product estimates to disjoint double translates with arbitrary
collisions between their numerical difference ranges. It is a class
theorem, not a theorem for every source and not an unconditional Ramsey
improvement.

For a finite integer set X, let

    r_X(t)=|{(x,y) in X^2:x-y=t}|,
    E(X)=sum_t r_X(t)^2.

For a source A put m=|A|, M=binom(m,2), L=span(A), and
T=sum_(t>0) binom(r_A(t),2). The inherited identity is

    E(A)=2m^2-m+4T.                                    (1)

## 1. Statement

**Paired-source theorem.** Suppose that V(A) is properly two-colored
and that, for some integer d>0 and finite S,

    A=S disjoint union (S+d).                          (2)

Then

    T(A)<=10M(A),
    M(A)<=21 span(A).                                  (3)

There is no assumption that d exceeds span(S), that the source has
separated clusters, or that differences of S avoid coincidences after
shifts by d or 2d. Disjointness in (2) concerns marks only.

## 2. Shifted energy of one Golomb set

Let B be Golomb, b=|B|>=1, and define, for h>0,

    C_h(B)=sum_t r_B(t) r_B(t+h).                       (4)

Its signed nonzero difference set D has b(b-1) elements, each of
multiplicity one, while r_B(0)=b. Consequently

    E(B)=2b^2-b.                                       (5)

If h is not a difference of B, neither t=0 nor t=-h contributes
to (4), and all remaining products are zero or one. Thus

    C_h(B)<=b(b-1)  when r_B(h)=0.                     (6)

If r_B(h)=1, the terms t=0,-h together contribute 2b. Among t in D,
the value -h is excluded from the remaining count, and so is max D,
since max D+h is outside D. These are distinct. Hence

    C_h(B)<=2b+b(b-1)-2=b^2+b-2.                       (7)

The right side of (7) also bounds (6), since their difference is
2b-2>=0. In particular (7) holds for every h>0. For b=1 both sides
of (4) vanish and the upper bound in (7) is zero.

Assume now that B and B+d are disjoint, and put P=B union (B+d).
Its indicator is the sum of the two translate indicators, so

    r_P(t)=2r_B(t)+r_B(t-d)+r_B(t+d).

Squaring and summing gives the exact identity

    E(P)=6E(B)+8C_d(B)+2C_(2d)(B).                     (8)

Disjointness implies r_B(d)=0. Substituting (5)-(7) into (8) yields

    E(P)<=6(2b^2-b)+8(b^2-b)+2(b^2+b-2)
         =22b^2-12b-4.                                (9)

All near-difference collisions are retained in C_d and C_(2d).
Unlike an exact no-carry factorization, (8) remains valid when these
terms are nonzero.

## 3. The actual source coloring partitions the matching starts

For each x in S, the cell (x+d,x) is in V(A). Partition S into B and C
according to these two actual cell colors. Both B and C are Golomb:
this is the inherited signed-fiber property, since S is a subset of
F_d=A intersect (A-d). It is not necessary that F_d equal S.

Write b=|B|, c=|C|, s=b+c, so m=2s. The four sets B,C,B+d,C+d are
pairwise disjoint. Put

    P_B=B union (B+d),  P_C=C union (C+d),
    A=P_B disjoint union P_C.                         (10)

For finite sets X,Y, additive energy obeys

    E(X disjoint union Y)^(1/4)
        <=E(X)^(1/4)+E(Y)^(1/4).                      (11)

For completeness, let f_X(theta)=sum_(x in X) exp(2 pi i x theta).
Orthogonality on [0,1] gives E(X)=integral |f_X|^4. Disjointness gives
f_(X union Y)=f_X+f_Y, and the L4 triangle inequality gives (11).
This is the same energy-norm inequality used in the earlier product
derivations, now applied to the two actual signed matching classes.

Suppose first that b,c>=1. Define

    g(t)=22t^2-12t-4,  f(t)=g(t)^(1/4),  t>=1.

The function f is concave. Indeed its second derivative has the sign
of

    4g(t)g''(t)-3g'(t)^2
       =-1936(t-3/11)^2-992<0.                        (12)

Equations (9)-(12) and concavity therefore give

    E(A)^(1/4)<=f(b)+f(c)<=2f(s/2),
    E(A)<=16g(s/2)=88s^2-96s-64
                   =22m^2-48m-64.                    (13)

If one signed class is empty and s>=1, (9) directly gives

    E(A)<=22s^2-12s-4=(11/2)m^2-6m-4.                 (14)

For m>=2, the upper bounds in both (13) and (14) are at most
22m^2-21m. In the second case, the difference is

    (33/2)m^2-15m+4>0;

for example m>=2 makes (33/2)m-15 positive. The empty source is
immediate. Thus, uniformly,

    E(A)<=22m^2-21m.                                  (15)

Using (1),

    4T<=20m^2-20m,
    T<=5m(m-1)=10M.

Finally sum_(t>0) r_A(t)=M and there are at most L positive offsets.
For M>0, Cauchy-Schwarz and the preceding bound give

    M^2<=L sum_(t>0) r_A(t)^2
        =L(M+2T)<=21LM.

Dividing by M proves the second assertion of (3). For M=0 it is
automatic. This completes the derivation.

## 4. Exact combinatorial scope

For fixed d>0, join two marks of A when their difference is d. Every
component is a path along one residue class modulo d. Such a component
has a perfect matching exactly when its number of marks is even: a
path's first vertex must be paired with its next vertex, and iteration
both proves necessity and constructs the matching in the even case.

Therefore condition (2) is equivalent to every component of this
step-d graph having even cardinality. The set S consists of the lower
endpoints of its matched edges. In particular, every source whose
ordinary consecutive runs all have even length satisfies the theorem
by taking d=1.

This includes sources with interlaced matching starts and many
coincidences between shifted numerical differences. It does not imply
that an arbitrary source has such a perfect matching. Odd components
leave unmatched marks; simply discarding those marks cannot prove a
bound for the original source. No residual estimate closing that gap
is supplied here.

The theorem establishes the S21 conclusion on this entire class at
every span. Applying the existing S21-to-Ramsey transfer to arbitrary
grid diagonal classes would still require a general source theorem;
the matching hypothesis has not been proved for those classes.

## 5. Comparison with the simpler cardinality estimate on this class

The new content above is an energy estimate in the presence of arbitrary
shifted-difference collisions. Its source-size consequence on perfectly
matched sources is not a stronger cardinality estimate than the basic
signed-Golomb count. This distinction matters for the main research goal.

Indeed B,C in Section 3 lie in an interval of span at most L-d<=L-1.
Counting their distinct positive differences separately gives

    b,c <= (1+sqrt(8L-7))/2,
    s<=1+sqrt(8L-7).

Since m=2s and s(2s-1) is increasing for s>=1,

    M(A)<=16L-13+3sqrt(8L-7)<18L.                      (16)

The last inequality follows from positivity of 2L+13 and

    (2L+13)^2-9(8L-7)=4L^2-20L+232
                         =4(L-5/2)^2+207>0.

Here L>=1 for a nonempty paired source. Thus perfect matching already
permits an S21 cardinality conclusion through this simpler argument.
The energy theorem does not resolve why an arbitrary source should
behave similarly, and its wider product scope must not be presented
as a new unconditional small-color improvement.
