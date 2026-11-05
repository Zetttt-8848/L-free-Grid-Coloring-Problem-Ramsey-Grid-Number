"""Provenance wrapper for the fresh reviewer programs, not a research producer."""
import datetime
import hashlib
import json
import pathlib
import platform
import subprocess
import sys
import time

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SKILL=pathlib.Path('C:/Users/ZhuanZ/.codex/skills/exact-verify/scripts/self_test.py')

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    clock=time.perf_counter()
    inputs={}
    for result in ['G_results.json','J_results.json','F_results.json']:
        p=HERE/result
        if p.exists():
            for rel,sha in json.loads(p.read_text())['input_sha256'].items():
                inputs[rel]=digest(ROOT/rel)
    logs=[]
    for script in [SKILL,HERE/'audit_g.py',HERE/'audit_j.py',HERE/'audit_f.py']:
        runstart=datetime.datetime.now(datetime.timezone.utc).isoformat()
        tick=time.perf_counter()
        command=[sys.executable,str(script)]
        proc=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
        log=HERE/(script.stem+'.log')
        log.write_text(proc.stdout+proc.stderr)
        logs.append(dict(argv=command,started_at=runstart,runtime_seconds=time.perf_counter()-tick,
                         returncode=proc.returncode,log=str(log.relative_to(ROOT)).replace('\\','/')))
        assert proc.returncode==0,(script,proc.stdout,proc.stderr)
        if script==SKILL:
            assert 'ENVIRONMENT OK' in proc.stdout
        print(script.name,'PASS',flush=True)
    for result in ['G_results.json','J_results.json','F_results.json']:
        obj=json.loads((HERE/result).read_text())
        for rel,sha in obj['input_sha256'].items():
            assert digest(ROOT/rel)==sha
            if rel in inputs:
                assert sha==inputs[rel]
            inputs[rel]=sha
    git=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True)
    commit=git.stdout.strip() if git.returncode==0 else 'unversioned workspace; git rev-parse HEAD returned no repository'
    all_outputs=['G_results.json','J_results.json','F_results.json','F_exact_arrays.json',
                 'self_test.log','audit_g.log','audit_j.log','audit_f.log']
    manifest=dict(schema_version=1,claim_id='R3-FRESH-ASTRA-G-J-F-INDEPENDENT-AUDIT',
                  repository=dict(commit=commit,dirty=True),
                  command=f'{sys.executable} research_round3/audits/fresh_astra/run_review.py',
                  environment=dict(software=[f'Python {platform.python_version()}','SymPy 1.13.3','Python standard-library integer/Boolean arithmetic'],
                                   hardware=platform.platform()+'; '+platform.machine()),
                  mathematics=dict(assertion_tested='Fresh exact checks of G scalars/identities, J finite witnesses/RUP/window coverage and uniform coefficients, F all 561 capacity witnesses and all 35999 score terms',
                                   coefficient_domain='arbitrary-precision integers, exact rational fractions, Boolean bit masks; no verdict-bearing floats',
                                   conventions='corner (x,y),(x+d,y),(x+d,y+d), positive integer d; H table counts positions; Q takes span; all G capacities at fixed N',
                                   inputs=[dict(path=rel,sha256=sha) for rel,sha in sorted(inputs.items())],
                                   bounds=dict(G_k=list(range(5,13)),window_width=13,supports=8192,minimal_bad=109,maximal_good=334,
                                               source_n=464,source_size=155,affine_copies=543170,F_n=21991300,F_t=36000,F_runs=561,F_distances=35999),
                                   non_claims=['G universal theorem is proved separately by the written audit, not inferred from finite k checks.',
                                               'No 464 grid coloring, Ramsey lower-bound improvement or feasibility after the newest hook/AP5 lemma.',
                                               'No all-outer-c optimization or sensitivity-table audit; 561 strict witnesses suffice for the F bound.',
                                               'No author research generator or checker was imported or executed.']),
                  randomness=dict(used=False,generator='none',seed=None),
                  run=dict(started_at=start,runtime_seconds=time.perf_counter()-clock,exit_status=0),
                  outputs=[dict(path=str((HERE/x).relative_to(ROOT)).replace('\\','/'),sha256=digest(HERE/x)) for x in all_outputs],
                  checks=['exact-verify environment self-test passed','independent geometry and bit-mask RUP checks passed',
                          'input hashes unchanged during final evidence run','all three fresh-review programs returned PASS'],
                  result='PASS for the exact finite scope; complete universal proof audit is in REVIEW.md',
                  residual_risks=['Depends on explicitly accepted Round-2 proof leaves.',
                                  'V1 manifest records commands and checksums but is not an OS-level execution attestation.'])
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (HERE/'execution.json').write_text(json.dumps(dict(started_at=start,subprocesses=logs,inputs_before_after_equal=True),indent=2)+'\n')

if __name__=='__main__':
    main()
