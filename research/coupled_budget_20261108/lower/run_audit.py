"""Re-run finite proof checks and record public, portable v2 provenance."""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PRIOR=ROOT/'research/boundary_extension_20261108/lower'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return p.relative_to(ROOT).as_posix()


def main():
    inputs=[Path(__file__),HERE/'verify.py',HERE/'verify_defect.py',HERE/'defect_certified.json',HERE/'cut_catalog.json',
            PRIOR/'verify.py',PRIOR/'paper20.json',PRIOR/'packing_results.json']
    inputs.extend(sorted((HERE/'runs').glob('*.json')))
    before={rel(p):sha(p)for p in inputs}
    started=datetime.now(timezone.utc).isoformat();tick=time.monotonic();logs=[];codes=[]
    for name in ('verify.py','verify_defect.py'):
        done=subprocess.run([sys.executable,rel(HERE/name)],cwd=ROOT,capture_output=True,text=True,timeout=30)
        logs.append(done.stdout+done.stderr);codes.append(done.returncode)
    log=HERE/'audit_stdout.txt';log.write_text('\n'.join(logs),encoding='utf-8',newline='\n')
    results=[HERE/'verification.json',HERE/'defect_verification.json']
    passed=all(code==0 for code in codes) and all(json.loads(p.read_text(encoding='utf-8'))['status']=='PASS'for p in results)
    stable=all(before[rel(p)]==sha(p)for p in inputs)
    manifest={'schema_version':2,'claim_id':'L-CUT-DISCREPANCY-20261108',
      'repository':{'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'dirty':bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip())},
      'command':['python',rel(Path(__file__))],
      'environment':{'software':[{'name':'Python','version':platform.python_version()}],'hardware':platform.platform()},
      'mathematics':{'assertion_tested':'All 22,680 lifted clauses follow from checked seed cores; the complete candidate has one bad L; proof streams exclude repairs at radii1 through10.',
        'coefficient_domain':'Exact integer geometry, finite three-color domains, lossless integer proof stream',
        'conventions':'Full21 square; only positive-step directed equal-leg L; Hamming changes relative to one fixed complete candidate',
        'inputs':[rel(p)for p in inputs],'bounds':{'base_cores':34,'lifted_cuts':22680,'max_radius':10,'radius10_nodes':1235525},
        'non_claims':['No new Ramsey lower bound','No globally impossible21 square','No proof that11 changes suffice','No SAT speedup']},
      'randomness':{'used':False,'generator':'none','seed':None},
      'run':{'started_at':started,'runtime_seconds':time.monotonic()-tick,'exit_status':0 if passed and stable else 1,
        'status':'completed'if passed and stable else'failed',
        'resource_limits':{'wall_seconds':60,'cpu_seconds':None,'memory_bytes':None,'max_cores':None,'max_threads':None}},
      'input_artifacts':[{'path':rel(p),'sha256':before[rel(p)],'sha256_after':sha(p)}for p in inputs],
      'outputs':[{'path':rel(p),'sha256':sha(p),'kind':'log'if p==log else'result'}for p in results+[log]],
      'declared_results':[rel(p)for p in results],
      'checks':['Rechecked prior complete proof trees','Independently reconstructed all geometric lifts',
                'All2,870 candidate corners','Complete discrepancy branch coverage, no discovery or solver imports'],
      'result':'Certified lifted clauses and radius10 barrier; all construction attempts remain undecided.',
      'residual_risks':['Python runtime trusted','Search runs are heuristic or interrupted; only finite certificates are mathematical negative evidence'],
      'portability_note':'Actual interpreter absolute path omitted; actual version recorded.'}
    (HERE/'computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':manifest['run']['status'],'input_files':len(inputs),'checks':codes}))
    if not passed or not stable:raise RuntimeError('Finite audit failed')


if __name__=='__main__':main()
