"""Exact certificates; Python standard library only.

Run: python verify.py
The external Golomb lower bounds in inputs.json are cited inputs, not proved
by this checker. Float-valued scouting files are not imported or read.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def choose2(m):
    return m * (m - 1) // 2


def capacity(n, d):
    """One diagonal color's positive-difference multiplicity.

    Uses ONLY G(24)>=425, G(25)>=480 and the trivial n-d bound.
    """
    assert 1 <= d < n <= 481
    span = n - 1 - d
    assert span < 480
    return min(n - d, 46 if span < 425 else 48)


def max_class_size(n):
    budget = sum(capacity(n, d) for d in range(1, n))
    m = 0
    while choose2(m + 1) <= budget:
        m += 1
    return min(m, n)


def greedy_distance(n, count):
    """Exact optimum of count objects of cost d and capacity 3*C_d."""
    remaining = count
    total = 0
    occupied = []
    for d in range(1, n):
        used = min(remaining, 3 * capacity(n, d))
        total += d * used
        if used:
            occupied.append([d, used])
        remaining -= used
        if remaining == 0:
            return total, occupied
    assert remaining == 0, 'Requested count exceeds total capacity'


def endpoint_coefficients(m, c):
    # Construct from actual selected pairs, rather than assuming a formula.
    out = [0] * m
    for j in range(1, c + 1):
        for i in range(m - j):
            out[i] -= 1
            out[i + j] += 1
    return out


def joint_endpoint(n, c):
    minimum_class = n - 2 * max_class_size(n)
    assert minimum_class >= 2 * c
    count = c * n - 3 * c * (c + 1) // 2
    lower, occupied = greedy_distance(n, count)
    # Any partition with all sizes >=2c has this same coefficient multiset.
    coeff = sorted([-j for j in range(1, c + 1)] * 3
                   + [j for j in range(1, c + 1)] * 3
                   + [0] * (n - 6 * c))
    upper = sum(i * a for i, a in enumerate(coeff))
    assert upper == 3 * c * (c + 1) * (n - 2 * c - 1) // 2
    return dict(n=n, c=c, count=count, minimum_class=minimum_class,
                max_class=max_class_size(n), lower=lower, upper=upper,
                gap=lower-upper, occupied=occupied)


def endpoint_scan():
    rows = []
    for n in range(300, 481):
        minclass = n - 2 * max_class_size(n)
        candidates = [joint_endpoint(n, c) for c in range(1, minclass // 2 + 1)]
        if candidates:
            best = max(candidates, key=lambda r: r['gap'])
            rows.append({k: best[k] for k in ('n', 'c', 'gap', 'minimum_class')})
    positive = [row for row in rows if row['gap'] > 0]
    return dict(domain_n=[300, 480], cutoff_rule='1 <= c <= floor((n-2*M(n))/2)',
                first_positive=positive[0] if positive else None, rows=rows)


def convolution_465():
    n = 465
    w = [min(i, 94-i) for i in range(1, 94)]
    # Reconstruct autocorrelations by ordered pairs of weight positions.
    corr = Counter()
    for i, left in enumerate(w):
        for j, right in enumerate(w):
            if j >= i:
                corr[j-i] += left * right
    a0 = corr[0]
    p = sum(corr[d] for d in range(1, 40))
    q = sum(corr[d] for d in range(40, 93))
    dist = sum(d * corr[d] for d in range(1, 93))
    # Direct convolution of the full diagonal indicator with w.
    h = [0] * (n + len(w) - 1)
    for x in range(n):
        for i, weight in enumerate(w):
            h[x+i] += weight
    required_energy = sum(value * value for value in h)
    max_three_color_energy = n*a0 + 6*sum(capacity(n,d)*corr[d] for d in range(1,93))
    cauchy_gap = required_energy - 3*max_three_color_energy
    gap = sum((n-d-9*capacity(n,d))*corr[d] for d in range(1,93))-n*a0
    assert cauchy_gap == 2*gap
    assert gap == n*(p+q)-dist-18*(24*p+23*q)-n*a0
    residue_nonzero = sum(value % 3 != 0 for value in h)
    return dict(n=n, weight=w, a0=a0, P=p, Q=q, D=dist, gap=gap,
                direct_cauchy_gap=cauchy_gap, required_energy=required_energy,
                max_three_color_energy=max_three_color_energy,
                integer_occupancy_gap=gap+residue_nonzero,
                residue_nonzero=residue_nonzero,
                autocorrelation=[corr[d] for d in range(93)])


def small_endpoint_check():
    # Supplement to the general proof: check every 3-color partition through
    # n=9 for which each class contains >=2c points, and all eligible c.
    checked = 0
    for n in range(1, 10):
        for colors in product(range(3), repeat=n):
            parts = [[i for i, k in enumerate(colors) if k == color] for color in range(3)]
            for c in range(1, min(map(len, parts))//2+1):
                actual = sum(a[i+j]-a[i] for a in parts for j in range(1,c+1)
                             for i in range(len(a)-j))
                coeff = sorted(sum((endpoint_coefficients(len(a),c) for a in parts), []))
                bound = sum(i*b for i,b in enumerate(coeff))
                assert actual <= bound
                assert bound == 3*c*(c+1)*(n-2*c-1)//2
                checked += 1
    return dict(n_max=9, partition_cutoff_cases=checked, result='PASS')


def main():
    inputs = json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    assert inputs['external_lower_bounds'] == {'24':425, '25':480}
    endpoint = joint_endpoint(466,22)
    convolution = convolution_465()
    assert (endpoint['count'],endpoint['lower'],endpoint['upper'],endpoint['gap']) == (9493,319760,319539,221)
    assert (convolution['a0'],convolution['P'],convolution['Q'],convolution['D'],convolution['gap']) == (69231,2038439,366786,53496528,285630)
    report = dict(status='PASS', arithmetic='Python integers only',
                  external_dependency='G(24)>=425 and G(25)>=480; not replayed',
                  endpoint_466=endpoint, restored_465=convolution,
                  endpoint_scan=endpoint_scan(), small_endpoint_check=small_endpoint_check(),
                  sha256={name:sha256((HERE/name).read_bytes()).hexdigest()
                          for name in ('inputs.json','verify.py','THEOREM.md')})
    (HERE/'results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:report[key] for key in ('status','arithmetic','external_dependency')},indent=2))
    print('466 endpoint gap:',endpoint['gap'])
    print('465 convolution gap:',convolution['gap'])
    print('Endpoint scan first positive:',report['endpoint_scan']['first_positive'])
    print('Exhaustive small partition cases:',report['small_endpoint_check']['partition_cutoff_cases'])


if __name__ == '__main__':
    main()
