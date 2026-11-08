"""Independent integer audit of the inherited side-465 convolution proof.

The two external inputs G(24)>=425 and G(25)>=480 are mathematical
lower bounds on Golomb ruler span, not local exhaustive-computation claims.
No implementation from research_round4 or the numeric agent is imported.
"""
from pathlib import Path
import hashlib
import json


def main():
    n = 465
    weights = [min(i, 94-i) for i in range(1, 94)]
    # Two independent constructions of every autocorrelation coefficient.
    correlation = [sum(weights[i]*weights[i+d]
                       for i in range(len(weights)-d))
                   for d in range(len(weights))]
    pair_sums = [0]*len(weights)
    for i, wi in enumerate(weights):
        for j, wj in enumerate(weights):
            if j >= i:
                pair_sums[j-i] += wi*wj
    if correlation != pair_sums:
        raise ValueError('Autocorrelation constructions disagree')
    a0 = correlation[0]
    p = sum(correlation[1:40])
    q = sum(correlation[40:93])
    weighted_distance = sum(d*value for d, value in enumerate(correlation))
    difference_budgets = [24 if d <= 39 else 23 for d in range(1, 93)]
    direct_margin = sum((n-d-18*b)*correlation[d]
                        for d, b in enumerate(difference_budgets, 1))-n*a0
    grouped_margin = n*(p+q)-weighted_distance-18*(24*p+23*q)-n*a0
    expected = (69231, 2038439, 366786, 53496528, 285630)
    actual = (a0, p, q, weighted_distance, direct_margin)
    if actual != expected or direct_margin != grouped_margin:
        raise ValueError(f'Arithmetic disagreement: {actual}')
    result = {
        'status': 'PASS',
        'claim': 'Historical convolution implies R3<=465 from two external Golomb lower bounds.',
        'provenance': 'exploration/research_round4/checks/build_verification_report.py, direct conditional proof section',
        'external_inputs': {'G(24)>=': 425, 'G(25)>=': 480},
        'a0': a0, 'P_d1_to39': p, 'Q_d40_to92': q,
        'distance_weighted_sum': weighted_distance,
        'contradiction_margin': direct_margin,
        'weights': weights, 'autocorrelation': correlation,
        'verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Exact finite arithmetic and two independent correlation loops. No local replay of the two external Golomb exclusions.'
    }
    Path(__file__).with_name('convolution_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ('weights', 'autocorrelation')}))


if __name__ == '__main__':
    main()
