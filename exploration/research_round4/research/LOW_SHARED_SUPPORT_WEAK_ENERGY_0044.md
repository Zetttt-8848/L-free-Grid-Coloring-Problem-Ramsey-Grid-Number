# Weak-source energy with an explicit shared-difference error

Root derivation, continuation0044. The earlier universal two-Golomb
estimate T(B union C)<=2M loses information when the within-class
difference supports barely meet. Keeping that overlap gives an exact
defect identity and the additional estimate T<=M+5rho. No source-size
or Ramsey improvement is asserted.

Let B,C be disjoint Golomb sets, b=|B|, c=|C|, S=B union C,
M=binom(b+c,2), and U=binom(b,2)+binom(c,2), so M=U+bc.
For h>0 use the established notation

    beta_h=1_(h in Delta B), gamma_h=1_(h in Delta C),
    x_h=|{u in B:u+h in C}|,
    y_h=|{u in C:u+h in B}|,
    D=Delta B intersect Delta C, rho=|D|.

The exact decomposition from TWO_GOLOMB_MIXED_ENERGY_0040.md is

    T(S)=2rho+N+Q,
    N=sum_h(beta_h+gamma_h)(x_h+y_h),
    Q=sum_h x_h y_h,
    sum_h(x_h+y_h)=bc,
    sum_h[binom(x_h,2)+binom(y_h,2)]=rho,
    Q<=U.                                             (1)

These are inputs, not objects for a separate verification pass.

## 1. An exact separation of the mixed queries

Define

    J=sum_(h in D)(x_h+y_h),
    Z=sum_(h not in Delta B union Delta C)(x_h+y_h).

The multiplier beta_h+gamma_h equals two on D, zero outside the
union, and one elsewhere. Thus the exact, not merely upper, formula is

    N=bc+J-Z.                                         (2)

Combining (1)-(2),

    T(S)=M+2rho+J-Z-(U-Q).                            (3)

Only queries at a shared length can exceed the baseline bc in N.

## 2. Paying those shared-length queries by collision resources

For each nonnegative integer k, put

    p(k)=binom(max(k-1,0),2).

Direct expansion for k>=1, with the k=0 case immediate, gives

    k=1_(k>0)+binom(k,2)-p(k).                       (4)

Define four nonnegative integers

    nu=sum_(h in D)[binom(x_h,2)+binom(y_h,2)],
    E=sum_(h in D)[2-1_(x_h>0)-1_(y_h>0)],
    P=sum_(h in D)[p(x_h)+p(y_h)],
    H=Z+(U-Q)+E+P.

The collision identity in (1) gives 0<=nu<=rho. Summing (4) in the
two orientations over D gives exactly

    J=2rho+nu-E-P.                                   (5)

Consequently the strengthened energy identity is

    T(S)=M+4rho+nu-H,       0<=nu<=rho, H>=0.          (6)

In particular,

    T(S)<=M+5rho,
    T(S)<=min(2M,M+5rho).                             (7)

The second line retains the completed universal H2 theorem as well.
Empty classes and rho=0 are included in these formulas.

There is a useful geometric interpretation of nu. A shared length
ell has a unique B-pair and C-pair. Their lower endpoints differ by
a nonzero displacement d. The bijection in (1) turns this shared
length into one same-orientation collision at mixed length d.
Thus nu counts those shared lengths whose displacement d is itself
in D. The other terms in H record wholly unsupported mixed queries,
unused same-class pair-sum resources, missing mixed orientations at
shared lengths, and the excess collision cost when an orientation
has three or more starts. No injectivity of the displacement map is
claimed.

## 3. The case of disjoint within-class difference supports

When rho=0, both x_h and y_h are at most one for every h, by (1).
Also beta_h+gamma_h<=1. Formula (6) specializes to the sharper exact
identity

    T(S)=M-Z-(U-Q)<=M.                               (8)

Equivalently,

    E_add(S)=2|S|^2-|S|+4T(S)
             <=4|S|^2-3|S|.                         (9)

Here E_add denotes ordinary ordered additive energy, distinguished
from the orientation-deficit symbol E above. This is a theorem about
two Golomb classes with disjoint positive difference supports. It
applies to a proper weak source with those actual diagonal classes.
It does not assert that an arbitrary strict source has such a
two-class partition.

More generally, (7) gives a quantitative alternative: for any real
alpha>0,

    T(S)>(1+alpha)M  implies  rho>alpha M/5.           (10)

This alternative uses the additional shared-difference resource
only when the weak energy exceeds the H1 baseline.

## 4. The simultaneous strict-source moment condition

Let A have a proper two-color strict source triangle. For its actual
weak fibers F_d=B_d disjoint union C_d, define

    R(A)=sum_d rho_d,
    T(A)=sum_d binom(|F_d|,2),
    K_3(A)=sum_d T(F_d).

Summing (6) yields the exact colored moment identity

    K_3(A)=T(A)+4R(A)+sum_d nu_d-sum_d H_d.           (11)

In particular,

    K_3(A)<=min(2T(A),T(A)+5R(A)).                   (12)

Thus if all rho_d vanish, K_3(A)<=T(A). This does not imply K_3=0:
SHARED_DIFFERENCE_FREE_THREE_CUBE_0044.md supplies a proper family
with R(A)=0, T(A)=24, and K_3(A)=6.

For windows A_u=A intersect[u,u+t-1], define

    R^(t)(A)=sum_u R(A_u).

The restrictions use the inherited actual colors. Applying (12) to
them gives

    K_3^(t)(A)<=K_2^(t)(A)+5R^(t)(A),
    K_3^(t)(A)<=2K_2^(t)(A).                         (13)

A shared h-pair in the d-fiber, with pair-start displacement p,
uses starts of total span h+p; including their d-translates makes
the whole span d+h+p. Therefore R^(t) is explicitly the sum of
(t-d-h-p)_+ over these actual colored shared-pair incidences.
It is not an independently optimized weak-fiber partition, and it
is not a scalar multiple of the unweighted R(A).

## 5. The main gap retained

The interlaced-pair theorem pays activated shared lengths by units
and holes. The present result identifies a complementary range:
few shared lengths force the weaker upper moment K_3<=T+5R.
Together these distinguish low shared support from large shared
support without calling either range impossible.

What is missing is a lower estimate, or a different actual-color
constraint, connecting these alternatives to M(A)/span(A). The
already recorded uncolored sources with Golomb overlaps and growing
T/M obey even K_3=0, although their properness is not established.
They show why the numerical moment inequality alone cannot close
the general source-energy target. None of (7)-(13) proves S21,
F11(5), F12(7), or a new R4 bound.
