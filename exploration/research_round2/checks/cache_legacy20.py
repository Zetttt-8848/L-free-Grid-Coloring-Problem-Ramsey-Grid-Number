from pathlib import Path
from hashlib import sha256
import json
src=Path('C:/Users/ZhuanZ/Desktop/L-free coloring Ramsey Number/Kimi_Agent_核心推导PDF/lgrid_sat/witnesses_n20_k3.txt')
rows=[[int(v) for v in row.split()] for row in src.read_text().splitlines() if row.strip()]
assert len(rows)==20 and all(len(row)==20 and all(v in (1,2,3) for v in row) for row in rows)
grid=list(map(list,zip(*rows)))
canonical='\n'.join(' '.join(map(str,row)) for row in grid)+'\n'
digest=sha256(canonical.encode('ascii')).hexdigest()
assert digest=='a2008d366873eb21df85479a63a4e6e5a0ed0a594200370ee623f8b08cb11f83'
checked=0
for x in range(20):
 for y in range(20):
  for d in range(1,min(20-x,20-y)):
   assert len({grid[x][y],grid[x+d][y],grid[x+d][y+d]})>1
   checked+=1
assert checked==2470
out=Path('research_round2/sources/legacy20_transposed.txt')
out.write_bytes(canonical.encode('ascii'))
record={'status':'PASS: exact inherited benchmark match','source':str(src),
        'source_sha256':sha256(src.read_bytes()).hexdigest(),'transposed':True,
        'cached_file':out.name,'cached_sha256':digest,'corners_checked':checked,
        'claim':'Existing accepted lower-bound witness cached for reproduction; no new lower bound.'}
out.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(record)
