"""Build and exactly hash-check the reviewed checkpoint with its inherited files."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib,json
ROOT=Path(__file__).resolve().parent.parent
R3=ROOT/'research_round3'
matrix=json.loads((R3/'audits/final_review_matrix.json').read_text())
assert matrix['release_status']=='PASS' and not matrix['unresolved_issues']
for name,entries in matrix['cores'].items():
    assert len(entries)>=2 and all(e['verdict']=='PASS' for e in entries)
    assert len({e['reviewer'] for e in entries})==len(entries)
    assert any('astra' in e['reviewer'] for e in entries)
    for e in entries:
        for f in e['evidence']:
            p=ROOT/f['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
files={}
with ZipFile(ROOT/'research_round2_package.zip') as prior:
    for entry in prior.infolist():
        if entry.is_dir():continue
        rel=Path(entry.filename)
        assert not rel.is_absolute() and '..' not in rel.parts
        files[entry.filename]=prior.read(entry)
for p in sorted(R3.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if '__pycache__' in p.parts or 'preview' in p.parts or 'package_smoke' in p.parts:continue
    if p.suffix in ['.aux','.out','.pyc']:continue
    if p.name in ['RELEASE_MANIFEST.json','RELEASE_CHECK.json']:continue
    files[rel]=p.read_bytes()
manifest={'schema':'round3-reviewed-release-v1','status':'PASS','scientific_scope':'certified research checkpoint; R3 remains21..465; n21 and global exhaustion not decided','file_count':len(files),'files':[{'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()} for p,b in sorted(files.items())]}
raw=(json.dumps(manifest,indent=2)+'\n').encode()
(R3/'RELEASE_MANIFEST.json').write_bytes(raw)
files['research_round3/RELEASE_MANIFEST.json']=raw
target=ROOT/'research_round3_package.zip'
with ZipFile(target,'w',compression=ZIP_DEFLATED,compresslevel=9) as out:
    for path,data in sorted(files.items()):out.writestr(path,data)
with ZipFile(target) as check:
    assert check.testzip() is None and set(check.namelist())==set(files)
    for f in manifest['files']:
        b=check.read(f['path']);assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256']
result={'status':'PASS','archive':str(target),'archive_bytes':target.stat().st_size,'archive_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'manifest_files':len(manifest['files']),'archive_entries':len(files),'crc_and_every_file_hash_verified':True}
(R3/'RELEASE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
