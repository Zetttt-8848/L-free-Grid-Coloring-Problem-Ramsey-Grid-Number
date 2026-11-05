"""Reproduce root-author finite checks and seal their exact artifact hashes."""
from pathlib import Path
import subprocess,sys,time,json,hashlib,platform
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
commands=[
 'research_round3/cap/ap5_exact_checks.py',
 'research_round3/cap/endpoint_audit.py',
 'research_round3/cap/verify_pair_forcing.py',
 'research_round3/overlap/exact_overlap.py',
 'research_round3/general/exact_scalars.py',
 'research_round3/audits/verify_joint_root.py',
]
records=[]
for name in commands:
    r=subprocess.run([sys.executable,name],cwd=ROOT,capture_output=True,text=True)
    records.append({'script':name,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode:raise RuntimeError(json.dumps(records[-1]))
elapsed=time.perf_counter()-tick
audit=ROOT/'research_round3/audits'
(audit/'root_check_outputs.json').write_text(json.dumps(records,indent=2)+'\n')
files=commands+[
 'research_round3/cap/ap5_exact_results.json','research_round3/cap/endpoint_exact.json',
 'research_round3/cap/pair_forcing_certificate.json','research_round3/cap/pair_forcing_checked.json',
 'research_round3/cap/conditional_descent.json','research_round3/overlap/exact_overlap.json',
 'research_round3/general/scalar_reproduction.json','research_round3/audits/joint_root_verified.json',
 'research_round3/general/refined_constants_proof.md','research_round3/general/refined_minus_one.md',
 'research_round3/general/square_root_barrier.md','research_round3/cap/ap5_uniqueness.md',
 'research_round3/cap/endpoint_neighbor.md','research_round3/overlap/ordered_overlap.md',
 'research_round3/audits/root_check_outputs.json'
]
outputs=[{'path':f,'sha256':hashlib.sha256((ROOT/f).read_bytes()).hexdigest()} for f in files]
manifest={'schema_version':1,'claim_id':'R3-root-author-core-finite-checks','repository':{'commit':'not a Git repository; pinned BASE.json','dirty':True},'command':'python research_round3/audits/root_checks.py','environment':{'software':[f'Python {platform.python_version()}'],'hardware':platform.platform()},'mathematics':{'assertion_tested':'Finite arithmetic, enumeration and literal forcing/witness checks supporting separately written AP5, endpoint, overlap and general-k claims','coefficient_domain':'integers, rational fractions and Boolean values','conventions':'positive-step fixed-orientation corners; H table counts positions; Python zero-based arrays mapped explicitly','inputs':[{'path':'research_round3/BASE.json','sha256':hashlib.sha256((ROOT/'research_round3/BASE.json').read_bytes()).hexdigest()}],'bounds':{'weak_triangles_max_order':5,'endpoint_mark_universe_max_n':10,'overlap_source_n':[1,7],'ruler_pair_cases':60,'general_scalar_k':[6,12]},'non_claims':['No R3 improvement','No n21 decision','No universal theorem from a finite scan','No all-ruler impossibility','No global coefficient optimum']},'randomness':{'used':False,'generator':'none','seed':None},'run':{'started_at':start,'runtime_seconds':elapsed,'exit_status':0},'outputs':outputs,'checks':['All six commands completed with exit0','Independent literal bitset reconstruction for base155-set','Geometry-only forcing trace checker imports no solver','Direct identity and overlap exhaustive tests','Exact Fraction comparisons'],'result':'Finite checks PASS; final author-independent agent reviews pending','residual_risks':['Version1 reproduction provenance; universal claims require written reductions and independent reviews','Conditionally assumed45/46 caps are not proved']}
(audit/'root_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'PASS','commands':len(commands),'manifest_files':len(outputs),'runtime_seconds_telemetry':str(elapsed)},indent=2))
