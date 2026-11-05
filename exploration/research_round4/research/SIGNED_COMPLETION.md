# Signed completion identities for the two-color triangle problem

Base R4-RESEARCH-0001. Root derivation. These are exact auxiliary identities and a sufficient spectral obstruction; no improved Ramsey bound or priority claim follows yet.

Let A be a finite integer set, and let V=T(A)={(v,u):u<v, u,v in A}. Write M=|V|. A corner-free three-color grid with a monochromatic diagonal on A induces a two-color corner-free coloring of V. Encode those two colors by z_q in {-1,1}.

For q=(v,u), define

D_q={d in Z: 0<d<v-u, u+d in A, v-d in A},
L(q,d)=(u+d,u), and R(q,d)=(v,v-d).

These are exactly the pairs of equal-diagonal cells whose positive completion is q. Indeed R-L=(v-u-d,v-u-d), whose entries are positive. Conversely any corner completed at q has its first and third cells of this form with their common offset d. This remains true when u+d=v-d; the two cells are still distinct.

Define the real linear operator K on functions on V by

(Kz)_q=(1/2) sum_(d in D_q) (z_L(q,d)+z_R(q,d)).

Every input cell has smaller span than q. Ordering V by span makes K strictly triangular, hence nilpotent. This is a finite operator depending only on A.

## Exact local identity

Let H_q be the number of d in D_q for which z_L=z_R. In every corner-free two-color coloring,

H_q = -z_q(Kz)_q = |(Kz)_q|.

Proof. If the two signs disagree, their sum is zero and they contribute zero to H_q and to Kz. If they agree, their common sign must be -z_q, since otherwise their corner with q is monochromatic. Such a pair contributes -z_q to Kz and one to H_q. Summing proves the first equality. It also proves that Kz is either zero or has sign opposite to z_q, which gives the second equality.

In particular, a cell with H_q>0 has a uniquely forced color, and two families forcing opposite colors cannot share an output cell. The identity gives a simultaneous constraint across all its source distances, beyond separate cardinality bounds for individual distance fibers.

## Global energy identity

For d>0 let V_d={(u+d,u):u,u+d in A}, r_d=|V_d|, and s_d=sum_(q in V_d)z_q. Then sum_d r_d=M. Counting equal-sign unordered pairs in each V_d gives

sum_q H_q = (1/4) sum_d (r_d^2+s_d^2-2r_d).

Proof. A fiber has (r_d+s_d)/2 positive and (r_d-s_d)/2 negative signs. Its equal-sign pair count is the sum of the two corresponding binomial coefficients, which expands to (r_d^2+s_d^2-2r_d)/4. Each such pair has exactly one positive completion in V and is counted once by the local definition. Completion belongs to V because its row and column come from A and the row exceeds the column.

Combining this count with the local identity yields

4 z^T Kz + sum_d s_d^2 = 2M - sum_d r_d^2.             (1)

No estimate or probabilistic model enters (1). It is necessary for every valid two-coloring of T(A).

Let F have one row for each nonempty distance fiber and one column for each cell, with F_(d,q)=1 when q is in V_d and zero otherwise. Put

Q = F^T F + 2(K+K^T).

Then Q is real symmetric, ||z||_2^2=M, and (1) becomes

z^T Qz = 2M-sum_d r_d^2.                             (2)

Thus, for M>0, the following is a sufficient obstruction to two-colorability:

lambda_min(Q) > 2 - (sum_d r_d^2)/M.                 (3)

Proof. The least-eigenvalue inequality gives z^TQz >= lambda_min(Q)M. Under (3), this exceeds the right side of (2), a contradiction. A rigorous use of (3) would require an analytic eigenvalue bound or an exact positive-definiteness certificate. Floating-point eigenvalues serve only to investigate whether this route is promising.

## Relation to known machinery and open step

Q is the identity plus the adjacency matrix of the graph obtained by replacing every corner in T(A) with its three pairs. A pair of cells belongs to at most one such positive corner; its slope identifies its role. Hence (3) is a familiar spectral bound for the cut problem on this graph, specialized through the exact source geometry. It must not be called an original spectral method merely because it is written in these coordinates.

The potentially useful feature for further research is the triangular operator K and the stronger pointwise identity H_q=|Kz_q|, which retain the output of each completion. A uniform estimate strong enough to improve the known cardinality bounds has not been established. The old square-root obstruction and arbitrary balanced pair data do not by themselves determine whether this stronger system can provide such an estimate.

## An exact limitation of the unweighted spectral criterion

The exploratory eigenvalues in spectral_probe.json suggested a simple obstruction, which has the following direct derivation. For A={0,...,m-1}, every horizontal or vertical pair in T(A) completes a corner in T(A). For example, two cells (a,u),(v,u) with u<a<v have completing partner (v,u+v-a), whose second coordinate lies strictly between u and v and is in A. The vertical case follows by the same calculation. Consequently, if F_R and F_C are incidence matrices for rows and columns, then

Q=F^T F+F_R^T F_R+F_C^T F_C-2I.

This gives lambda_min(Q)>=-2. For m>=5 equality holds: use a vector supported on the six cells

(2,0), (3,0), (4,1), (4,2), (3,2), (2,1),

with signs +,-,+,-,+,- in that order and zero elsewhere. Its sum on every row, column and slope-one diagonal is zero, so all three incidence matrices annihilate it. It is therefore an eigenvector of Q with eigenvalue -2.

For this A, r_d=m-d for d=1,...,m-1 and M=m(m-1)/2. Summing consecutive integer squares gives

2-(sum_d r_d^2)/M=(7-2m)/3.

At m=6 the right side is -5/3, which exceeds lambda_min(Q)=-2. Thus criterion (3) cannot even detect the already known two-color obstruction T({0,...,5}). At m=7 it does detect an obstruction, since -2>-7/3. This is an exact limitation of this particular unweighted spectral criterion, not of the full pointwise identities. Repeating unweighted eigenvalue scans will not supply the missing strength at this basic example.
