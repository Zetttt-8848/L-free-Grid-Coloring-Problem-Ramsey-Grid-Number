"""Finite arithmetic checks for GN1; universal argument is in the proof."""
from fractions import Fraction
from pathlib import Path
import json
rows=[]
for k in range(3,13):
    N=k**(2**k);t=k*k
    assert t<=N and k**(2**(k-1))>=4*(k-2)
    scaled_margin=3*(k**3-2*k+1)*N-k*k*(k**4-1)
    direct=(Fraction(2*k-1,k*k)*N)*(t-1)-Fraction(t*t-1,3)-(k-1)*N
    assert direct==Fraction(scaled_margin,3*k*k)>0
    ratio=Fraction(2**(2**(k-1)),k)
    assert ratio>1
    rows.append({'k':k,'N':str(N),'scaled_margin':str(scaled_margin),
                 'margin_denominator':3*k*k,'inherited_V_over_new':str(ratio)})
out={'label':'PROVED finite arithmetic, not the universal proof','k_range':[3,12],'rows':rows}
Path('research_round2/checks/general_neighbor_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print({'label':out['label'],'k_range':out['k_range'],'first_three':rows[:3]})
