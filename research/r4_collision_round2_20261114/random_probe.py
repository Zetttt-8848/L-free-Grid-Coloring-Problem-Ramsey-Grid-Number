"""Deterministic bounded reconnaissance, not an infeasibility certificate."""
import json,random,time
from pathlib import Path
from pilot import golomb_partition,search

rng=random.Random(20261114); begin=time.monotonic(); attempts=0; nonpart=0
for i in range(1200):
    if time.monotonic()-begin>90:break
    H=sorted(rng.sample(range(101,131),rng.choice([8,9,10,11,12])))
    if golomb_partition(H) is not None:continue
    nonpart+=1;attempts+=1
    witness=search(H,1000)
    if witness:
        Path(__file__).with_name('counterexample.json').write_text(json.dumps(witness,indent=2)+'\n')
        print('WITNESS',H);break
else:i=1199
out=dict(seed=20261114,draws=i+1,nonpartition_candidates=nonpart,solver_attempts=attempts,elapsed=time.monotonic()-begin,
         scope='Reconnaissance only; false/limited solver returns are not infeasibility evidence')
Path(__file__).with_name('random_log.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
