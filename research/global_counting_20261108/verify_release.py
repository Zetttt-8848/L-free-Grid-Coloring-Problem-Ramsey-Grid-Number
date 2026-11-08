"""Replay exact checks in a temporary copy; keep original evidence unchanged."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REL=HERE.relative_to(ROOT)
OUTPUTS={'release_validation.json','release_manifest.json'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    started=datetime.now(timezone.utc).isoformat()
    start=time.monotonic()
    deps=[Path('manuscript')/p for p in ('main.tex','references.bib','verify_directed_L_manuscript.py')]
    navigation=[Path(p) for p in ('.gitattributes','README.md','docs/ROADMAP.md',
                'docs/RESULTS_INDEX.md','docs/OPEN_PROBLEMS.md',
                '.agents/skills/directed-l-grid-research/references/repository-map.md',
                'research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md')]
    files=[p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts
           and p.name not in OUTPUTS]+[ROOT/p for p in deps+navigation]
    before={p.relative_to(ROOT).as_posix():sha(p) for p in sorted(files)}
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    dirty=bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip())
    records=[]
    with tempfile.TemporaryDirectory(prefix='lgrid-global-check-') as tmp:
        dest=Path(tmp)
        shutil.copytree(HERE,dest/REL,ignore=shutil.ignore_patterns('__pycache__'))
        for p in deps:
            (dest/p).parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/p,dest/p)
        commands=[['python','-B',(REL/p).as_posix()] for p in
                  ('information_gap.py','multilayer/verify.py','completion/verify.py',
                   'multiscale/verify.py','review/independent_check.py','review/supplemental_check.py')]
        commands.append(['python','-B','manuscript/verify_directed_L_manuscript.py',
                         '--source','manuscript/main.tex','--bib','manuscript/references.bib',
                         '--output',(REL/'main_regression.json').as_posix()])
        for cmd in commands:
            tick=time.monotonic()
            result=subprocess.run([sys.executable]+cmd[1:],cwd=dest,capture_output=True,
                                  text=True,timeout=60)
            records.append({'command':cmd,'exit_code':result.returncode,
                            'elapsed_seconds':time.monotonic()-tick,
                            'stdout':result.stdout,'stderr':result.stderr})
            if result.returncode:
                raise RuntimeError('Exact check failed: '+cmd[2]+'\n'+result.stderr)
    after={p:sha(ROOT/p) for p in before}
    if before!=after:
        raise RuntimeError('Original input changed during verification')
    release={'status':'PASS','python':platform.python_version(),'checks':records,
             'source_inventory_sha256':before,
             'scope':'Fresh exact reconstructions and 13 main-manuscript finite regression groups; original reports preserved. Scouts and OGR exhaustive searches not rerun.'}
    (HERE/'release_validation.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8',newline='\n')
    risks=['No new Ramsey bound below464 is established.',
           'Finite checks supplement the displayed universal proofs.',
           'External OGR uniqueness and span searches were not replayed.',
           'No new Lean compilation or formalization. Floating scouts are not proof inputs.']
    manifest={'schema_version':2,'claim_id':'global_counting_checkpoint_exact_checks',
      'repository':{'commit':commit,'dirty':dirty},
      'command':['python',(REL/'verify_release.py').as_posix()],
      'environment':{'software':[{'name':'CPython','version':platform.python_version()}],
                     'hardware':platform.machine()+'; '+platform.platform(),
                     'note':'Observed interpreter version recorded; absolute host path omitted.'},
      'mathematics':{'assertion_tested':'Exact reconstruction of endpoint, source-conflict, rigidity and occurrence-budget claims in the stated finite audit domains.',
                    'coefficient_domain':'Z and Q, exact integers',
                    'conventions':'zero-based coordinates; positive directed equal-leg L; Golomb length is span',
                    'inputs':['all binary sources on subsets of0..5','all ternary words lengths1..8',
                              'explicit n10 partial coloring','published24-mark ruler','n463,464 integer weights'],
                    'bounds':{'source_ambient_max':6,'word_length_max':8,'Golomb_capacity_audit_positions_max':14,
                              'rigidity_positions_max':480,'main_finite_groups':13},
                    'non_claims':risks},
      'randomness':{'used':False,'generator':'none','seed':None},
      'run':{'started_at':started,'runtime_seconds':time.monotonic()-start,
             'exit_status':0,'status':'completed',
             'resource_limits':{'memory_bytes':None,'cpu_seconds':None,'max_cores':None,'max_threads':None},
             'note':'Each subprocess has a60second wall limit; no aggregate memory or CPU cap requested.'},
      'outputs':[{'path':(REL/'release_validation.json').as_posix(),
                  'sha256':sha(HERE/'release_validation.json'),'kind':'result'}],
      'checks':['All seven exact-check commands exit0','Before/after hashes of original inputs identical',
                'Independent proof reviewer and independent physical-triple reconstructions pass'],
      'result':'PASS within stated finite audit domains; mathematical research target remains open.',
      'residual_risks':risks,
      'input_artifacts':[{'path':p,'sha256':h,'sha256_after':after[p]} for p,h in before.items()],
      'declared_results':[(REL/'release_validation.json').as_posix()]}
    (HERE/'release_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'PASS','checks':len(records),'input_files':len(before)}))

if __name__=='__main__':main()
