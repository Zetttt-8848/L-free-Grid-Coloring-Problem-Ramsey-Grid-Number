# round4_q5 answer: MS via the analytic / uniformity route

## Status summary (read first)

- **MS is NOT proved and NOT refuted here.** It remains OPEN.
- What is proved here (all complete, elementary):
  1. **Reduction R0.** MS for all lambda implies MS at lambda = 1, which reads
     `sum_e |F_1(S_e(d))| <= (1-delta) * 3 (Q(S-1)+Q(S-2))`. So a counterexample family only has to
     saturate lag 1, and any proof of MS must in particular prove this lag-1 statement.
  2. **Lemma E** (uniformity of near-maximal Sidon sets, explicit L^2 form). This is step (1) of the suggested approach.
  3. **Lemma B** (binary reduction). For each corner colour f, the union `Y_f` of the two pieces with corner colour f
     carries a proper 2-colouring of its strict source, with forced colours on same-class pairs. Corollary: `r_{Y_f}(m) <= 2Q` for every m.
  4. **Lemma C** (no-collision). This is the complete first-generation consequence of Lemma F together with the AABA/ABAA forcing.
  5. **Obstruction O** (the reason step (3) of the approach fails as posed). If A is any Sidon set with no differences in {1,2,3,4}, the pair (A, A+2) satisfies
     every constraint of Lemma C with zero violations. Both sets are near-maximal and Fourier-uniform whenever A is.
     So uniformity of the individual pieces cannot force collisions at a positive rate. A proof must exclude
     *translate-correlated* pieces using constraints beyond the single same-corner pair.
  6. **Chain check, steps 2-5.** The chain is sound. Step 4-5 is made rigorous as a conditional statement (Lemma P):
     under MS(delta), the average class size satisfies the single-class certificate inequality with its budget multiplied by (1-delta),
     up to an explicit additive term. The heuristic is delta' ~ 1 - sqrt(1-delta). A numeric delta' needs the certificate's
     numbers, which I do not have.
- The approach was followed in its steps (1) and (2). I depart from step (3) because Obstruction O shows that step (3) cannot
  work using uniformity of the pieces alone.

---

## 0. Notation and the L's in pair language

Write a cell `(y,x)` with `x<y`, both in D, as the pair `{x<y}`, and write `col(x,y) = chi(y,x)`.
By Lemma 0 of Part A, the directed L's inside V(D) are exactly the triples

    (a, a+delta), (c, c+delta), (a, c+delta),   with a < c, delta > 0, and a, a+delta, c, c+delta in D,

where each entry is a pair (smaller, larger). Proof: L(u,d,h) has cells `(u+d,u), (u+h,u), (u+h,u+h-d)`, i.e. the pairs
`(u,u+d), (u,u+h), (u+h-d,u+h)`. Put `a=u`, `c=u+h-d`, `delta=d`. Then `c > a` because `h>d`, and `c+delta = u+h`. The map is reversible.
So chi is proper iff **no two pairs of equal length delta with distinct left ends a<c have the same colour as the pair
(a, c+delta) that spans them.** In the z-notation this says: never `z_delta(a) = z_delta(c) = z_{c-a+delta}(a)`.

Fix d, a lag l and h = d+l. As in Lemma F, a point u is in the piece `G_x^f` (class x, corner colour f, x != f) iff
`z_d(u)=z_d(u+l)=x` and `z_h(u)=f`. For p<q put `C(p,q) = col(p, q+h)` (this is the cell `(q+h,p)`).

## 1. Reduction R0 (proved)

MS asserts the inequality for every lambda in [1,S]. At lambda = 1 it says
`sum_e r_{S_e(d)}(1) <= (1-delta) 3 v_1`. This is a special case, so MS implies it. Also, if some source has
`sum_e r_{S_e(d)}(1) / (3 v_1)` arbitrarily close to 1, then MS fails for every delta. Conversely, the lag-1 statement does not imply MS.
Hence **the cleanest open core of MS is the lag-1 statement**: the six lag-1 pieces `G_x^f(1)` (six Sidon sets) cannot all be
near-maximal in the span of `F_d(D)`.

## 2. Lemma E: near-maximal Sidon sets are equidistributed (proved, explicit)

