"""Independent normalization and affine-copy count audit for the window cuts."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
source=json.loads((ROOT/'window13.json').read_text());check=json.loads((ROOT/'window13.check.json').read_text());catalog=json.loads((ROOT/'patterns_window13.json').read_text())
assert check['verdict']=='PASS' and check['source_sha256']==hashlib.sha256((ROOT/'window13.json').read_bytes()).hexdigest()
normalized=set()
for bad in source['minimal_bad']:
    mask=bad['mask'];marks=[i for i in range(source['width']) if mask>>i&1];offsets=[x-min(marks) for x in marks];g=0
    for x in offsets:
        a,b=g,x
        while b:a,b=b,a%b
        g=a
    normalized.add(tuple(x//g for x in offsets))
assert len(catalog['patterns'])==len(normalized) and set(map(tuple,catalog['patterns']))==normalized
copy_counts=[sum((464-first)//p[-1] for first in range(1,465)) for p in catalog['patterns']]
out=dict(verdict='PASS',source_minimal_bad_supports=len(source['minimal_bad']),normalized_shapes=len(normalized),shape_counts_by_cardinality={k:sum(len(p)==k for p in normalized) for k in sorted({len(p) for p in normalized})},affine_copies_at464=sum(copy_counts),copy_counts=copy_counts,scope='Every listed pattern is an integer-affine normalization of a RUP-certified bad support; every source support is represented')
(ROOT/'patterns_window13.check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='copy_counts'},indent=2))
