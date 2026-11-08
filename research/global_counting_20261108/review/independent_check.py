"""Independent reconstruction from physical directed-L triples and integer sets.

No author verifier, saved statistic, or extremal table is imported. Author
artifacts are read only at the final comparison/provenance stage.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def differences_unique(points):
    counts = Counter(b - a for a, b in combinations(points, 2))
    return max(counts.values(), default=0) <= 1


def capacities(limit):
    # Enumerate by mark cardinality and retain the shortest occupied span.
    # Translation sends every nonempty ruler to one beginning at zero.
    shortest = {1: 0}
    witnesses = {1: (0,)}
    for size in range(2, limit + 1):
        found = None
        for endpoint in range(1, limit):
            if size > endpoint + 1 or comb(size, 2) > endpoint:
                continue
            for interior in combinations(range(1, endpoint), size - 2):
                candidate = (0,) + interior + (endpoint,)
                if differences_unique(candidate):
                    found = candidate
                    break
            if found is not None:
                break
        if found is None:
            break
        shortest[size] = found[-1]
        witnesses[size] = found
    g = [sum(span < length for span in shortest.values()) for length in range(limit + 1)]
    return g, shortest, witnesses


def transport(points, g):
    if len(points) <= 1:
        return len(points)
    lows, highs = points[:2], points[-2:]
    return max(sum(g[max(0, upper - lower + 1)] for lower, upper in zip(lows, perm))
               for perm in (highs, highs[::-1]))


def physical_geometry(marks):
    cells = tuple((x, y) for x in marks for y in marks if y < x)
    cellset = set(cells)
    position = {point: i for i, point in enumerate(cells)}
    triples = []
    span = max(marks, default=0) - min(marks, default=0)
    # The primitive is the requested physical shape, not equal-offset pairs.
    for x, y in cells:
        for step in range(1, span + 1):
            corner, last = (x + step, y), (x + step, y + step)
            if corner in cellset and last in cellset:
                triples.append((position[(x, y)], position[corner], position[last]))
    lines = []
    for coordinate in (0, 1):
        for value in marks:
            lines.append(tuple(i for i, point in enumerate(cells) if point[coordinate] == value))
    diagonals = []
    for offset in sorted({x - y for x, y in cells}):
        diagonals.append(tuple(i for i, (x, y) in enumerate(cells) if x - y == offset))
    actual_legs = Counter()
    requests = defaultdict(list)
    for left, corner, top in triples:
        actual_legs[tuple(sorted((left, corner)))] += 1
        actual_legs[tuple(sorted((corner, top)))] += 1
        requests[corner].append((left, top))
    assert all(count == 1 for count in actual_legs.values())
    line_pairs = [pair for line in lines for pair in combinations(line, 2)]
    assert len(line_pairs) == len(set(line_pairs))
    missing = tuple(pair for pair in line_pairs if pair not in actual_legs)
    assert len(missing) == 2 * comb(len(marks), 3) - 2 * len(triples)
    assert len(triples) == sum(comb(len(line), 2) for line in diagonals)
    return cells, triples, lines, diagonals, missing, requests


def count_source(marks, signs, data):
    cells, triples, lines, diagonals, missing, requests = data
    mono = sum(signs[left] == signs[corner] == signs[top] for left, corner, top in triples)
    phi = sum(sum(signs[i] for i in line) ** 2 for line in diagonals)
    line_square = sum(sum(signs[i] for i in line) ** 2 for line in lines)
    signed_missing = sum(signs[i] * signs[j] for i, j in missing)
    assert 8 * mono == 2 * len(triples) + phi + line_square - 3 * len(cells) - 2 * signed_missing
    collisions = 0
    second_moment = 0
    edges = set()
    for corner, reqs in requests.items():
        demands = [signs[left] if signs[left] == signs[top] else 0 for left, top in reqs]
        direct = 0
        for (left1, top1), (left2, top2) in combinations(reqs, 2):
            assert len({left1, top1, left2, top2}) == 4
            direct += signs[left1] == signs[top1] and signs[left2] == signs[top2] and signs[left1] != signs[left2]
        assert direct == demands.count(1) * demands.count(-1)
        collisions += direct
        second_moment += sum(abs(d) for d in demands) ** 2 - sum(demands) ** 2
        for left, top in reqs:
            if signs[left] == signs[top] == -signs[corner]:
                edges.add(tuple(sorted((left, corner))))
                edges.add(tuple(sorted((top, corner))))
    assert 4 * collisions == second_moment
    if mono == 0:
        assert collisions == 0
        assert 6 * len(triples) + phi + line_square <= 3 * len(cells) + 4 * comb(len(marks), 3)
    return mono, collisions, edges


def word_stats(word, g):
    n = len(word)
    counts, firsts, lasts, boths, transports = [], [], [], [], []
    for lag in range(1, n):
        starts = [tuple(i for i in range(n - lag) if word[i] == word[i + lag] == c) for c in range(3)]
        first = [sum(g[n - lag - i] for i in positions[:2]) for positions in starts]
        last = [sum(g[i + 1] for i in positions[-2:]) for positions in starts]
        counts.append(sum(map(len, starts)))
        firsts.append(sum(first))
        lasts.append(sum(last))
        boths.append(sum(map(min, zip(first, last))))
        transports.append(sum(transport(positions, g) for positions in starts))
    return dict(correlations=counts, first=firsts, last=lasts, both=boths, transport=transports)


def main():
    g, spans, rulers = capacities(14)
    # Enumerate all subsets, then enumerate their binary partitions. This is
    # independent of ternary state generation and includes the empty domain.
    partitions = 0
    for length in range(0, 11):
        for size in range(length + 1):
            for points in combinations(range(length), size):
                bound = transport(points, g)
                assert bound <= sum(g[length - p] for p in points[:2])
                assert bound <= sum(g[p + 1] for p in points[-2:])
                for bits in product((0, 1), repeat=size):
                    classes = tuple(tuple(p for p, bit in zip(points, bits) if bit == c) for c in (0, 1))
                    if all(differences_unique(c) for c in classes):
                        assert size <= bound
                        partitions += 1
    rejected = (0, 2, 3, 4, 5, 6, 7, 8, 11, 12)
    feasible_partitions = sum(all(differences_unique(tuple(p for p, bit in zip(rejected, bits) if bit == c))
                                  for c in (0, 1)) for bits in product((0, 1), repeat=len(rejected)))
    separation = [sum(g[14-p] for p in rejected[:2]), sum(g[p+1] for p in rejected[-2:]),
                  2*g[rejected[-1]-rejected[0]+1], transport(rejected, g)]

    words = identities = 0
    for length in range(0, 9):
        for word in product(range(3), repeat=length):
            words += 1
            for lag in range(1, length):
                for color in range(3):
                    pairs = tuple((i,j) for i,j in combinations(range(length), 2) if j-i == lag and word[i] == word[j] == color)
                    left = sum(g[length-lag-i] for i,j in pairs[:2])
                    right = sum(min(2, sum(j < length-span for i,j in pairs)) for span in spans.values())
                    assert left == right
                    identities += 1

    sets = assignments = proper = 0
    by_size = defaultdict(lambda: dict(sets=0, colorings=0, proper=0))
    six_min = None
    six_witness = None
    for size in range(7):
        for marks in combinations(range(6), size):
            sets += 1
            by_size[size]['sets'] += 1
            data = physical_geometry(marks)
            for signs in product((-1, 1), repeat=len(data[0])):
                mono, collision, edges = count_source(marks, signs, data)
                assignments += 1
                by_size[size]['colorings'] += 1
                if mono == 0:
                    proper += 1
                    by_size[size]['proper'] += 1
                    for i,j,k,l in combinations(range(len(data[0])), 4):
                        pts = {data[0][idx]:idx for idx in (i,j,k,l)}
                        xs = sorted({x for x,y in pts})
                        ys = sorted({y for x,y in pts})
                        if len(xs) == len(ys) == 2:
                            cycle = [(xs[0],ys[0]),(xs[1],ys[0]),(xs[1],ys[1]),(xs[0],ys[1])]
                            if all(pt in pts for pt in cycle):
                                assert not all(tuple(sorted((pts[cycle[t]],pts[cycle[(t+1)%4]]))) in edges for t in range(4))
                if size == 6 and (six_min is None or mono < six_min):
                    six_min, six_witness = mono, signs

    marks = (0,1,2,3)
    rectangle_signs = (1,-1,1,1,-1,1)
    data = physical_geometry(marks)
    mono, collision, edges = count_source(marks, rectangle_signs, data)
    rectangle = ((2,1),(3,1),(3,0),(2,0))
    index = {pt:i for i,pt in enumerate(data[0])}
    assert all(tuple(sorted((index[rectangle[t]],index[rectangle[(t+1)%4]]))) in edges for t in range(4))

    word1 = (0,0,0,0,0,0,1,2,1)
    word2 = (0,0,0,0,1,0,1,1,1)
    stats = [word_stats(word, g) for word in (word1, word2)]
    assert stats[0]['correlations'] == stats[1]['correlations']
    assert stats[0]['both'] != stats[1]['both']
    assert stats[0]['transport'] != stats[1]['transport']

    # Compare only after rebuilding all values from definitions.
    author_multi = json.loads((ROOT/'multilayer/results.json').read_text(encoding='utf-8'))
    author_completion = json.loads((ROOT/'completion/verification.json').read_text(encoding='utf-8'))
    author_gap = json.loads((ROOT/'information_gap.json').read_text(encoding='utf-8'))
    assert g == author_multi['exhaustively_computed_g']
    assert partitions-1 == author_multi['actual_two_class_partitions_checked']
    assert words-1 == author_multi['words_checked']
    assert identities == author_multi['literal_layercake_identities_checked']
    assert (sets, assignments, proper, six_min) == tuple(author_completion[k] for k in ('sets','binary_colorings','proper_colorings','six_mark_interval_minimum_monochromatic_L'))
    for i in range(2):
        assert [stats[i][key] for key in ('first','last','transport')] == author_gap[f'word{i+1}_caps']
    assert stats[0]['correlations'] == author_gap['correlations']

    files = ['CONTRACT.md','multilayer/THEOREM.md','multilayer/verify.py','multilayer/results.json',
             'completion/COUNTING.md','completion/verify.py','completion/verification.json',
             'information_gap.py','information_gap.json']
    output = dict(status='PASS', scope_findings_resolved_in_review=True,
                  capacities=g, shortest_spans=spans, ruler_witnesses=rulers,
                  partitions_checked_including_empty_domain=partitions,
                  word_count_including_empty_word=words, layer_identities=identities,
                  rejected_set=rejected, separation_capacities=separation, valid_partitions=feasible_partitions,
                  source_sets=sets, source_assignments=assignments, source_proper=proper,
                  by_size=dict(by_size), six_interval_minimum=six_min, six_interval_witness=six_witness,
                  improper_rectangle=dict(marks=marks,cells=data[0],signs=rectangle_signs,cycle=rectangle,
                                          monochromatic_L=mono,collisions=collision),
                  information_gap=dict(words=[word1,word2],statistics=stats,
                                       transport_also_distinguished=True),
                  source_sha256={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
                  checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'independent_results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:output[k] for k in ('status','partitions_checked_including_empty_domain','word_count_including_empty_word','layer_identities','source_sets','source_assignments','source_proper','six_interval_minimum','separation_capacities')}))


if __name__ == '__main__':
    main()
