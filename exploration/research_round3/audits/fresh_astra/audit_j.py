"""Fresh reviewer implementation: standard-library only, no author imports.
Triangle geometry is built from horizontal cell pairs, and RUP uses bit masks.
"""
import collections
import hashlib
import itertools
import json
import math
import pathlib
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / 'research_round3' / 'joint'
OUT = pathlib.Path(__file__).resolve().parent
READ = {}

def raw(name):
    p = SRC / name
    data = p.read_bytes()
    READ[str(p.relative_to(ROOT)).replace('\\', '/')] = hashlib.sha256(data).hexdigest()
    return data.decode('utf-8-sig')

def get(name):
    return json.loads(raw(name))

def triangle(A):
    A = sorted(A)
    cells = [(x, y) for y in A for x in A if x > y]
    ids = {p: i+1 for i, p in enumerate(cells)}
    corners = []
    clauses = []
    for y in A:
        xs = [x for x in A if x > y]
        for x, z in itertools.combinations(xs, 2):
            top = (z, y+z-x)
            if top in ids:
                triple = ((x,y),(z,y),top)
                corners.append((x,y,z-x))
                clause = tuple(ids[p] for p in triple)
                clauses.extend((clause, tuple(-v for v in clause)))
    if cells:
        clauses.append((1,))
    return cells, corners, clauses

def clause_set(clauses):
    return collections.Counter(frozenset(c) for c in clauses)

def parse_cnf(name):
    clauses, pending, header = [], [], None
    for line in raw(name).splitlines():
        if line.startswith('c') or not line.strip():
            continue
        if line.startswith('p '):
            assert header is None
            _, kind, n, m = line.split()
            assert kind == 'cnf'
            header = int(n), int(m)
            continue
        for x in map(int, line.split()):
            if x:
                pending.append(x)
            else:
                clauses.append(tuple(pending)); pending = []
    assert not pending and header is not None
    assert len(clauses) == header[1]
    assert all(1 <= abs(x) <= header[0] for c in clauses for x in c)
    return header[0], clauses

def parse_rup(name):
    rows = []
    for line in raw(name).splitlines():
        if not line.strip() or line.startswith('c'):
            continue
        values = list(map(int, line.split()))
        assert values[-1] == 0 and 0 not in values[:-1]
        rows.append(values[:-1])
    return rows

def bits(clause, n):
    pos, neg = 0, 0
    for v in clause:
        assert 1 <= abs(v) <= n
        if v > 0:
            pos |= 1 << (v-1)
        else:
            neg |= 1 << (-v-1)
    return pos, neg

def conflict(db, true, false):
    if true & false:
        return True
    while True:
        old = true | false
        for pos, neg in db:
            if (pos & true) or (neg & false):
                continue
            left = (pos | neg) & ~(true | false)
            if not left:
                return True
            if left & (left-1) == 0:
                if pos & left:
                    true |= left
                else:
                    false |= left
        if true | false == old:
            return False

def check_rup(clauses, proof, n):
    db = [bits(c, n) for c in clauses]
    assert proof and proof[-1] == []
    for i, row in enumerate(proof):
        pos, neg = bits(row, n)
        # Negating the proposed clause assigns its positive literals false.
        assert conflict(db, neg, pos), ('RUP failure', i+1, row)
        db.append((pos, neg))
    return len(proof)

