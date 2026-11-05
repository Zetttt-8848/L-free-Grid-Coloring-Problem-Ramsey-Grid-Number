"""Run the coordinator's two bounded exact checks and capture provenance."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json, platform, subprocess, sys, time

root=Path(__file__).resolve().parents[2]
check=Path(__file__).resolve().parent
scripts=[check/'verify_primary.py',check/'verify_relaxations.py']
hashfile=lambda p:sha256(p.read_bytes()).hexdigest()
inputs=[{'path':str(p.relative_to(root)).replace('\\','/'),'sha256':hashfile(p)} for p in scripts]
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
for p in scripts:
    result=subprocess.run([sys.executable,str(p)],cwd=root,timeout=30,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stdout+result.stderr)
assert all(hashfile(root/item['path'])==item['sha256'] for item in inputs)
outputs=[check/'primary_result.json',check/'relaxations_result.json']
manifest={
 'schema_version':1,'claim_id':'CP1-R3-weighted465-and-route-benchmarks',
 'repository':{'commit':'unavailable: CP0 source hashes, workspace is not a Git repository','dirty':True},
 'command':[sys.executable,str(Path(__file__).resolve())],
 'environment':{'software':[f'Python {platform.python_version()}',platform.platform()],
                'hardware':platform.machine()+'; '+platform.processor()},
 'mathematics':{'assertion_tested':'465 integer certificate, independent convolution expansion, small-word and triangle enumeration, 490/466 arithmetic, bounded reconstruction of493.',
   'coefficient_domain':'arbitrary-precision integers',
   'conventions':'fixed positive-step corner; scripts explicitly document zero-based enumeration and one-based weights',
   'inputs':inputs,
   'bounds':{'word_lengths':[1,7],'word_colors':3,'profiles_per_word':4,'triangle_mark_counts':[2,6],
             'benchmark_n':[100,493],'benchmark_c':'1..min(49,ceil(n/3)-1)','wall_timeout_per_script_seconds':30},
   'non_claims':['Golomb optimality is accepted from supplied sources, not recomputed.','No global novelty or optimality of465 is certified.','Finite checks do not substitute for the written universal proof.']},
 'randomness':{'used':False,'generator':'none','seed':None},
 'run':{'started_at':started,'runtime_seconds':time.perf_counter()-tick,'exit_status':0},
 'outputs':[{'path':str(p.relative_to(root)).replace('\\','/'),'sha256':hashfile(p)} for p in outputs],
 'checks':['All exact assertions passed.','Input hashes unchanged across both subprocesses.','Each subprocess exited zero within its 30-second timeout.'],
 'result':'Verified exact score285630, energy gap190420, unweighted gap442, independent structural gap48, and benchmark first493 in stated scan.',
 'residual_risks':['Version1 manifest has no operating-system memory cap.','Universal validity depends on the report proof and the two accepted Golomb bounds.']}
(check/'primary_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Recorded successful bounded exact runs:',manifest['run'])
