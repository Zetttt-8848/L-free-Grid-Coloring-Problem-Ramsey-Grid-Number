"""Independent physical-triple and span-debt reconstructions for added claims."""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def mixed_check():
    classes = ({1,2,6,7,8}, {3,4,9}, {0,5})
    diagonal = {v:c for c,marks in enumerate(classes) for v in marks}
    source = {(2,1):2,(6,1):2,(6,2):2,(7,1):2,(7,2):1,(7,6):1,
              (8,1):2,(8,2):1,(8,6):2,(8,7):1,
              (4,3):0,(9,3):0,(9,4):0,(5,0):0}
    expected = {(v,u) for marks in classes for u,v in combinations(sorted(marks),2)}
    assert set(source) == expected
    assert all(color != diagonal[x] == diagonal[y] for (x,y),color in source.items())
    prescribed = source | {(v,v):color for v,color in diagonal.items()}
    # Enumerate every physical directed L in the square once.
    triples = tuple(((x,y),(x+d,y),(x+d,y+d)) for x in range(10)
                    for y in range(10) for d in range(1,10) if x+d < 10 and y+d < 10)
    source_counts = [0,0,0]
    prescribed_count = 0
    requests = defaultdict(lambda: defaultdict(list))
    other_parallel_requests = defaultdict(list)
    for triple in triples:
        if all(pt in prescribed for pt in triple):
            prescribed_count += 1
            assert len({prescribed[pt] for pt in triple}) > 1
        if all(pt in source for pt in triple):
            colors = {diagonal[pt[0]] for pt in triple}
            assert len(colors) == 1
            source_counts[next(iter(colors))] += 1
        for role,q in enumerate(triple):
            if not (q[0] > q[1] and diagonal[q[0]] != diagonal[q[1]]):
                continue
            pair = tuple(pt for index,pt in enumerate(triple) if index != role)
            if all(pt in source for pt in pair) and source[pair[0]] == source[pair[1]]:
                color = source[pair[0]]
                if role == 1:
                    other_parallel_requests[q].append((color,pair))
                else:
                    requests[q][color].append((role,pair))
    conflicts = []
    unique_requests = set()
    family_minimum = 0
    for q, by_color in requests.items():
        family_minimum += min(len(by_color[c]) for c in range(3))
        for color, reqs in by_color.items():
            for role,pair in reqs:
                triple_key = tuple(sorted(pair+(q,)))
                assert triple_key not in unique_requests
                unique_requests.add(triple_key)
    for q, by_color in sorted(requests.items()):
        count = 0
        for triple_requests in product(*(by_color[c] for c in range(3))):
            supports = tuple(pt for role,pair in triple_requests for pt in pair)
            assert len(set(supports)) == 6
            count += 1
        if count:
            conflicts.append(dict(cell=q,count=count,requests={c:by_color[c] for c in range(3)}))
    return dict(classes=[sorted(c) for c in classes],source_L_counts=source_counts,
                prescribed_L_count=prescribed_count,mixed_conflict_count=sum(c['count'] for c in conflicts),
                conflicts=conflicts,listed_request_family_minimum=family_minimum,
                listed_request_count=len(unique_requests),
                parallel_request_count_excluded_from_C_mix=sum(map(len,other_parallel_requests.values())))


