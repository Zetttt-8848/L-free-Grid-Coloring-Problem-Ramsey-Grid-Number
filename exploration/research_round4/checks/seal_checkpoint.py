"""Final read-only evidence validation, followed by a checkpoint hash index."""
from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess, sys

root=Path(__file__).resolve().parents[2]
base=root/'research_round4'
validator=Path('C:/Users/ZhuanZ/.codex/plugins/cache/openai-curated-remote/mathbox/3.0.0/skills/computation-audit/scripts/validate_manifest.py')
manifests=['audits/general/run_gate_0003/manifest.json','audits/certificates/run_gate_0003/manifest.json',
 'audits/geometry/run_gate_0002/manifest.json','audits/lower_and_provenance/run_gate_0002/manifest.json',
 'audits/inherited_obstructions/computation_manifest.json','audits/remaining_details/computation_manifest.json',
 'audits/remaining_details/mammel_theorem2_manifest.json','audits/general_independent/computation_manifest.json',
 'audits/four/computation_manifest.json',
 'audits/golomb_sources/run_witnesses_0001/manifest.json',
 'audits/golomb_sources/run_all_witnesses_0001/manifest.json',
 'audits/golomb_small/root/run_0001/manifest.json',
 'audits/golomb_small/agent/run_benchmark_0003/manifest.json',
 'audits/golomb_small/agent/run_targets_0003/manifest.json',
 'audits/golomb_small/agent/run_witnesses_0002/manifest.json',
 'audits/golomb_small/root/run_order9_0001/manifest.json',
 'audits/golomb_small/agent/run_order9_benchmark_0001/manifest.json',
 'audits/golomb_small/agent/run_order9_target_0001/manifest.json',
 'audits/golomb_small/agent/run_order9_witness_0001/manifest.json',
 'audits/golomb_small/root/run_next10_0001/manifest.json',
 'audits/golomb_small/root/run_next11_0001/manifest.json',
 'audits/golomb_small/root/run_next11_0002/manifest.json',
 'audits/golomb_small/agent/run_orders10_11_benchmark_0001/manifest.json',
 'audits/golomb_small/agent/run_order10_target_0001/manifest.json',
 'audits/golomb_small/agent/run_order11_target_0001/manifest.json',
 'audits/golomb_small/agent/run_order10_witness_0001/manifest.json',
 'audits/golomb_small/agent/run_order11_witness_0001/manifest.json',
 'audits/golomb_small/agent/run_order11_target_0002/manifest.json']
manifests += ['audits/golomb_small/root/run_order12_tail_0001/manifest.json',
 'audits/golomb_small/root/run_order12_gap_0001/manifest.json',
 'audits/golomb_small/root/native_order12/run_0001/manifest.json']
stale_rel = 'audits/golomb_small/agent/order12/run_gap_benchmark_0001/manifest.json'
manifests += [p.relative_to(base).as_posix() for p in sorted(
    (base/'audits/golomb_small/agent/order12').glob('run_*/manifest.json'))
    if p.relative_to(base).as_posix() != stale_rel]
manifests += ['audits/golomb_small/root/native_order13/run_0001/manifest.json']
manifests += [p.relative_to(base).as_posix() for p in sorted(
    (base/'audits/golomb_small/agent/order13').glob('run_*/manifest.json'))]
validation=[]
for rel in manifests:
    p=base/rel
    run=subprocess.run([sys.executable,'-E',str(validator),str(p),'--root',str(root)],capture_output=True,text=True)
    validation.append({'path':rel,'exit_code':run.returncode,'stdout':run.stdout.strip(),'stderr':run.stderr.strip()})
if any(r['exit_code'] for r in validation):
    print(json.dumps(validation,indent=2))
    raise RuntimeError('Evidence validation failed; checkpoint not sealed')

# This early benchmark is retained, but its source changed after execution.
# Its fresh replacement, benchmark_0002, is among current valid manifests.
stale_path = base/stale_rel
stale_run = subprocess.run([sys.executable,'-E',str(validator),str(stale_path),'--root',str(root)],
                           capture_output=True,text=True)
