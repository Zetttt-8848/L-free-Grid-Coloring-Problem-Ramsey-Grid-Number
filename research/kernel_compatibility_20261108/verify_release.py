"""Fresh exact checks in a temporary copy; preserve published run records."""
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
ASSET = Path('.agents/skills/directed-l-grid-research/assets/paper20.json')


def main():
    files = [p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts
             and p.name != 'release_validation.json'] + [ROOT/ASSET]
    before = {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(files)}
    records = []
    with tempfile.TemporaryDirectory(prefix='lgrid-counting-check-') as tmp:
        dest = Path(tmp)
        shutil.copytree(HERE, dest/REL, ignore=shutil.ignore_patterns('__pycache__'))
        (dest/ASSET).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT/ASSET, dest/ASSET)
        for name in ('kernel_upper/certificate.py', 'geometry/audit_464.py',
                     'geometry/verify_geometry.py', 'combinatorial_upper/verify.py',
                     'review/independent_counting_check.py'):
            script = (REL/name).as_posix()
            tick = time.monotonic()
            done = subprocess.run([sys.executable, script], cwd=dest, capture_output=True,
                                  text=True, timeout=60)
            records.append({'command':['python',script], 'exit_code':done.returncode,
                            'elapsed_seconds':time.monotonic()-tick,
                            'stdout':done.stdout, 'stderr':done.stderr})
            if done.returncode:
                raise RuntimeError(f'Check failed: {name}: {done.stderr}')
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h for p,h in before.items())
    result = {'status':'PASS', 'python':platform.python_version(), 'checks':records,
              'source_inventory_sha256':before,
              'scope':'Exact arithmetic, geometry, and local diagnostics; discovery scouts and external OGR searches not rerun. Originals unchanged.'}
    (HERE/'release_validation.json').write_text(json.dumps(result,indent=2)+'\n',
                                               encoding='utf-8',newline='\n')
    print(json.dumps({'status':'PASS','checks':len(records),'source_files':len(before)}))


if __name__ == '__main__':
    main()
