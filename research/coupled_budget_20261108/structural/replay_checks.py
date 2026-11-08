"""Run the declared finite checks and snapshot their result files for provenance."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time


def main():
    here = Path(__file__).parent.resolve()
    destination = (here/sys.argv[1]).resolve()
    if not destination.is_relative_to(here):
        raise ValueError('Results must stay inside this experiment directory')
    destination.mkdir(parents=True, exist_ok=True)
    tasks = [
        ('enumerate_frustration.py', ['frustration_results.json']),
        ('certify_balance.py', ['balance_certificate.json', 'balance_branch_proof.json']),
        ('check_branch_proof.py', ['balance_proof_check.json']),
        ('verify_extension.py', ['extension_verification.json']),
        ('audit_joint_bound.py', ['joint_bound_audit.json']),
        ('audit_convolution.py', ['convolution_audit.json'])
    ]
    records = []
    for script, outputs in tasks:
        started = time.monotonic()
        run = subprocess.run([sys.executable, str(here/script)], cwd=here,
                             capture_output=True, text=True, timeout=40, check=True)
        for output in outputs:
            shutil.copyfile(here/output, destination/output)
        records.append({'script': script, 'exit_code': run.returncode,
                        'elapsed_seconds': time.monotonic()-started, 'outputs': outputs})
    result = {'status': 'PASS', 'checks': records,
              'scope': 'Exact source classifications, certificate check, full extension witness, and finite bound arithmetic. External Golomb exclusions are cited inputs, not locally replayed.'}
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
