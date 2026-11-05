"""Re-run the bounded audit and write a truthful version-1 evidence record."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json, platform, subprocess, sys, time

root=Path(__file__).resolve().parents[2]
script=root/'research_20260909/checks/general_k_check.py'
output=root/'research_20260909/checks/general_k_output.json'
proof=root/'research_20260909/routes/general_k.md'
started=datetime.now(timezone.utc).isoformat()
tic=time.perf_counter()
completed=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True,timeout=30)
runtime=time.perf_counter()-tic
if completed.returncode:
    raise RuntimeError(completed.stderr)
data=json.loads(completed.stdout)
output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

def record(path):
    return dict(path=path.relative_to(root).as_posix(),sha256=sha256(path.read_bytes()).hexdigest())

manifest={
 'schema_version':1,
 'claim_id':'general-k-G3-G6-bounded-checks',
 'repository':{'commit':'unavailable: supplied CP0 workspace; no git revision used','dirty':True},
 'command':'python research_20260909/checks/general_k_check.py',
 'environment':{'software':['Python '+platform.python_version(),platform.platform()],
                'hardware':platform.machine()+'; '+platform.processor()},
 'mathematics':{
  'assertion_tested':'Exact recurrence expansion for k=1..8, exact R4 certificate at N=91^4, and exhaustive small-grid instances of nesting, Golomb equivalence, and diagonal capacity bounds.',
  'coefficient_domain':'arbitrary-precision integers and rational Fractions; integer square roots only',
  'conventions':'grid rows downward; corner {(x,y),(x+d,y),(x+d,y+d)}, d>0; script uses zero-based coordinates and proof uses one-based coordinates',
  'inputs':[record(script),record(proof)],
  'bounds':{'diagonal_subsets':'all subsets for N=1..8','all_colorings':[[2,1],[2,2],[3,2],[4,2],[3,3]],'general_recurrence_k':[1,8],'R4_N':91**4,'timeout_seconds':30},
  'non_claims':['Bounded color enumeration is not a universal proof.','No unconditional tower-height reduction is asserted.','No global novelty claim is asserted.']},
 'randomness':{'used':False,'generator':'none','seed':None},
 'run':{'started_at':started,'runtime_seconds':runtime,'exit_status':completed.returncode},
 'outputs':[record(output)],
 'checks':['510 diagonal subsets; 1579 nested pair completions','All listed colorings exhaustively enumerated','Integer recurrence formula checked independently against rational recurrence','R4 certificate evaluated by exact Fraction arithmetic','Every rational coefficient comparison checked by squaring positive sides'],
 'result':data['status'],
 'residual_risks':['Version 1 manifest has no machine-enforced memory cap; the wrapper enforces a 30-second wall timeout.','No git revision exists in the supplied CP0 provenance; input and output content hashes are recorded.','Universal theorem validity still requires the written proof audit.']}
dest=root/'research_20260909/checks/general_k_manifest.json'
dest.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest':str(dest),'runtime_seconds':runtime,'status':data['status']},indent=2))
