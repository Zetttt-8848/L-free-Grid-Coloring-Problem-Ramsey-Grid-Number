"""Build and round-trip verify the explicit research checkpoint archive."""
from pathlib import Path
from hashlib import sha256
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
report = json.loads((ROOT / 'audits/FINAL_REPORT_RELEASE.json').read_text())
preflight = json.loads((ROOT / 'audits/PDF_PREFLIGHT.json').read_text())
assert report['status'] == preflight['mechanical_status'] == 'PASS'
assert sha256((ROOT / 'round2_report.tex').read_bytes()).hexdigest() == report['final_report_sha256']
assert sha256((ROOT / 'round2_report.pdf').read_bytes()).hexdigest() == preflight['pdf_sha256']
assert preflight['pdf_sha256'] in (ROOT / 'audits/PDF_VISUAL_REVIEW.md').read_text()
assert json.loads((ROOT / 'checks/core_verified.json').read_text())['status'] == 'PASS'

excluded_names = {'RELEASE_MANIFEST.json', 'PACKAGE_VERIFIED.json'}
def include(path):
    rel = path.relative_to(PROJECT)
    if any(part in {'__pycache__', '.git', 'package_smoke'} for part in rel.parts):
        return False
    if path.name in excluded_names or path.suffix in {'.aux', '.out', '.toc', '.pyc'}:
        return False
    if path.name.startswith(('final_page-', 'review_page-')) and path.suffix == '.png':
        return False
    if path.suffix == '.png' and 'qa' in rel.parts:
        return False
    if path.name == 'contact_draft.png':
        return False
    return True

files = []
for folder in ('research_round2', 'research_20260909'):
    files.extend(path for path in (PROJECT / folder).rglob('*') if path.is_file() and include(path))
for name in ('2312.01159v1.pdf', '2502.05162v1.pdf', 'graham_solymosi_RkL_upper_bound_reconstruction.pdf'):
    files.append(PROJECT / name)
files.sort(key=lambda path: path.relative_to(PROJECT).as_posix())
payloads = {path.relative_to(PROJECT).as_posix(): path.read_bytes() for path in files}
assert len(payloads) == len(files)
for name in payloads:
    assert not name.startswith('/') and '..' not in Path(name).parts
manifest = {
    'checkpoint': 'Round2 verified research checkpoint; exact R3 unresolved',
    'R3_interval': [21,465], 'R4_upper_bound': 22006246,
    'general_upper_bound': 'k^(2^k), every integer k>=3',
    'review_status': 'All assigned bundles PASS; see independently authored audit files',
    'pdf_pages': preflight['pages'], 'pdf_sha256': preflight['pdf_sha256'],
    'manifest_self_excluded': True,
    'files': [{'path': name, 'bytes': len(data), 'sha256': sha256(data).hexdigest()} for name,data in payloads.items()],
}
manifest_bytes = (json.dumps(manifest,indent=2)+'\n').encode()
(ROOT / 'RELEASE_MANIFEST.json').write_bytes(manifest_bytes)
payloads['research_round2/RELEASE_MANIFEST.json'] = manifest_bytes
archive = PROJECT / 'research_round2_package.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for name,data in payloads.items():
        entry = zipfile.ZipInfo(name, date_time=(2026,9,9,0,0,0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        z.writestr(entry,data)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == set(payloads)
    for entry in manifest['files']:
        data = z.read(entry['path'])
        assert len(data) == entry['bytes'] and sha256(data).hexdigest() == entry['sha256']
    assert z.read('research_round2/RELEASE_MANIFEST.json') == manifest_bytes
result = {'status': 'PASS', 'archive': archive.name, 'bytes': archive.stat().st_size,
          'sha256': sha256(archive.read_bytes()).hexdigest(),
          'entries': len(payloads), 'hashed_file_entries': len(manifest['files']),
          'zip_crc': 'PASS', 'all_manifest_hashes_after_compression': 'PASS'}
(ROOT / 'PACKAGE_VERIFIED.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
