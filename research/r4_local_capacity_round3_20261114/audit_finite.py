"""Independent finite encoding reconstruction and literal witness validation.

Pass --checker PATH to also invoke the separate complete drat-trim checker.
No imports from finite_caps.py or a SAT solver are used.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import argparse
import json
import lzma
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).parent


def geometry(points):
    """Find Ls by pairing their equal-diagonal arms, not by a step loop."""
    cells = [(x, y) for x in sorted(points) for y in sorted(points) if y < x]
    present = set(cells)
    triples = []
    for first, last in combinations(cells, 2):
        x, y = first
        v, u = last
        if v - x == u - y and v > x and (v, y) in present:
            triples.append((first, (v, y), last))
    return cells, triples


def canonical(clauses):
    return Counter(tuple(sorted(c)) for c in clauses)


def reconstruct(n, k):
    cells, triples = geometry(range(n))
    ids = {c: n + i + 1 for i, c in enumerate(cells)}
    clauses = []
    for triple in triples:
        absent = sorted({-(coordinate + 1) for cell in triple for coordinate in cell})
        colors = [ids[cell] for cell in triple]
        clauses += [absent + colors, absent + [-c for c in colors]]
    base = n + len(cells)

    def threshold(i, j):
        if j == 0:
            return True
        if j > i:
            return False
        return base + sum(min(t, k) for t in range(1, i)) + j

    def opposite(value):
        return not value if isinstance(value, bool) else -value

    def clause(values):
        if any(isinstance(v, bool) and v for v in values):
            return
        clauses.append([v for v in values if not isinstance(v, bool)])

    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            current = threshold(i, j)
            previous = threshold(i - 1, j)
            lower = threshold(i - 1, j - 1)
            # previous -> current; (mark and lower) -> current;
            # current -> (previous or mark) and (previous or lower).
            clause([opposite(previous), current])
            clause([-i, opposite(lower), current])
            clause([-current, previous, i])
            clause([-current, previous, lower])
    clause([threshold(n, k)])
    return base + sum(min(i, k) for i in range(1, n + 1)), clauses, len(triples)


def read_dimacs(path):
    tokens = []
    header = None
    for line in path.read_text().splitlines():
        if not line or line.startswith('c'):
            continue
        if line.startswith('p '):
            assert header is None
            prefix, kind, variables, count = line.split()
            assert (prefix, kind) == ('p', 'cnf')
            header = (int(variables), int(count))
        else:
            tokens.extend(map(int, line.split()))
    clauses = []
    current = []
    for literal in tokens:
        if literal:
            assert header is not None and abs(literal) <= header[0]
            current.append(literal)
        else:
            clauses.append(current)
            current = []
    assert not current and header is not None and len(clauses) == header[1]
    return header[0], clauses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checker', type=Path,
                        help='Path to a complete drat-trim executable; enables proof verification')
    args = parser.parse_args()
    checker = args.checker.resolve() if args.checker else None
    if checker is not None:
        assert checker.is_file(), checker
    # Independent propositional truth table for the threshold gate.
    for z, p, a, q in product((False, True), repeat=4):
        clauses = ((not p or z), (not a or not q or z),
                   (not z or p or a), (not z or p or q))
        assert all(clauses) == (z == (p or (a and q)))
    output = {'cnfs': [], 'witnesses': [], 'proofs': [], 'scope':
              'CNF reconstruction and complete source witnesses; optional full external DRAT checking',
              'proof_checker': checker.name if checker else None}
    if checker is not None:
        output['proof_checker_sha256'] = sha256(checker.read_bytes()).hexdigest()
    for path in sorted((ROOT / 'proofs').glob('*.cnf')):
        n, k = map(int, re.fullmatch(r'n(\d+)_k(\d+)\.cnf', path.name).groups())
        variables, clauses = read_dimacs(path)
        expected_variables, expected, triples = reconstruct(n, k)
        assert variables == expected_variables
        assert canonical(clauses) == canonical(expected), path.name
        output['cnfs'].append(dict(file=path.name, variables=variables,
                                  clauses=len(clauses), physical_Ls=triples,
                                  sha256=sha256(path.read_bytes()).hexdigest()))
        if checker is not None:
            packed = path.with_suffix('.drat.xz')
            raw = path.with_suffix('.drat')
            source = packed if packed.exists() else raw
            assert source.is_file(), source
            with tempfile.TemporaryDirectory(prefix='lgrid-proof-audit-') as temporary:
                expanded = Path(temporary) / raw.name
                opener = lzma.open if source == packed else open
                with opener(source, 'rb') as src, expanded.open('wb') as dst:
                    shutil.copyfileobj(src, dst, 1024 * 1024)
                digest = sha256()
                with expanded.open('rb') as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                        digest.update(chunk)
                done = subprocess.run([str(checker), str(path.resolve()),
                                       str(expanded), '-t', '120'],
                                      capture_output=True, text=True, timeout=130)
                log = ROOT / (path.stem + '.audit.check.txt')
                rendered = '\n'.join(line.rstrip() for line in (done.stdout + '\n' + done.stderr).splitlines()).strip() + '\n'
                log.write_text(rendered)
                assert done.returncode == 0 and 's VERIFIED' in done.stdout, path.name
                output['proofs'].append(dict(cnf=path.name, stored_proof=source.name,
                                             expanded_sha256=digest.hexdigest(),
                                             log=log.name, status='VERIFIED'))
    for path in sorted((ROOT / 'proofs').glob('*.witness.json')):
        data = json.loads(path.read_text())
        marks = data['A']
        assert len(set(marks)) == len(marks) >= data['k']
        assert all(isinstance(a, int) and 0 <= a < data['n'] for a in marks)
        cells, triples = geometry(marks)
        colors = {(x, y): e for x, y, e in data['colors']}
        assert len(data['colors']) == len(colors) == len(cells)
        assert set(colors) == set(cells) and set(colors.values()) <= {0, 1}
        assert all(len({colors[c] for c in triple}) > 1 for triple in triples)
        output['witnesses'].append(dict(file=path.name, marks=len(marks),
                                       cells=len(cells), physical_Ls=len(triples),
                                       sha256=sha256(path.read_bytes()).hexdigest()))
    (ROOT / 'finite_audit_results.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
