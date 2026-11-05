"""Randomized reviewer allocation, subject to author and model constraints."""
from pathlib import Path
from hashlib import sha256
import json,random
root=Path('research_round2')
rng=random.Random(2026090902)
pool=['fresh_astra','r2_four_multi','r2_lower','r2_weights']
astra={'fresh_astra','r2_four_multi'}
tasks=[
 ('FM_all',['r2_four_multi','r2_weights'],2,True),
 ('GN_general',['root'],2,True),
 ('K1_dual',['root'],2,True),
 ('STRUCT_moments',['root'],2,True),
 ('LOWER',['r2_lower'],1,False),
 ('WEIGHTS_R3',['r2_weights'],1,False),
 ('SETUP',['r2_setup'],1,False)]
assign=[]
for task,authors,count,needs_astra in tasks:
    eligible=[p for p in pool if p not in authors]
    while True:
        reviewers=rng.sample(eligible,count)
        if not needs_astra or astra.intersection(reviewers):break
    assign.append(dict(task=task,authors=authors,reviewers=reviewers))
files=['round2_report.tex','routes/kernel_dual_proof.md','routes/general_neighbor_proof.md',
       'routes/structural_moments_proof.md','routes/four_multi_core.md',
       'routes/four_multi_overlap.md','routes/four_multi_region_alternative.md',
       'routes/four_multi_joint_report.md','routes/weights_report.md',
       'routes/weights_four_report.md','routes/lower/SUBTASK_REPORT.md',
       'routes/setup_inherited_toolkit_audit.md','certificates/kernel_dual_464.json',
       'certificates/four_multi_final.json','certificates/weights_four_22006246.json']
hashes={name:sha256((root/name).read_bytes()).hexdigest() for name in files}
out={'checkpoint':'R2-CP1-preintegration','seed':2026090902,
     'policy':'Author exclusion; two reviewers for every Level3 core, at least one Astra. FM_all excludes both the proof and profile authors.',
     'assignments':assign,'source_hashes':hashes,
     'status':'Assignments prepared; execution starts only after all author reports frozen.'}
(root/'audits/CROSS_ASSIGNMENTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(assign,indent=2))
