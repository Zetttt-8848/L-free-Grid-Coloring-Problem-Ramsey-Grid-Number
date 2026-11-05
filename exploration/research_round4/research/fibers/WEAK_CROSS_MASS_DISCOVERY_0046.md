# Weak cross-mass discovery (0046)

This is one bounded statistic extracted from already saved **proper weak**
witnesses. It does not recheck their colorings, enumerate new ones, or make a
universal assertion.

For a weak source \(W(S)\), with actual diagonal partition
\(S=B\sqcup C\), write
\[
T(S)=\sum_{h>0}{r_S(h)\choose2},
\qquad r_S(h)=|S\cap(S-h)|.
\tag{1}
\]
The new measured quantity is
\[
\Xi(S;B,C)=T(S)-2|B||C|.
\tag{2}
\]
The saved two-Golomb decomposition also writes
\[
T(S)=2\rho+N+Q,
\tag{3}
\]
where \(\rho,N,Q\) are the actual signed-fiber resources from
**TWO_GOLOMB_MIXED_ENERGY_0040.md**. Equation (3) is an input identity, not
a fresh derivation.

## 1. Immediate saved proper-weak counterexample

Use the twelve-mark proper weak coloring in
**WEAK_SOURCE_PRODUCT_SPAN_0035.md**:
\[
S=\{0,1,4,5,7,8,12,13,21,22,23,24\},
\qquad B=P,\quad C=P+1,
\]
with \(|B|=|C|=6\). From this literal saved set, the multiplicities
\(r_S(h)\), grouped by their value, are
\[
\#\{h:r_S(h)=1\}=1,quad
\#\{h:r_S(h)=2\}=11,quad
\#\{h:r_S(h)=3\}=8,quad
\#\{h:r_S(h)=4\}=3,quad
\#\{h:r_S(h)=7\}=1.
\tag{4}
\]
Thus
\[
T(S)=11{2\choose2}+8{3\choose2}+3{4\choose2}+{7\choose2}
=11+24+18+21=74,
\tag{5}
\]
whereas
\[
2|B||C|=2\cdot6\cdot6=72.
\tag{6}
\]
Consequently
\[
\boxed{\Xi(S;B,C)=2>0.}
\tag{7}
\]
This refutes the proposed universal weak-source inequality
\(T(S)\le2|B||C|\) already within a saved proper weak witness.

## 2. Contrasting saved weak cube

For the proper weak three-cube in
**PROPER_WEAK_RESOURCE_CYCLE_CONSTRUCTION_0044.md**, the two diagonal
classes have \(|B|=|C|=4\), and the stated actual resources are
\[
\rho=6,\qquad N=0,\qquad Q=12.
\]
Using the saved identity (3) gives
\[
T(S)=24,qquad
\Xi(S;B,C)=24-2\cdot4\cdot4=-8.
\tag{8}
\]
This is only a contrast: the first witness already settles the bounded
universal test negatively.

## Scope

The counterexample concerns the exact weak-source inequality in (2). It does
not address a corrected inequality, a restricted strict-source-fiber class,
or any implication involving \(K_3(A)\), and it is not by itself an S21
statement.

