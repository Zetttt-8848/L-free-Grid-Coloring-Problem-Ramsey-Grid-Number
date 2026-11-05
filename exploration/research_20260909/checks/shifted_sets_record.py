"""Record a bounded exact-certificate run and its reproducible artifacts."""
import datetime
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
CHECK=ROOT/'research_20260909/checks/shifted_sets_certificate.py'
OUTPUT=CHECK.with_name('shifted_sets_certificate_output.json')
MANIFEST=CHECK.with_name('shifted_sets_manifest.json')
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
t0=time.perf_counter()
run=subprocess.run([sys.executable,str(CHECK)],cwd=ROOT,text=True,capture_output=True,timeout=30)
elapsed=time.perf_counter()-t0
if run.returncode:
    raise RuntimeError(run.stderr)
OUTPUT.write_text(run.stdout,encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest={
 'schema_version':1,
 'claim_id':'weighted-three-color-diagonal-R3-at-most-465',
 'repository':{'commit':'not a Git repository','dirty':True},
 'command':f'python research_20260909/checks/{CHECK.name}',
 'environment':{'software':[sys.version, 'Python standard library only'],
                'hardware':f'{platform.platform()}; {platform.machine()}; {platform.processor()}'},
 'mathematics':{
  'assertion_tested':'The explicit tent-weight certificate at n=465 has positive exact contradiction margin 285630; the geometric incidences and moment identities pass all stated bounded enumerations.',
  'coefficient_domain':'Arbitrary-precision integers',
  'conventions':'Rows increase downwards; columns rightwards; corner ((x,y),(x+d,y),(x+d,y+d)); positive d; Golomb length=max-min; ternary colors 0,1,2.',
  'inputs':['G(24)>=425 and G(25)>=480, copied from supplied 2502.05162v1.pdf Algorithm 3, PDF page 12',
            'w_i=min(i,94-i), 1<=i<=93',f'certificate_sha256={digest(CHECK)}'],
  'bounds':{'n':465,'weight_count':93,'fiber_geometry_n_min':2,'fiber_geometry_n_max':10,
            'word_n_min':1,'word_n_max':7,'wall_timeout_seconds':30},
  'non_claims':['The code does not prove the external optimal-Golomb lower bounds.',
                'Finite small-case tests alone do not imply the universal forcing lemma or weighted inequality.',
                'No claim of global novelty or optimality of the constant 465.']},
 'randomness':{'used':False,'generator':'none','seed':None},
 'run':{'started_at':started,'runtime_seconds':elapsed,'exit_status':run.returncode},
 'outputs':[{'path':str(OUTPUT.relative_to(ROOT)).replace('\\','/'),'sha256':digest(OUTPUT)},
            {'path':str(CHECK.relative_to(ROOT)).replace('\\','/'),'sha256':digest(CHECK)}],
 'checks':['Direct finite autocorrelation sums equal the displayed closed forms.',
           'All 4643 repeated-difference witnesses in the declared range satisfy the seven corner incidences.',
           'All 3279 ternary words of lengths 1..7 satisfy both weighted moment identities.',
           'Exact contradiction arithmetic gives 1064933097 > 1064647467.'],
 'result':'implementation and finite assertion verified in the stated range',
 'residual_risks':['The two supplied Golomb lower bounds are accepted external mathematical inputs.',
                   'The accompanying universal proof requires independent mathematical review.']}
MANIFEST.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(f'Wrote {MANIFEST.relative_to(ROOT)}; exact-certificate runtime {elapsed:.6f}s')
