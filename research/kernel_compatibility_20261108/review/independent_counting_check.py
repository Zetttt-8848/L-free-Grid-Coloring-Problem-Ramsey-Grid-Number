"""Independent, standard-library audit of the six-class 464 certificate.

Run from any directory: python <this file>
No claimant code, cached arithmetic, solver, or numerical package is imported.
External OGR lower bounds are inputs, not computationally re-established here.
"""

from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import platform
import sys
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INPUTS = [
    Path(__file__).resolve(),
    ROOT / "research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md",
    ROOT / "research/kernel_compatibility_20261108/kernel_upper/README.md",
    ROOT / "research/kernel_compatibility_20261108/combinatorial_upper/THEOREM.md",
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def golomb(marks):
    differences = [v - u for u, v in combinations(sorted(marks), 2)]
    return len(differences) == len(set(differences))


def convolution(left, right):
    if not left or not right:
        return []
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def squared_norm(sequence):
    return sum(x * x for x in sequence)


def pair_correlations(weights):
    """Distance histogram of all ordered index pairs, keeping i <= j."""
    out = [0] * len(weights)
    for i, x in enumerate(weights):
        for j in range(i, len(weights)):
            out[j - i] += x * weights[j]
    return out


def capacity(positions):
    """Charge one distinct early minimum for each class exceeding 23 marks."""
    assert 1 <= positions <= 480
    eligible_minima = sum(1 for u in range(positions) if positions - 1 - u >= 425)
    return min(positions, 6 * 23 + min(6, eligible_minima))


def old_capacity(positions):
    assert 1 <= positions <= 480
    return min(positions, 6 * (23 if positions - 1 < 425 else 24))


def certificate(n=464, N=86):
    # Shifting indices 1,...,N-1 down to 0,...,N-2 preserves correlations.
    weights = [i * (N - i) for i in range(1, N)]
    correlations = pair_correlations(weights)
    full = convolution([1] * n, weights)
    actual_full_energy = squared_norm(full)
    # This is an UPPER bound on sum_c ||f_c*w||^2 for a proper coloring.
    upper_color_energy = n * correlations[0] + 2 * sum(
        capacity(n - d) * correlations[d] for d in range(1, len(weights))
    )
    # Cauchy requires actual_full_energy <= 3 * upper_color_energy.
    direct_deficit = actual_full_energy - 3 * upper_color_energy
    expanded_full_energy = n * correlations[0] + 2 * sum(
        (n - d) * correlations[d] for d in range(1, len(weights))
    )
    assert actual_full_energy == expanded_full_energy
    rows = [
        {"d": d, "p": n - d, "U": capacity(n - d),
         "a": correlations[d], "coefficient": n - d - 3 * capacity(n - d)}
        for d in range(1, len(weights))
    ]
    lhs = sum(row["coefficient"] * row["a"] for row in rows)
    rhs = n * correlations[0]
    assert direct_deficit == 2 * (lhs - rhs)
    old_gap = sum(
        (n - d - 3 * old_capacity(n - d)) * correlations[d]
        for d in range(1, len(weights))
    ) - rhs
    return {
        "n": n, "N": N, "weights": weights, "correlations": correlations,
        "a0": correlations[0], "full_convolution_energy": actual_full_energy,
        "upper_color_energy": upper_color_energy,
        "cauchy_deficit": direct_deficit, "lhs": lhs, "rhs": rhs,
        "gap": lhs - rhs, "old_gap": old_gap, "gain": lhs - rhs - old_gap,
        "grouped_lhs": [sum(row["coefficient"] * row["a"] for row in rows
                            if lo <= row["d"] <= hi)
                        for lo, hi in [(1, 33), (34, 38), (39, 84)]],
        "rows": rows,
    }


# Sparse exact polynomial ring Q[m,d,i], independent of the asserted formula.
def constant(value):
    return {(0, 0, 0): Fraction(value)} if value else {}


def add(*polys):
    out = defaultdict(Fraction)
    for poly in polys:
        for exponent, value in poly.items():
            out[exponent] += value
    return {e: v for e, v in out.items() if v}


def scale(poly, scalar):
    return {e: v * scalar for e, v in poly.items() if v * scalar}


def multiply(*polys):
    out = constant(1)
    for poly in polys:
        new = defaultdict(Fraction)
        for a, x in out.items():
            for b, y in poly.items():
                new[tuple(a[j] + b[j] for j in range(3))] += x * y
        out = {e: v for e, v in new.items() if v}
    return out


def evaluate(poly, m, d, i=0):
    return sum(v * m ** e[0] * d ** e[1] * i ** e[2] for e, v in poly.items())


def symbolic_autocorrelation():
    m, d, i = ({(1, 0, 0): Fraction(1)}, {(0, 1, 0): Fraction(1)},
               {(0, 0, 1): Fraction(1)})
    one = constant(1)
    minus_one = constant(-1)
    m_minus_one = add(m, minus_one)
    summand = multiply(i, add(m, d, scale(i, -1)), add(i, d), add(m, scale(i, -1)))
    powers = [
        m_minus_one,
        scale(multiply(m, m_minus_one), Fraction(1, 2)),
        scale(multiply(m, m_minus_one, add(scale(m, 2), minus_one)), Fraction(1, 6)),
        scale(multiply(m, m, m_minus_one, m_minus_one), Fraction(1, 4)),
        scale(multiply(m, m_minus_one, add(scale(m, 2), minus_one),
                       add(scale(multiply(m, m), 3), scale(m, -3), minus_one)),
              Fraction(1, 30)),
    ]
    summed = {}
    for (em, ed, ei), coefficient in summand.items():
        summed = add(summed, multiply({(em, ed, 0): coefficient}, powers[ei]))
    closed = scale(multiply(m, add(multiply(m, m), minus_one),
                            add(multiply(m, m), one, scale(multiply(d, add(m, d)), 5))),
                   Fraction(1, 30))
    residual = add(summed, scale(closed, -1))
    assert residual == {}
    # Rational points test the polynomial extension; finite sums require integer m.
    points = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(1)),
              (Fraction(1, 2), Fraction(3, 2)), (Fraction(1000), Fraction(37))]
    for mm, dd in points:
        assert evaluate(summed, mm, dd) == evaluate(closed, mm, dd)
    literal_cases = 0
    for N in range(2, 121):
        for shift in range(N):
            mm = N - shift
            literal = sum(x * (N - x) * (x + shift) * (N - x - shift)
                          for x in range(1, mm))
            assert Fraction(mm * (mm * mm - 1) * (mm * mm + 1 + 5 * shift * N), 30) == literal
            literal_cases += 1
    return {"symbolic_residual": "zero polynomial over Q[m,d]",
            "rational_points": [[str(x), str(y)] for x, y in points],
            "literal_cases": literal_cases, "N_range": [2, 120], "d_range": "0 <= d < N"}


