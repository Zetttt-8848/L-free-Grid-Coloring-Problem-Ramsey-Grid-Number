"""Executed integer waterfilling scout; not a new sub-493 certificate."""
from bisect import bisect_right
G=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
def cap(n,h):return 2*(bisect_right(G,n-h)-1)
def water(caps,s):
 q=0
 while sum(min(q+1,c) for c in caps)<=s:q+=1
 vals=[min(q,c) for c in caps];r=s-sum(vals)
 return sum(x*x for x in vals)+r*(2*q+1)
def test(n):
 a=(n+2)//3;best=(-10**9,None)
 for t in range(2,200):
  cs=[min(t,x+1,n+t-1-x,a) for x in range(n+t-1)]
  lo=water(cs,a*t);up=a*t+2*sum((t-h)*cap(n,h) for h in range(1,t))
  if lo-up>best[0]:best=(lo-up,t)
 return best
for n in [460,470,480,487,490,492,493,500,510,520]:print(n,test(n))
