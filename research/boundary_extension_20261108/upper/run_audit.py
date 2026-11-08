"""Run the independent verifier and write a v2 computation manifest."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[3]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return p.relative_to(ROOT).as_posix()

def main():
    inputs=[HERE/'verify.py',HERE/'witnesses.json']
    hashes=[sha(p) for p in inputs]
    started=datetime.now(timezone.utc).isoformat(); tick=time.monotonic()
    command=[sys.executable,rel(HERE/'verify.py')]
    process=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=30)
    elapsed=time.monotonic()-tick
    output=HERE/'verification.json'
    log=HERE/'verification_stdout.txt'; log.write_text(process.stdout+process.stderr,encoding='utf-8')
    result=json.loads(output.read_text(encoding='utf-8'))
    manifest={
      'schema_version':2,'claim_id':'U-field-20261108',
      'repository':{'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'dirty':bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip())},
      'command':['python',rel(HERE/'verify.py')],
      'command_note':'Executed with the running Python interpreter; its absolute executable path is omitted for portability and privacy. The actual Python version is recorded below.',
      'environment':{'software':[{'name':'Python','version':platform.python_version()}],
        'hardware':platform.machine()+' '+platform.processor()},
      'mathematics':{'assertion_tested':result['assertion_tested'],
        'coefficient_domain':'integers','conventions':'Full strict source; directed equal-leg L with positive step; signs 1-2c.',
        'inputs':[rel(p) for p in inputs],
        'bounds':{'marks':10,'cells':45,'corners':46,'colorings':2},
        'non_claims':['No R3 bound improvement.','No exhaustive enumeration of all colorings.','No global novelty claim.']},
      'randomness':{'used':False,'generator':'none','seed':None},
      'run':{'started_at':started,'runtime_seconds':elapsed,'exit_status':process.returncode,
        'status':'completed' if process.returncode==0 and result['status']=='PASS' else 'failed',
        'resource_limits':{'memory_bytes':None,'cpu_seconds':None,'wall_seconds':30,'max_cores':None,'max_threads':None}},
      'outputs':[{'path':rel(p),'sha256':sha(p),'kind':kind} for p,kind in [(output,'result'),(log,'log')]],
      'checks':['Independent unordered-triple geometry','All colors and all L constraints','Parity and field bounds attain equality'],
      'result':'Two proper source colorings certify exact minima 9 and 13, with local potential 8 to 4.',
      'residual_risks':['Python runtime trusted; no formal proof checker used.'],
      'input_artifacts':[{'path':rel(p),'sha256':h,'sha256_after':sha(p)} for p,h in zip(inputs,hashes)],
      'declared_results':[rel(output)]}
    (HERE/'computation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(process.stdout)

if __name__=='__main__': main()