def span_check():
    # Read the actual primary-source gap list, transcribed as mathematical input.
    gaps = (9,24,4,1,59,25,7,11,2,10,39,14,3,44,26,8,40,6,21,15,16,19,22)
    ruler = [0]
    for gap in gaps:
        ruler.append(ruler[-1]+gap)
    differences = Counter(b-a for a,b in combinations(ruler,2))
    assert len(ruler) == 24 and ruler[-1] == 425
    assert set(differences.values()) == {1}
    missing = min(d for d in range(1,426) if d not in differences)
    assert missing == 128
    assert not (set(x+1 for x in ruler) & set(425-x for x in ruler))
    old, new = {}, {}
    feasible_counts = {}
    for positions in range(1,481):
        feasible = []
        for t in range(7):
            # Direct endpoint extremal sums, independent of t*(p-t) shortcut.
            largest_total = sum(range(positions-t,positions))-sum(range(t))
            # At most two of t rulers may have minimum span; every other one
            # incurs at least one integer unit of additional span.
            minimum_total = sum(425 if j < 2 else 426 for j in range(t))
            if minimum_total <= largest_total:
                feasible.append(t)
        feasible_counts[positions] = feasible
        new[positions] = min(positions, 138+max(feasible))
        old[positions] = min(positions, 138+min(6,max(0,positions-425)))
    changed = [[p,old[p],new[p]] for p in range(1,481) if old[p] != new[p]]
    weights = {i:i*(86-i) for i in range(1,86)}
    margins = []
    for n in (463,464):
        quadratic = {}
        for label,cap in (('old',old),('new',new)):
            quadratic[label] = (sum((n-(j-i)-3*cap[n-(j-i)])*weights[i]*weights[j]
                                    for i,j in combinations(weights,2))
                                -n*sum(w*w for w in weights.values()))
        margins.append(dict(n=n,old=quadratic['old'],new=quadratic['new'],gain=quadratic['new']-quadratic['old']))
    occurrences = []
    total_weight = sum(weights.values())
    diagonal_energy = sum(w*w for w in weights.values())
    for n in (463,464):
        source_pair_term = 2*sum((48 if n-(j-i) >= 426 else 46)*weights[i]*weights[j]
                                 for i,j in combinations(weights,2))
        def residual(m):
            return m*m*total_weight*total_weight-(n+84)*(m*diagonal_energy+source_pair_term)
        possible_sizes = [m for m in range(n+1) if residual(m) <= 0]
        mmax = max(possible_sizes)
        possible_occurrences = [t for t in range(n-424)
                                if 24*t-t*(t-1)//2 <= mmax
                                and 576*t <= mmax*(t+23)]
        max_t = max(possible_occurrences)
        # The actual relevant Bonferroni range is short enough that it alone
        # already excludes all t>=9 once m<=164 is established.
        assert min(24*t-t*(t-1)//2 for t in range(9,n-424)) > mmax
        for orientation in (ruler, [425-x for x in ruler]):
            copies = [{q+s for q in orientation} for s in range(n-425)]
            assert all(len(left & right) == 1 for left,right in combinations(copies,2))
            for starts in ((0,), (0,1), (0,3,7,11), tuple(range(n-425))):
                incidence = Counter(x for s in starts for x in copies[s])
                t = len(starts)
                assert sum(incidence.values()) == 24*t
                assert sum(r*(r-1)//2 for r in incidence.values()) == t*(t-1)//2
                assert sum(r*r for r in incidence.values()) == t*(t+23)
        occurrences.append(dict(n=n,W=total_weight,a0=diagonal_energy,S=source_pair_term,
                                max_color_class=mmax,max_occurrences_per_orientation=max_t,
                                max_extremal_completion_classes_both_orientations=max_t*(max_t-1),
                                residual_at_164=residual(164),residual_at_165=residual(165),
                                minimum_bonferroni_for_t9_to_possible_max=min(24*t-t*(t-1)//2 for t in range(9,n-424))))
    return dict(ruler=ruler,positive_differences=len(differences),first_missing_difference=missing,
                changed_capacities=changed,margins=margins,global_occurrences=occurrences,
                external_theorems_not_reproved=['G(24)=425 and unique normalized ruler up to reflection','G(25)>=480'])


def main():
    mixed = mixed_check()
    span = span_check()
    author_mixed = json.loads((ROOT/'completion/verification.json').read_text(encoding='utf-8'))['proper_sources_with_incompatible_mixed_completion']
    assert mixed['source_L_counts'] == author_mixed['source_L_counts']
    assert mixed['prescribed_L_count'] == author_mixed['fully_prescribed_L_count']
    assert mixed['mixed_conflict_count'] == author_mixed['mixed_conflict_count']
    assert mixed['listed_request_family_minimum'] == author_mixed['minimum_monochromatic_Ls_in_listed_request_family']
    assert mixed['listed_request_count'] == author_mixed['listed_monochromatic_input_request_count']
    author_span = json.loads((ROOT/'multiscale/verification.json').read_text(encoding='utf-8'))
    assert span['ruler'] == author_span['optimal_ruler']
    assert span['changed_capacities'] == [[c['positions'],c['old'],c['new']] for c in author_span['capacity_changes']]
    assert span['margins'] == [dict(n=c['n'],old=c['old_gap'],new=c['shape_cost_gap'],gain=c['gain']) for c in author_span['kernel_margins']]
    for mine,theirs in zip(span['global_occurrences'],author_span['global_occurrence_counts']):
        for key in ('n','W','a0','S','max_color_class','max_occurrences_per_orientation','max_extremal_completion_classes_both_orientations'):
            assert mine[key] == theirs[key]
    artifacts = ['completion/COUNTING.md','completion/verify.py','completion/verification.json',
                 'multiscale/THEOREM.md','multiscale/verify.py','multiscale/verification.json']
    output = dict(status='PASS',mixed=mixed,span=span,
                  source_sha256={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts},
                  checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'supplemental_results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output))


if __name__ == '__main__':
    main()
