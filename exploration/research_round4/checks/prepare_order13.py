"""Create a fresh, bounded root order-13 verification without changing order 12."""
from pathlib import Path
import hashlib, json, math, subprocess, sys

if not __debug__:
    raise RuntimeError('Assertions-active Python required')
base = Path(__file__).resolve().parents[1]
old = base/'audits/golomb_small/root/native_order12'
new = base/'audits/golomb_small/root/native_order13'
if new.exists():
    raise RuntimeError('New directory already exists; inspect instead of overwriting')
snapshot = base/'audits/checkpoint_0004_snapshot'
seal = json.loads((snapshot/'audits/checkpoint_seal.json').read_text())
assert seal['checkpoint'] == 'R4-GATE-0004'
for rel, digest in seal['hashes_sha256'].items():
    assert hashlib.sha256((snapshot/rel).read_bytes()).hexdigest() == digest, rel
status = json.loads((snapshot/'audits/golomb_sources/golomb_table_status.json').read_text())
assert status['exact_equality_orders_locally_established'] == list(range(1,13))
assert status['rows'][12]['printed_G'] == 106
raw = math.comb(105,12)
assert raw == math.factorial(105)//(math.factorial(12)*math.factorial(93)) == 1951641934005400
assert 1+12*raw == 23419703208064801 < 2**64
new.mkdir()

def change_once(text, before, after):
    if text.count(before) != 1:
        raise RuntimeError(f'Nonunique source change: {before}')
    return text.replace(before, after)

source = (old/'ExactGolomb.cs').read_text()
source = source.replace('ExactGolomb12', 'ExactGolomb13')
source = change_once(source, 'm <= 12 && length >= 0 && length <= 84', 'm <= 13 && length >= 0 && length <= 105')
source = change_once(source, '{0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72}', '{0, 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85}')
source = change_once(source, '18574174153080UL', '1951641934005400UL')
(new/'ExactGolomb.cs').write_text(source,encoding='utf-8')

wrapper = (old/'run_native.ps1').read_text()
wrapper = wrapper.replace('root/order12_preflight.json', 'root/native_order13/preflight.json')
wrapper = wrapper.replace('checkpoint_0003_snapshot', 'checkpoint_0004_snapshot').replace('R4-GATE-0003', 'R4-GATE-0004')
wrapper = wrapper.replace('$snapshot.rows[11].order -ne 12 -or $snapshot.rows[11].printed_G -ne 85',
                          '$snapshot.rows[12].order -ne 13 -or $snapshot.rows[12].printed_G -ne 106')
wrapper = change_once(wrapper, '$i -lt 11;', '$i -lt 12;')
wrapper = wrapper.replace("marks_by_order.'12'", "marks_by_order.'13'")
wrapper = wrapper.replace('$marks.Count -ne 12', '$marks.Count -ne 13').replace('$marks[-1] -ne 85', '$marks[-1] -ne 106')
# The prior-minimum loop and the witness loop now have identical bounds: change
# only the witness loop that follows the HashSet allocation.
marker = '$seen = [Collections.Generic.HashSet[int]]::new()'
before, after = wrapper.split(marker)
after = after.replace('$i -lt 12;', '$i -lt 13;', 1).replace('$j -lt 12;', '$j -lt 13;', 1)
wrapper = before + marker + after
wrapper = wrapper.replace('$seen.Count -ne 66', '$seen.Count -ne 78').replace('span=85; positive_distinct_pairs=66', 'span=106; positive_distinct_pairs=78')
wrapper = wrapper.replace('order=12; maximum_span=84', 'order=13; maximum_span=105').replace("'C(84,11)'", "'C(105,12)'")
wrapper = wrapper.replace('actually_consultable=11', 'actually_consultable=12')
wrapper = wrapper.replace('@(11,71,0)))', '@(11,71,0), @(12,84,0)))')
wrapper = wrapper.replace('[ExactGolomb12]', '[ExactGolomb13]').replace('::Run(12, 84, 300', '::Run(13, 105, 300')
wrapper = wrapper.replace('No order above 12 searched.', 'No order above 13 searched.')
(new/'run_native.ps1').write_text(wrapper,encoding='utf-8')

