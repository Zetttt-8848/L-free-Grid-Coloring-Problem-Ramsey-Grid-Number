"""Recheck publication evidence in a temporary copy without rewriting records."""
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REL = HERE.relative_to(ROOT)


def main():
    commands = [
        'numeric_upper/verify.py', 'lower/verify.py', 'lower/verify_defect.py',
        'structural/check_branch_proof.py', 'structural/verify_extension.py',
        'structural/audit_joint_bound.py', 'structural/audit_convolution.py',
        'spectral/verify.py',
    ]
    inputs = {}
    for folder in (HERE, ROOT/'research/boundary_extension_20261108/lower'):
        for path in sorted(folder.rglob('*')):
            if not path.is_file() or any(p in path.parts for p in ('__pycache__', '_scratch')):
                continue
            if path.name == 'checkpoint_validation.json':
                continue
            inputs[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    records = []
    with tempfile.TemporaryDirectory(prefix='lgrid-proof-check-') as tmp:
        dest = Path(tmp)
        for folder in (HERE, ROOT/'research/boundary_extension_20261108/lower'):
            shutil.copytree(folder, dest/folder.relative_to(ROOT), ignore=shutil.ignore_patterns('__pycache__', '_scratch'))
        for name in commands:
            script = (REL/name).as_posix()
            start = time.monotonic()
            done = subprocess.run([sys.executable, script], cwd=dest, capture_output=True, text=True, timeout=60)
            records.append({'command':['python', script], 'exit_code':done.returncode,
                            'elapsed_seconds':time.monotonic()-start,
                            'stdout':done.stdout, 'stderr':done.stderr})
            if done.returncode:
                raise RuntimeError(f'{name} failed: {done.stderr}')
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h for p, h in inputs.items())
    result = {'status':'PASS', 'python':platform.python_version(), 'checks':records,
              'source_inventory_sha256':inputs,
              'scope':'Fresh checks in temporary copies; originals unchanged. External OGR searches and Lean not rerun.'}
    (HERE/'checkpoint_validation.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({'status':'PASS', 'checks':len(records), 'source_files':len(inputs)}))


if __name__ == '__main__':
    main()
