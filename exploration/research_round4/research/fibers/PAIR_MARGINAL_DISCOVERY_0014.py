"""One pair-marginal feasibility relaxation for the prescribed eight-mark source.

This is bounded discovery only: factor states are enumerated directly and one
HiGHS feasibility call enforces agreement of pair-product expectations.
"""

from __future__ import annotations

import itertools
import json
import time
from collections import defaultdict, Counter
from pathlib import Path

from scipy.optimize import linprog


A = [0, 1, 2, 3, 4, 6, 7, 8]
OUT = Path(__file__).with_name("PAIR_MARGINAL_DISCOVERY_0014.json")
TIME_LIMIT = 120.0


def key_pair(p, q):
    return tuple(sorted((p, q)))


def enumerate_states(vertices, admissible):
    """Enumerate signs modulo global reversal by fixing the first sign to +1."""
    states = []
    for tail in itertools.product((-1, 1), repeat=max(0, len(vertices) - 1)):
        signs = (1,) + tail
        assign = dict(zip(vertices, signs))
        if admissible(assign):
            products = {key_pair(p, q): assign[p] * assign[q]
                        for p, q in itertools.combinations(vertices, 2)}
            states.append((signs, products))
    return states


def make_line_factors(corners):
    factors = []
    source = set(A)
    for d in range(1, A[-1] - A[0] + 1):
        vertices = [(x + d, x) for x in A if x + d in source]
        if vertices:
            factors.append((f"D:{d}", tuple(vertices), [], lambda _: True))
    for v in A:
        vertices = [(v, u) for u in A if u < v]
        if vertices:
            factors.append((f"R:{v}", tuple(vertices), [], lambda _: True))
    for u in A:
        vertices = [(v, u) for v in A if v > u]
        if vertices:
            factors.append((f"C:{u}", tuple(vertices), [], lambda _: True))
    return factors


def make_block_factors():
    source = set(A)
    factors = []
    for d in range(1, A[-1] - A[0] + 1):
        for e in range(d + 1, A[-1] - A[0] + 1):
            starts = [x for x in A if x + d in source and x + e - d in source and x + e in source]
            if not starts:
                continue
            corners = [((x + d, x), (x + e, x), (x + e, x + e - d), x) for x in starts]
            vertices = tuple(sorted({cell for left, middle, right, _ in corners for cell in (left, middle, right)}))

            def admissible(assign, corners=corners):
                by_sign = {s: {"J": [], "C": [], "R": []} for s in (-1, 1)}
                for left, middle, right, x in corners:
                    if assign[left] == assign[middle] == assign[right]:
                        return False
                    s = assign[middle]
                    if assign[left] == assign[right] == -s:
                        by_sign[s]["J"].append(x)
                    elif assign[left] == s and assign[right] == -s:
                        by_sign[s]["C"].append(x)
                    elif assign[left] == -s and assign[right] == s:
                        by_sign[s]["R"].append(x)
                    else:
                        return False
                for groups in by_sign.values():
                    if len(groups["J"]) > 1:
                        return False
                    if groups["C"] and groups["R"] and max(groups["C"]) >= min(groups["R"]):
                        return False
                return True

            factors.append((f"B:{d},{e}", vertices, corners, admissible))
    return factors


def main() -> None:
    started = time.monotonic()
    raw_factors = make_line_factors([]) + make_block_factors()
    factors = []
    for name, vertices, corners, admissible in raw_factors:
        if time.monotonic() - started > TIME_LIMIT:
            raise TimeoutError("state enumeration exceeded the 120-second cap")
        states = enumerate_states(vertices, admissible)
        if not states:
            raise RuntimeError(f"empty local state set: {name}")
        factors.append({"name": name, "vertices": vertices, "corners": corners, "states": states})

    pair_factors = defaultdict(list)
    for factor_index, factor in enumerate(factors):
        for pair in factor["states"][0][1]:
            pair_factors[pair].append(factor_index)
    shared = {pair: indices for pair, indices in pair_factors.items() if len(indices) >= 2}

    variable_offsets = []
    count = 0
    for factor in factors:
        variable_offsets.append(count)
        count += len(factor["states"])
    equalities = []
    rhs = []
    for factor_index, factor in enumerate(factors):
        row = [0.0] * count
        base = variable_offsets[factor_index]
        for state_index in range(len(factor["states"])):
            row[base + state_index] = 1.0
        equalities.append(row)
        rhs.append(1.0)
    for pair, factor_indices in shared.items():
        reference = factor_indices[0]
        for other in factor_indices[1:]:
            row = [0.0] * count
            for state_index, (_, products) in enumerate(factors[reference]["states"]):
                row[variable_offsets[reference] + state_index] += products[pair]
            for state_index, (_, products) in enumerate(factors[other]["states"]):
                row[variable_offsets[other] + state_index] -= products[pair]
            equalities.append(row)
            rhs.append(0.0)
    if time.monotonic() - started > TIME_LIMIT:
        raise TimeoutError("LP construction exceeded the 120-second cap")
    solve = linprog(c=[0.0] * count, A_eq=equalities, b_eq=rhs, bounds=(0, None), method="highs")
    output = {
        "purpose": "one pair-marginal feasibility relaxation; floating discovery only",
        "marks": A,
        "solver": "scipy.optimize.linprog(method=highs)",
        "status": solve.message,
        "feasible": bool(solve.success),
        "seconds": time.monotonic() - started,
        "factors": [{"name": factor["name"], "vertices": [list(v) for v in factor["vertices"]],
                     "corner_count": len(factor["corners"]), "state_count": len(factor["states"])}
                    for factor in factors],
        "variable_count": count,
        "normalization_equalities": len(factors),
        "shared_pairs": len(shared),
        "pair_consistency_equalities": len(equalities) - len(factors),
        "scope": "No global SAT, dual optimization, or proof claim is made from this one LP.",
    }
    if solve.success:
        marginals = []
        for pair, factor_indices in sorted(shared.items()):
            factor_index = factor_indices[0]
            expected = sum(solve.x[variable_offsets[factor_index] + state_index] * products[pair]
                           for state_index, (_, products) in enumerate(factors[factor_index]["states"]))
            marginals.append({"pair": [list(pair[0]), list(pair[1])], "factors": len(factor_indices),
                              "expectation": float(expected)})
        output["shared_pair_expectation_histogram_rounded_6"] = dict(
            sorted(Counter(f"{entry['expectation']:.6f}" for entry in marginals).items()))
        output["shared_pair_marginals"] = marginals
        support = []
        for factor_index, factor in enumerate(factors):
            entries = []
            for state_index, (signs, _) in enumerate(factor["states"]):
                weight = solve.x[variable_offsets[factor_index] + state_index]
                if weight > 1e-9:
                    entries.append({"signs": list(signs), "weight": float(weight)})
            support.append({"name": factor["name"], "positive_states": entries})
        output["factor_distribution_support"] = support
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: output[key] for key in ("feasible", "seconds", "variable_count", "shared_pairs", "pair_consistency_equalities")}))


if __name__ == "__main__":
    main()