def check_packing():
    # Complete labeled disjoint families, including unused positions and empties.
    counts = {"visited_families": 0, "golomb_families": 0}
    g = [0] * 9
    for p in range(9):
        g[p] = max((mask.bit_count() for mask in range(1 << p)
                    if golomb([u for u in range(p) if mask & (1 << u)])), default=0)
        for q in (1, 2, 3):
            bound = sum(g[max(0, p - j)] for j in range(q))
            for labels in product(range(q + 1), repeat=p):
                counts["visited_families"] += 1
                sets = [[u for u, label in enumerate(labels) if label == c] for c in range(q)]
                if not all(golomb(marks) for marks in sets):
                    continue
                counts["golomb_families"] += 1
                assert sum(map(len, sets)) <= bound
    counts.update({"p_range": [0, 8], "q_values": [1, 2, 3], "g": g})
    return counts


def check_geometry_indices():
    # Verify the physical forcing triples, including h=t and interlacing pairs.
    cases = 0
    for a, d, h, t in product(range(4), range(1, 7), range(1, 7), range(1, 7)):
        marks = sorted({a, a + h, a + t, a + t + h})
        n = max(marks) + d + 1
        for u, v in combinations(marks, 2):
            cell = (v + d, u)
            excludes_c = [(u, u), cell, (v + d, v + d)]
            excludes_b = [(u + d, u), cell, (v + d, v)]
            for triple, step in [(excludes_c, v + d - u), (excludes_b, v - u)]:
                x, y = triple[0]
                assert step > 0
                assert triple == [(x, y), (x + step, y), (x + step, y + step)]
                assert all(0 <= xx < n and 0 <= yy < n for xx, yy in triple)
        forced = [(a + h + d, a), (a + t + h + d, a), (a + t + h + d, a + t)]
        x, y = forced[0]
        assert forced == [(x, y), (x + t, y), (x + t, y + t)]
        assert len(set(forced)) == 3
        cases += 1
    return {"cases": cases, "a_range": [0, 3], "d_h_t_range": [1, 6]}


