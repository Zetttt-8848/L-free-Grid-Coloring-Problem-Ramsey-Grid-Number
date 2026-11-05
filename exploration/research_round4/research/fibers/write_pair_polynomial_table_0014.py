"""Lay out fixed integer polynomial definitions from the saved discovery data.

This writes a mathematical table; it does not solve an optimization problem,
evaluate local bounds, or perform a verification pass.
"""
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'PAIR_POTENTIAL_CANDIDATE_0014.json').read_text())
factors = data['factor_states']
coefficients = defaultdict(lambda: defaultdict(Fraction))
transfers = []
for entry in data['nonzero_candidate_potential_support']:
    value = 5 * Fraction(entry['fraction_guess_negative_dual'])
    pair = tuple(tuple(v) for v in entry['pair'])
    f, g = entry['reference_factor'], entry['other_factor']
    coefficients[f][pair] += value
    coefficients[g][pair] -= value
    transfers.append((f, g, pair, value))

lines = ['# Integer pair-polynomial definitions for the eight-mark source', '',
         'Companion to EIGHT_MARK_PAIR_OBSTRUCTION_0014.md. The coefficients',
         'are fixed exact definitions. The local inequality derivations are',
         'in that proof and its cited auxiliary algebra notes.', '',
         'For each factor, its signs s1,s2,... follow the displayed vertex order.',
         'A coefficient list (i,j:c) means the term c*s_i*s_j. An omitted',
         'coefficient is zero. The lower column records the bound derived in',
         'the proof, not a solver status.', '']
for f, target in zip(factors, data['normalization_duals']):
    terms = {pair: v for pair, v in coefficients[f['index']].items() if v}
    if not terms:
        continue
    pos = {tuple(v): i + 1 for i, v in enumerate(f['vertices'])}
    lines += [f"## {f['name']}", '',
              'Vertex order: ' + ', '.join(f'{i+1}=({v[0]},{v[1]})'
                                         for i, v in enumerate(f['vertices'])) + '.', '',
              '```text',
              '  '.join(f'({pos[pair[0]]},{pos[pair[1]]}:{value})'
                        for pair, value in terms.items()),
              '```', '',
              'Lower bound: ' + str(5 * Fraction(target['fraction_guess'])) + '.', '']
lines += ['## Definition by cancelling transfers', '',
          'An entry F, G, p, q, c adds c*z_p*z_q to P_F and subtracts',
          'the same term from P_G. This is the defining transfer list of',
          'the polynomials above. Consequently their total is identically',
          'zero for every assignment of cell signs. No optimization fact is',
          'needed for cancellation.', '',
          '| F | G | p | q | c |', '|---|---|---|---|---:|']
for f, g, pair, value in transfers:
    lines.append(f"| {factors[f]['name']} | {factors[g]['name']} | {pair[0]} | {pair[1]} | {value} |")
(HERE.parent / 'PAIR_POLYNOMIAL_TABLE_0014.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Wrote PAIR_POLYNOMIAL_TABLE_0014.md')
