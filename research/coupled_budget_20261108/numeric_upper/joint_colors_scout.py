"""Initial balanced-class scout, not a universal theorem; use verify.py instead."""
from capacities import difference_cap

def max_weight(n,ms,c):
 coeff=[]
 for m in ms:
  coeff.extend(min(c,r)-min(c,m-1-r) for r in range(m))
 return sum(i*w for i,w in enumerate(sorted(coeff)))
def greedy(n,K,capsmult=3):
 val=0
 for d in range(1,n):
  use=min(K,capsmult*difference_cap(n,d));val+=use*d;K-=use
  if K==0:return val
 return 10**20

def test(n):
 ms=[n//3+(i<n%3) for i in range(3)]
 b=(-1e20,None)
 for c in range(1,40):
  K=sum(sum(m-j for j in range(1,min(c,m-1)+1)) for m in ms)
  gap=greedy(n,K)-max_weight(n,ms,c)
  if gap>b[0]:b=(gap,c)
 return b
for n in range(300,494):
 b=test(n)
 if n%10==0 or b[0]>0:print(n,b)