**Lemma E.** Let `A ⊆ [0,N]` be a Sidon set with |A| = k, and let T >= 1 be an integer. For integers x in [-(T-1), N]
(there are N+T of them), put `a(x) = |A ∩ [x, x+T)|` and `abar = Tk/(N+T)`. Then

    sum_x (a(x) - abar)^2  <=  T ( k + T - 1 - T k^2/(N+T) ).

In particular, if `k >= (1-eta) sqrt(N)` with `0 <= eta <= 1` and `T <= N`, the relative mean-square deviation satisfies

    (1/(N+T)) sum_x (a(x)-abar)^2 / abar^2  <=  (1+T/N)^2 * ( sqrt(N)/((1-eta)^2 T) + 2eta/(1-eta)^2 + T/((1-eta)^2 N) ).

*Proof.* `sum_x a(x) = Tk`, because each element lies in exactly T windows. Next, `sum_x a(x)(a(x)-1)` counts ordered pairs
(a,a') with a != a' together with a window containing both. That number is `sum_{a != a'} (T-|a-a'|)_+`. Since A is Sidon, every
positive difference g occurs for at most one ordered pair, and so does every negative one. Hence the sum is at most `2 sum_{g=1}^{T-1}(T-g) = T(T-1)`.
So `sum a^2 <= Tk + T(T-1)`, and `sum (a-abar)^2 = sum a^2 - (Tk)^2/(N+T)`. This gives the first claim.
For the second claim, `T k^2/(N+T) >= T(1-eta)^2 N/(N+T) >= T(1-eta)^2 (1 - T/N)`. So the bracket is at most
`k + T(1-(1-eta)^2) + T^2/N <= sqrt(N)+1 + 2 eta T + T^2/N`, using `k <= sqrt(N)+1`, which itself follows from
the first claim (the left side is >= 0) up to lower-order terms. The `+1` is absorbed after dividing. Dividing by `(N+T) abar^2 = T^2k^2/(N+T)`
and using `k^2 >= (1-eta)^2 N` gives the bound. ∎

With `T = N^{3/4}` the relative mean-square deviation is at most `(2eta + 2N^{-1/4})/(1-eta)^2 + o(1)`. So near-maximal Sidon sets
are equidistributed in windows of length `>> sqrt(N)`, in mean square, with explicit dependence on eta. (The `+1` bookkeeping in the
second display is crude. The first display is the exact statement to cite.)

**Remark.** Lemma E is invariant under translation: A and A+t are equally uniform. Section 5 shows why this matters.

## 3. Lemma B: binary reduction of the same-corner union (proved)

**Lemma B.** Fix d, l, h = d+l and a corner colour f. Let `Y = G_x^f ∪ G_{x'}^f` with `{x,x',f} = P`, and put
`beta(p,q) = C(p,q) = col(p, q+h)` for p<q in Y. Then:
(a) beta takes values in `{x,x'}`;
(b) beta(p,q) = x' if p,q are both in `G_x^f`, and beta(p,q) = x if both are in `G_{x'}^f`;
(c) beta is a proper colouring of the strict source V(Y): for p1<p3 in Y and g>0 with p1+g, p3+g in Y, the three values
   beta(p1,p1+g), beta(p3,p3+g), beta(p1,p3+g) are not all equal;
(d) consequently, for every m >= 1, `F_m(Y)` is the union of two Sidon sets, so `r_Y(m) <= 2 Q(span Y)`.

*Proof.* (a) and (b) are Lemma F; I re-derive it. For p<q in Y, the L with `a=p, c=q, delta=h` consists of `col(p,p+h)=f`, `col(q,q+h)=f`
and `col(p,q+h)`, so `C(p,q) != f`. If p and q are both in class x, the L with `a=p, c=q+l, delta=d` consists of `col(p,p+d)=x`,
`col(q+l,q+h)=z_d(q+l)=x` and `col(p,q+h)`. So `C(p,q) != x`, hence it is the third colour.
(c) Take `a=p1`, `c=p3`, `delta=g+h`. The pairs are `(p1,p1+g+h) = C(p1,p1+g)`, `(p3,p3+g+h)=C(p3,p3+g)` and `(p1,p3+g+h)=C(p1,p3+g)`.
All endpoints lie in D, since `p+h` is in D for every p in Y. This is an L of V(D).
(d) Split `F_m(Y)` by the value of beta(p,p+m) into `Z_x, Z_{x'}`. For p<q in Z_y, part (c) with g=m and (a) give `beta(p,q+m) = ybar`, the other colour.
If `p1<p3`, `p1+g = p2`, `p3+g = p4` are all in Z_y (g>0; p2 = p3 is allowed), then (c) with gap g+m gives the three values
`beta(p1,p2+m), beta(p3,p4+m), beta(p1,p4+m)`, all equal to ybar. This contradicts (c). So Z_y is Sidon. ∎

(d) only bounds the cross-correlation `#{(a,b) in A x B : b-a = ±m} <= 2Q-2`. That is far above the random value of about 1,
so it gives no saving. Likewise the binary-source cap `|Y| <= K(span)` is about span/48, far above 2 sqrt(span). **Lemma B gives no saving by itself.**

## 4. Lemma C: complete first-generation forcing and no-collision (proved)

Keep the setting of Lemma B. Write `A = G_x^f` (class colour x) and `B = G_{x'}^f`.

**Lemma C1 (forcing).** Let p in A and q in B.
- If p<q and there is r>0 with p+r and q+r in A, then `C(p,q) = x`.
- If q<p and there is r>0 with q-r and p-r in A, then `C(q,p) = x`.
- With A and B swapped (and x and x' swapped): if p<q and there is r>0 with p-r and q-r in B, then `C(p,q) = x'`;
  if q<p and there is r>0 with q+r and p+r in B, then `C(q,p) = x'`.

*Proof (re-derived; no earlier text is relied on).* **AABA lemma:** let a, a+r, a+r+s be in A and a+s in B, with r,s>0
(r ≠ s is automatic, because A and B are disjoint). Lemma B(b) gives `C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = x'`.
- The L with `(a, c, delta) = (a, a+s, r+h)` has pairs `C(a,a+r)=x'`, `C(a+s,a+r+s)` and `C(a,a+r+s)=x'`. So `C(a+s,a+r+s) != x'`, and with
  Lemma B(a) this gives `C(a+s,a+r+s) = x`.
- The L with `(a, c, delta) = (a, a+r, s+h)` has pairs `C(a,a+s)`, `C(a+r,a+r+s)=x'` and `C(a,a+r+s)=x'`. So `C(a,a+s) = x`.

For the first bullet, take `a=p` and `s=q-p`. For the second, take `a = q-r`, `s = r` and `r_new = p-q`: then `a+r_new = p-r` is in A, `a+s = q` is in B,
and `a+r_new+s = p` is in A, so `C(q,p) = C(a+s, a+r_new+s) = x`. The swapped statements follow by symmetry. ∎

**Lemma C (no-collision).** There are no p in A, q in B, p<q, with r,s>0 such that p+r, q+r are in A and p-s, q-s are in B.
There are no q in B, p in A, q<p, with r,s>0 such that q-r, p-r are in A and q+s, p+s are in B.
Equivalently, for each Delta>0, let `alpha` be the start of the (at most one) A-pair at difference Delta, and `beta0` the start of the
B-pair at difference Delta. If `beta0 < alpha`, no AB-crossing `p` (p in A, p+Delta in B) lies strictly between them.
If `alpha < beta0`, no BA-crossing `q` (q in B, q+Delta in A) lies strictly between them. *Proof:* Lemma C1 would force two different colours on the same cell. ∎

**Heuristic only.** If A and B were independent "random-like" near-maximal Sidon sets in [0,N], each small Delta would have an A-pair, a
B-pair and a crossing with constant probability, and a collision would occur at a positive rate. That would give a
proportional saving. This is the director's heuristic in concrete form.

## 5. Obstruction O: translate pairs defeat the uniformity route (proved)

**Proposition O.** Let A be a Sidon set with no positive difference in {1,2,3,4}, and put B = A+2. (Every Sidon set loses at most
4 points when this condition is imposed, since each difference occurs at most once.) Then A ∩ B = ∅, and the pair (A,B) has **no** configuration
excluded by Lemma C.

*Proof.* (AB case) Suppose p in A, q = a'+2 in B, p<q, p+r and q+r in A, and p-s and q-s in B, i.e. p-s-2 and q-s-2 in A. Then `(p+r, q+r)` and
`(p-s-2, q-s-2)` are two A-pairs with the same difference q-p, and their left ends differ (`p+r > p > p-s-2`). This contradicts Sidon.
(BA case) Suppose q = a1+2 in B, p = a2 in A, q<p, q-r and p-r in A, and q+s and p+s in B, i.e. a1+s and a2+s-2 in A. The A-pairs
`(a1+2-r, a2-r)` and `(a1+s, a2+s-2)` have the same difference a2-a1-2. Sidon forces them to coincide, so `r+s = 2`, i.e. r = s = 1.
Then a1, a1+1 are in A, which is a difference 1 in A, excluded. ∎

**Consequence for the suggested approach.** If A is near-maximal, then by Lemma E both A and A+2 are near-maximal and equidistributed.
Translation does not change any Fourier magnitude: `|hat 1_{A+2}| = |hat 1_A|`. Yet the pair has zero Lemma C collisions. So
**no argument whose only inputs are (i) uniformity of the individual pieces and (ii) Lemma F with the AABA/ABAA forcing can
produce a positive density of contradictions.** Step (3) of the suggested approach needs, in addition, a *cross-uniformity*
statement: the pieces are not translate-correlated. Near-maximality does not supply that.

The translate pattern is also locally consistent with the lag-1 definitions. If A = G_x^f(1) and B = A+2 = G_{x'}^f(1), then for each u in A,
`z_d(u..u+3) = x x x' x'`. No contradiction arises inside the four-point window. (`B = A+1` would be impossible, since
`z_d(u+1)` would have to equal both x and x'.)

**What Proposition O does NOT show.** It is not a counterexample to MS. It checks only the Lemma C constraints. It does not check
the full binary system of Lemma B(c) on Y = A ∪ (A+2), and it does not check the rest of V(D). I began checking whether the whole Lemma B(c)
system on `A ∪ (A+2)` is satisfiable. The non-accidental quadruples reduce to one family:
for a1<a3 in A, the values beta(a1,a1+2), beta(a3,a3+2), beta(a1,a3+2) are not all equal. "Accidental" quadruples
`a1+a4-a2-a3 in {±2,±4}` occur about N times each for near-maximal A, and they impose constraints that depend on position on the
mixed pairs. I did not settle whether the system is satisfiable (**OPEN**). If it is satisfiable for some family of near-maximal A,
the whole same-corner binary layer is powerless, and MS would have to come from cross-corner or cross-lag interactions.

## 6. The colour Cauchy-Schwarz step (2), assessed

The identity `sum_k a_k r_Y(k) <= 3 sum_e sum_k a_k r_{S_e}(k)` is correct: it is `(y0+y1+y2)^2 <= 3 sum y_e^2` applied to `y_e = (1_{S_e} * w)(x)`.
It runs in the wrong direction for MS, because it *lower*-bounds the class agreements by the total agreement. It shows that
saturating MS is compatible with equidistributed classes. It does not show that saturation is impossible. Near-equality in it forces only
`1_{S_e} * w` to be nearly equal across e, which is again a uniformity statement. By Section 5, uniformity of single sets is
translation-blind, so this step adds no exclusion beyond Lemma E. I found no way to convert it into a deficit.

## 7. Chain check (steps 2-5) and a rigorous conditional form of steps 4-5

**Step 2 (summed rank-neighbour inequality):** correct. Remarks:
(i) `H_tot = c s - 3c(c+1)/2` depends only on the total `s = sum_e s_e`.
(ii) It needs `c < min_e s_e`. If some `s_e <= c`, then directly `s <= 2K(S) + c`, which is a large saving whenever `c << K`. So unbalanced
triples are harmless.
(iii) It uses the single span S of F_d(D) for all three classes. This forgoes the staggering gain of about 12 starts per shift, which the
sensitivity analysis says is negligible. U_d must be rebuilt as a sum over main colours of the triple caps (as stated).
**Step 3 (prefix lemma):** correct. MS is needed only for lambda <= S, because `w_l = 0` and `v_l = 0` for l > S, so both prefix sums are constant there.
**Step 4:** the scaling identity `P*(H) = (1-delta) P_{3v}(H/(1-delta))` holds, and so does `P_{3v}(x) = 3P_v(x/3)`.

**Lemma P (scaling, proved).** Let v_l >= 0 be nonincreasing in l. Put `C(lambda) = sum_{l<=lambda} v_l` and `P_v(x) = sum_{lambda>=0} (x - C(lambda))_+`
(with value +infinity allowed). Then `P_v(mu x) >= mu^2 (P_v(x) - x)` for every mu >= 1 and x >= 0.

*Proof.* Let `Ct` be the piecewise-linear interpolation of C. It is concave with Ct(0) = 0, because the increments v_l are nonincreasing,
so `C(lambda)/mu <= Ct(lambda/mu)`. Put `f(y) = (x - Ct(y))_+`, which is nonincreasing. Then
`P_v(mu x) = mu sum_{lambda>=0} (x - C(lambda)/mu)_+ >= mu sum_{lambda>=0} f(lambda/mu) >= mu^2 int_0^inf f >= mu^2 sum_{lambda>=1} f(lambda) = mu^2 (P_v(x) - x)`.
The steps are Riemann-sum comparisons for a nonincreasing f, together with f(0) = x. ∎

Here `v_l = Q(S-l)+Q(S-l-1)` is nonincreasing, so Lemma P applies.

**Corollary (conditional; this is the rigorous form of step 5).** Assume MS(delta) at shift d. Let `sbar = s/3` and `Hbar = c sbar - c(c+1)/2`, with `c < min s_e`. Then

    2 ( P_v(Hbar) - Hbar )  <=  (1-delta) ( S c(c+1) - 4 sum_{i=0}^{c-1} (c-i) e_{i+1} ).

*Proof.* `2P(H_tot;w) + 12Σ <= 3Sc(c+1)`. Next, `P(H_tot;w) >= 3(1-delta) P_v(Hbar/(1-delta))`, and by Lemma P with mu = 1/(1-delta)
this is `>= 3 (P_v(Hbar) - Hbar)/(1-delta)`. Divide by 3. ∎

Compare the single-class certificate: `2P_v(H(s)) <= S c(c+1) - 4Σ`. Since `P_v(H) ~ H^2/(2 vbar)`, the budget factor (1-delta)
lowers the admissible H by about `sqrt(1-delta)`. Hence **delta' ≈ 1 - sqrt(1-delta) ≈ delta/2** for the average class size, the correction from the
`Hbar` term being negligible because `Hbar/P_v(Hbar) ~ 2vbar/Hbar` is tiny at the problem's scale. An explicit numeric delta' requires rerunning the certificate (its c, e_{i+1} and Q table) with this inequality. I cannot do that without the certificate data and code; it is a routine recomputation.
**No flaw found in the chain.** The heuristic in step 5 is confirmed up to the additive `Hbar` term.

## 8. Open questions (precise)

- **OQ1 (core of MS, lag 1).** Is there an absolute delta > 0 such that for every proper ternary source and every d,
  `sum_e |F_1(S_e(d))| <= (1-delta) 3 (Q(S-1)+Q(S-2))`? This is necessary for MS. OPEN.
- **OQ2 (translate test).** For a near-maximal Sidon A without small differences, is the Lemma B(c) system on `A ∪ (A+2)` (forced same-class
  colours, free mixed pairs) satisfiable? If it is not, at a positive rate, the same-corner layer might still yield a saving. If it is, any proof of MS must use
  cross-corner or cross-lag constraints. OPEN.
- **OQ3 (cross-uniformity).** Find a constraint of the ternary source that forbids two same-corner pieces at lag l from being
  translates `B = A + t` with t small, beyond the trivial exclusions t ∈ {0, ±l}. Without it, Fourier methods cannot close MS. OPEN.
- **OQ4.** An explicit numeric delta' (Section 7) for the certified K table, conditional on MS(delta).

No statement about R_4 is made, beyond the conditional chain of Section 7: if MS(delta) holds, then U_d shrinks
by about the factor (1 - delta'), with delta' ≈ 1 - sqrt(1-delta).

=== END OF ANSWER round4_q5 ===
