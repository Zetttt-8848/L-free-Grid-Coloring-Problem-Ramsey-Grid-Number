"""Construct rational K1 data. It is not certified until independent verification."""
from pathlib import Path
import json
src=Path(__file__).with_name('kernel_dual_discovery.json')
data=json.loads(src.read_text())
assert data['status']==0
Q=2**50
R=10**12
out={'label':'UNVERIFIED until kernel_dual_verify.py passes','n':464,'degree':463,
     'node_denominator':Q,'mass_denominator':R,
     'nodes':[[round(v['x']*Q),round(v['lambda']*R)] for v in data['nodes']],
     'claimed_mass_upper_bound':448,'claimed_coefficient_margin':'1/1000',
     'table_position_counts':[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,
        217,247,284,334,357,373,426,481,493,554,586]}
target=Path('research_round2/certificates/kernel_dual_464.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(target,len(out['nodes']))
