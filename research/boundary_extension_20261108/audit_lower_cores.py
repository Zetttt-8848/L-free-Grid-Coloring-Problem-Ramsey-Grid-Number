"""Coordinator certificate audit: geometric constraints and complete proof trees.

Does not import discovery, minimization, or their propagation routines.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def audit_group(group, rows):
    n = len(rows)
    ox, oy = group['offset']
    fixed = {(x+ox, y+oy): int(rows[x][y]) for x in range(n) for y in range(n)}
    cells = list(map(tuple, group['cells']))
    expected = {(x, y) for x in range(n+1) for y in range(n+1)} - fixed.keys()
    if set(cells) != expected or len(cells) != len(expected):
        raise ValueError('Boundary domain mismatch')
    core = group['core']
    support = set()
    for rule in core:
        a, b, c = list(map(tuple, rule['points']))
        if not (a[1] == b[1] and b[0] == c[0] and b[0]-a[0] == c[1]-b[1] > 0):
            raise ValueError('Wrong geometric L')
        if any(p not in fixed and p not in expected for p in (a, b, c)):
            raise ValueError('Outside domain')
        unknown = {p for p in (a, b, c) if p not in fixed}
        if {cells[i] for i in rule['vars']} != unknown or len(rule['vars']) != len(unknown):
            raise ValueError('Wrong residual variables')
        support.update(p for p in (a, b, c) if p in fixed)
        if any(fixed[p] != rule['color'] for p in (a, b, c) if p in fixed):
            raise ValueError('Residual forbidden color not implied')
    nodes = 0

    def verify_tree(tree, assignments):
        nonlocal nodes
        nodes += 1
        domains = [set(s) for s in assignments]
        changed = True
        contradiction = False
        while changed and not contradiction:
            changed = False
            for rule in core:
                vs, color = rule['vars'], rule['color']
                if any(color not in domains[v] for v in vs):
                    continue
                free = [v for v in vs if domains[v] != {color}]
                if not free:
                    contradiction = True
                    break
                if len(free) == 1:
                    domains[free[0]].remove(color)
                    changed = True
        if contradiction:
            if tree != {'conflict': True}:
                raise ValueError('Conflict leaf not explicit')
            return
        if 'branch' not in tree:
            raise ValueError('Unjustified conflict leaf')
        v = tree['branch']
        if not 0 <= v < len(cells) or len(domains[v]) < 2:
            raise ValueError('Invalid branching variable')
        if set(tree['children']) != {str(c) for c in domains[v]}:
            raise ValueError('Branch coverage missing')
        for color in sorted(domains[v]):
            nxt = [set(s) for s in domains]
            nxt[v] = {color}
            verify_tree(tree['children'][str(color)], nxt)

    verify_tree(group['proof_tree'], [{0, 1, 2} for _ in cells])
    if nodes != group['proof_tree_nodes']:
        raise ValueError('Node count mismatch')
    models = group.get('deletion_models', [])
    if models:
        ids = group['core_ids']
        if len(models) != len(core) or {m['omitted'] for m in models} != set(ids):
            raise ValueError('Missing deletion witnesses')
        for model in models:
            colors = model['colors']
            if len(colors) != len(cells) or set(colors) - {0, 1, 2}:
                raise ValueError('Invalid deletion coloring')
            for i, rule in zip(ids, core):
                if i != model['omitted'] and all(colors[v] == rule['color'] for v in rule['vars']):
                    raise ValueError('Invalid edge-deletion witness')
    return {'constraints': len(core), 'nodes': nodes,
            'deletion_witnesses': len(models), 'support': sorted(support)}


def main():
    paths = [HERE/'lower'/n for n in ('paper20.json', 'extension_results.json', 'packing_results.json')]
    paper, ext, packing = [json.loads(p.read_text(encoding='utf-8')) for p in paths]
    checked = [audit_group(g, paper['rows']) for g in ext['placements']]
    left = audit_group(ext['left_side_core'], paper['rows'])
    packed = []
    for placement in packing['placements']:
        used = set()
        for core in placement['cores']:
            merged = {**core, 'cells': placement['cells'], 'offset': placement['offset']}
            result = audit_group(merged, paper['rows'])
            support = set(map(tuple, result['support']))
            if support != set(map(tuple, core['support'])) or used & support:
                raise ValueError('Repair supports not correct and disjoint')
            used.update(support)
        packed.append({'offset': placement['offset'], 'certified_repair_lower_bound': len(placement['cores'])})
    report = {'status': 'PASS', 'placements': checked, 'left': left, 'packing': packed,
              'inputs': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Only listed fixed-matrix residual cores and their disjoint support packing; no global R3 bound.'}
    (HERE/'lower_cores_audit.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'packing': packed, 'left_nodes': left['nodes']}))


if __name__ == '__main__':
    main()
