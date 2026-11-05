"""Adversarial finite check of the fourth-moment multiplicity expansion."""
from itertools import product,combinations
from pathlib import Path
import json
checks=0
for n in (1,2,3,4):
 for word in product(range(3),repeat=n):
  for w in ([1],[0,2],[1,2,3],[0,1,2,1]):
   t=len(w)
   def q(indices):
    count=0
    for s in range(n+t-1):
     positions=[s-i for i in indices]
     if all(0<=p<n for p in positions) and len({word[p] for p in positions})==1:count+=1
    return count
   direct=0
   for s in range(n+t-1):
    f=[sum(w[i] for i in range(t) if 0<=s-i<n and word[s-i]==c) for c in range(3)]
    direct+=sum(v**4 for v in f)
   expanded=n*sum(v**4 for v in w)
   expanded+=4*sum(w[i]**3*w[j]*q([i,j]) for i in range(t) for j in range(t) if i!=j)
   expanded+=6*sum(w[i]**2*w[j]**2*q([i,j]) for i,j in combinations(range(t),2))
   expanded+=12*sum((w[i]**2*w[j]*w[k]+w[i]*w[j]**2*w[k]+w[i]*w[j]*w[k]**2)*q([i,j,k]) for i,j,k in combinations(range(t),3))
   expanded+=24*sum(w[i]*w[j]*w[k]*w[l]*q([i,j,k,l]) for i,j,k,l in combinations(range(t),4))
   assert direct==expanded,(word,w,direct,expanded)
   checks+=1
out={'label':'PROVED finite identity checks','cases':checks,'n_range':[1,4],
     'scope':'Supports the independently proved multinomial expansion; not a grid theorem.'}
Path('research_round2/checks/structural_moment_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
