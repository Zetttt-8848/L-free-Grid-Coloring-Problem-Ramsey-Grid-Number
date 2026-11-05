"""Re-run final independent check with a durable computation manifest."""
from pathlib import Path
import hashlib,json,platform,subprocess,sys,time
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[2]

def main():
    started=datetime.now(timezone.utc).isoformat()
    tick=time.perf_counter()
    cmd=[sys.executable,'research_round2/checks/four_multi_verify.py']
    run=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    elapsed=time.perf_counter()-tick
    print(run.stdout,end='')
    assert run.returncode==0,run.stderr
    paths=['research_round2/certificates/four_multi_final.json',
           'research_round2/certificates/four_multi_verification.json',
           'research_round2/certificates/four_multi_overlap.json']
    record=dict(schema_version=1,claim_id='R2-FM8',
      repository=dict(commit='No Git repository; durable base R2-CP0 in research_round2/BASE.json',dirty=True),
      command='python research_round2/checks/four_multi_verify.py',
      environment=dict(software=[sys.version,platform.platform()],hardware=platform.machine()),
      mathematics=dict(assertion_tested='First-forbidden Golomb and three-color capacities in every run; exact four-color weighted contradiction; literal finite counterexamples',
        coefficient_domain='Unbounded Python integers',
        conventions='C(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}, positive integer d',
        inputs=['research_round2/certificates/four_multi_final.json','research_round2/certificates/four_multi_overlap.json'],
        bounds=dict(n=22007053,t=28443,runs=300,naive_grid_n=4,overlap_region_marks=[1,4,8,14,18,21]),
        non_claims=['No global weight/cap optimality','No new lower bound','Finite verifier supplements rather than replaces the universal FM1--FM8 proof']),
      randomness=dict(used=False,generator='none',seed=None),
      run=dict(started_at=started,runtime_seconds=elapsed,exit_status=run.returncode),
      outputs=[dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()) for p in paths],
      checks=['Complete run coverage of distances','First-forbidden inequalities at maximum span per run','Run-polynomial weighted sum independent of generator','All literal counterexample corners and region closure'],
      result='PASS: R4 certificate doubled margin 84929137',
      residual_risks=['Independent agent proof review pending','Version 1 manifest gives no before/after input mutation guard'])
    (ROOT/'research_round2/certificates/four_multi_manifest.json').write_text(json.dumps(record,indent=2)+'\n')

if __name__=='__main__':main()
