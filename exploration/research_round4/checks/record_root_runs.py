from pathlib import Path
import json, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
RUN_TAG=sys.argv[1] if len(sys.argv)>1 else 'run_gate_0002'
if not RUN_TAG.isidentifier():
    raise ValueError('The run tag must be a simple directory name.')
SKILL=Path('C:/Users/ZhuanZ/.codex/plugins/cache/openai-curated-remote/mathbox/3.0.0/skills/computation-audit')
jobs=[
 ('general','research_round4/checks/general_and_legacy_exact.py','exact_results.json',
 ['research_round3/L-free Grid_Upper bound Research.pdf','2502.05162v1.pdf','research_round2/round2_report.tex','research_20260909/grid_L_upper_bounds.tex'],
 'Exact scalar identities, stated legacy counterexamples and repairs, setup and sensitivity scans, R3 tent, and the ten stated prime examples.',
 {'general_scalar_k':[5,6],'rational_coefficient_q':[3,4,5,6,7],'legacy_rounding_n':[3,2000],'legacy_average_scan_n':[3,3000],'corollary_k3_N_t_cap':[729,81,66],'setup_n':[450,465],'prime_list':[3,5,7,11,13,17,19,23,29,31]}),
 ('certificates','research_round4/checks/certificates_independent.py','results.json',
 ['research_round3/'+x for x in json.loads((ROOT/'research_round4/audits/certificates/results.json').read_text())['provenance']['source_hashes']],
 'All fixed RUP traces, both coefficient-wise parametric lifts, full labeled window-13 coverage, literal 155 sets, and the prescribed 60 ruler pairs.',
 {'window_width':13,'source_side':464,'pair_family_count':60,'fixed_cores':4,'parametric_lifts':2})
]
for name,script,result,inputs,assertion,bounds in jobs:
    out=f'research_round4/audits/{name}/{RUN_TAG}'
    contract_path=ROOT/f'research_round4/audits/{name}/{RUN_TAG}_contract.json'
    files=[script]+inputs
    contract={'claim_id':'R4-GATE-'+name.upper(),
      'mathematics':{'assertion_tested':assertion,'coefficient_domain':('exact integers, rationals and symbolic rational identities' if name=='general' else 'exact integers'),
        'conventions':'Directed positive-step L, row-first zero/one coordinate conventions explicitly documented in scripts; finite ranges only.',
        'inputs':files,'bounds':bounds,'non_claims':['No new Ramsey bound.','No proof of universal inequalities from finite samples.','No independent regeneration of external Golomb optimality searches.']},
      'execution_artifacts':files,'software':[{'name':'Python','version':sys.version.split()[0]}],
      'randomness':{'used':False,'generator':'','seed':None}}
    contract_path.write_text(json.dumps(contract,indent=2),encoding='utf-8')
    args=[sys.executable,str(SKILL/'scripts/run_experiment.py'),'--root',str(ROOT),'--contract',str(contract_path)]
    for p in files:args+=['--input',p]
    args+=['--output',out,'--result',out+'/'+result,'--timeout','60','--max-output-bytes','1048576','--',sys.executable,'-E',script,out]
    done=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
    print(name,done.returncode,done.stdout,done.stderr)
    if done.returncode:raise SystemExit(done.returncode)
    check=subprocess.run([sys.executable,str(SKILL/'scripts/validate_manifest.py'),str(ROOT/out/'manifest.json'),'--root',str(ROOT)],cwd=ROOT,capture_output=True,text=True)
    print('manifest_validation',name,check.returncode,check.stdout,check.stderr)
    if check.returncode:raise SystemExit(check.returncode)