expected_error = 'invalid manifest: input changed since the run: research_round4/audits/golomb_small/agent/order12/golomb_order12_gap_independent.py'
if stale_run.returncode != 1 or stale_run.stderr.strip() != expected_error or stale_run.stdout.strip():
    raise RuntimeError('Historical stale benchmark no longer matches its documented limitation')
stale_data = json.loads(stale_path.read_text(encoding='utf-8'))
for row in stale_data['outputs']:
    p = (root/row['path']).resolve()
    if not p.is_relative_to(root.resolve()) or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        raise RuntimeError('Historical stale benchmark output integrity failed')
stale_record = {'path':stale_rel,'current_manifest_validation':'FAIL_EXPECTED_STALE_INPUT',
 'validator_exit_code':stale_run.returncode,'validator_stderr':stale_run.stderr.strip(),
 'output_hashes_match':True,'mathematical_premise':False,
 'replacement':'audits/golomb_small/agent/order12/run_gap_benchmark_0002/manifest.json'}
(base/'audits/historical_stale_record_0004.json').write_text(json.dumps(stale_record,indent=2),encoding='utf-8')

archive=base/'audits/golomb_sources/archive_20_23'
archive_manifest=json.loads((archive/'MANIFEST.json').read_text(encoding='utf-8'))
archive_checks=[]
for row in archive_manifest['records']:
    path=(archive/row['file']).resolve()
    if not path.is_relative_to(archive.resolve()) or not path.is_file():
        raise RuntimeError('Missing/out-of-scope archived source artifact')
    payload=path.read_bytes()
    digest=hashlib.sha256(payload).hexdigest()
    if len(payload)!=row['bytes'] or digest!=row['sha256']:
        raise RuntimeError('Archived source byte/hash mismatch: '+row['file'])
    archive_checks.append({'file':row['file'],'bytes':len(payload),'sha256':digest,'status':'PASS'})
archive22=base/'audits/golomb_sources/archive_22_terminal_followup'
manifest22=json.loads((archive22/'MANIFEST.json').read_text(encoding='utf-8'))
for row in manifest22['files']:
    path=(archive22/row['path']).resolve()
    if not path.is_relative_to(archive22.resolve()) or not path.is_file():
        raise RuntimeError('Missing/out-of-scope new O22 source artifact')
    payload=path.read_bytes()
    digest=hashlib.sha256(payload).hexdigest()
    if len(payload)!=row['bytes'] or digest!=row['sha256']:
        raise RuntimeError('New O22 source byte/hash mismatch')
    archive_checks.append({'file':'archive_22_terminal_followup/'+row['path'],
                           'bytes':len(payload),'sha256':digest,'status':'PASS'})
for row in manifest22['reused_retained_evidence']:
    path=(archive22/row['path']).resolve()
    if not path.is_relative_to((base/'audits/golomb_sources').resolve()) or hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:
        raise RuntimeError('Reused O22 source integrity failure')
marks=json.loads((base/'audits/golomb_sources/all_witness_inputs.json').read_text(encoding='utf-8'))['marks_by_order']
gaps21=[2,22,32,21,5,1,12,34,15,35,7,9,60,10,20,8,3,14,19,4]
official21=[0]
for gap in gaps21: official21.append(official21[-1]+gap)
official23=[0,3,7,17,61,66,91,99,114,159,171,199,200,226,235,246,277,316,329,348,350,366,372]
if official21[-1]!=333 or sorted(333-x for x in official21)!=marks['21']:
    raise RuntimeError('Order21 official-gap numerical crosswalk failed')
if sorted(372-x for x in official23)!=marks['23']:
    raise RuntimeError('Order23 archive-witness reflection failed')
source_validation={'source_artifacts':archive_checks,
 'order21_gap_sum':333,'order21_reflection_matches_saved_witness':True,
 'order23_reflection_matches_saved_witness':True,
 'scope':'Integrity and exact literal arithmetic checks only; not validation of historical search coverage or acceptance of external results.'}
(base/'audits/source_record_validation.json').write_text(json.dumps(source_validation,indent=2),encoding='utf-8')

