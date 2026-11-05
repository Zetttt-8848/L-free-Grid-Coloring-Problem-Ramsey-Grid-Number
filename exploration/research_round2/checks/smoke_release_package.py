"""Verify the portable core checker from a fresh, safely bounded extraction."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
archive = ROOT.parent / 'research_round2_package.zip'
dest = (ROOT / 'audits/package_smoke').resolve()
assert dest.parent == (ROOT / 'audits').resolve()
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    manifest = json.loads(z.read('research_round2/RELEASE_MANIFEST.json'))
    expected = {item['path']:item for item in manifest['files']}
    for name in z.namelist():
        target = (dest / name).resolve()
        assert target.is_relative_to(dest) and target != dest
        data = z.read(name)
        if name in expected:
            item = expected[name]
            assert len(data) == item['bytes'] and sha256(data).hexdigest() == item['sha256']
        else:
            assert name == 'research_round2/RELEASE_MANIFEST.json'
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
run = subprocess.run([sys.executable, str(dest / 'research_round2/checks/verify_round2_core.py')],
                     cwd=dest, capture_output=True, text=True, timeout=60)
(ROOT / 'audits/PACKAGE_SMOKE_OUTPUT.txt').write_text(run.stdout+run.stderr)
assert run.returncode == 0, run.stdout+run.stderr
result = json.loads((dest / 'research_round2/checks/core_verified.json').read_text())
assert result['status'] == 'PASS' and result['R4_upper_bound'] == 22006246
record = {'status':'PASS', 'tested_archive_sha256':sha256(archive.read_bytes()).hexdigest(),
          'scope':'Portable finite checker run from an independent extracted copy',
          'core_checker_sha256':sha256((dest/'research_round2/checks/verify_round2_core.py').read_bytes()).hexdigest(),
          'R4_upper_bound':result['R4_upper_bound'], 'exact_R3':'UNRESOLVED',
          'release_note':'Subsequent repackaging may add this smoke record; the tested proof and checker inputs remain unchanged.'}
(ROOT/'audits/PACKAGE_SMOKE.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
