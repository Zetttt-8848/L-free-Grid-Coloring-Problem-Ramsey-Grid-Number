"""Check a complete finite branching certificate without search or SAT.

Each internal node covers both values of an unassigned Boolean variable.
Each propagation cites a physical NAE triple; each dead leaf cites a
monochromatic triple. The two successful leaves and their complements are
therefore the complete set, not just four exhibited colorings.
"""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    here = Path(__file__).parent
    path = here/'balance_branch_proof.json'
    raw = path.read_bytes()
    proof = json.loads(raw)
    marks = proof['A']
    cells = [tuple(p) for p in proof['cells']]
    expected = sorted((v, u) for v in marks for u in marks if v > u)
    require(cells == expected and len(set(marks)) == len(marks), 'Full source mismatch')
    ids = {p: i for i, p in enumerate(cells)}
    physical = set()
    # Independent coordinate construction, unlike the generator's unordered
    # triple enumeration. All x,h are bounded by the source's mark span.
    for x, y in cells:
        for h in range(1, max(marks)-min(marks)+1):
            if (x+h, y) in ids and (x+h, y+h) in ids:
                physical.add((1 << ids[x, y]) | (1 << ids[x+h, y]) |
                             (1 << ids[x+h, y+h]))
    full = (1 << len(cells))-1
    models = []
    nodes = conflicts = propagations = 0

    def check(node, colors):
        nonlocal nodes, conflicts, propagations
        nodes += 1
        colors = dict(colors)
        for corner, variable, value in node['propagation']:
            require(corner in physical, 'Nonphysical propagation corner')
            require(value in (0, 1) and variable > 0 and variable & (variable-1) == 0,
                    'Malformed propagation')
            v = variable.bit_length()-1
            require(v not in colors and variable & corner == variable, 'Assigned variable propagated')
            other = [i for i in range(len(cells)) if corner >> i & 1 and i != v]
            require(len(other) == 2 and all(colors.get(i) == 1-value for i in other),
                    'Propagation lacks two equal opposite witnesses')
            colors[v] = value
            propagations += 1
        tags = set(node)-{'propagation'}
        if tags == {'conflict'}:
            corner = node['conflict']
            require(corner in physical, 'Nonphysical conflict')
            colors_here = [colors.get(i) for i in range(len(cells)) if corner >> i & 1]
            require(colors_here in ([0, 0, 0], [1, 1, 1]), 'Unproved conflict')
            conflicts += 1
        elif tags == {'model'}:
            require(set(colors) == set(range(len(cells))), 'Partial model leaf')
            model = sum(value << i for i, value in colors.items())
            require(model == node['model'], 'Stored model disagrees with path')
            for corner in physical:
                values = [colors[i] for i in range(len(cells)) if corner >> i & 1]
                require(values not in ([0, 0, 0], [1, 1, 1]), 'Improper model leaf')
            models.append(model)
        else:
            require(tags == {'branch_variable', 'one', 'zero'}, 'Malformed branch coverage')
            v = node['branch_variable']
            require(isinstance(v, int) and 0 <= v < len(cells) and v not in colors,
                    'Branch must cover an unassigned source variable')
            check(node['one'], {**colors, v: 1})
            check(node['zero'], {**colors, v: 0})

    require(proof['pinned_zero_variable'] == 0, 'Unexpected symmetry pin')
    check(proof['tree'], {0: 0})
    require(len(models) == 2 and models[0] ^ models[1] == 1 << ids[3, 1],
            'Claim of 35 rigid cells is not supported')
    models += [full ^ model for model in models]
    require(len(set(models)) == len(models), 'Repeated model')
    fibers = defaultdict(list)
    for i, (x, y) in enumerate(cells):
        fibers[x-y].append(i)
    distribution = Counter(sum(sum(1-2*(model >> i & 1) for i in fiber)**2
                               for fiber in fibers.values()) for model in models)
    forced_equal = all((model >> ids[9, 1] & 1) == (model >> ids[10, 2] & 1)
                       for model in models)
    require(len(models) == 4 and distribution == {8: 4} and forced_equal,
            'Claim not supported by the fully covered assignment domain')
    saved = json.loads((here/'balance_certificate.json').read_text())
    saved_models = {sum(bit << i for i, bit in enumerate(row))
                    for row in saved['all_proper_colorings']}
    require(saved_models == set(models), 'Independent model list disagreement')
    result = {
        'status': 'PASS', 'nodes_checked': nodes, 'conflict_leaves': conflicts,
        'propagations_checked': propagations, 'corners_checked': len(physical),
        'full_binary_domain': 1 << len(cells), 'proper_count': len(models),
        'phi_distribution': dict(distribution),
        'parity_floor': sum(len(fiber) % 2 for fiber in fibers.values()),
        'forced_equal_cells': [[9, 1], [10, 2]],
        'rigid_cells_up_to_global_complement': 35,
        'only_free_cell_up_to_global_complement': [3, 1],
        'proof_sha256': hashlib.sha256(raw).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Complete finite branching certificate for this one full strict source; no SAT library.'
    }
    (here/'balance_proof_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