report=base/'VERIFICATION_REPORT.md'
body=report.read_text(encoding='utf-8')
inventory=json.loads((base/'audits/inventory/inventory.json').read_text(encoding='utf-8'))
ledger=json.loads((base/'audits/integrated_verdicts.json').read_text(encoding='utf-8'))
ids=re.findall(r'^### ([A-Z]\d{2}) — PDF p',body,re.M)
expected=[c['id'] for c in inventory['claims']]
pages=sorted({n for c in inventory['claims'] for n in c['pages']})
counts=Counter(e['status'] for e in ledger['entries'].values())
if ids!=expected or set(expected)!=set(ledger['entries']) or len(ids)!=90 or pages!=list(range(1,23)):
    raise RuntimeError('Inventory coverage mismatch')
if dict(counts)!=ledger['entry_counts'] or ledger['gate_passed'] is not False:
    raise RuntimeError('Ledger count or gate status mismatch')
table=json.loads((base/'audits/golomb_sources/golomb_table_status.json').read_text(encoding='utf-8'))
if ledger['checkpoint']!='R4-GATE-0005' or table['checkpoint']!='R4-GATE-0005' or 'Checkpoint R4-GATE-0005.' not in body:
    raise RuntimeError('Checkpoint labels disagree')
if table['exact_equality_orders_locally_established']!=list(range(1,14)) or table['lower_bound_orders_unreplayed']!=list(range(14,29)):
    raise RuntimeError('Incorrect Golomb range')
links=re.findall(r'\]\(([^)]+)\)',body)
local=[x for x in links if not re.match(r'https?://',x)]
missing=[x for x in local if not (base/x).exists()]
if missing: raise RuntimeError(('Missing links',missing))
if 'R3=465 chain' in body: raise RuntimeError('Uncorrected equality wording')

