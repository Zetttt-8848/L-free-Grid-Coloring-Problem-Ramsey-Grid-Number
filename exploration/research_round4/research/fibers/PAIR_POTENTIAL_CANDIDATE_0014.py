"""Single Phase-I dual-candidate extraction for the eight-mark pair relaxation.

Floating duals and denominator-limited fractions below are discovery material,
not an inequality certificate.  This script intentionally makes one LP call.
"""

from __future__ import annotations

import json
import time
from fractions import Fraction
from pathlib import Path

from scipy.optimize import linprog

from PAIR_MARGINAL_DISCOVERY_0014 import A, make_block_factors, make_line_factors, enumerate_states, key_pair


OUT = Path(__file__).with_name("PAIR_POTENTIAL_CANDIDATE_0014.json")


def fraction_guess(value: float) -> str:
    return str(Fraction(float(value)).limit_denominator(10000))


def main() -> None:
    started = time.monotonic()
    factors = []
    for name, vertices, corners, admissible in make_line_factors([]) + make_block_factors():
        states = enumerate_states(vertices, admissible)
        if not states:
            raise RuntimeError(f"empty local state set: {name}")
        factors.append({"name": name, "vertices": vertices, "corners": corners, "states": states})
    pair_factors = {}
    for factor_index, factor in enumerate(factors):
        for pair in factor["states"][0][1]:
            pair_factors.setdefault(pair, []).append(factor_index)
    shared = {pair: indices for pair, indices in pair_factors.items() if len(indices) >= 2}
    offsets, primal_count = [], 0
    for factor in factors:
        offsets.append(primal_count)
        primal_count += len(factor["states"])
    rows, rhs, row_meta = [], [], []
    total_variables = primal_count
    for factor_index, factor in enumerate(factors):
        row = [0.0] * total_variables
        for state_index in range(len(factor["states"])):
            row[offsets[factor_index] + state_index] = 1.0
        rows.append(row); rhs.append(1.0)
        row_meta.append({"kind": "normalization", "factor": factor_index})
    pair_rows = []
    for pair, factor_indices in sorted(shared.items()):
        reference = factor_indices[0]
        for other in factor_indices[1:]:
            row = [0.0] * total_variables
            terms = []
            for factor_index, sign in ((reference, 1), (other, -1)):
                products = []
                for state_index, (_, product_map) in enumerate(factors[factor_index]["states"]):
                    product = product_map[pair]
                    row[offsets[factor_index] + state_index] += sign * product
                    products.append(product)
                terms.append({"factor": factor_index, "sign": sign, "state_pair_products": products})
            rows.append(row); rhs.append(0.0)
            meta = {"kind": "pair", "pair": pair, "reference_factor": reference,
                    "other_factor": other, "terms": terms}
            row_meta.append(meta); pair_rows.append(meta)
    pair_start = primal_count
    pair_count = len(pair_rows)
    expanded_rows = []
    for index, row in enumerate(rows):
        expanded = row + [0.0] * (2 * pair_count)
        if index >= len(factors):
            slack_index = index - len(factors)
            expanded[pair_start + slack_index] = 1.0
            expanded[pair_start + pair_count + slack_index] = -1.0
        expanded_rows.append(expanded)
    costs = [0.0] * primal_count + [1.0] * (2 * pair_count)
    solve = linprog(c=costs, A_eq=expanded_rows, b_eq=rhs, bounds=(0, None), method="highs")
    normalization_duals = []
    pair_duals = []
    if solve.success:
        marginals = solve.eqlin.marginals
        for row_index, meta in enumerate(row_meta):
            dual = float(marginals[row_index])
            if meta["kind"] == "normalization":
                normalization_duals.append({"factor": meta["factor"], "factor_name": factors[meta["factor"]]["name"],
                                            "local_lower_target": dual, "fraction_guess": fraction_guess(dual)})
            else:
                pair_duals.append({
                    "pair": [list(meta["pair"][0]), list(meta["pair"][1])],
                    "reference_factor": meta["reference_factor"], "other_factor": meta["other_factor"],
                    "pair_row_dual": dual, "candidate_potential_negative_dual": -dual,
                    "fraction_guess_negative_dual": fraction_guess(-dual),
                    "terms": meta["terms"],
                })
    output = {
        "purpose": "one Phase-I floating dual candidate; not a certificate, verification, or proved inequality",
        "marks": A,
        "solver": "scipy.optimize.linprog(method=highs)",
        "status": solve.message,
        "phase_i_total_slack": float(solve.fun) if solve.success else None,
        "primal_probability_variables": primal_count,
        "pair_consistency_rows": pair_count,
        "slack_variables": 2 * pair_count,
        "normalization_rows": len(factors),
        "factor_states": [{"index": i, "name": factor["name"], "vertices": [list(v) for v in factor["vertices"]],
                           "states_mod_global_reversal": [list(signs) for signs, _ in factor["states"]]}
                          for i, factor in enumerate(factors)],
        "pair_coefficient_mapping": pair_duals,
        "normalization_duals": normalization_duals,
        "positive_target_factors": [entry for entry in normalization_duals if entry["local_lower_target"] > 1e-9],
        "nonzero_candidate_potential_support": [entry for entry in pair_duals if abs(entry["candidate_potential_negative_dual"]) > 1e-9],
        "seconds": time.monotonic() - started,
        "scope": "Fractions are denominator-limited formatting of floating output. No recheck, dual polishing, or proof claim was performed.",
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "phase_i_total_slack": output["phase_i_total_slack"],
        "positive_target_factor_count": len(output["positive_target_factors"]),
        "nonzero_candidate_potential_count": len(output["nonzero_candidate_potential_support"]),
        "seconds": output["seconds"],
    }))


if __name__ == "__main__":
    main()
