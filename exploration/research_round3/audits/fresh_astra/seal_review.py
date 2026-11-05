"""Seal the precise reviewed source revision and all reviewer-owned artifacts."""
import datetime
import hashlib
import json
import pathlib

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

source={}
for name in ['G_results.json','J_results.json','F_results.json']:
    for rel,value in json.loads((HERE/name).read_text())['input_sha256'].items():
        assert sha(ROOT/rel)==value,('reviewed input changed',rel)
        source[rel]=value
for rel in ['research_round3/MANDATE.txt','research_round3/ROOT_AUTHOR_REPORT.md',
            'research_round3/audits/reviewer_assignment.json','research_round3/joint/REPORT.md',
            'research_round3/four/R3_R4_REPORT.md','research_round3/cap/ap5_uniqueness.md',
            'research_round3/cap/endpoint_neighbor.md','research_round2/routes/four_multi_core.md',
            'research_round3/round3_report.tex']:
    source[rel]=sha(ROOT/rel)
(HERE/'reviewed_sources.json').write_text(json.dumps(source,indent=2,sort_keys=True)+'\n')
artifacts={p.name:sha(p) for p in HERE.iterdir() if p.is_file() and p.name!='seal.json'}
seal=dict(reviewer='fresh_astra',assigned_cores=['G','J','F'],verdict='PASS',
          issues=dict(major=[],minor=[]),
          sealed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
          source_hashes_unchanged=True,reviewer_artifact_sha256=artifacts)
(HERE/'seal.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n')
print(json.dumps({name:artifacts[name] for name in ['REVIEW.md','G_results.json','J_results.json','F_results.json','manifest.json']},indent=2))
