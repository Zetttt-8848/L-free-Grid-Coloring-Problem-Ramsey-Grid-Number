# A dyadic source condition sufficient for S21

Root derivation, checkpoint 0019. The dyadic hypothesis below is open.
This note derives a new sufficient implication without assuming a global
constant additive-energy bound. It does not change the Ramsey bounds.

For a finite integer source A set L=span(A), M=binom(|A|,2),
r(h)=|A intersect (A-h)|, and T_H=sum_{H<=h<2H} binom(r(h),2),
where r(h)=0 outside 1<=h<=L. Consider the following hypothesis:

    D1: if V(A) has a proper two-coloring, then T_H<=M
        for every H that is a positive power of two.          (1)

Unlike H10, (1) permits total energy growing with the number of dyadic
scales. It asserts a uniform budget at one scale only. Properness refers
to one coloring of the entire strict source triangle, not a Cartesian
rectangle, and not independently colored fibers.

## 1. Difference mass from the scale budgets

Assume (1), and suppose L>=1 and M>0. Let 2^J<=L<2^(J+1).
Partition the positive integer differences through L into dyadic bands

    I_j={2^j,...,2^(j+1)-1}, 0<=j<J,
    I_J={2^J,...,L}.

Write n_j=|I_j| and X_j=sum_{h in I_j} r(h). Then

    sum_j X_j=M,
    sum_{h in I_j} r(h)^2=2T_{2^j}+X_j<=2M+X_j<=3M.   (2)

Cauchy--Schwarz in each band gives X_j<=sqrt(3M n_j). Adding,

    M<=sqrt(3M) sum_j sqrt(n_j).                      (3)

Put q=2^J and a=L-q+1, so that 1<=a<=q. The geometric sum is

    sum_j sqrt(n_j)
      = (sqrt(q)-1)/(sqrt(2)-1)+sqrt(a)
      = (1+sqrt(2))(sqrt(q)-1)+sqrt(a).               (4)

We need an estimate respecting the integer endpoint in a. Since
sqrt(q)-1<=sqrt(q-1) for q>=1, another Cauchy--Schwarz inequality yields

    [(1+sqrt(2))(sqrt(q)-1)+sqrt(a)]^2
      <=[(1+sqrt(2))sqrt(q-1)+sqrt(a)]^2
      <=[(1+sqrt(2))^2+1][q-1+a]
      =(4+2sqrt(2))L.                               (5)

The first inequality is valid because both sides before squaring are
nonnegative. Combining (3) and (5), and dividing by M>0, proves

    M<=(12+6sqrt(2))L<21L.                          (6)

For the last strict comparison, sqrt(2)<3/2, so 12+6sqrt(2)<21.
Empty and singleton sources have M=0, and L=0 permits at most one mark.
Thus all cases are covered.

## 2. Consequence and research scope

The implication D1 => M<=(12+6sqrt(2))span(A) is unconditional as a
conditional theorem: its only unproved premise is D1 itself. In
particular D1, or just its restriction to spans at most 99994, implies
S21 of FINITE_SOURCE_SIZE_TARGET_0018.md. That note then supplies the
complete conditional small-color transfers R3<=379 and R4<=99996.

This scale route does not require T(A)<=10M(A). Its source-size deduction
uses the lengths of the bands, rather than summing their energy budgets
and losing one factor for every scale. A proof of D1 is still missing;
the derivation above is not itself a proved improvement or an established
original superior method.

## 3. A more generous single-scale budget is sufficient

The linear term X_j in (2) need not be replaced by M separately in
each band. Retaining it allows the weaker hypothesis

    D(7/5): T_H<=(7/5)M for every dyadic H.           (7)

We show directly that (7) implies M<21L whenever M,L are positive.
Suppose, to obtain a contradiction, that M>=21L. Cauchy--Schwarz and
(7) give

    X_j^2<=n_j[(14/5)M+X_j],

and solving this quadratic for its nonnegative root gives

    X_j<=n_j/2+sqrt(n_j^2/4+(14/5)M n_j).            (8)

Since n_j<=L<=M/21, the expression inside the square root is at most

    (1/84+14/5)M n_j < (17/6)M n_j.                 (9)

Indeed 1/84+14/5=1181/420<1190/420=17/6. Summing (8) and applying
(5), together with 4+2sqrt(2)<7, yields

    M<L/2+sqrt((119/6)ML)
      <=M/42+M sqrt(119/126)
      =M[1/42+sqrt(17/18)]<M.                       (10)

The last comparison follows by squaring positive numbers:

    17/18=1666/1764 <1681/1764=(41/42)^2.

This contradiction proves the claimed source-size conclusion. Thus even
the single-band budget (7), which is forty percent larger than D1, would
suffice for S21 and the already derived small-color transfers. The
budget (7) is open too; its value is a less restrictive source-color
inequality to pursue. This refinement still assumes one proper coloring
on the whole source triangle and asserts no unconditional Ramsey bound.

## 4. Discovery scope

The bounded observations in fibers/SOURCE_DYADIC_PROFILE_0019.json use
stored proper-source records as discovery inputs. They do not prove D1.
One stored candidate has T_H/M=29/36 at H=4, so the earlier coefficient
3/5 is not a viable target on those records. No raw candidate in that
bounded run exceeded coefficient one. No independent checking pass was
conducted or used as a theorem premise.
