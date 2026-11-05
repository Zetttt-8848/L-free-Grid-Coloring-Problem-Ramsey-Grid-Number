"""Check the literal hashes frozen by independent reviewers; no proof rerun."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
R3 = ROOT / 'research_round3'
AUD = R3 / 'audits'
records = []

def check(base, path, expected):
    p = base / path
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    assert actual == expected, (str(p), expected, actual)
    records.append({'path': p.relative_to(ROOT).as_posix(), 'sha256': actual})

fresh = AUD / 'fresh_astra'
seal = json.loads((fresh / 'seal.json').read_text())
assert seal['verdict'] == 'PASS' and seal['source_hashes_unchanged']
assert not seal['issues']['major'] and not seal['issues']['minor']
for p, h in seal['reviewer_artifact_sha256'].items():
    check(fresh, p, h)
addendum = json.loads((fresh / 'addendum_seal.json').read_text())
assert addendum['verdict'] == 'PASS' and addendum['no_new_proof_premise']
assert not addendum['issues']['major'] and not addendum['issues']['minor']
check(fresh, 'seal.json', addendum['original_seal_sha256'])
check(fresh, 'ADDENDUM.md', addendum['addendum_sha256'])
for p, h in json.loads((fresh / 'reviewed_sources.json').read_text()).items():
    if p in addendum['new_manuscript_sha256']:
        assert h == addendum['old_manuscript_sha256'][p]
        check(ROOT, p, addendum['new_manuscript_sha256'][p])
    else:
        check(ROOT, p, h)

joint = AUD / 'joint_astra'
for row in json.loads((joint / 'manifest.json').read_text())['files']:
    check(joint, row['path'], row['sha256'])
for p in sorted(joint.glob('*_provenance.json')):
    data = json.loads(p.read_text())
    for name, h in data['input_sha256'].items():
        check(R3, name, h)
    check(joint, 'independent_audit.py', data['script_sha256'])

lower = json.loads((AUD / 'lower_sol/manifest.json').read_text())
for key in ['principal_input_sha256', 'review_file_sha256']:
    for p, h in lower[key].items():
        check(R3, p, h)
tree = hashlib.sha256()
window = R3 / 'joint/window13'
window_files = sorted(p for p in window.rglob('*') if p.is_file())
for p in window_files:
    tree.update(p.relative_to(window).as_posix().encode())
    tree.update(b'\0')
    tree.update(hashlib.sha256(p.read_bytes()).digest())
assert len(window_files) == lower['window13_external_files']['count']
assert tree.hexdigest() == lower['window13_external_files']['tree_sha256']

setup_path = AUD / 'setup_sol/computation_manifest.json'
if setup_path.exists():
    setup = json.loads(setup_path.read_text())
    for row in setup['mathematics']['inputs'] + setup['outputs']:
        check(ROOT, row['path'], row['sha256'])

out = {'status': 'PASS', 'scope': 'reviewer frozen hashes with explicit fresh_astra manuscript addendum',
       'checked_hash_records': len(records), 'files': records}
(AUD / 'review_provenance_check.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checked_hash_records': len(records)}))