tests = {
 'exact_verify': Path('C:/Users/ZhuanZ/.codex/skills/exact-verify/scripts/self_test.py'),
 'enumeration_sanity': Path('C:/Users/ZhuanZ/.codex/skills/small-case-enumerator/scripts/sanity_suite.py'),
}
preflight = {}
for name,path in tests.items():
    run = subprocess.run([sys.executable,'-E',str(path)],capture_output=True,text=True)
    preflight[name] = {'exit_code':run.returncode,'stdout':run.stdout.strip(),'stderr':run.stderr.strip()}
    assert run.returncode == 0
assert preflight['exact_verify']['stdout'] == 'ENVIRONMENT OK'
assert preflight['enumeration_sanity']['stdout'].startswith('SANITY OK')
(new/'preflight.json').write_text(json.dumps(preflight,indent=2),encoding='utf-8')

prefix = 'research_round4/audits/golomb_small/root/native_order13/'
artifacts = [prefix+x for x in ['ExactGolomb.cs','run_native.ps1','preflight.json','contract.json','PLAN_AND_PROOF.md']]
artifacts += ['research_round4/audits/golomb_sources/all_witness_inputs.json',
 'research_round4/audits/checkpoint_0004_snapshot/audits/golomb_sources/golomb_table_status.json',
 'research_round4/audits/checkpoint_0004_snapshot/audits/checkpoint_seal.json',
 'research_round4/audits/golomb_small/TAIL_BOUND_REVIEW.md',
 'research_round4/audits/golomb_small/UNUSED_GAP_BOUND_REVIEW.md']
contract = {
 'claim_id':'R4-GATE-GOLOMB13-NATIVE-CS-ROOT',
 'mathematics': {
  'assertion_tested':'Existing G(13)=106: exclude every normalized 13-mark Golomb ruler of span at most 105 and check a span-106 attaining witness.',
  'coefficient_domain':'checked UInt64 counts and binomials; exact integer marks and differences; floating-point timing only',
  'conventions':'Zero fixed before pruning; no symmetry quotient; first rejection priority tail, collision, updated unused-gap; exact C(L-x,r) child weights.',
  'inputs':artifacts,
  'bounds': {'target_order':13,'maximum_span':105,'raw_universe':raw,'raw_formula':'C(105,12)',
    'prior_minima_maximum_order':12,'root_plus_depth_counter_bound':1+12*raw,
    'benchmark_cases':[[1,0,1],[3,2,0],[3,3,2],[4,5,0],[4,6,2],[11,71,0],[12,84,0]],
    'benchmark_seconds_each':30,'target_seconds':300,'external_total_seconds':360},
  'non_claims':['No G(13) lower bound used in pruning.','No higher-order exclusion or new L-grid research.','No Lean proof.','Incomplete traversal remains UNDECIDED.']},
 'execution_artifacts':artifacts,
 'software':[{'name':'PowerShell','version':'7.6.5'},{'name':'.NET','version':'10.0.11'},
             {'name':'C# compilation','version':'PowerShell Add-Type /optimize+; explicit checked arithmetic'}],
 'randomness':{'used':False,'generator':'','seed':None}}
(new/'contract.json').write_text(json.dumps(contract,indent=2),encoding='utf-8')
(new/'preparation.json').write_text(json.dumps({'previous_checkpoint':'R4-GATE-0004','previous_sealed_files_verified':len(seal['hashes_sha256']),
 'raw_universe':raw,'uniform_counter_bound':1+12*raw,'status':'prepared_not_executed'},indent=2),encoding='utf-8')
print(json.dumps({'prepared':str(new),'raw_universe':raw,'counter_bound':1+12*raw,'preflights':'PASS','search_executed':False}))
