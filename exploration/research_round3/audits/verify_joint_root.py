"""Independent bitset verification of the literal one-class witness."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'joint/witness_464.json'
data=json.loads(path.read_text())
A=data['marks'];n=464
assert len(A)==155 and A==sorted(set(A)) and A[0]==1 and A[-1]<=n
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
mask=sum(1<<(a-1) for a in A)
profile=[]
for d in range(1,n):
    actual=(mask & (mask>>d)).bit_count()
    cap=2*sum(h<=n-d for h in H[1:])
    assert actual<=cap,(d,actual,cap)
    profile.append(actual)
assert sum(profile)==155*154//2
aps=0;bad=0
for d in range(1,(n-1)//5+1):
    starts=mask
    for j in range(1,6):starts&=mask>>(j*d)
    bad+=starts.bit_count();aps+=n-5*d
assert bad==0
result={'verdict':'PASS','method':'Independent integer-bitset intersections for distances and sixfold shifts for AP starts',
        'source_sha256':sha256(path.read_bytes()).hexdigest(),
        'n':n,'size':len(A),'pairs':sum(profile),'distance_constraints':len(profile),
        'APs':aps,'bad_APs':bad,'small_distance_profile':profile[:27],
        'small_distances_above_45':[d for d in range(1,28) if profile[d-1]>45],
        'scope':'One-class necessary conditions are feasible; no grid coloring or Ramsey lower bound is asserted.'}
(ROOT/'audits/joint_root_verified.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
