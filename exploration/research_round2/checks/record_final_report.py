"""Check the exact reviewed mathematical body and record final release metadata."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[1]
old = (ROOT / 'audits/report_reviewed_rev003.tex').read_bytes()
new = (ROOT / 'round2_report.tex').read_bytes()
assert sha256(old).hexdigest() == '8740b7f47c53d38c3c4b09e2a8d24a0099cb5566ecf71f8e94c80edf729cb1ca'
start = rb'\section{Round-1 Method Recap and Slack Analysis}'
end = rb'\section{Self-Verification Reports}'
def math_body(data):
    assert data.count(start) == data.count(end) == 1
    return data[data.index(start):data.index(end)]
old_path = rb'\texttt{checks/setup\_exact\_audit.py}'
new_path = rb'\path{checks/setup_exact_audit.py}'
assert math_body(old).count(old_path) == math_body(new).count(new_path) == 1
restored_body = math_body(new).replace(new_path, old_path, 1)
assert math_body(old) == restored_body, 'Body differs beyond the one logged path-formatting edit'
spacing_snapshot = (ROOT / 'audits/report_before_heading_spacing.tex').read_bytes()
assert sha256(spacing_snapshot).hexdigest() == 'cabca7c694f76ba3a5e9e559bf4f70bf8f0ce4e7163d949a3fc1b00d0e768f2d'
begin = rb'\begin{document}'
assert new[new.index(begin):] == spacing_snapshot[spacing_snapshot.index(begin):]
assignment = json.loads((ROOT / 'audits/CROSS_ASSIGNMENTS.json').read_text())
pins = dict(assignment['source_hashes'])
pins.pop('round2_report.tex')
pins.update({
    'routes/general_neighbor_proof.md': '62e5684b1f4488253d68750e437c61312033970672f5bf391fba7888f1b77c9e',
    'routes/four_multi_core.md': 'f2d3549298f9ec921a52d9d226795cc09d29fdd3cb41b8dc1c69815f8771fbfb',
    'routes/setup_inherited_toolkit_audit.md': '1376ba24a1c9190345a46c6c37d47693a68be47df0020751de4f849eb1a5a62d',
})
for name, expected in pins.items():
    assert sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
reviews = {
    'fresh_astra': 'audits/cross_astra.md',
    'r2_lower': 'audits/cross_lower_sol.md',
    'r2_weights': 'audits/cross_weights_sol.md',
    'r2_four_multi': 'audits/cross_four_astra_general.md',
}
for entry in assignment['assignments']:
    assert not set(entry['authors']) & set(entry['reviewers'])
    assert all(reviewer in reviews for reviewer in entry['reviewers'])
    if entry['task'] in ('FM_all', 'GN_general', 'K1_dual', 'STRUCT_moments'):
        assert len(set(entry['reviewers'])) >= 2
        assert set(entry['reviewers']) & {'fresh_astra', 'r2_four_multi'}
result = {
    'status': 'PASS',
    'verification_scope': 'Exact mathematical-body preservation, pinned file integrity, and assignment coverage. Mathematical verdicts are in the independently authored review files.',
    'reviewed_report_sha256': sha256(old).hexdigest(),
    'final_report_sha256': sha256(new).hexdigest(),
    'sections_2_through_6_identical_after_one_path_formatting_reversal': True,
    'formatting_substitution': {'old': old_path.decode(), 'new': new_path.decode(), 'occurrences': 1},
    'reviewed_mathematical_body_sha256': sha256(restored_body).hexdigest(),
    'final_mathematical_body_sha256': sha256(math_body(new)).hexdigest(),
    'current_reviewed_pins': pins,
    'reviews': {key: {'path': name, 'sha256': sha256((ROOT / name).read_bytes()).hexdigest()} for key, name in reviews.items()},
    'review_verdict_record': 'All assigned bundles PASS; see the four review documents and ISSUES.md for repair history.',
    'final_report_edits': ['Review-status and review-report insertion', 'Explicit PROVED environment labels', 'Expanded correction record', 'Corrected Section7 profile label from unit to integer polynomial weights', 'One breakable path in Section2; exact reversal restores the reviewed mathematical body'],
    'exact_R3': 'UNRESOLVED',
    'pagination_only_after_final_astra_review': True,
    'final_provenance_audit_sha256': sha256((ROOT / 'audits/final_release_provenance_astra.md').read_bytes()).hexdigest(),
    'R3_interval': [21, 465],
    'global_exhaustion': 'NOT PROVED',
}
(ROOT / 'audits/FINAL_REPORT_RELEASE.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'sections_2_through_6_identical_after_one_path_formatting_reversal': True, 'final_report_sha256': result['final_report_sha256'], 'reviewed_pins_checked': len(pins), 'review_files': len(reviews)}))
