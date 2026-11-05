"""Exact, dependency-free checks for cross_diagonal.md and the 465 audit.

Uses integers only. Exhaustive checks concern only the ranges reported in JSON.
The proofs, including their universal reductions, are in the route documents.
"""
from itertools import product
import json
from pathlib import Path
import sys


def triangle(size):
    pts = [(i, j) for i in range(size) for j in range(i)]
    index = {p: i for i, p in enumerate(pts)}
    corners = [(index[i, j], index[i + d, j], index[i + d, j + d])
               for i, j in pts for d in range(1, size - i)]
    return pts, corners


names = "abcdefghijklmno"
declared = "abc adf agj ako bde bgi bkn cef chj clo dgh dkm ehi eln fij fmo gkl hlm imn jno".split()
pts, corners = triangle(6)
actual = {"".join(names[i] for i in c) for c in corners}
assert actual == set(declared)

# (assumptions, forced value with justifying corner, contradiction)
certificate = [
    ("b0 d0", "c1:abc f1:adf e1:bde", "cef"),
    ("b0 d1 h0 k0", "c1:abc o1:ako n1:bkn l0:clo g1:gkl m1:hlm i0:imn j0:jno e1:ehi f1:fij", "fmo"),
    ("b0 d1 h0 k1", "c1:abc m0:dkm l1:hlm o0:clo f1:fmo g0:gkl j1:agj i1:bgi e0:cef", "fij"),
    ("b0 d1 h1", "c1:abc j0:chj g0:dgh", "agj"),
    ("b1 n0 f0", "d1:adf e0:bde c1:cef l1:eln o0:clo m1:fmo h0:hlm j1:jno k1:ako", "dkm"),
    ("b1 n0 f1 g0", "j1:agj i0:fij m1:imn o0:fmo k1:ako d0:dkm h1:dgh l0:hlm c0:chj", "clo"),
    ("b1 n0 f1 g1", "i0:bgi m1:imn o0:fmo j1:jno k1:ako d0:dkm l0:gkl c1:clo e1:eln", "cef"),
    ("b1 n1", "k0:bkn o1:ako j0:jno g1:agj i0:bgi f1:fij m0:fmo d1:dkm e0:bde h0:dgh", "ehi"),
]
for assumptions, forces, contradiction in certificate:
    state = {"a": 0}
    state.update((s[0], int(s[1])) for s in assumptions.split())
    for forced in forces.split():
        assignment, corner = forced.split(":")
        v, value = assignment[0], int(assignment[1])
        assert corner in actual and v in corner and v not in state
        assert all(state[t] == 1 - value for t in corner if t != v)
        state[v] = value
    assert contradiction in actual
    assert len({state[t] for t in contradiction}) == 1

for tail in product(range(2), repeat=14):
    state = dict(zip(names, (0,) + tail))
    covering = sum(all(state[s[0]] == int(s[1]) for s in ass.split())
                   for ass, _, _ in certificate)
    assert covering == 1

triangle_counts = {}
for size in [2, 3, 4, 5, 6]:
    pts, corners = triangle(size)
    count = sum(all(not (values[a] == values[b] == values[c])
                    for a, b, c in corners)
                for values in product(range(2), repeat=len(pts)))
    triangle_counts[str(size)] = {"points": len(pts), "corners": len(corners),
                                  "corner_free_colorings": count}
assert triangle_counts["5"]["corner_free_colorings"] == 36
assert triangle_counts["6"]["corner_free_colorings"] == 0
_, t5 = triangle(5)
witness = tuple(map(int, "0011000011"))
assert all(not (witness[a] == witness[b] == witness[c]) for a, b, c in t5)

aps11 = [tuple(range(start, start + 6 * d, d))
         for d in (1, 2) for start in range(11 - 5 * d)]
alpha11 = max(sum(values) for values in product(range(2), repeat=11)
              if all(not all(values[i] for i in ap) for ap in aps11))
assert alpha11 == 9

# Independent direct-convolution audit of both energy identities.
test_w = [1, 2, 3, 2, 1]
test_a = [sum(test_w[i] * test_w[i + d] for i in range(len(test_w) - d))
          for d in range(len(test_w))]
energy_cases = 0
for sequence in product(range(3), repeat=6):
    E = 0
    W2 = 0
    for s in range(12):
        f = [sum(test_w[i] for i in range(5)
                 if 0 <= s - i < 6 and sequence[s - i] == c)
             for c in range(3)]
        E += sum(x * x for x in f)
        W2 += sum(f) ** 2
    r = [sum(sequence[j] == sequence[j + d] for j in range(6 - d))
         for d in range(1, 5)]
    assert E == 6 * test_a[0] + 2 * sum(test_a[d] * r[d - 1] for d in range(1, 5))
    assert W2 == 6 * test_a[0] + 2 * sum((6 - d) * test_a[d] for d in range(1, 5))
    assert 3 * E >= W2
    energy_cases += 1

n = 465
w = [min(i, 94 - i) for i in range(1, 94)]
a = [sum(w[i] * w[i + d] for i in range(len(w) - d))
     for d in range(len(w))]
blocks = []
for lo, hi, q in [(1, 39, 24), (40, 92, 23)]:
    sum_a = sum(a[d] for d in range(lo, hi + 1))
    sum_da = sum(d * a[d] for d in range(lo, hi + 1))
    contribution = (n - 18 * q) * sum_a - sum_da
    blocks.append({"lo": lo, "hi": hi, "q": q, "sum_a": sum_a,
                   "sum_da": sum_da, "contribution": contribution})
score = sum(b["contribution"] for b in blocks) - n * a[0]
assert a[0] == 69231 and score == 285630

output = {
    "arithmetic": "exact Python integers",
    "triangle_counts": triangle_counts,
    "certificate_leaves": len(certificate),
    "certificate_branch_assignments_tested": 2 ** 14,
    "alpha6_of_11": alpha11,
    "energy_identity_sequences_tested": energy_cases,
    "energy465": {"n": n, "weight": "w_i=min(i,94-i), 1<=i<=93",
                  "golomb_length_lower_bounds": {"24": 425, "25": 480},
                  "a0": a[0], "n_a0": n * a[0], "blocks": blocks,
                  "contradiction_score": score, "autocorrelations": a},
    "nonclaims": ["No exhaustive search beyond the stated triangle, interval, and word sizes",
                  "The Golomb lower bounds are supplied source inputs, not proved by this script"]
}
output_path = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).with_name("cross_diagonal_verify.json")
output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, indent=2))
