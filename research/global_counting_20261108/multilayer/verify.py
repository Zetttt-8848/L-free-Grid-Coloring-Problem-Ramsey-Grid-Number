"""Exact short-domain audit of all-level recurrence and endpoint transport.

No SAT solver and no imported large Golomb optimality result is used.
The general proofs are in THEOREM.md; this audits their finite formulas.
"""

from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform
import sys

HERE = Path(__file__).resolve().parent


def golomb(points):
    differences = [b-a for i, a in enumerate(points) for b in points[i+1:]]
    return len(set(differences)) == len(differences)


def make_g(limit):
    values = [0]
    for p in range(1, limit+1):
        values.append(max(
            len(points)
            for mask in range(1 << p)
            if golomb(points := tuple(i for i in range(p) if mask >> i & 1))
        ))
    return values


def endpoint_bound(points, g):
    r = len(points)
    if r < 2:
        return r
    return max(
        g[max(0, points[-1]-points[0]+1)]
        + g[max(0, points[-2]-points[1]+1)],
        g[max(0, points[-2]-points[0]+1)]
        + g[max(0, points[-1]-points[1]+1)],
    )


def main():
    limit = 14
    g = make_g(limit)
    spans = [next(p-1 for p in range(1, limit+1) if g[p] >= m)
             for m in range(1, max(g)+1)]
    partition_count = 0
    strict_examples = []
    for p in range(1, 11):
        # Ternary state 0 is absent, 1/2 identify the two actual classes.
        for state in product(range(3), repeat=p):
            classes = [tuple(i for i, color in enumerate(state) if color == c)
                       for c in (1, 2)]
            if not all(golomb(s) for s in classes):
                continue
            points = tuple(i for i, color in enumerate(state) if color)
            bound = endpoint_bound(points, g)
            assert len(points) <= bound
            prefix = sum(g[p-u] for u in points[:2])
            suffix = sum(g[u+1] for u in points[-2:])
            assert bound <= min(prefix, suffix)
            partition_count += 1
            if len(points) >= 4 and bound < min(p, prefix, suffix) and len(strict_examples) < 5:
                strict_examples.append({
                    'p': p, 'classes': classes, 'marks': points,
                    'first_return': prefix, 'last_return': suffix,
                    'endpoint_transport': bound,
                })

    rejected = (0, 2, 3, 4, 5, 6, 7, 8, 11, 12)
    rejected_p = 14
    rejected_prefix = sum(g[rejected_p-u] for u in rejected[:2])
    rejected_suffix = sum(g[u+1] for u in rejected[-2:])
    rejected_span = 2*g[rejected[-1]-rejected[0]+1]
    rejected_transport = endpoint_bound(rejected, g)
    assert (rejected_prefix, rejected_suffix, rejected_span, rejected_transport) == (10,10,10,9)
    valid_partitions = sum(all(golomb(tuple(rejected[i] for i in range(len(rejected))
                                          if assignment[i] == c)) for c in (0,1))
                           for assignment in product(range(2), repeat=len(rejected)))
    assert valid_partitions == 0

    word_count = 0
    identity_count = 0
    for n in range(1, 9):
        for word in product(range(3), repeat=n):
            for d in range(1, n):
                p = n-d
                for c in range(3):
                    starts = [u for u in range(p) if word[u] == word[u+d] == c]
                    first = sum(g[p-u] for u in starts[:2])
                    # Independent layer reconstruction from entire prefixes.
                    layers = sum(min(2, sum(
                        word[u] == word[u+d] == c
                        for u in range(max(0, n-span-d))
                    )) for span in spans)
                    assert first == layers
                    identity_count += 1
            word_count += 1
    assert strict_examples
    files = ['CONTRACT.md', 'THEOREM.md', 'README.md', 'verify.py']
    output = {
        'status': 'PASS',
        'scope': 'Exact finite formula audit, not a new Ramsey bound.',
        'python': platform.python_version(),
        'golomb_positions': list(range(limit+1)),
        'exhaustively_computed_g': g,
        'tested_span_thresholds': spans,
        'actual_two_class_partitions_checked': partition_count,
        'partition_interval_lengths': [1, 10],
        'transport_strict_examples': strict_examples,
        'rejected_by_transport_only': {
            'ambient_positions': rejected_p, 'marks': rejected,
            'first_return_bound': rejected_prefix,
            'last_return_bound': rejected_suffix,
            'two_independent_span_capacities': rejected_span,
            'transport_bound': rejected_transport,
            'two_class_assignments_checked': 2**len(rejected),
            'valid_two_golomb_partitions': valid_partitions,
            'scope': 'A set of lag starts, not a square coloring or Ramsey bound.',
        },
        'all_three_color_words_lengths': [1, 8],
        'words_checked': word_count,
        'literal_layercake_identities_checked': identity_count,
        'external_optimal_ruler_exhaustions_replayed': False,
        'command': ['python', 'research/global_counting_20261108/multilayer/verify.py'],
        'sources_sha256': {name: sha256((HERE/name).read_bytes()).hexdigest()
                           for name in files},
    }
    (HERE/'results.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
