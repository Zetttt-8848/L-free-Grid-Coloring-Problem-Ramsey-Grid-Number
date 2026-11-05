# Signed weights with both upper and lower correlation bounds

Root derivation and bounded discriminator, R4-RESEARCH-0004. The statements in the first two sections are algebraic lemmas. The final numerical envelope is discovery evidence, not an exact certificate or a new Ramsey upper bound.

## A valid score without nonnegative autocorrelations

Let chi:[N]->[k] be a colored word, and let M_d count equal-color pairs at distance d. Suppose 0<=M_d<=U_d. For any finite real weight vector w of length at most N, extend it by zero and set

    a_d=sum_i w_i w_{i+d},       a_0=sum_i w_i^2.

No sign restriction is imposed on w or a_d. Define

    S(w)=sum_{d=1}^{N-1}(N-d)a_d
           -k sum_{d=1}^{N-1} U_d max(a_d,0)
           -(k-1)N a_0/2.                            (1)

Every such colored word satisfies S(w)<=0.

Proof. Put v_i=e_{chi(i)}-(1/k)1 inside [N] and zero outside. Expanding the nonnegative quantity V=sum_x ||sum_i w_i v_{x+i}||^2 gives

    kV=(k-1)Na_0+2 sum_d a_d(kM_d-(N-d)).

When a_d>=0, the term a_d M_d is at most a_d U_d. When a_d<0, the lower bound M_d>=0 makes a_d M_d at most zero. Hence kV<=-2S(w). Since V>=0, (1) follows.

In particular, inserting an upper correlation cap into a negative coefficient would be invalid; the score above uses the lower bound at precisely those coefficients. The natural bound U_d<=N-d may also be included.

## A two-sided Fourier-envelope lemma

Set l_d=N-d-kU_d and u_d=N-d. Suppose finitely many nodes x_j in [-1,1] and masses lambda_j>=0 satisfy

    l_d <= f_d := -2 sum_j lambda_j T_d(x_j) <= u_d

for every 1<=d<N, where T_d is the Chebyshev polynomial of degree d. Then, for every real w as above,

    S(w) <= (sum_j lambda_j-(k-1)N/2) a_0.            (2)

Proof. The d-th term of (1) before its constant diagonal term is l_d a_d if a_d>=0 and u_d a_d otherwise. Both are at most f_d a_d by the two-sided assumptions. For x_j=cos(theta_j),

    p_j=|sum_i w_i exp(i sqrt(-1) theta_j)|^2
       =a_0+2 sum_d a_d T_d(x_j) >=0.

Consequently sum_d f_d a_d=sum_j lambda_j(a_0-p_j)<=a_0 sum_j lambda_j. Subtracting (k-1)Na_0/2 proves (2). The notation i in the exponential is the integer index of the weight, and sqrt(-1) is the imaginary unit.

The existing one-sided envelope only bounded scores whose autocorrelations were all nonnegative. The extra upper inequality f_d<=u_d is required here. It must not be inferred from that earlier result.

## Executed discovery and its scope

The old literal envelope fails the new upper inequality at 31 offsets, including d=84. Thus its previous proof does not settle this enlarged class of signed scores.

A fresh bounded linear program used N=464, k=3, and U_d=min(N-d,6q(N-d)). The initial 4001-node calculation reached its declared time limit without a solution. After that process ended, a 1001-node interior-point calculation with a required coefficient margin of 0.001 returned a numerical envelope with mass approximately 446.81775683, below the diagonal threshold 464. Its displayed largest coefficient residual was about -0.001. The literal numerical nodes and masses are in signed_kernel_lp_1001.json.

This is evidence against this signed-score route with the unchanged caps. Floating optimization output is not a proof that an envelope meets all exact inequalities. No exact mass bound, universal negative optimum, or improved Ramsey bound is claimed from it. Producing a separate certificate audit is not the next research task under the user's revised mandate; the computation already indicates that retaining only these pair-count bounds loses the shared color information needed for an improvement.

A separate bounded search for an actual ternary word satisfying every aggregate cap remains distinct from the envelope problem. A low positive violation score is not a word construction and does not imply nonexistence. Such a word, if found, would still not be a coloring of a grid or of any completion triangle.