structure={'entries':len(ids),'unique_entries':len(set(ids)),'same_inventory_order':True,
 'source_pages':pages,'local_links':len(local),'missing_links':[],
 'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'counts':dict(counts)}
(base/'audits/report_structure_check.json').write_text(json.dumps(structure,indent=2),encoding='utf-8')
(base/'audits/final_manifest_validation.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')

paths=set(manifests)
paths.update(x for x in local if (base/x).is_file())
paths.update(['VERIFICATION_REPORT.md','STATUS.md','TARGET.md','NEXT_CHECKPOINT.md',
 'GOLOMB_VERIFICATION_SUPPLEMENT.md','audits/golomb_sources/golomb_table_status.json',
 'audits/golomb_sources/EXISTENCE_AND_SMALL_ORDERS.md','audits/golomb_sources/WITNESS_REVIEW.md',
 'audits/golomb_sources/TABLE_SCOPE_AUDIT.md','audits/golomb_sources/ORDERS_9_13_PRIMARY.md',
 'audits/golomb_sources/ORDERS_14_23_PRIMARY.md','audits/golomb_sources/RANKIN_1993_FOLLOWUP.md',
 'audits/golomb_sources/orders26_28_followup.md','audits/golomb_sources/ALL_WITNESSES_REVIEW.md',
 'audits/golomb_sources/13_SCOPE_IN_RANKIN.md','audits/SELF_AUDIT_GATE_0002.md',
 'audits/golomb_sources/G13_PRIMARY_NUMERIC_FOLLOWUP.md','audits/INTEGRATION_SNAPSHOT_REVIEW_0002.md',
 'audits/golomb_small/ORDER9_PROOF.md','audits/golomb_small/agent/ORDER9_ADDENDUM.md',
 'audits/golomb_sources/ORDERS_20_23_FOLLOWUP.md','audits/golomb_sources/ORDERS_20_23_INDEPENDENT_REVIEW.md',
 'audits/golomb_sources/rankin93optimal.ps','audits/golomb_small/PROOF.md','audits/golomb_small/agent/AUDIT.md',
 'audits/integrated_verdicts.json','audits/inventory/inventory.json','audits/SELF_AUDIT_GATE.md',
 'audits/report_structure_check.json','audits/final_manifest_validation.json',
 'formal/compilation_gate_0001/manifest.json','formal/geometry/Geometry.lean',
 'formal/small_cases/SmallCases.lean','audits/certificates_independent_review/REVIEW.md'])
paths.add('audits/source_record_validation.json')
paths.add('audits/FINAL_DELTA_REVIEW_0002.md')
paths.update(['audits/FINAL_DELTA_REVIEW_0003.md','audits/SELF_AUDIT_GATE_0003.md',
 'audits/golomb_small/ORDERS10_11_PROOF.md','audits/golomb_small/agent/ORDERS10_11_ADDENDUM.md',
 'audits/golomb_small/agent/ORDER11_COMPLETION_ADDENDUM.md',
 'audits/golomb_small/root/validate_next_records.py','audits/golomb_small/root/next_records_validation.json',
 'audits/golomb_small/agent/orders10_11_counter_crosscheck.json',
 'audits/golomb_small/agent/orders10_11_root_crossreview.json',
 'audits/golomb_small/agent/order11_completion_crosscheck.json',
 'audits/golomb_small/agent/root_v1_v2_diff_review.json',
 'audits/golomb_sources/O22_TERMINAL_FOLLOWUP.md','audits/golomb_sources/O22_TERMINAL_INDEPENDENT_REVIEW.md'])
paths.update(['checks/build_golomb_status.py','checks/build_verification_report.py','checks/seal_checkpoint.py',
 'audits/golomb_small/agent/AUDIT_pre_witness_wording_20260910.md'])
paths.update(p.relative_to(base).as_posix() for p in archive.iterdir() if p.is_file())
paths.update(p.relative_to(base).as_posix() for p in archive22.iterdir() if p.is_file())
paths.update(['audits/golomb_small/ORDER12_PROOF.md','audits/golomb_small/ORDER12_PROOF_REVIEW.md',
 'audits/golomb_small/TAIL_BOUND_REVIEW.md','audits/golomb_small/UNUSED_GAP_BOUND_REVIEW.md',
 'audits/golomb_small/NATIVE_ORDER12_CODE_REVIEW.md','audits/SELF_AUDIT_GATE_0004.md',
 'audits/historical_stale_record_0004.json',
 'audits/golomb_small/root/validate_order12_records.py',
 'audits/golomb_small/root/order12_record_validation.json','checks/integrate_checkpoint_0004.py',
 'audits/golomb_small/root/tail_bound_enumerator.py','audits/golomb_small/root/unused_gap_enumerator.py'])
paths.update(p.relative_to(base).as_posix() for p in (base/'audits/golomb_small/root').glob('order12_*.json'))
for rel in ['audits/golomb_small/root/native_order12','audits/golomb_small/root/run_order12_tail_0001',
            'audits/golomb_small/root/run_order12_gap_0001','audits/golomb_small/agent/order12',
            'audits/golomb_small/root/native_order13','audits/golomb_small/agent/order13']:
    paths.update(p.relative_to(base).as_posix() for p in (base/rel).rglob('*')
                 if p.is_file() and '__pycache__' not in p.parts)
paths.update(['audits/FINAL_DELTA_REVIEW_0004.md','audits/SELF_AUDIT_GATE_0005.md',
 'audits/golomb_small/ORDER13_PROOF.md','audits/golomb_small/NATIVE_ORDER13_CODE_REVIEW.md',
 'checks/prepare_order13.py','checks/integrate_checkpoint_0005.py'])
review_rel = 'audits/FINAL_DELTA_REVIEW_0005.md'
if (base/review_rel).is_file():
    paths.add(review_rel)
seal={p:hashlib.sha256((base/p).read_bytes()).hexdigest() for p in sorted(paths)}
result={'checkpoint':'R4-GATE-0005','gate_passed':False,'mathematical_review_complete_except_external_inputs':True,
 'external_input_standard':'awaiting_user_clarification','current_manifests_validated':len(validation),
 'archived_source_artifacts_validated':len(archive_checks),
 'historical_stale_manifests_retained':1,'current_delta_review_included':review_rel in paths,
 'counts':dict(counts),'hashes_sha256':seal,
 'scope':'Completed checkpoint including honest UNDECIDED initial-run records; manifest validity does not imply mathematical completion. No new research or overall-goal completion. Legacy-v1 metadata limitations remain explicit in validator outputs.'}
(base/'audits/checkpoint_seal.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'current_manifests_validated':len(validation),'sealed_files':len(seal),'structure':structure,'gate_passed':False},indent=2))
