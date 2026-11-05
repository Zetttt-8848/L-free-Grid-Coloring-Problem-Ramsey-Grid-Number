"""Discovery: do the literal colorings span a uniform rainbow marginal?"""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parent
a=json.loads((root/'signed_rainbow_functional_probe.json').read_text())
vs=np.array([w['vector'] for w in a['witnesses']],dtype=float)
size=np.array(a['sizes'],dtype=float)
r=linprog(-np.ones(len(vs)),A_eq=vs.T,b_eq=size,bounds=(0,None),method='highs')
out=dict(witness_count=len(vs),orbit_count=len(size),status=r.message,success=r.success)
if r.success:out.update(mass=float(-r.fun),coefficients=r.x.tolist(),residual=float(np.max(np.abs(vs.T@r.x-size))))
(root/'signed_rainbow_mixture_probe.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='coefficients'}))
