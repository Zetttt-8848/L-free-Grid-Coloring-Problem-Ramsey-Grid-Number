"""Integer-only independent certificate from a polynomial autocorrelation.

No solver or discovery code is imported. The geometry proof is written in
README.md and the parallel geometry package. External Golomb inputs are
declared rather than re-proved by this finite arithmetic check.
"""
import hashlib
import json
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent


def correlation(N, d):
    m = N-d
    numerator = m*(m*m-1)*(m*m+1+5*d*N)
    assert numerator % 30 == 0
    return numerator//30


def result_for_side(n):
    N = 86
    a = [correlation(N, d) for d in range(N-1)]
    # All used p=n-d are at most479, so each Golomb class has at most24 marks.
    assert n-1 < 480
    caps = [min(n-d, 138+min(6, max(0, n-d-425))) for d in range(1, N-1)]
    old_caps = [min(n-d, 144 if n-d >= 426 else 138) for d in range(1, N-1)]
    gap = sum((n-d-3*caps[d-1])*a[d] for d in range(1, N-1))-n*a[0]
    old_gap = sum((n-d-3*old_caps[d-1])*a[d] for d in range(1, N-1))-n*a[0]
    gains = [[d, old_caps[d-1]-caps[d-1], 3*(old_caps[d-1]-caps[d-1])*a[d]]
             for d in range(1, N-1) if old_caps[d-1] != caps[d-1]]
    return {'n':n, 'N':N, 'weight':'w_i=i(86-i), i=1,...,85',
            'a0':a[0], 'autocorrelation':a, 'aggregate_caps':caps,
            'gap':gap, 'old_separate_cap_gap':old_gap,
            'gain_from_distinct_minima':gap-old_gap, 'gain_terms':gains}


def main():
    # Rebuild each correlation by literal weight products in a separate loop.
    cases = 0
    for N in list(range(2, 31))+[86]:
        w = [i*(N-i) for i in range(1, N)]
        for d in range(N-1):
            direct = sum(w[i]*w[i+d] for i in range(len(w)-d))
            assert direct == correlation(N, d)
            cases += 1
    cert = result_for_side(464)
    a = cert['autocorrelation']
    groups = [sum((32-d)*a[d] for d in range(1, 34)),
              sum((2*d-67)*a[d] for d in range(34, 39)),
              sum((50-d)*a[d] for d in range(39, 85))]
    assert groups == [70470797408, 1810500079, 956045048]
    assert cert['a0'] == 156809003
    assert sum(groups)-464*a[0] == cert['gap'] == 477965143
    assert cert['old_separate_cap_gap'] == -2799639872
    output = {'status':'PASS', 'certificate_464':cert,
              'grouped_left_terms':groups, 'right_term':464*a[0],
              'side_463_comparison':result_for_side(463),
              'closed_formula_product_checks':cases,
              'python':platform.python_version(),
              'external_inputs':{'G(24)>=425':'cited computational theorem',
                                 'G(25)>=480':'cited computational theorem'},
              'non_claims':['No local OGR exhaustive replay',
                            'No 463 exclusion by this certificate',
                            'No global novelty or optimality claim'],
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'certificate.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({'status':'PASS', 'n':464, 'gap':cert['gap'],
                      'old_separate_cap_gap':cert['old_separate_cap_gap'],
                      'closed_formula_product_checks':cases}))


if __name__ == '__main__':
    main()
