"""Executed single-class integer scout; see PROVENANCE.md for evidence limits."""
from bisect import bisect_right
G=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
def cap(n,h): return 2*(bisect_right(G,n-h)-1)
def nearest(n):
 m=(n+2)//3; best=(-10**9,None)
 for c in range(1,m//2+1):
  K=c*m-c*(c+1)//2
  rem=K;val=0
  for d in range(1,n):
   use=min(rem,cap(n,d));val+=d*use;rem-=use
   if rem==0:break
  upper=c*(c+1)//2*n-c*(c+1)*(2*c+1)//6
  if val-upper>best[0]:best=(val-upper,c)
 return best
for n in range(450,500):
 b=nearest(n)
 if n%10==0 or b[0]>0: print(n,b)