def check_cauchy_expansion():
    cases = 0
    kernels = [[1], [0, 1, 0], [1, 3, 1], [2, 0, 1, 4]]
    for n in range(1, 7):
        for colors in product(range(3), repeat=n):
            counts = [sum(colors[u] == colors[u + d] for u in range(n - d))
                      for d in range(n)]
            for weights in kernels:
                corr = pair_correlations(weights)
                energies = sum(squared_norm(convolution([int(c == color) for c in colors], weights))
                               for color in range(3))
                expanded = n * corr[0] + 2 * sum(counts[d] * corr[d]
                                                for d in range(1, min(n, len(corr))))
                full_energy = squared_norm(convolution([1] * n, weights))
                assert energies == expanded
                assert full_energy == n * corr[0] + 2 * sum(
                    (n - d) * corr[d] for d in range(1, min(n, len(corr))))
                assert 3 * energies >= full_energy
                cases += 1
    return {"cases": cases, "n_range": [1, 6], "kernels": kernels}


def capped_layer(x, y, k):
    counts = [sum(x[i] == y[len(y) - k + i] == c for i in range(k)) for c in range(3)]
    return sum(min(2, count) for count in counts)


def check_adjacent_path(certs):
    bounds = {str(k): max(min(4 * r, 2 * k - r) for r in (1, 2, 3)) for k in range(2, 9)}
    assert list(bounds.values()) == [3, 4, 6, 8, 9, 11, 12]
    x, y = [int(c) for c in "0011122"], [int(c) for c in "0001122"]
    witness = [capped_layer(x, y, k) for k in (6, 7)]
    assert witness == [5, 6]
    # Verify the graph description, separately from the universal written proof.
    for k in range(2, 65):
        edges = [(("X", i), ("Y", i)) for i in range(k)]
        edges += [(("X", i), ("Y", i + 1)) for i in range(k - 1)]
        path = [vertex for i in range(k) for vertex in [("Y", i), ("X", i)]]
        assert {frozenset(edge) for edge in edges} == {
            frozenset((path[i], path[i + 1])) for i in range(2 * k - 1)}
    applications = {}
    for cert in certs:
        b = cert["n"] - 425
        assert b >= 14  # Two disjoint seven-letter windows suffice.
        v = [cert["correlations"][b - k] for k in range(1, 8)]
        assert all(v[i] <= v[i + 1] for i in range(6))
        loss = v[2] + v[4] + v[5]
        applications[str(cert["n"])] = {"b": b, "q": 7, "v": v,
                                         "boundary_weighted_deficit": loss,
                                         "new_gap": cert["gap"] + 3 * loss}
    assert applications["464"]["boundary_weighted_deficit"] == 240395555
    assert applications["464"]["new_gap"] == 1199151808
    assert applications["463"]["boundary_weighted_deficit"] == 249859659
    assert applications["463"]["new_gap"] == -2778001795
    return {"bounds": bounds, "k7_sharp_witness": {"X": x, "Y": y, "t6_t7": witness},
            "path_topology_k_range": [2, 64], "applications": applications,
            "excluded": "The separate length-six enumeration was not audited."}


