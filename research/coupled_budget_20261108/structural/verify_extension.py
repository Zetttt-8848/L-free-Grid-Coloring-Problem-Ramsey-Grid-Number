"""Independently check the local-frustration cancellation witness."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    here = Path(__file__).parent
    raw = (here/'extension_discovery.json').read_bytes()
    data = json.loads(raw)
    marks = data['A']
    cells = [tuple(p) for p in data['cells']]
    colors = data['coloring']
    base = {0, 1, 2, 3, 4, 6, 7, 9, 10}
    require(marks == sorted(base | {14}), 'Unexpected extension')
    require(cells == sorted((v, u) for u, v in combinations(marks, 2)), 'Source is incomplete')
    require(len(colors) == len(cells) and set(colors) <= {0, 1}, 'Invalid coloring domain')
    coloring = dict(zip(cells, colors))
    corners = 0
    for triple in combinations(cells, 3):
        p, q, r = sorted(triple)
        if p[1] == q[1] and q[0] == r[0] and q[0]-p[0] == r[1]-q[1] > 0:
            corners += 1
            require(len({coloring[x] for x in triple}) > 1, 'Monochromatic physical L')
    potentials = []
    for subset in (base, set(marks)):
        fibers = defaultdict(list)
        for (x, y), color in coloring.items():
            if x in subset and y in subset:
                fibers[x-y].append(1-2*color)
        potentials.append({'marks': sorted(subset),
                           'phi': sum(sum(v)**2 for v in fibers.values()),
                           'parity': sum(len(v) % 2 for v in fibers.values()),
                           'signed_fiber_sums': {d: sum(v) for d, v in fibers.items()}})
    require([(p['phi'], p['parity']) for p in potentials] == [(8, 4), (7, 7)],
            'Potential claim failed')
    require(coloring[9, 1] == coloring[10, 2] != coloring[14, 6], 'Cancellation failed')
    result = {'status': 'PASS', 'cells': len(cells), 'physical_corners': corners,
              'potentials': potentials, 'cancelled_difference': 8,
              'witness_sha256': hashlib.sha256(raw).hexdigest(),
              'verifier_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'One full 45-cell source witness. Global minimum 7 follows from parity and its attainment.'}
    (here/'extension_verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
