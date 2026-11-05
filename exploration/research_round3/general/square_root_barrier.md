# G5: precise scope of the remaining square-root obstruction

Author root, Level3. UNVERIFIED pending required reviews.

The exact nesting statement is profile-valued: for a monochromatic set S
in a q-color completion-closed region, its distance-d fiber is partitioned
into at most q-1 monochromatic sets in T(S). Each is bounded by its own
completion-closed capacity and actual span. Replacing these capacities by
a common bound yields V_q<=(q-1)C_(q-1), then the generalized Golomb
estimate gives the leading term C_q<=sqrt(V_q*N). This replacement retains
alpha_q=(1+alpha_(q-1))/2. Distance profiles improve constants (as in the
R4 route) but do not by themselves prove a new exponent.

Lemma G5a. For every odd prime p, the integer set

 S_p={2pi+(i^2 mod p):0<=i<p}

is a p-mark Golomb ruler of span below2p^2.

Proof. Marks strictly increase with i because the change in residues is
between -(p-1) and p-1, while the leading increment is2p. If the positive
differences b_j-b_i and b_l-b_k are equal, then
2p[(j-i)-(l-k)] is the difference of two residue differences and has
absolute value at most2p-2. Thus j-i=l-k=t, with1<=t<p. Reduction
modulo p gives (j^2-i^2)-(l^2-k^2)=2t(i-k)=0 mod p. Since p is odd,
t is nonzero mod p and the prime field has no zero divisors, i=k and
j=l. The largest mark is at most2p(p-1)+(p-1)<2p^2.

Lemma G5b. The weak triangle W(S)={(x,y):x,y in S,x>=y}, with all
diagonal cells color0 and all strict-triangle cells color1, is
completion closed and corner-free whenever S is Golomb.

Proof. Same-diagonal cells (u+sigma,u),(v+sigma,v),u<v, in W(S)
have their completion(v+sigma,u) in W(S). A color0 corner is impossible
because its vertical edge cannot have two distinct diagonal cells.
A color1 corner would have x>y and x,x+d,y,y+d in S. The equal positive
differences (x+d)-x=(y+d)-y in a Golomb set imply x=y, a contradiction.

Checks. The prime must be odd: at p2 the displayed proof uses a factor2
which is not invertible (no claim depends on p2). The construction starts
at0 and may be translated by1 to enter a positive-coordinate square.
The singleton case is harmless. Every used d is positive. Missing cells
of the square are not filled arbitrarily: the example is a specified
completion-closed region, and no full-grid lower bound is asserted.
Color counts k1 or k2 do not enter the general-k theorem via this example;
G5b uses at most two colors exactly as stated. Direct finite checks of
all pair differences and geometric corners are recorded separately.

Consequence and limitation. The capacity at the first two-color level
can be at least p inside a region of ambient side below2p^2+1 while
the complete difference multiplicity profile is0/1. Therefore a universal
sub-square-root bound for such regions cannot replace this step. This
does not construct nested extremizers at all later levels, does not prove
the double exponential necessary, and does not rule out using full-grid
structure. The missing statement for a tower reduction remains a bound
coupling several color levels or several full-grid scales simultaneously.

A conditional density implication is elementary but separate: if every
corner-free subset of[N]^2 has density at most C/(log N)^a for fixed
C,a>0, then every k-coloring forces a corner whenever log N>(Ck)^(1/a).
Indeed one color has density at least1/k. Thus such a hypothesis would
give R_k(L)<=floor(exp((Ck)^(1/a)))+1, provided the asserted density
bound holds at that integer N. No such density theorem is proved or
imported here, and this conditional observation is not a novelty claim.