def primitive(A):
    A = [a-min(A) for a in A]
    g = math.gcd(*A)
    return tuple(a//g for a in A)

def window_check():
    data = get('window13.json')
    width = data['width']
    assert width == 13
    bad, good = [], []
    rup_total = 0
    for obj in data['minimal_bad']:
        mask, A = obj['mask'], obj['marks']
        assert A == [i for i in range(width) if mask >> i & 1]
        cells, _, clauses = triangle(A)
        proof = obj['proof']
        nv, disk_clauses = parse_cnf(f'window13/bad_{mask}.cnf')
        assert nv == len(cells) and clause_set(disk_clauses) == clause_set(clauses)
        assert proof == parse_rup(f'window13/bad_{mask}.rup')
        rup_total += check_rup(clauses, proof, len(cells))
        bad.append(mask)
    print('window bad proofs independently checked:', len(bad), rup_total, flush=True)
    for obj in data['maximal_good']:
        mask, A = obj['mask'], obj['marks']
        assert A == [i for i in range(width) if mask >> i & 1]
        cells, corners, _ = triangle(A)
        colors = obj['colors']
        assert len(colors) == len(cells) and set(colors) <= {0,1}
        color = dict(zip(cells, colors))
        assert all(len({color[x,y],color[x+d,y],color[x+d,y+d]}) > 1 for x,y,d in corners)
        good.append(mask)
    assert len(set(bad)) == len(bad) and len(set(good)) == len(good)
    assert all(a == b or a & b != a for a in bad for b in bad)
    assert all(a == b or a & b != a for a in good for b in good)
    classes = []
    for mask in range(1 << width):
        isbad = any(b & mask == b for b in bad)
        isgood = any(mask & g == mask for g in good)
        assert isbad != isgood, ('coverage conflict/missing', mask)
        classes.append(int(isgood))
    # Check minimality/maximality from the now established whole classification.
    assert all(classes[b ^ (1 << i)] for b in bad for i in range(width) if b >> i & 1)
    assert all(not classes[g | (1 << i)] for g in good for i in range(width) if not g >> i & 1)
    capacities = [max(m.bit_count() for m in range(1 << w) if classes[m]) for w in range(1,14)]
    normalized = sorted({primitive(obj['marks']) for obj in data['minimal_bad']})
    catalog = get('patterns_window13.json')
    assert sorted(map(tuple,catalog['patterns'])) == normalized
    assert all(tuple(p[-1]-x for x in reversed(p)) in normalized for p in normalized)
    measured = dict(total=len(classes), good=sum(classes), bad=len(classes)-sum(classes),
                    minimal_bad=len(bad), maximal_good=len(good), rup_additions=rup_total,
                    capacities=capacities, primitive_patterns=len(normalized))
    assert measured == dict(total=8192,good=7147,bad=1045,minimal_bad=109,maximal_good=334,
                            rup_additions=31605,capacities=[1,2,3,4,5,5,6,7,7,8,9,9,10],primitive_patterns=56)
    return measured, normalized

def ap_list(n, length):
    # Independent endpoint enumeration: a progression is determined by its ends.
    for first in range(1, n+1):
        for last in range(first+length-1, n+1, length-1):
            step = (last-first)//(length-1)
            yield first, step, tuple(range(first, last+1, step))

def family_occurrences(A, n, left, right, separation):
    found = []
    for h in range(1, n):
        if (separation+max(right))*h+1 > n-1:
            break
        ls = [x for x in A if x+max(left)*h <= n and all(x+i*h in A for i in left)]
        rs = [x for x in A if x+max(right)*h <= n and all(x+i*h in A for i in right)]
        found.extend((h, x, z) for x in ls for z in rs if z > x+separation*h)
    return sorted(found)

def witness_check(name, patterns, window_required=False, family_required=False):
    obj = get(name)
    A = obj['marks']; n = obj['n']; s = set(A)
    assert n == 464 and obj['size'] == 155 and len(A) == len(s) == 155
    assert A == sorted(A) and A[0] == 1 and A[-1] <= n
    H = [0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
    profile = [sum(x+d in s for x in s) for d in range(1,n)]
    cap = [2*max(j for j,v in enumerate(H) if v <= n-d) for d in range(1,n)]
    assert all(a<=b for a,b in zip(profile,cap)) and sum(profile) == math.comb(155,2)
    aps6 = list(ap_list(n,6))
    assert not any(set(p) <= s for _,_,p in aps6)
    aps5 = list(ap_list(n,5))
    contained5 = [(a,h) for a,h,p in aps5 if set(p) <= s]
    counts5 = collections.Counter(h for a,h in contained5)
    result = dict(size=155, pair_count=sum(profile), cap_checks=len(cap), ap6_checks=len(aps6),
                  max_multiplicity=max(profile), first27=profile[:27],
                  first27_above45=sum(x>45 for x in profile[:27]),
                  restricted_sizes=[sum(a<=m for a in A) for m in (463,462)],
                  ap5_checks=len(aps5), ap5_groups=len({h for a,h,p in aps5}),
                  ap5_contained=contained5, ap5_max_same_step=max(counts5.values(),default=0))
    if window_required:
        count = 0
        for pat in patterns:
            for step in range(1,(n-1)//pat[-1]+1):
                for first in range(1,n-pat[-1]*step+1):
                    count += 1
                    assert not all(first+x*step in s for x in pat), (name,first,step,pat)
        assert count == 543170
        assert max(counts5.values(),default=0) <= 1
        result['window_affine_checks'] = count
    first_family = family_occurrences(s,n,[0,1,2,4,5,6],[0,3,4,5],6)
    reflected = family_occurrences({n+1-a for a in s},n,[0,1,2,4,5,6],[0,3,4,5],6)
    result['family1_forward'] = first_family
    result['family1_reflected'] = reflected
    if family_required:
        assert not first_family and not reflected
        lastcore = set(get('triangle_core_v4.json')['marks'])
        assert lastcore <= s
    second = family_occurrences(s,n,[0,1,2,4],[0,1,2,3,4],4)
    result['family2_forward'] = second
    print(name, 'independently checked', flush=True)
    return result

def core_check(tag):
    obj = get(tag+'.json')
    cells, corners, clauses = triangle(obj['marks'])
    assert cells == list(map(tuple,obj['cells']))
    assert set(corners) == set(map(tuple,obj['corners']))
    assert len(cells) == obj['variables'] and len(clauses) == obj['clause_count']
    nv, serialized = parse_cnf(tag+'.cnf')
    assert nv == len(cells) and clause_set(clauses) == clause_set(serialized)
    lines = check_rup(clauses,parse_rup(tag+'.rup'),len(cells))
    return dict(marks=obj['marks'],cells=len(cells),corners=len(corners),clauses=len(clauses),rup_additions=lines)

def coefficients(tag, left, right, separation, specialization):
    obj = get(tag+'.json')
    x,h,b = specialization
    forms = [(1,i,0) for i in left]+[(1,i,1) for i in right]
    assert [a*x+c*h+d*b for a,c,d in forms] == obj['marks']
    cells,corners,_ = triangle(obj['marks'])
    bymark = dict(zip(obj['marks'],forms))
    def sub(a,b): return tuple(x-y for x,y in zip(a,b))
    def add(a,b): return tuple(x+y for x,y in zip(a,b))
    steps = collections.Counter()
    for x0,y0,d0 in corners:
        horizontal = sub(bymark[x0+d0],bymark[x0])
        vertical = sub(bymark[y0+d0],bymark[y0])
        assert horizontal == vertical
        assert horizontal[0] == 0
        # h>=1 and b>=separation*h+1 are the exact integer domain.
        a,c = horizontal[1:]
        assert c >= 0 and a+separation*c >= 0 and (a+separation*c > 0 or c > 0)
        steps[(a,c)] += 1
    for old,new in zip(forms,forms[1:]):
        delta = sub(new,old); a,c=delta[1:]
        assert delta[0]==0 and c>=0 and a+separation*c >=0 and (a+separation*c>0 or c>0)
    # Exactly evaluate identities, including out-of-domain points without calling them instances.
    for xx,hh,bb in [(0,0,0),(1,1,1),(1,1,separation+1),(1000,99,100000)]:
        evaluate = lambda f: f[0]*xx+f[1]*hh+f[2]*bb
        for x0,y0,d0 in corners:
            assert evaluate(sub(bymark[x0+d0],bymark[x0])) == evaluate(sub(bymark[y0+d0],bymark[y0]))
    # Only now compare the independently obtained geometry/coefficients to the
    # corresponding serialized author audit record; the record was not an input.
    comparison = get('parametric_core.check.json' if separation==6 else 'parametric_ap5_core.check.json')
    record_rows = comparison['identities'] if separation==6 else comparison['coefficient_checks']
    recorded={tuple(row['original_corner'] if separation==6 else row['corner']):
              (row['step_h_coefficient'],row['step_b_coefficient']) for row in record_rows}
    assert set(recorded)==set(corners)
    for x0,y0,d0 in corners:
        assert recorded[x0,y0,d0]==sub(bymark[x0+d0],bymark[x0])[1:]
    assert all(row['zero_difference' if separation==6 else 'identity']==[0,0,0] for row in record_rows)
    return dict(cells=len(cells),identities=len(corners),separation=separation,
                step_coefficient_counts=[dict(h=a,b=c,count=v) for (a,c),v in sorted(steps.items())],
                universal_positive_steps=True,universal_order=True)

def self_tests():
    assert conflict([bits([1],1),bits([-1],1)],0,0)
    assert not conflict([bits([1,2],2)],0,0)
    assert conflict([bits([1,2],2)],0,3)
    for A in [[],[0],[0,1],[0,1,2]]:
        cells,corners,clauses=triangle(A)
        for x,y,d in corners:
            assert d>0 and (x,y) in cells and (x+d,y) in cells and (x+d,y+d) in cells
    # Small UNSAT triangle T_6 also independently exhaustive over all 2^15 assignments.
    cells,corners,_=triangle(list(range(6)))
    assert len(cells)==15 and len(corners)==20
    ids={p:i for i,p in enumerate(cells)}
    triples=[sum(1<<ids[p] for p in [(x,y),(x+d,y),(x+d,y+d)]) for x,y,d in corners]
    assert not any(all(mask & c not in (0,c) for c in triples) for mask in range(1<<len(cells)))

def main():
    start=time.perf_counter()
    self_tests()
    cores={tag:core_check(tag) for tag in ['triangle_core','triangle_core_v2','triangle_core_v3','triangle_core_v4']}
    print('four triangle cores independently checked',flush=True)
    window,patterns=window_check()
    witnesses={name:witness_check(name,patterns,*options) for name,options in [
        ('witness_464.json',(False,False)),('witness_464_window_ap5.json',(True,False)),
        ('witness_464_parametric.json',(True,True))]}
    families={
        'first':coefficients('triangle_core_v3',[0,1,2,4,5,6],[0,3,4,5],6,(2,1,20)),
        'second':coefficients('triangle_core_v4',[0,1,2,4],[0,1,2,3,4],4,(1,1,9))}
    assert len(witnesses['witness_464_window_ap5.json']['family1_forward'])==7
    assert len(witnesses['witness_464_window_ap5.json']['family1_reflected'])==4
    assert (1,1,10) in map(tuple,witnesses['witness_464_parametric.json']['family2_forward'])
    result=dict(verdict='PASS',scope='Finite certificate checks and exact coefficient lifting; no full-grid existence claim',
                cores=cores,window=window,witnesses=witnesses,families=families,
                input_sha256=READ,runtime_seconds=time.perf_counter()-start)
    (OUT/'J_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(verdict=result['verdict'],window=window,cores=cores,families=families),indent=2),flush=True)

if __name__=='__main__':
    main()
