# Nested forcing loads in a reflected Golomb source

This is a new construction analysis for a proposed source-energy route.
It refutes a constant global squared-forcing-load bound, even with actual
properness. The construction has small total corner energy and does not
refute H10 or S21.

## 1. Source and coloring

Let P={p_0<...<p_(r-1)} be a Golomb set of nonnegative integers with
p_0=0 and span l. Choose an integer D>4l and put

    A=P disjoint union (D-P).

The lower copy is P and the upper copy is D-P. Color a cell of V(A)
by the following rule:

    within either copy:                   0;
    cross cell (D-p_j,p_i), i=j:           1;
    cross cell (D-p_j,p_i), i!=j:          0.       (1)

All cross cells have the displayed strict orientation. Denote the matched
cross cell by Q_i=(D-p_i,p_i).

## 2. Exhaustive difference types and properness

A Golomb set has unique unordered pair sums, including repeated marks.
Two different distinct-pair representations of a sum give a repeated
positive difference; a relation a+b=2c gives the repeated difference
c-a=b-c. Thus all sums p_i+p_j with i<=j are distinct.

Every within-copy positive difference has the form h=p_j-p_i, i<j.
It has exactly two representations in A:

    p_i -> p_j,       D-p_j -> D-p_i.              (2)

Their starts are ordered as shown. Their unique corner has outer
completion Q_i, so its colors in original corner order are (0,1,0).

Every cross difference has the form d=D-p_i-p_j. The separation
D>4l puts all these differences above every within-copy difference.
Uniqueness of unordered pair sums gives exactly two representations
when i<j:

    p_i -> D-p_j,     p_j -> D-p_i.                (3)

These again complete at Q_i, and their colors are again (0,1,0).
When i=j, the difference D-2p_i has just one representation and creates
no corner. Equations (2)--(3) exhaust all positive differences and hence
all corners of the strict source. This proves that (1) is proper for
every choice of P,D under the stated hypotheses.

In particular every corner is a forcing corner: its two equal-offset
endpoint cells have the same color and its outer completion has the
opposite color.

## 3. Complete forcing-load profile

For an actual cell q, let H_q count equal-color endpoint pairs whose
outer completion is q. For every j>i, (2) contributes one to H_(Q_i)
and (3) contributes one more. No corner completes elsewhere. Therefore

    H_(Q_i)=2(r-1-i),  0<=i<r,
    H_q=0 for all other q.                         (4)

The number of cells and total corners are

    M=binom(2r,2)=r(2r-1),
    T=sum_q H_q=2 binom(r,2)=r(r-1).               (5)

Using sum_(k=0)^(r-1) k^2=r(r-1)(2r-1)/6 gives

    sum_q H_q^2 = 2r(r-1)(2r-1)/3,
    (sum_q H_q^2)/M = 2(r-1)/3.                    (6)

Similarly,

    sum_q binom(H_q,2)=r(r-1)(4r-5)/6.             (7)

Thus neither sum H_q^2<=C M nor sum binom(H_q,2)<=C M holds with an
absolute constant on all proper strict sources. The obstruction is
spread over nested output cells, rather than concentrated at one output.
All those output cells have the same endpoint sum D.

This differs materially from the coloring analyzed in
fibers/COMPLETION_LOAD_MOMENT_FAMILY_0045.md. That earlier coloring
concentrates all forcing at its hull-spanning cell and has bounded
normalized second moment. Reusing its one-cell profile for (1) would
miss the nested loads in (4).

## 4. An explicit instance within the S21 span range

The obstruction is not only an asymptotic large-span issue. For an odd
prime p, let t_i be the least residue of i^2 modulo p and put

    P={2p i+t_i:0<=i<p}.                            (8)

This is a Golomb set. To prove it, suppose the positive differences
from indices i<j and k<l agree. The residue terms differ by absolute
value at most 2(p-1), so comparison of the multiples of 2p forces
j-i=l-k=h. Reducing the same equality modulo p then gives

    h(j+i)=h(l+k) mod p.

Since 1<=h<p and p is odd, this implies 2i+h=2k+h modulo p, hence i=k
and j=l. Also consecutive values in (8) differ by at least p+1, so
their index order is their numerical order. The maximum mark is

    l=2p(p-1)+1.

Take p=101 and D=4l+1. The integer 101 is prime: its possible prime
divisors below its square root are 2,3,5,7, none of which divides it.
The displayed construction therefore has

    r=101, l=20201, D=80805,
    |A|=202, M=20301, T=10100,
    sum_q H_q^2=1353400=(200/3)M.                   (9)

Its span 80805 lies within the S21 range. In particular the tempting
cap sum H_q^2<=25M already fails inside that finite range. Its size and
energy are entirely consistent with the open source-size target.

## 5. Consequence for the attempted source method

The exact proper-only identities from the signed completion operator are

    H_q=|(Kz)_q|,
    sum_q H_q=(2T-M+sum_d s_d^2)/4,                (10)

where s_d is the signed count on the actual difference fiber. A bound
sum H_q^2<=C M would, by Cauchy--Schwarz and (10), give a constant
energy bound: sum H_q<=sqrt(C) M and therefore

    T<=(2 sqrt(C)+1/2)M.                            (11)

In particular C<=361/16 would be sufficient for H10. The finite instance
(9) violates that threshold as well as 25. Equations (6)--(9) rule out
that proposed unweighted
second-moment route. They do not rule out a source-span-sensitive
argument that separates the repeated common-sum concentration in (4)
and pays for it using the actual shared colors at other sums.

The pair-of-forcing-offset calculation in
fibers/PAIRED_FORCING_OFFSETS_0045.md remains valid. Its common-difference
resources can be reused by the many nested outputs in (4), so that
resource cannot be assigned an unexplained constant capacity. No Ramsey
bound changes, and no substitute global capacity is asserted here.

The same limitation holds for a single dyadic band. Choose D to be a
power of two greater than 4l and use the band [D/2,D). Every nontrivial
cross difference (3) lies in that band, while every internal difference
lies below it. The forcing loads restricted to this band are therefore

    H_(Q_i),band=r-1-i,
    (sum_q H_(q,band)^2)/M=(r-1)/6.                (12)

This ratio is unbounded. Nevertheless the actual band corner count is
binom(r,2)<M/4. Thus a universal squared-load cap would be a substantially
stronger and false substitute for the still-open dyadic energy target;
its failure does not refute that target.
