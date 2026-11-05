"""Exact evaluation of the newly derived interval discrepancy inequality."""
import bisect,json
from pathlib import Path
H=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
def q(m):return bisect.bisect_right(H,m)-1
rows=[]
for n in [430,440,450,454,460,463,464,465,470,480]:
    cap=[0]+[6*q(n-d) for d in range(1,n)]
    best=None
    for t in range(3,n,3):
        # V upper multiplied by three; no floating-point arithmetic.
        upper=2*n*t+2*sum((t-d)*(3*cap[d]-(n-d)) for d in range(1,t))
        boundary=8*t//3  # three times the boundary minimum, t divisible by 3
        lower=3*max(0,n-t-cap[t])+boundary
        margin=lower-upper
        row=dict(n=n,t=t,upper_times3=upper,lower_times3=lower,margin_times3=margin)
        if best is None or margin>best['margin_times3']:best=row
    rows.append(best)
    print(json.dumps(best))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
