"""One-time prose update after both order-13 exclusions and reviews pass."""
from pathlib import Path
import json

base = Path(__file__).resolve().parents[1]
record = json.loads((base/'audits/golomb_small/root/native_order13/record_validation.json').read_text())
if record.get('independent_full_target_comparison',{}).get('verdict') != 'PASS':
    raise RuntimeError('Independent target integration has not passed')
for rel in ['audits/golomb_small/NATIVE_ORDER13_CODE_REVIEW.md',
            'audits/golomb_small/agent/order13/ORDER13_ADDENDUM.md',
            'audits/SELF_AUDIT_GATE_0005.md']:
    if not (base/rel).is_file():
        raise RuntimeError('Missing reviewed evidence: '+rel)

p = base/'checks/build_verification_report.py'
s = p.read_text(encoding='utf-8')
if "record['checkpoint']='R4-GATE-0004'" not in s:
    raise RuntimeError('Expected predecessor builder not found')
s = s.replace('R4-GATE-0004','R4-GATE-0005')
s = s.replace('The previous complete checkpoint is preserved in `audits/checkpoint_0003_snapshot`',
              'The previous complete checkpoint is preserved in `audits/checkpoint_0004_snapshot`')
s = s.replace('orders 6 through 12 have two','orders 6 through 13 have two')
s = s.replace('orders 1 through 12','orders 1 through 13').replace('orders 13 through 28','orders 14 through 28')
s = s.replace("'audits/golomb_small/ORDER12_PROOF_REVIEW.md']",
              "'audits/golomb_small/ORDER12_PROOF_REVIEW.md','audits/golomb_small/ORDER13_PROOF.md','audits/golomb_small/NATIVE_ORDER13_CODE_REVIEW.md','audits/golomb_small/agent/order13/ORDER13_ADDENDUM.md']")
needle='The implementations agree on every depth counter; earlier incomplete or failed attempts remain explicitly non-evidentiary for the lower bound.'
addition=' The [order-thirteen proof](audits/golomb_small/ORDER13_PROOF.md) further establishes G(13)=106 by two complete independent exclusions through span 105 and a checked span-106 witness. Its new execution contract is itself hashed. The original order-thirteen publication\'s numeric statement remains uninspected, but the local proof removes dependence on that external minimum.'
if needle not in s:
    raise RuntimeError('Order12 summary anchor missing')
s = s.replace(needle,needle+addition)
s = s.replace('especially the original numerical statement at order 13 and the exact no-shorter outcome at order 22',
              'especially the exact no-shorter outcome at order 22')
s = s.replace('Accepting cited theorems would not itself verify a source statement or an unstated link.',
              'Accepting cited theorems would not itself verify a source statement or an unstated link. The uninspected original numerical statement at order 13 is now a historical literature gap; the local proof establishes that minimum independently.')
s = s.replace('[checkpoint-0004 self-audit](audits/SELF_AUDIT_GATE_0004.md)',
              '[checkpoint-0005 self-audit](audits/SELF_AUDIT_GATE_0005.md)')
s = s.replace('records the latest completed exclusion and its limits.',
              'records the latest completed exclusion and its limits. The [checkpoint-0004 self-audit](audits/SELF_AUDIT_GATE_0004.md) retains the order-twelve work.')
p.write_text(s,encoding='utf-8')

p = base/'GOLOMB_VERIFICATION_SUPPLEMENT.md'
s = p.read_text(encoding='utf-8')
s = s.replace('R4-GATE-0004','R4-GATE-0005').replace('audits/checkpoint_0003_snapshot','audits/checkpoint_0004_snapshot')
s = s.replace('This continuation independently verified the existing order-twelve Golomb minimum.',
              'This continuation independently verified the existing order-thirteen Golomb minimum.')
s = s.replace('| Shorter-ruler exclusions at orders 13..28',
              '| Exact minimum at order 13 | Separate complete Boolean-array and UInt128-mask exclusions through span 105, with witness | G(13)=106 |\n| Shorter-ruler exclusions at orders 14..28')
s = s.replace('order-9/10/11/12 minima','order-9/10/11/12/13 minima')
s = s.replace('Exact minima through order 12 are locally established.', 'Exact minima through order 13 are locally established.')
s = s.replace('orders 13 through 28 remain unreplayed','orders 14 through 28 remain unreplayed')
s = s.replace('The next unclosed local minimum is order 13;', 'The next unclosed local minimum is order 14;')
s = s.replace('The original exact numerical statement at order 13 and the original no-shorter outcome at order 22 remain explicit source gaps.',
              'The original no-shorter outcome at order 22 remains an explicit source gap. The uninspected original numerical statement at order 13 is retained as a historical literature gap; its minimum is now independently proved locally.')
addition='''The [order-thirteen proof](audits/golomb_small/ORDER13_PROOF.md), [native source review](audits/golomb_small/NATIVE_ORDER13_CODE_REVIEW.md), and [independent addendum](audits/golomb_small/agent/order13/ORDER13_ADDENDUM.md) establish G(13)=106. Both complete searches exclude C(105,12)=1,951,641,934,005,400 raw normalized tuples. They use only the already proved minima through order twelve, retain both reflections, and agree on every depth counter. The span-106 witness has 78 distinct positive pair differences. The new root manifest pins its contract file as well as source, proof, inputs, and outputs. This removes the need to use the external order-thirteen minimum, while leaving its original publication's exact numeric statement uninspected.\n\n'''
s = s.replace('## Source authentication\n',addition+'## Source authentication\n')
s = s.replace('Later exact reports and attaining witnesses do not supply a local exclusion.',
              'Later reports and attaining witnesses did not supply the missing local exclusion; the new independent order-thirteen computations now do.')
p.write_text(s,encoding='utf-8')
print('Prepared checkpoint-0005 report builder and supplement; no gate closure asserted.')
