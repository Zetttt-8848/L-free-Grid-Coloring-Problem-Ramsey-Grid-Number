"""Exact arithmetic and a finite boundary-word diagnostic; no solver import."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent


def profile(a, b):
    q = len(a)
    result = []
    for k in range(1, q+1):
        count = [0, 0, 0]
        for i in range(k):
            if a[i] == b[q-k+i]:
                count[a[i]] += 1
        result.append(sum(min(2, n) for n in count))
    return result


def boundary_six():
    best = -1
    maxima = []
    checked = 0
    for tail in product(range(3), repeat=5):
        a = (0,)+tail
        for b in product(range(3), repeat=6):
            p = profile(a, b)
            for k in range(2, 7):
                limit = max(min(4*r, 2*k-r) for r in (1, 2, 3))
                assert p[k-2]+p[k-1] <= limit
            value = sum(p)
            if value > best:
                best = value
                maxima = []
            if value == best:
                maxima.append({'X':a, 'Y':b, 'profile':p})
            checked += 1
    assert checked == 3**11 and best == 14 and len(maxima) == 2
    return {'status':'FINITE-CHECKED', 'q':6, 'normalization':'X[0]=0 by global color relabeling',
            'word_pairs':checked, 'maximum':best, 'maximizers':maxima,
            'non_claim':'No arbitrary-length extremal formula is proved by this finite enumeration.'}


def check_paths():
    for k in range(2, 21):
        edges = [(i, k+i) for i in range(k)] + [(i, k+i+1) for i in range(k-1)]
        degrees = [0]*(2*k)
        graph = [[] for _ in degrees]
        for u, v in edges:
            degrees[u] += 1; degrees[v] += 1
            graph[u].append(v); graph[v].append(u)
        seen = {0}; todo = [0]
        while todo:
            for v in graph[todo.pop()]:
                if v not in seen:
                    seen.add(v); todo.append(v)
        assert len(seen) == 2*k
        assert sorted(degrees) == [1, 1]+[2]*(2*k-2)
    values = [max(min(4*r, 2*k-r) for r in (1, 2, 3)) for k in range(2, 9)]
    assert values == [3, 4, 6, 8, 9, 11, 12]
    return {'checked_k':[2,20], 'B_2_through_8':values,
            'scope':'Graph construction check only; the general path proof is in THEOREM.md.'}


def arithmetic():
    w = [i*(86-i) for i in range(1, 86)]
    a = [sum(w[i]*w[i+d] for i in range(85-d)) for d in range(85)]
    assert all(x >= y >= 0 for x, y in zip(a, a[1:]))
    rows = []
    for n in (463, 464):
        b = n-425
        cap = [138+min(6, max(0, n-d-425)) for d in range(1, 85)]
        base = sum((n-d-3*cap[d-1])*a[d] for d in range(1, 85))-n*a[0]
        v = [0]+[a[b-k] for k in range(1, 8)]
        # Literal coefficient verification of the three displayed multipliers.
        multipliers = [v[3], v[5], v[6]-v[5]]
        coeff = [0]*8
        rhs = 0
        for multiplier, (i, j, need) in zip(multipliers, ((3,4,1),(5,6,2),(6,7,1))):
            assert multiplier >= 0
            coeff[i] += multiplier; coeff[j] += multiplier
            rhs += multiplier*need
        assert all(0 <= coeff[k] <= v[k] for k in range(1, 8))
        assert rhs == v[3]+v[5]+v[6]
        rows.append({'n':n, 'base_gap':base, 'weighted_deficit':rhs,
                     'enhanced_gap':base+3*rhs, 'multipliers':multipliers})
    assert [r['enhanced_gap'] for r in rows] == [-2778001795, 1199151808]
    return {'weights':w, 'autocorrelation':a, 'rows':rows,
            'external_inputs':['G(24)>=425','G(25)>=480'], 'external_exhaustions_replayed':False}


def main():
    result = {'status':'PASS', 'arithmetic':'Python exact integers', 'python':platform.python_version(),
              'paths':check_paths(), 'convolution':arithmetic(), 'boundary_six':boundary_six(),
              'sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in ('verify.py','THEOREM.md','CONTRACT.md')}}
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({'status':'PASS','n464_gap':result['convolution']['rows'][1]['enhanced_gap'],
                      'q6_maximum':result['boundary_six']['maximum'], 'q6_pairs':result['boundary_six']['word_pairs']}))


if __name__ == '__main__':
    main()
