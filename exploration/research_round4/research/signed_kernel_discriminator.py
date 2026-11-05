"""Test a new two-sided coefficient condition, not the old admissibility claim."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
data=json.loads((root.parent.parent/'research_round2/certificates/kernel_dual_464.json').read_text(encoding='utf-8'))
Q=data['node_denominator'];R=data['mass_denominator'];nodes=data['nodes'];n=data['n']
p0=[1]*len(nodes);p1=[x for x,l in nodes];Qd=1
violations=[];worst=None
for d in range(1,n):
    Qd*=Q
    # f_d=-2 sum lambda_j T_d(x_j). Test f_d <= n-d.
    numerator=(n-d)*R*Qd+2*sum(l*p for (x,l),p in zip(nodes,p1))
    value=numerator/(R*Qd)
    if numerator<0:violations.append(dict(d=d,upper_gap=float(value)))
    if worst is None or value<worst['upper_gap']:worst=dict(d=d,upper_gap=float(value))
    p0,p1=p1,[2*x*b-Q*Q*a for (x,l),a,b in zip(nodes,p0,p1)]
out=dict(purpose='new two-sided dual condition for signed autocorrelations',
         condition='f_d<=n-d for every positive d<n',violations=violations,worst=worst,
         scope='integer signs decide each comparison; decimal gap only displays its size')
(root/'signed_kernel_discriminator.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
