"""Independently check source literals; never infer Golomb optimality."""
from pathlib import Path
from collections import Counter
import json
import sys

ROOT = Path(__file__).resolve().parents[2]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect(witness):
    raw = witness['values']
    require(all(type(x) is int for x in raw), 'Noninteger source input')
    if witness['representation'] == 'marks':
        marks = raw
    else:
        require(witness['representation'].startswith('consecutive gaps'), 'Unknown representation')
        marks = [0]
        for gap in raw:
            require(gap > 0, 'Nonpositive gap')
            marks.append(marks[-1] + gap)
    require(len(marks) == witness['order'], 'Wrong number of marks')
    require(marks[0] == 0 and marks[-1] == witness['length'], 'Wrong endpoints')
    require(all(a < b for a, b in zip(marks, marks[1:])), 'Marks not strictly increasing')
    # A full positive-difference table: each unordered pair occurs exactly once.
    pairs = [(marks[j] - marks[i], i, j)
             for i in range(len(marks)) for j in range(i + 1, len(marks))]
    multiplicities = Counter(d for d, _, _ in pairs)
    require(all(v == 1 for v in multiplicities.values()), 'Repeated positive difference')
    # Orthogonal cross-check: intersection with each shift counts all representations.
    mark_set = set(marks)
    shift_counts = [sum(x + d in mark_set for x in marks)
                    for d in range(1, marks[-1] + 1)]
    require(all(v <= 1 for v in shift_counts), 'Shift intersection has multiple pairs')
    require(sum(shift_counts) == len(pairs), 'Pair and shift computations disagree')
    require(all(shift_counts[d - 1] == multiplicities[d]
                for d in range(1, marks[-1] + 1)), 'Difference profile disagrees')
    return {
        'order': len(marks), 'length': marks[-1], 'marks': marks,
        'pair_count': len(pairs), 'distinct_positive_differences': len(multiplicities),
        'max_difference_multiplicity': max(multiplicities.values()),
        'sorted_difference_pair_table': sorted(pairs),
        'smallest_missing_positive_difference': next(
            (d for d in range(1, marks[-1] + 1) if d not in multiplicities), None),
        'shift_count_crosscheck': 'PASS', 'existence_verdict': 'PASS',
        'optimality_verdict': 'UNDECIDED', 'source': witness['source']
    }


def main():
    require(len(sys.argv) == 2, 'Supply a new run directory relative to the project')
    out = (ROOT / sys.argv[1]).resolve()
    require(out.is_relative_to(ROOT / 'research_round4'), 'Output outside research_round4')
    source = ROOT / 'research_round4/audits/golomb_sources/witness_inputs.json'
    data = json.loads(source.read_text(encoding='utf-8'))
    result = {
        'scope': 'Only the two literal source witnesses. No optimality or grid bound.',
        'python_version': sys.version, 'optimize': sys.flags.optimize,
        'witnesses': [inspect(w) for w in data['witnesses']]
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / 'results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    for w in result['witnesses']:
        print(f"order={w['order']} length={w['length']} pairs={w['pair_count']} existence=PASS optimality=UNDECIDED")


if __name__ == '__main__':
    main()
