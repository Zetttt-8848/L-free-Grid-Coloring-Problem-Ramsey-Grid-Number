# Formal property and strengthened model

For n in {464,463,462}, let s=ceil(n/3). Seek a literal increasing set A
of s integers in [n], with min A=1, such that for each 1<=d<n the number
of ordered increasing pairs (a,b) in A with b-a=d is at most
2 max{j:H[j]<=n-d}, and no positive-step six-term AP is contained in A.
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,
284,334,357,373,426,481,493,554,586).

These are one-class necessary conditions for a three-color grid. A YES
does not imply either a ternary partition or a grid coloring. A certified
NO yields the stated upper-bound implication by the inherited pigeonhole
reduction. Translating the least mark to 1 preserves all predicates and
keeps the set inside [n], so normalization is complete.

Occupancies x_i in {0,1}, 0<=i<n, sum to s and x_0=1. For i<j,
p_ij in {0,1} is defined by three clauses equivalent to p_ij=x_i AND x_j.
For each d, sum_i p_(i,i+d)<=cap_d. Every admissible AP has sum x<=5.

Rank variables a_0<...<a_(s-1) in [0,n-1] have x_(a_i)=1, implemented
by exact element constraints. Since the ranks are s distinct occupied
positions and sum x=s, they enumerate every occupied position exactly.
Thus this redundant representation is equivalent in both directions.

Rank constraints: a_i>=i+floor(i/5) follows by starting at a_0=0 and
using a_(i+5)>=a_i+6: otherwise those six distinct integer ranks occupy
six consecutive integers and form a forbidden AP. More generally each
consecutive block of six ranks cannot have all five adjacent gaps equal.
Four reified gap inequalities and their OR enforce this consequence.
These constraints are necessary; they do not replace the complete AP list.

Neighbor cuts (PROVED): for 1<=c<s, collect the H_c=c*s-c*(c+1)/2
pairs of ranks whose index gap is at most c. Their distance multiset is
a submultiset of all pair distances, so multiplicity at distance d is
at most cap_d. Greedily filling the smallest distances up to their caps
therefore gives an exact lower bound M_c on their total distance. Their
total is the linear rank expression
T_c=sum_(j=1)^c sum_(i=0)^(s-1-j)(a_(i+j)-a_i), so T_c>=M_c is valid.
Also telescoping gives
T_c=sum_(j=1)^c(sum last j ranks - sum first j ranks)
<= (n-1)c(c+1)/2. The implemented cuts use rank variables; replacing
T_c by an arbitrary all-pair indicator sum would be invalid and is not
done. The lower bound is not claimed sufficient for an actual difference
multiset or set. The upper bound is redundant given rank domains.

No UNSAT theorem will be claimed from a CP-SAT status. A negative result
requires a complete certified encoding/proof and independent checker.
All arithmetic predicates in the witness checker are integer exact.