def main():
    started = datetime.now(timezone.utc).isoformat()
    before = {path.relative_to(ROOT).as_posix(): digest(path) for path in INPUTS}
    start = time.perf_counter()
    main_result = certificate()
    shorter = certificate(n=463)
    checks = {
        "symbolic_autocorrelation": symbolic_autocorrelation(),
        "packing_exhaustion": check_packing(),
        "physical_geometry_indices": check_geometry_indices(),
        "cauchy_expansion_exhaustion": check_cauchy_expansion(),
        "adjacent_path_extension": check_adjacent_path([main_result, shorter]),
    }
    # Compare only AFTER computing independently from the definitions above.
    expected = {"a0": 156809003, "lhs": 73237342535, "rhs": 72759377392,
                "gap": 477965143, "old_gap": -2799639872, "gain": 3277605015,
                "grouped_lhs": [70470797408, 1810500079, 956045048]}
    for key, value in expected.items():
        assert main_result[key] == value, (key, main_result[key], value)
    assert shorter["gap"] == -3527580772
    assert main_result["gap"] > 0
    checks["threshold_boundaries"] = {str(p): capacity(p) for p in [1, 138, 425, 426, 430, 431, 480]}
    for p in range(1, 481):
        formula = min(p, 138 + min(6, max(0, p - 425)))
        assert formula == capacity(p)
    elapsed = time.perf_counter() - start
    after = {path.relative_to(ROOT).as_posix(): digest(path) for path in INPUTS}
    assert before == after, "Audited inputs changed during the check"
    output = {"status": "PASS", "certificate": main_result, "same_kernel_at_463": shorter["gap"],
              "checks": checks, "inputs_sha256": before,
              "external_inputs": {"G24_span_lower_bound": 425, "G25_span_lower_bound": 480},
              "limitations": ["OGR exhaustive searches were not rerun", "No formal proof assistant was used",
                              "Small-case enumerations supplement the written universal proof",
                              "No optimality of 464 or of the weight sequence is claimed"]}
    output_path = HERE / "independent_counting_results.json"
    output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": 2, "claim_id": "six_class_disjoint_minima_R3_le_464",
        "repository": {"commit": "654cc044cad3d8ca6079a1931565a6ec44dcf2b5", "dirty": True,
                       "note": "Base supplied by the coordinator; no Git command was run by this reviewer. Audited working-file revisions are pinned by content hashes."},
        "command": ["python", "research/kernel_compatibility_20261108/review/independent_counting_check.py"],
        "environment": {"software": [{"name": "CPython", "version": platform.python_version()}],
                        "hardware": platform.machine() + "; " + platform.platform(),
                        "note": "Actual absolute interpreter path is omitted for portability; its observed version is recorded."},
        "mathematics": {"assertion_tested": "Exact 464 contradiction from the stated six-class capacities and parabolic weights",
                        "coefficient_domain": "Z and Q, exact Python integers and Fraction",
                        "conventions": "zero-based square; positive equal-leg L; Golomb lengths are spans",
                        "inputs": ["n=464", "N=86", "G(24)>=425", "G(25)>=480"],
                        "bounds": {"d_min": 1, "d_max": 84, "p_min": 380, "p_max": 463},
                        "non_claims": output["limitations"]},
        "randomness": {"used": False, "generator": "none", "seed": None},
        "run": {"started_at": started, "runtime_seconds": elapsed, "exit_status": 0,
                "status": "completed", "resource_limits": {"memory_bytes": None, "cpu_seconds": None,
                                                           "max_cores": None, "max_threads": None}},
        "outputs": [{"path": output_path.relative_to(ROOT).as_posix(), "sha256": digest(output_path), "kind": "result"}],
        "checks": ["Independent distance histogram and literal convolution agree",
                   "Autocorrelation identity reduced to the zero polynomial over Q",
                   "All claimed integer totals match independent outputs"],
        "result": "PASS: weighted gap 477965143; direct Cauchy deficit 955930286",
        "residual_risks": output["limitations"],
        "input_artifacts": [{"path": path, "sha256": checksum, "sha256_after": after[path]}
                            for path, checksum in before.items()],
        "declared_results": [output_path.relative_to(ROOT).as_posix()],
    }
    (HERE / "independent_counting_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "gap": main_result["gap"],
                      "direct_cauchy_deficit": main_result["cauchy_deficit"],
                      "full_convolution_energy": main_result["full_convolution_energy"],
                      "upper_color_energy": main_result["upper_color_energy"],
                      "checks": checks, "runtime_seconds": elapsed}, indent=2))


if __name__ == "__main__":
    main()
