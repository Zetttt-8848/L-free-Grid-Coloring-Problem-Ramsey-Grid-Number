"""Independent exact audit for Round-3 cores C and L.

This program does not import or execute any author checker or generator.  It
reconstructs every finite assertion from the literal mathematical definitions
and treats the author JSON files only as certificates/data to be checked.
"""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
import platform
import subprocess
import time


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def read_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def file_sha(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def is_corner(corner: tuple[tuple[int, int], ...]) -> bool:
    if len(corner) != 3:
        return False
    (x, y), (x2, y2), (x3, y3) = corner
    d = x2 - x
    return d > 0 and y2 == y and x3 == x2 and y3 == y + d


def ap5_and_weak_triangle_audit() -> dict:
    points = tuple((j, i) for j in range(5) for i in range(j + 1))
    point_set = set(points)
    corners = []
    for x, y in points:
        for d in range(1, 5):
            c = ((x, y), (x + d, y), (x + d, y + d))
            if all(p in point_set for p in c):
                corners.append(c)
    assert len(points) == 15
    assert len(corners) == 20

    valid = 0
    minimum_mono = len(corners)
    for mask in range(1 << len(points)):
        colors = {p: (mask >> i) & 1 for i, p in enumerate(points)}
        mono = sum(len({colors[p] for p in c}) == 1 for c in corners)
        minimum_mono = min(minimum_mono, mono)
        valid += mono == 0
    assert valid == 0
    assert minimum_mono >= 1

    translated = {(j + 1, i) for j, i in points}
    strict_t6 = {(r, s) for r in range(1, 6) for s in range(r)}
    assert translated == strict_t6

    ap5_count_464 = sum(464 - 4 * a for a in range(1, 116))
    assert ap5_count_464 == 26680
    return {
        "weak_triangle_points": len(points),
        "weak_triangle_corners": len(corners),
        "assignments_exhausted": 1 << len(points),
        "corner_free_assignments": valid,
        "minimum_monochromatic_corners": minimum_mono,
        "translation_to_strict_T6_exact": True,
        "ap5_occurrences_at_n464": ap5_count_464,
    }


def positive_differences(marks: list[int]) -> list[int]:
    return [b - a for a, b in combinations(marks, 2)]


def ap5_count(marks: set[int]) -> int:
    if not marks:
        return 0
    lo, hi = min(marks), max(marks)
    total = 0
    for a in range(1, (hi - lo) // 4 + 1):
        for x in range(lo, hi - 4 * a + 1):
            total += all(x + i * a in marks for i in range(5))
    return total


def pair_forcing_audit() -> dict:
    cert = read_json("research_round3/cap/pair_forcing_certificate.json")
    rulers = {int(k): list(v) for k, v in cert["rulers"].items()}
    golomb_counts = {}
    for order, ruler in rulers.items():
        assert len(ruler) == order and ruler[0] == 0
        diffs = positive_differences(ruler)
        assert len(diffs) == comb(order, 2)
        assert len(set(diffs)) == len(diffs)
        golomb_counts[str(order)] = len(diffs)

    expected = {}
    for order, ruler in rulers.items():
        span = ruler[-1]
        for reflected in (False, True):
            for shift in range(1, 462 - span + 1):
                transformed = {
                    shift + (span - r if reflected else r) for r in ruler
                }
                if set(ruler).isdisjoint(transformed):
                    expected[(order, reflected, shift)] = transformed

    cases = cert["cases"]
    actual_keys = [(c["order"], c["reflected"], c["shift"]) for c in cases]
    assert len(actual_keys) == len(set(actual_keys))
    assert set(actual_keys) == set(expected)
    assert len(cases) == 60

    total_steps = 0
    ap5_free = 0
    special = None
    order_counts = Counter()
    reflection_counts = Counter()
    for case in cases:
        order = case["order"]
        reflected = case["reflected"]
        shift = case["shift"]
        key = (order, reflected, shift)
        base = set(rulers[order])
        second = expected[key]
        F = set(case["F"])
        assert F == base | second
        assert base.isdisjoint(second)
        assert len(F) == 2 * order
        assert min(F) == 0 and max(F) <= 462

        domain = {(x, y) for x in F for y in F if y <= x}
        colors = {(z, z): 0 for z in base}
        colors.update({(z, z): 1 for z in second})
        assert len(colors) == len(F)

        for step in case["steps"]:
            point = tuple(step["point"])
            color = int(step["color"])
            corner = tuple(tuple(p) for p in step["corner"])
            assert color in (0, 1)
            assert point in domain and point not in colors
            assert is_corner(corner)
            assert all(p in domain for p in corner)
            assert point in corner
            other = [p for p in corner if p != point]
            assert len(other) == 2
            assert all(p in colors for p in other)
            assert colors[other[0]] == colors[other[1]] == 1 - color
            colors[point] = color
            total_steps += 1

        conflict = tuple(tuple(p) for p in case["conflict"])
        assert is_corner(conflict)
        assert all(p in domain and p in colors for p in conflict)
        assert len({colors[p] for p in conflict}) == 1

        count5 = ap5_count(F)
        assert count5 == case["five_ap_count"]
        ap5_free += count5 == 0
        order_counts[order] += 1
        reflection_counts[reflected] += 1
        if key == (24, True, 2):
            special = {
                "points": len(F),
                "five_ap_count": count5,
                "steps": len(case["steps"]),
                "span": max(F) - min(F),
            }

    assert total_steps == 16425
    assert ap5_free == 59
    assert special == {"points": 48, "five_ap_count": 0, "steps": 192, "span": 427}
    return {
        "ruler_difference_counts": golomb_counts,
        "configuration_count": len(cases),
        "configuration_orders": {str(k): v for k, v in sorted(order_counts.items())},
        "configuration_reflections": {
            str(k).lower(): v for k, v in sorted(reflection_counts.items())
        },
        "forcing_steps_checked": total_steps,
        "five_ap_free_unions": ap5_free,
        "special_R24_reflection_shift2": special,
        "coverage_reconstructed_from_literal_family": True,
    }


H_TABLE = [
    0, 1, 2, 4, 7, 12, 18, 26, 35, 45, 56, 73, 86, 107, 128,
    152, 178, 200, 217, 247, 284, 334, 357, 373, 426, 481, 493,
    554, 586,
]
ELL_WINDOW = [
    0, 1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 18, 19,
    21, 22, 24, 25, 26, 27, 28, 30, 31, 33, 34, 36, 37, 38, 39,
]


def q_from_positions(number_of_positions: int) -> int:
    return max(i for i, h in enumerate(H_TABLE) if h <= number_of_positions)


def multiplicity_cap(n: int, d: int, profile: str) -> int:
    # The remaining source interval has n-d positions and span n-d-1.
    inherited = 2 * q_from_positions(n - d)
    if profile == "45" and d <= 27:
        return min(inherited, 45)
    if profile == "46+3":
        if d <= 3:
            return min(inherited, 45)
        if d <= 27:
            return min(inherited, 46)
    return inherited


def smallest_multiset_sum(n: int, H: int, profile: str) -> tuple[int, int]:
    remaining = H
    total = 0
    last = 0
    for d in range(1, n):
        take = min(remaining, multiplicity_cap(n, d, profile))
        total += take * d
        remaining -= take
        if take:
            last = d
        if remaining == 0:
            return total, last
    raise AssertionError("profile has too few distance copies")


def endpoint_witness(n: int, s: int, c: int, profile: str, ell: list[int]) -> dict:
    H = c * s - c * (c + 1) // 2
    minimum, last = smallest_multiset_sum(n, H, profile)
    correction = 2 * sum((c - i) * ell[i] for i in range(c))
    upper = (n - 1) * c * (c + 1) // 2 - correction
    return {
        "n": n,
        "s": s,
        "c": c,
        "H": H,
        "minimum": minimum,
        "upper": upper,
        "margin": minimum - upper,
        "last_distance": last,
        "correction": correction,
        "profile": profile,
    }


def endpoint_audit() -> dict:
    identity_checks = 0
    for mask in range(1 << 10):
        marks = [i for i in range(10) if (mask >> i) & 1]
        s = len(marks)
        if s < 2:
            continue
        L = marks[-1] - marks[0]
        for c in range(1, s):
            direct = sum(
                marks[h + j] - marks[h]
                for j in range(1, c + 1)
                for h in range(s - j)
            )
            telescoped = sum(
                (c - i) * (marks[s - 1 - i] - marks[i])
                for i in range(c)
            )
            correction = 2 * sum((c - i) * i for i in range(c))
            upper = L * c * (c + 1) // 2 - correction
            assert direct == telescoped
            assert direct <= upper
            assert correction == 2 * comb(c + 1, 3)
            identity_checks += 1

    # Source-position convention: H_24=426, so at n=464 cap 48 lasts
    # through d=38 (464-38=426 positions) and becomes 46 at d=39.
    assert multiplicity_cap(464, 38, "inherited") == 48
    assert multiplicity_cap(464, 39, "inherited") == 46

    actual = endpoint_witness(464, 159, 13, "inherited", list(range(13)))
    conditional45 = endpoint_witness(454, 152, 11, "45", ELL_WINDOW)
    conditional46_3 = endpoint_witness(464, 155, 10, "46+3", ELL_WINDOW)
    assert actual == {
        "n": 464, "s": 159, "c": 13, "H": 1976,
        "minimum": 41676, "upper": 41405, "margin": 271,
        "last_distance": 42, "correction": 728, "profile": "inherited",
    }
    assert conditional45 == {
        "n": 454, "s": 152, "c": 11, "H": 1606,
        "minimum": 29414, "upper": 29390, "margin": 24,
        "last_distance": 36, "correction": 508, "profile": "45",
    }
    assert conditional46_3 == {
        "n": 464, "s": 155, "c": 10, "H": 1495,
        "minimum": 25110, "upper": 25091, "margin": 19,
        "last_distance": 33, "correction": 374, "profile": "46+3",
    }
    return {
        "direct_identity_checks": identity_checks,
        "source_position_transition_n464": {"d38": 48, "d39": 46},
        "actual_inherited_bound_158": actual,
        "conditional_45_profile_n454": conditional45,
        "conditional_46_plus_first3to45_n464": conditional46_3,
        "window_ell_dependency": ELL_WINDOW,
        "conditional_profiles_are_not_cap_theorems": True,
    }


def all_subsets(items: list[int]):
    for mask in range(1 << len(items)):
        yield {items[i] for i in range(len(items)) if (mask >> i) & 1}


def fiber(A: set[int], d: int) -> set[int]:
    return {u for u in A if u + d in A}


def Q(B: set[int], d: int) -> set[tuple[int, int]]:
    return {(v + d, u) for u in B for v in B if u < v}


def overlap_audit() -> dict:
    cases = 0
    sum_overlap = 0
    for n in range(1, 8):
        for A in all_subsets(list(range(n))):
            fibers = {d: fiber(A, d) for d in range(1, n)}
            for d in range(1, n):
                for e in range(d + 1, n):
                    delta = e - d
                    for Bd in all_subsets(sorted(fibers[d])):
                        for Be in all_subsets(sorted(fibers[e])):
                            qd, qe = Q(Bd, d), Q(Be, e)
                            intersection = qd & qe
                            C = Bd & Be
                            D = {q for q in Be if q + delta in Bd}
                            formula = sum(u < q for q in D for u in C)
                            assert len(intersection) == formula

                            X = {u for u in A if u + d in A and u + e in A}
                            Y = {q for q in A if q + delta in A and q + e in A}
                            assert C <= X and D <= Y
                            caps = [len(fibers[d]), len(fibers[e]), len(fibers[delta])]
                            assert len(X) <= min(caps) and len(Y) <= min(caps)
                            J = sum(u < q for u in X for q in Y)
                            bound = min(
                                comb(len(Bd), 2), comb(len(Be), 2),
                                J, min(caps) ** 2,
                            )
                            assert len(intersection) <= bound

                            M = len(qd) + len(qe)
                            if M:
                                lower = (M * M + (M + 2 * len(intersection)) - 1) // (
                                    M + 2 * len(intersection)
                                )
                                assert len(qd | qe) >= lower
                            cases += 1
                            sum_overlap += len(intersection)
    assert cases == 26104
    assert sum_overlap == 3491

    A = {1, 4, 8, 14, 18, 21}
    d, e = 3, 7
    Bd, Be = {1, 18}, {1, 14}
    qd, qe = Q(Bd, d), Q(Be, e)
    C = Bd & Be
    D = {q for q in Be if q + (e - d) in Bd}
    witness = {
        "Bd_subset_Fd": Bd <= fiber(A, d),
        "Be_subset_Fe": Be <= fiber(A, e),
        "C": sorted(C),
        "D": sorted(D),
        "Qd": sorted(map(list, qd)),
        "Qe": sorted(map(list, qe)),
        "M": len(qd) + len(qe),
        "O": len(qd & qe),
        "union": len(qd | qe),
        "cauchy_lower": Fraction((len(qd) + len(qe)) ** 2,
                                  len(qd) + len(qe) + 2 * len(qd & qe)).numerator,
    }
    assert witness == {
        "Bd_subset_Fd": True, "Be_subset_Fe": True,
        "C": [1], "D": [14], "Qd": [[21, 1]], "Qe": [[21, 1]],
        "M": 2, "O": 1, "union": 1, "cauchy_lower": 1,
    }
    return {
        "direct_cases_n1_through_n7": cases,
        "sum_intersection_sizes": sum_overlap,
        "ordered_bijection_and_bounds_pass": True,
        "saturation_witness": witness,
    }


def parse_dimacs(path: Path) -> tuple[int, int, list[tuple[int, ...]]]:
    variables = declared = None
    clauses = []
    current = []
    for line in path.read_text(encoding="ascii").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("c"):
            continue
        if stripped.startswith("p "):
            _, fmt, nv, nc = stripped.split()
            assert fmt == "cnf" and variables is None
            variables, declared = int(nv), int(nc)
            continue
        for token in map(int, stripped.split()):
            if token == 0:
                clauses.append(tuple(current))
                current = []
            else:
                current.append(token)
    assert variables is not None and declared is not None and not current
    assert declared == len(clauses)
    assert all(clause and all(1 <= abs(lit) <= variables for lit in clause)
               for clause in clauses)
    return variables, declared, clauses


def variable(n: int, x: int, y: int, color: int) -> int:
    return 3 * (n * x + y) + color + 1


def reconstruct_n21() -> tuple[list[tuple[int, ...]], dict]:
    n = 21
    clauses = []
    cell_clauses = 0
    for x in range(n):
        for y in range(n):
            v = [variable(n, x, y, c) for c in range(3)]
            clauses.extend([tuple(v), (-v[0], -v[1]), (-v[0], -v[2]), (-v[1], -v[2])])
            cell_clauses += 4
    corners = 0
    for x in range(n):
        for y in range(n):
            for d in range(1, min(n - x, n - y)):
                for color in range(3):
                    clauses.append(tuple(-variable(n, px, py, color) for px, py in (
                        (x, y), (x + d, y), (x + d, y + d)
                    )))
                corners += 1
    before_symmetry = len(clauses)

    clauses.append((variable(n, 0, 0, 0),))
    # Row-major positions 1,...,440: color 2 may occur only after a prior
    # occurrence of color 1 among positions 1,...,p-1. Position 0 is fixed 0.
    for p in range(1, n * n):
        x, y = divmod(p, n)
        clause = [-variable(n, x, y, 2)]
        for prior in range(1, p):
            px, py = divmod(prior, n)
            clause.append(variable(n, px, py, 1))
        clauses.append(tuple(clause))
    assert corners == 2870
    assert cell_clauses == 1764
    assert before_symmetry == 10374
    assert len(clauses) == 10815
    return clauses, {
        "variables": 1323,
        "geometric_corners": corners,
        "cell_clauses": cell_clauses,
        "corner_clauses": 3 * corners,
        "clauses_before_symmetry": before_symmetry,
        "symmetry_clauses": 441,
        "total_clauses": len(clauses),
    }


def unit_propagation(
    clauses: list[tuple[int, ...]], variables: int, assumptions: list[int]
) -> tuple[bool, int]:
    occurrence: dict[int, list[int]] = {}
    for ci, clause in enumerate(clauses):
        for lit in clause:
            occurrence.setdefault(lit, []).append(ci)
    assigned = [0] * (variables + 1)
    remaining = [len(c) for c in clauses]
    satisfied = [False] * len(clauses)
    queue = [c[0] for c in clauses if len(c) == 1] + list(assumptions)
    head = 0
    while head < len(queue):
        lit = queue[head]
        head += 1
        var = abs(lit)
        value = 1 if lit > 0 else -1
        if assigned[var]:
            if assigned[var] != value:
                return True, sum(v != 0 for v in assigned)
            continue
        assigned[var] = value
        for ci in occurrence.get(lit, []):
            satisfied[ci] = True
        for ci in occurrence.get(-lit, []):
            if satisfied[ci]:
                continue
            remaining[ci] -= 1
            if remaining[ci] == 0:
                return True, sum(v != 0 for v in assigned)
            if remaining[ci] == 1:
                unit = None
                for candidate in clauses[ci]:
                    if assigned[abs(candidate)] == 0:
                        assert unit is None
                        unit = candidate
                assert unit is not None
                queue.append(unit)
    return False, sum(v != 0 for v in assigned)


def lower_audit() -> dict:
    expected, counts = reconstruct_n21()
    cnf_path = ROOT / "research_round3/lower/n21_exact.cnf"
    variables, declared, actual = parse_dimacs(cnf_path)
    assert variables == counts["variables"] and declared == counts["total_clauses"]
    assert Counter(actual) == Counter(expected)
    assert len(set(actual)) == len(actual)
    cnf_hash = file_sha("research_round3/lower/n21_exact.cnf")
    assert cnf_hash == "49a989044d4255e7aba75a0b45256a7b480172b8f121545eeaf350164177f8e5"

    cube_data = read_json("research_round3/lower/n21_cubes.json")
    cubes = cube_data["records"]
    split = [tuple(p) for p in cube_data["split_cells_0_based"]]
    assert split == [(0, 1), (1, 0), (1, 1), (20, 20)]
    assert len(cubes) == 81
    tuples = {tuple(c["cube_colors_0_based"]) for c in cubes}
    assert tuples == {
        (a, b, c, d) for a in range(3) for b in range(3)
        for c in range(3) for d in range(3)
    }
    assert {c["order"] for c in cubes} == set(range(81))
    for cube in cubes:
        expected_lits = [variable(21, x, y, color) for (x, y), color in zip(
            split, cube["cube_colors_0_based"]
        )]
        assert cube["assumption_literals"] == expected_lits

    up_conflicts = set()
    up_assigned = {}
    for cube in cubes:
        conflict, assigned_count = unit_propagation(
            actual, variables, cube["assumption_literals"]
        )
        up_assigned[str(cube["order"])] = assigned_count
        if conflict:
            up_conflicts.add(cube["order"])
    assert len(up_conflicts) == 33

    easy_manifest = read_json("research_round3/lower/n21_quick_cube_proofs.json")
    easy_records = easy_manifest["records"]
    easy_orders = {r["order"] for r in easy_records}
    assert len(easy_records) == 33 and len(easy_orders) == 33
    assert easy_orders == up_conflicts
    cube_by_order = {c["order"]: c for c in cubes}
    for record in easy_records:
        cube = cube_by_order[record["order"]]
        assert record["assumption_literals"] == cube["assumption_literals"]
        assert record["cube_colors_0_based"] == cube["cube_colors_0_based"]

    hard_data = read_json("research_round3/lower/n21_stage2_portfolio_merged.json")
    hard_records = hard_data["records"]
    hard_orders = {r["order"] for r in hard_records}
    assert len(hard_records) == 48 and len(hard_orders) == 48
    assert hard_data["actual_records"] == hard_data["expected_hard_cubes"] == 48
    assert hard_data["audit_pass"] is True and hard_data["sat_found"] is False
    assert hard_data["mathematical_status"] == "UNDECIDED_48_INTERRUPTED"
    assert hard_orders == set(range(81)) - easy_orders
    assert easy_orders.isdisjoint(hard_orders)
    assert all(r["status"] == "INTERRUPTED_UNDECIDED" for r in hard_records)
    assert all(r.get("proof_path") is None and r.get("proof_sha256") is None
               for r in hard_records)
    assert all(r.get("proof_lines") is None for r in hard_records)
    for record in hard_records:
        cube = cube_by_order[record["order"]]
        assert record["assumption_literals"] == cube["assumption_literals"]
        assert record["cube_colors_0_based"] == cube["cube_colors_0_based"]
    assert not (hard_orders & up_conflicts)

    global_audit = read_json("research_round3/lower/n21_global_checkpoint_audit.json")
    assert global_audit["certified_unit_unsat_cubes"] == 33
    assert global_audit["unresolved_hard_cubes"] == 48
    assert global_audit["mathematical_status"] == "UNDECIDED"

    matrix_path = ROOT / "research_round3/lower/difference_circulant_n3.txt"
    matrix = [list(map(int, line.split())) for line in matrix_path.read_text().splitlines() if line.strip()]
    assert len(matrix) == 3 and all(len(row) == 3 for row in matrix)
    assert {value for row in matrix for value in row} == {1, 2, 3}
    assert matrix == [[((y - x) % 3) + 1 for y in range(3)] for x in range(3)]
    inspected = violations = 0
    for x in range(3):
        for y in range(3):
            for d in range(1, min(3 - x, 3 - y)):
                inspected += 1
                colors = [matrix[x][y], matrix[x + d][y], matrix[x + d][y + d]]
                violations += len(set(colors)) == 1
    assert inspected == 5 and violations == 0

    return {
        "cnf_counts": counts,
        "cnf_sha256": cnf_hash,
        "clause_multiset_exact_match": True,
        "all_clauses_unique": True,
        "color_symmetry_normalization": {
            "fixed_first_cell_clause": [1],
            "restricted_growth_clauses": 440,
            "sound_by_residual_color_swap": True,
        },
        "cubes": {
            "count": len(cubes),
            "unique_color_tuples": len(tuples),
            "cover_all_3_power_4": True,
            "pairwise_disjoint_under_one_hot": True,
        },
        "unit_propagation": {
            "all_cubes_checked": 81,
            "contradictory": len(up_conflicts),
            "unresolved_by_unit_propagation": 81 - len(up_conflicts),
            "contradictory_orders": sorted(up_conflicts),
            "assigned_variable_counts_by_order": up_assigned,
        },
        "hard_portfolio": {
            "records": len(hard_records),
            "exact_complement_of_easy": True,
            "all_statuses": "INTERRUPTED_UNDECIDED",
            "proofs_or_witnesses": 0,
        },
        "side21_status": "UNDECIDED",
        "difference_circulant_n3": {
            "matrix": matrix,
            "corners_checked": inspected,
            "violations": violations,
            "formula_exact": True,
        },
        "difference_circulant_universal_ceiling": {
            "maximum_side": 3,
            "proof_basis": "for every i<j, corner (i,0),(j,0),(j,j-i) forces f(-i)!=f(-j)",
            "equality_witness_checked": True,
        },
    }


def main() -> None:
    started = datetime.now(timezone.utc)
    start_clock = time.perf_counter()
    results = {
        "schema": "round3_independent_core_C_L_audit_v1",
        "reviewer": "setup_sol / GPT-5.6 Sol xhigh",
        "independence": "fresh implementation; no author code imported or executed",
        "ap5": ap5_and_weak_triangle_audit(),
        "pair_forcing": pair_forcing_audit(),
        "endpoint": endpoint_audit(),
        "overlap": overlap_audit(),
        "lower": lower_audit(),
    }
    results["verdicts"] = {
        "C_AP5": "PASS",
        "C_endpoint": "PASS",
        "C_pair_forcing_finite_family": "PASS",
        "C_overlap": "PASS",
        "L_encoding_and_cube_cover": "PASS",
        "L_33_easy_cube_UP": "PASS",
        "L_48_hard_cube_accounting": "PASS_UNDECIDED",
        "L_difference_circulant": "PASS",
        "L_side21_decision": "UNDECIDED",
    }
    results["input_sha256"] = {
        rel: file_sha(rel) for rel in [
            "research_round3/cap/pair_forcing_certificate.json",
            "research_round3/lower/n21_exact.cnf",
            "research_round3/lower/n21_cubes.json",
            "research_round3/lower/n21_quick_cube_proofs.json",
            "research_round3/lower/n21_stage2_portfolio_merged.json",
            "research_round3/lower/n21_global_checkpoint_audit.json",
            "research_round3/lower/difference_circulant_n3.txt",
        ]
    }
    results["runtime_seconds"] = time.perf_counter() - start_clock
    result_path = OUT / "independent_audit_results.json"
    result_path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        dirty = bool(subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        ).strip())
    except Exception:
        commit, dirty = "unavailable", True
    manifest = {
        "schema_version": 1,
        "claim_id": "R3-C-L-independent-review-setup-sol",
        "repository": {"commit": commit, "dirty": dirty},
        "command": "python research_round3/audits/setup_sol/independent_audit.py",
        "environment": {
            "software": [f"Python {platform.python_version()}"],
            "hardware": f"{platform.system()} {platform.machine()}",
        },
        "mathematics": {
            "assertion_tested": "Exact finite assertions and arithmetic in Round-3 cores C and L",
            "coefficient_domain": "integers, finite Boolean assignments, and exact rational arithmetic",
            "conventions": "zero-based CNF cells; corner (x,y),(x+d,y),(x+d,y+d); source cap q(n-d)",
            "inputs": [
                {"path": rel, "sha256": digest}
                for rel, digest in results["input_sha256"].items()
            ],
            "bounds": {
                "W5_assignments": 32768,
                "pair_configurations": 60,
                "forcing_steps": 16425,
                "overlap_n_max": 7,
                "n21_cubes": 81,
            },
            "non_claims": [
                "No 45- or 46-profile cap theorem is proved.",
                "The side-21 Ramsey instance is not decided.",
                "The finite ruler family does not cover all Golomb rulers.",
                "The window-13 ell table is used as a named external project dependency.",
            ],
        },
        "randomness": {"used": False, "generator": "none", "seed": None},
        "run": {
            "started_at": started.isoformat(),
            "runtime_seconds": results["runtime_seconds"],
            "exit_status": 0,
        },
        "outputs": [{
            "path": "research_round3/audits/setup_sol/independent_audit_results.json",
            "sha256": sha256(result_path.read_bytes()).hexdigest(),
        }],
        "checks": [
            "literal geometry reconstruction",
            "complete finite enumeration",
            "exact integer arithmetic",
            "fresh DIMACS reconstruction",
            "fresh direct unit propagation",
            "certificate coverage and complement checks",
        ],
        "result": "PASS for all scoped C/L claims; side-21 remains UNDECIDED",
        "residual_risks": [
            "The accepted window-13 spacing profile was not independently re-enumerated in this assignment.",
            "Interrupted hard-cube telemetry cannot prove SAT or UNSAT.",
        ],
    }
    (OUT / "computation_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "status": "PASS",
        "runtime_seconds": results["runtime_seconds"],
        "result_sha256": manifest["outputs"][0]["sha256"],
        "verdicts": results["verdicts"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
