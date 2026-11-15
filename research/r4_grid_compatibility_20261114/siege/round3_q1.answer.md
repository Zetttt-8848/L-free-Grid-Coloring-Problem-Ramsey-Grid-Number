# round3_q1 answer: AABA / ABAA mixed quadruples

Notation as in the query: C(p,q) = (q+h,p) for p<q; L(u,x,y) has cells (u+x,u), corner (u+y,u), (u+y,u+y-x).

## 1. Degenerate case r = s (PROVED)
For AABA the points a+r and a+s coincide when r = s, but they must lie in class e and in class e'. The pieces G_e^f and G_{e'}^f are disjoint, so this is impossible. The same holds for ABAA. So only r < s matters.

## 2. AABA forcing (PROVED; reproduces the previous round)
Here a, a+r, a+r+s are in e and a+s is in e', with r<s. Lemma F gives C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = e'. Two further L's give the rest.
- L(a,h+r,h+r+s) forces C(a+s,a+r+s) = e.
- L(a,h+s,h+r+s) forces C(a,a+s) = e.

The remaining cell C(a+r,a+s) joins different classes, so it is only known to be in {e,e'}.

Checks run without a contradiction:
- every L with corner (a+h+r+s,a) and arm x in {h, h+r, h+s, d}, using the cells (p+h,p+l) whose colour is the class of p;
- the four corners C(.,.) among themselves.

## 3. ABAA forcing (PROVED, new)
Here a, a+s, a+r+s are in e and a+r is in e'. Lemma F on the same-class pairs gives C(a,a+s) = C(a,a+r+s) = C(a+s,a+r+s) = e'.
- **L(a,h+s,h+r+s).** Its arm cells are C(a,a+s) = e' and the vertical end (a+h+r+s, a+r) = C(a+r,a+r+s). Its corner is C(a,a+r+s) = e'. So C(a+r,a+r+s) ≠ e'. Lemma F (first half) gives ≠ f. Hence it is e.
- **L(a,h+r,h+r+s).** Its arm cells are C(a,a+r) and (a+h+r+s,a+s) = C(a+s,a+r+s) = e'. Its corner is e'. So C(a,a+r) ≠ e', and it is ≠ f. Hence it is e.

ABAA is the mirror image of AABA under r <-> s: the roles of the two middle points swap, and the forced triangle is the same up to that swap. Hence any forbidding proof or witness for one transfers formally to the other, provided the extra cells used are mirrored as well. This last point is NOT proved in general.

## 4. Status of the forbidden/allowed question: OPEN
- I derived no monochromatic L from the forced cells, nor from the d-cells and the shifted-source cells I examined.
- I did not construct an explicit witness. I have no code execution, and hand-checking a proper ternary source of size about 15 or more, L by L, was not feasible within this run.
- The non-occurrence in random sources with n <= 16 is evidence only.

## 5. Consequence (part 4): no proportional saving follows even if both patterns are forbidden
Forbidding AABA and ABAA leaves the shapes ABBA, AABB, ABAB, ABBB and AAAB, among others. Here is why that does not force a proportional saving.

- Take two Sidon sets A and B whose difference sets are disjoint. Every cross quadruple then needs differences shared between A-B and the inner sets. The patterns AABA and ABAA each have one same-class difference coinciding with a cross difference, together with three points in one class.
- Forbidding them does not stop A and B from separately each having about sqrt(S/2) elements with disjoint difference sets.
- The plain counting bound C(|A|,2) + C(|B|,2) <= S gives only |A|+|B| <= (2+o(1)) sqrt(S). This is the same order as 2Q(S/2) and is weaker than 2Q(S).
- I could not prove any bound of the form |A|+|B| <= (2-delta) Q(S) from the excluded patterns. A proof would need an Erdos-Turan-type interval argument that controls cross representations. I did not complete one, so none is claimed.

## Summary
- PROVED: the case r=s is degenerate (impossible) for both patterns; the complete forcing of five of the six triangle cells for ABAA (new), mirroring AABA.
- OPEN: whether AABA or ABAA is forbidden; whether AAAB is allowed (no witness found); any proportional bound on |G_e^f|+|G_{e'}^f| beyond 2Q(S).

=== END OF ANSWER round3_q1 ===
