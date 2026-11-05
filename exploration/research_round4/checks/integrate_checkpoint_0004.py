"""Update current prose/builders after the reviewed order-twelve exclusions."""
from pathlib import Path

base = Path(__file__).resolve().parents[1]
builder = base / 'checks/build_verification_report.py'
text = builder.read_text(encoding='utf-8')
text = text.replace('R4-GATE-0003', 'R4-GATE-0004')
text = text.replace('audits/checkpoint_0002_snapshot', 'audits/checkpoint_0003_snapshot')
text = text.replace('orders 6 through 11 have two', 'orders 6 through 12 have two')
text = text.replace('orders 12 through 28', 'orders 13 through 28')
text = text.replace('orders 1 through 11', 'orders 1 through 12')
text = text.replace("'audits/golomb_small/agent/ORDER11_COMPLETION_ADDENDUM.md']",
                    "'audits/golomb_small/agent/ORDER11_COMPLETION_ADDENDUM.md','audits/golomb_small/ORDER12_PROOF.md','audits/golomb_small/agent/order12/ORDER12_ADDENDUM.md','audits/golomb_small/ORDER12_PROOF_REVIEW.md']")
old = 'The completed order-10 and order-11 exclusions are recorded in the [new proof](audits/golomb_small/ORDERS10_11_PROOF.md).'
new = 'The order-10 and order-11 exclusions are recorded in their [proof](audits/golomb_small/ORDERS10_11_PROOF.md). The [order-twelve proof](audits/golomb_small/ORDER12_PROOF.md) now records two independent complete exclusions through span 84 and a checked span-85 witness, proving G(12)=85. The implementations agree on every depth counter; earlier incomplete or failed attempts remain explicitly non-evidentiary for the lower bound.'
if old not in text:
    raise RuntimeError('Expected prior order10/11 prose not found')
text = text.replace(old, new)
text = text.replace('[checkpoint-0003 self-audit](audits/SELF_AUDIT_GATE_0003.md)',
                    '[checkpoint-0004 self-audit](audits/SELF_AUDIT_GATE_0004.md)')
text = text.replace('records the latest completed exclusions, source progress, and limits.',
                    'records the latest completed exclusion and its limits. The [checkpoint-0003 self-audit](audits/SELF_AUDIT_GATE_0003.md) retains the earlier source progress.')
builder.write_text(text, encoding='utf-8')

supplement = base / 'GOLOMB_VERIFICATION_SUPPLEMENT.md'
text = supplement.read_text(encoding='utf-8')
text = text.replace('R4-GATE-0003', 'R4-GATE-0004')
text = text.replace('This continuation independently verified two more existing Golomb entries and narrowed an original-source gap.',
                    'This continuation independently verified the existing order-twelve Golomb minimum.')
text = text.replace('audits/checkpoint_0002_snapshot', 'audits/checkpoint_0003_snapshot')
text = text.replace('| Shorter-ruler exclusions at orders 12..28',
                    '| Exact minimum at order 12 | Separate complete Boolean-array and integer-bitset exclusions through span 84, with witness | G(12)=85 |\n| Shorter-ruler exclusions at orders 13..28')
text = text.replace('Local exclusions now remove the need for external order-9/10/11 minima.',
                    'Local exclusions now remove the need for external order-9/10/11/12 minima.')
text = text.replace('The new [order-22 follow-up]', 'The checkpoint-0003 [order-22 follow-up]')
text = text.replace('Exact minima through order 11 are locally established.', 'Exact minima through order 12 are locally established.')
text = text.replace('orders 12 through 28 remain unreplayed', 'orders 13 through 28 remain unreplayed')
text = text.replace('This goal turn made mathematical and source-verification progress.', 'This goal turn made mathematical verification progress.')
text = text.replace('The next unclosed local minimum is order 12;', 'The next unclosed local minimum is order 13;')
insertion = '''The [order-twelve proof](audits/golomb_small/ORDER12_PROOF.md), [independent addendum](audits/golomb_small/agent/order12/ORDER12_ADDENDUM.md), and [proof review](audits/golomb_small/ORDER12_PROOF_REVIEW.md) establish the next existing equality G(12)=85. The complete searches exclude all C(84,11)=18,574,174,153,080 raw normalized tuples, using only already proved smaller-order minima and sound unused-gap pruning. The root Boolean-array implementation and separate Python integer-bitset implementation agree on all eight reason fields at every depth. A further independently implemented UInt128 replay corroborates the result. The span-85 witness has all 66 distinct pair differences.\n\nThe earlier root and independent tail-only attempts remain UNDECIDED. The root Python gap attempt also remains incomplete; its reported wall time exceeded its declared cap for an unestablished reason. The independent first compiled attempt failed on a checked low-half bit conversion and yielded no result; a separate corrected driver completed. Those failures are preserved and provide no lower-bound premise. The native root manifest does not hash its separate contract file; later sealing pins current bytes only. These explicit limitations do not alter the completed independent Python exclusion.\n\n'''
text = text.replace('## Source authentication\n', insertion + '## Source authentication\n')
supplement.write_text(text, encoding='utf-8')
print('Updated report builder and Golomb supplement for checkpoint 0004; builders still require final evidence files.')
