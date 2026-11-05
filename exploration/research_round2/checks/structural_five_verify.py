from pathlib import Path
from hashlib import sha256
import json
path=Path('research_round2/certificates/structural_five_diagonal.json')
grid=json.loads(path.read_text())['grid']
assert len(grid)==5 and all(len(row)==5 and all(c in (0,1,2) for c in row) for row in grid)
assert all(grid[i][i]==0 for i in range(5))
checked=0
for x in range(5):
    for y in range(5):
        for d in range(1,min(5-x,5-y)):
            checked+=1
            assert len({grid[x][y],grid[x+d][y],grid[x+d][y+d]})>1
assert checked==30
out={'label':'PROVED finite witness','n':5,'corners_checked':checked,
     'source_sha256':sha256(path.read_bytes()).hexdigest(),'main_diagonal_color':0}
Path('research_round2/checks/structural_five_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
