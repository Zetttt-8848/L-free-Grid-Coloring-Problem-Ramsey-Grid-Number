"""Serialize root's completed review reconciliation with literal evidence hashes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[2]
AUD = ROOT / 'research_round3/audits'
assignment = json.loads((AUD / 'reviewer_assignment.json').read_text())
proof = json.loads((AUD / 'review_provenance_check.json').read_text())
assert proof['status'] == 'PASS'
evidence = {
    'fresh_astra': ['REVIEW.md', 'seal.json', 'manifest.json',
                    'ADDENDUM.md', 'addendum_seal.json'],
    'joint_astra': ['REPORT.md', 'verdicts.json', 'manifest.json'],
    'lower_sol': ['REPORT.md', 'joint_audit.json', 'four_audit.json', 'manifest.json'],
    'setup_sol': ['C_L_INDEPENDENT_REVIEW.md', 'independent_audit_results.json',
                  'computation_manifest.json'],
}
cores = {}
for core, reviewers in assignment['assignments'].items():
    assert len(reviewers) == 2 and len(set(reviewers)) == 2
    assert assignment['authors'][core] not in reviewers
    assert any('astra' in r for r in reviewers)
    cores[core] = []
    for reviewer in reviewers:
        files = []
        for name in evidence[reviewer]:
            path = AUD / reviewer / name
            files.append({'path': path.relative_to(ROOT).as_posix(),
                          'sha256': sha256(path.read_bytes()).hexdigest()})
        cores[core].append({'reviewer': reviewer, 'verdict': 'PASS', 'evidence': files})
out = {
    'schema': 'round3-final-independent-review-matrix-v1',
    'release_status': 'PASS',
    'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'integration_basis': 'Root read all four final reviews and the manuscript addendum; all scoped verdicts PASS.',
    'unresolved_issues': [],
    'cores': cores,
    'resolved_review_events': [
        'joint_astra A1/A2: reviewer profile parser and exact symmetry-CNF convention corrected before PASS.',
        'setup_sol E1: reviewer cube collection key corrected before PASS.',
        'R3-E6: integrated TeX hash changes separately re-reviewed and addendum-sealed; original seal preserved.',
        'Positive-shift ruler-family scope explicit; author-stage NTT checker attribution corrected.',
    ],
    'scientific_open_questions': [
        'R3 remains between 21 and 465.',
        '48 side-21 cubes remain undecided.',
        'The one-class system including the final hook/AP5 premise is not yet decided.',
        'No 45-cap theorem, reduced tower height, or global research exhaustion is claimed.',
    ],
}
(AUD / 'final_review_matrix.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'release_status': 'PASS', 'cores': len(cores),
                  'independent_core_verdicts': sum(map(len, cores.values())),
                  'unresolved_review_issues': 0}))
