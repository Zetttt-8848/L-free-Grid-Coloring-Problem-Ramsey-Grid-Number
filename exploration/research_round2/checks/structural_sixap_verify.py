"""Independent verification of the P2d word, using only integer arithmetic."""
from pathlib import Path
from hashlib import sha256
from bisect import bisect_right
import json

path=Path('research_round2/certificates/structural_sixap_word.json')
data=json.loads(path.read_text()); word=data['word']; n=len(word)
assert n==464 and all(type(c)==int and c in range(3) for c in word)
assert all(len(set(word[i:i+3]))==3 for i in range(0,n-2,3))
progressions=0
for d in range(1,(n-1)//5+1):
    for x in range(n-5*d):
        assert len({word[x+j*d] for j in range(6)})>1, (x,d)
        progressions+=1
w=[min(i,94-i) for i in range(1,94)]
f=[[0]*(n+len(w)-1) for _ in range(3)]
for j,c in enumerate(word):
    for i,weight in enumerate(w): f[c][j+i]+=weight
E=sum(v*v for row in f for v in row)
W2=sum(sum(f[c][s] for c in range(3))**2 for s in range(len(f[0])))
excess=3*E-W2
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
violations=[]
for d in range(1,n):
    q=bisect_right(H,n-d)-1
    counts=[sum(word[x]==c==word[x+d] for x in range(n-d)) for c in range(3)]
    for c,r in enumerate(counts):
        if r>2*q:violations.append([d,c,r,2*q])
assert excess<3114868
out={'label':'PROVED finite witness properties', 'source_sha256':sha256(path.read_bytes()).hexdigest(),
     'n':n,'six_APs_checked':progressions,'aligned_rainbow_triples':154,
     'E':E,'W2':W2,'excess':excess,'required_excess':3114868,
     'cap_violations':violations,'scope':'Six-AP exclusion alone does not force the required excess for the inherited tent at464. This word is not asserted to satisfy the Golomb caps or extend to a grid coloring.'}
Path('research_round2/checks/structural_sixap_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='cap_violations'})
print('violated individual caps',len(violations))
