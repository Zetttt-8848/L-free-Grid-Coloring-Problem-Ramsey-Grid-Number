"""Check all source-table existence halves via exact shift intersections."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    inputs = json.loads((ROOT / 'research_round4/audits/golomb_sources/all_witness_inputs.json').read_text(encoding='utf-8'))
    text = (ROOT / 'research_round4/sources/mammel_v1/page_012.txt').read_text(encoding='utf-8')
    match = re.search(r'Golomb←\s*\{([^}]+)\}', text, re.S)
    require(match is not None, 'Missing source table')
    table = [int(x) for x in re.findall(r'\d+', match.group(1))]
    require(len(table) == 29, 'Wrong table size')
    rulers = inputs['marks_by_order']
    require(set(rulers) == {str(m) for m in range(1, 29)}, 'Incomplete/extra order set')
    rows = []
    for order in range(1, 29):
        marks = rulers[str(order)]
        require(all(type(x) is int for x in marks), 'Noninteger mark')
        require(len(marks) == order and marks[0] == 0, 'Wrong order/origin')
        require(all(a < b for a, b in zip(marks, marks[1:])), 'Unordered marks')
        length = marks[-1]
        require(length == table[order] - 1, 'Witness does not attain the printed length')
        mark_set = set(marks)
        counts = [len(mark_set.intersection(x + d for x in marks)) for d in range(1, length + 1)]
        require(all(c <= 1 for c in counts), 'Repeated positive difference')
        require(sum(counts) == order * (order - 1) // 2, 'Pair accounting failed')
        rows.append({'order': order, 'length': length, 'marks': marks,
                     'positive_difference_count': sum(counts),
                     'differences': [d for d, count in enumerate(counts, 1) if count],
                     'existence_verdict': 'PASS', 'lower_bound_checked_in_this_run': False})
    require(len(sys.argv) == 2, 'Supply output directory')
    out = (ROOT / sys.argv[1]).resolve()
    require(out.is_relative_to(ROOT / 'research_round4'), 'Output outside research tree')
    out.mkdir(parents=True, exist_ok=True)
    result = {'scope': 'G(m)<=H_m-1 for each1<=m<=28; no exclusion of shorter rulers.',
              'python': sys.version, 'rows': rows,
              'total_positive_differences': sum(row['positive_difference_count'] for row in rows)}
    (out / 'results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(f'All {len(rows)} source-table existence halves PASS; {result["total_positive_differences"]} positive differences checked.')


if __name__ == '__main__':
    main()
