from pathlib import Path
from itertools import product
from collections import Counter
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[1]
A=set(json.loads((ROOT/'joint/witness_464.json').read_text())['marks'])
groups=[]
for a in range(1,116):
    starts=[x for x in range(1,465-4*a) if all(x+i*a in A for i in range(5))]
    groups.append({'step':a,'starts':starts})
bad=[row for row in groups if len(row['starts'])>1]
assert bad
enums=[]
for m in (1,2,4,5):
    pts=[(j,i) for j in range(m) for i in range(j+1)]
    ids={p:i for i,p in enumerate(pts)}
    corners=[]
    for p in pts:
        for d in range(1,m):
            q=(p[0]+d,p[1]);r=(p[0]+d,p[1]+d)
            if q in ids and r in ids:corners.append(tuple(ids[x] for x in (p,q,r)))
    patterns=Counter();accepted=0;witnesses=[]
    for bits in product((0,1),repeat=len(pts)):
        if any(bits[a]==bits[b]==bits[c] for a,b,c in corners):continue
        accepted+=1
        pattern=''.join(str(bits[ids[(j,j)]]) for j in range(m))
        patterns[pattern]+=1
        if m==4:witnesses.append(list(bits))
    enums.append({'m':m,'cells':len(pts),'corners':len(corners),
                  'raw':2**len(pts),'accepted':accepted,'rejected':2**len(pts)-accepted,
                  'diagonal_patterns':dict(patterns),'valid_colorings':witnesses})
assert [x['accepted'] for x in enums]==[2,6,36,0]
assert enums[-1]['corners']==20
result={'status':'finite exact checks PASS','ap5_occurrences':sum(464-4*a for a in range(1,116)),
        'groups':groups,'violated_groups':bad,'enumerations':enums,
        'scope':'Witness diagnostics and exhaustive weak-triangle colorings; universal CAP1 proof is separate.'}
(ROOT/'cap/ap5_exact_results.json').write_text(json.dumps(result,indent=2)+'\n')
log={'representation':'row-major labeled binarycolorings on weaktriangle W_m; no symmetryquotient',
     'raw_universe':'2^(m(m+1)/2)', 'coverage':'itertools.product yields everybitvector once',
     'pruning':'none; reject only a literal monochromaticcorner',
     'runtime':'Python standardlibrary, integer arithmetic',
     'domain_regressions':'W1 has2 colorings; W2 onecorner excludes000/111 and has6',
     'results':enums,'AP5_violation_steps':[row['step'] for row in bad]}
(ROOT/'cap/ap5_enumeration.log').write_text(json.dumps(log,indent=2)+'\nRUN COMPLETE\n')
print(json.dumps({'bad_AP5_groups':len(bad),'first_bad_group':bad[0],
                  'counts':[(x['m'],x['raw'],x['accepted']) for x in enums],
                  'W4_diagonal_patterns':enums[-2]['diagonal_patterns']}))
