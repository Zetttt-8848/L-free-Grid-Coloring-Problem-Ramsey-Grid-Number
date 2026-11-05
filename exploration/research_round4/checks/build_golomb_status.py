"""Record per-entry gate obligations without accepting external premises."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'research_round4'
data = json.loads((BASE / 'audits/golomb_sources/run_all_witnesses_0001/results.json').read_text(encoding='utf-8'))
if [r['order'] for r in data['rows']] != list(range(1, 29)) or any(r['existence_verdict'] != 'PASS' for r in data['rows']):
    raise RuntimeError('All-table existence evidence is incomplete')
order9 = json.loads((BASE / 'audits/golomb_small/root/run_order9_0001/results.json').read_text(encoding='utf-8'))
order9_target = order9['target']
if order9['overall_verdict'] != 'PASS' or (order9_target['order'], order9_target['maximum_span'],
        order9_target['visited'], order9_target['rejected'], order9_target['accepted']) != (9,43,145008513,145008513,0):
    raise RuntimeError('The order-nine local proof record is incomplete or inconsistent')
for m, span, universe, root_run, agent_run in [
    (10, 54, 5317936260, 'run_next10_0001', 'run_order10_target_0001'),
    (11, 71, 461738052776, 'run_next11_0002', 'run_order11_target_0002'),
]:
    checked = json.loads((BASE / f'audits/golomb_small/root/{root_run}/results.json').read_text(encoding='utf-8'))
    target = checked['target']
    other = json.loads((BASE / f'audits/golomb_small/agent/{agent_run}/results.json').read_text(encoding='utf-8'))['cases'][0]
    if checked['overall_verdict'] != 'PASS' or target['complete'] is not True or (
        target['order'], target['maximum_span'], target['raw_universe'], target['rejected_leaf_mass'],
        target['accepted'], target['coverage_difference']) != (m, span, universe, universe, 0, 0):
        raise RuntimeError('Incomplete root order10/11 exclusion')
    if other['complete'] is not True or (other['order'], other['maximum_span'],
        other['raw_universe_size'], other['pruned_raw_leaf_mass'], other['valid_leaf_count']) != (m, span, universe, universe, 0):
        raise RuntimeError('Incomplete independent order10/11 exclusion')
root12 = json.loads((BASE / 'audits/golomb_small/root/native_order12/run_0001/results.json').read_text(encoding='utf-8'))
agent12 = json.loads((BASE / 'audits/golomb_small/agent/order12/run_gap_target_0001/results.json').read_text(encoding='utf-8'))
cross12 = json.loads((BASE / 'audits/golomb_small/root/order12_record_validation.json').read_text(encoding='utf-8'))
for container, target in [(root12, root12['target']), (agent12, agent12['cases'][0])]:
    if container['overall_verdict'] != 'PASS' or target['complete'] is not True or (
        target['order'], target['maximum_span'], target['raw_universe'], target['accounted_leaf_mass'],
        target['accepted'], target['coverage_difference']) != (12, 84, 18574174153080, 18574174153080, 0, 0):
        raise RuntimeError('Incomplete order12 exclusion')
if cross12['independent_full_target_comparison']['verdict'] != 'PASS':
    raise RuntimeError('Missing order12 full-depth comparison')
root13 = json.loads((BASE / 'audits/golomb_small/root/native_order13/run_0001/results.json').read_text(encoding='utf-8'))
agent13 = json.loads((BASE / 'audits/golomb_small/agent/order13/run_compiled_uint128_0001/results.json').read_text(encoding='utf-8'))
cross13 = json.loads((BASE / 'audits/golomb_small/root/native_order13/record_validation.json').read_text(encoding='utf-8'))
for container in [root13, agent13]:
    target = container['target']
    if container['overall_verdict'] != 'PASS' or target['complete'] is not True or (
        target['order'], target['maximum_span'], target['raw_universe'], target['accounted_leaf_mass'],
        target['accepted'], target['coverage_difference']) != (13, 105, 1951641934005400, 1951641934005400, 0, 0):
        raise RuntimeError('Incomplete order13 exclusion')
if cross13['independent_full_target_comparison']['verdict'] != 'PASS':
    raise RuntimeError('Missing order13 full-depth comparison')
rows = []
for row in data['rows']:
    m = row['order']
    if m <= 5:
        lower = 'independently_proved_by_counting_and_parity'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_sources/EXISTENCE_AND_SMALL_ORDERS.md', 'audits/golomb_sources/WITNESS_REVIEW.md']
    elif m <= 8:
        lower = 'independently_proved_by_complete_enumeration'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_small/PROOF.md', 'audits/golomb_small/agent/AUDIT.md']
    elif m == 9:
        lower = 'independently_proved_by_complete_enumeration'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_small/ORDER9_PROOF.md', 'audits/golomb_small/agent/ORDER9_ADDENDUM.md', 'audits/golomb_small/root/run_order9_0001/manifest.json']
    elif m <= 11:
        lower = 'independently_proved_by_complete_enumeration'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_small/ORDERS10_11_PROOF.md', 'audits/golomb_small/agent/ORDERS10_11_ADDENDUM.md']
        if m == 11:
            evidence.append('audits/golomb_small/agent/ORDER11_COMPLETION_ADDENDUM.md')
    elif m == 12:
        lower = 'independently_proved_by_complete_enumeration'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_small/ORDER12_PROOF.md',
                    'audits/golomb_small/ORDER12_PROOF_REVIEW.md',
                    'audits/golomb_small/NATIVE_ORDER12_CODE_REVIEW.md',
                    'audits/golomb_small/agent/order12/ORDER12_ADDENDUM.md',
                    'audits/golomb_small/root/order12_record_validation.json']
    elif m == 13:
        lower = 'independently_proved_by_complete_enumeration'
        source = 'external_result_not_required'
        evidence = ['audits/golomb_small/ORDER13_PROOF.md',
                    'audits/golomb_small/NATIVE_ORDER13_CODE_REVIEW.md',
                    'audits/golomb_small/agent/order13/ORDER13_ADDENDUM.md',
                    'audits/golomb_small/root/native_order13/record_validation.json']
    else:
        lower = 'not_independently_replayed_or_proved'
        if m in (14, 15, 16, 19):
            source = 'primary_publication_exact_numeric_result'
            evidence = ['audits/golomb_sources/ORDERS_14_23_PRIMARY.md']
        elif m in (17, 18):
            source = 'primary_document_exact_numeric_result'
            evidence = ['audits/golomb_sources/RANKIN_1993_FOLLOWUP.md']
        elif m == 20:
            source = 'contemporary_published_exact_optimality_report_not_organizer_authored'
            evidence = ['audits/golomb_sources/ORDERS_20_23_FOLLOWUP.md', 'audits/golomb_sources/ORDERS_20_23_INDEPENDENT_REVIEW.md']
        elif m == 21:
            source = 'original_completion_report_with_cross_document_numeric_identification'
            evidence = ['audits/golomb_sources/ORDERS_20_23_FOLLOWUP.md', 'audits/golomb_sources/ORDERS_20_23_INDEPENDENT_REVIEW.md']
        elif m == 22:
            source = 'original_numeric_configuration_and_terminal_workload_status_exact_outcome_unstated'
            evidence = ['audits/golomb_sources/O22_TERMINAL_FOLLOWUP.md', 'audits/golomb_sources/O22_TERMINAL_INDEPENDENT_REVIEW.md']
        elif m == 23:
            source = 'primary_organizer_exact_numeric_result'
            evidence = ['audits/golomb_sources/ORDERS_20_23_FOLLOWUP.md', 'audits/golomb_sources/ORDERS_20_23_INDEPENDENT_REVIEW.md']
        elif m <= 25:
            source = 'primary_organizer_exact_numeric_result'
            evidence = ['audits/golomb_sources/source_audit.md', 'audits/golomb_sources/EXISTENCE_AND_SMALL_ORDERS.md']
        else:
            source = 'primary_organizer_exact_numeric_result'
            evidence = ['audits/golomb_sources/orders26_28_followup.md']
    for rel in evidence:
        if not (BASE / rel).is_file():
            raise RuntimeError(f'Missing evidence: {rel}')
    rows.append({'order': m, 'printed_G': row['length'], 'printed_H': row['length'] + 1,
                 'attaining_witness': 'independently_verified',
                 'lower_bound_status': lower, 'source_authentication_status': source,
                 'exact_equality_locally_established': m <= 13,
                 'evidence': evidence})
result = {
    'checkpoint': 'R4-GATE-0005', 'gate_passed': False,
    'sentinel': {'H_0': 0, 'status': 'algorithm_sentinel_not_an_optimality_claim'},
    'witness_orders_verified': list(range(1, 29)),
    'exact_equality_orders_locally_established': list(range(1, 14)),
    'lower_bound_orders_unreplayed': list(range(14, 29)),
    'current_original_source_followup_unresolved_or_composite': {
        '13': 'Historical source gap: original abstract omits the numeric length. The local order13 proof now establishes106 without this external minimum.',
        '20': 'Exact contemporary published report authenticated; original organizer statement not recovered.',
        '21': 'Original completion statement authenticated; numeric333 identification is a cross-document link.',
        '22': 'Original target356, job limit355, and same-project100%-complete workload are documented; the exact no-shorter outcome is not stated in the recovered original records.'
    },
    'source_classification_note': 'Original author reports, contemporary reportage, and cross-document identifications remain distinct. The earlier exact-primary-gap list is replaced by these explicit classifications; no external theorem has been accepted into the gate.',
    'external_input_acceptance': 'user_clarification_pending_no_reply_received',
    'rows': rows,
    'scope': 'Source authentication and an attaining witness do not equal independent proof of a minimum. No new grid research.'
}
(BASE / 'audits/golomb_sources/golomb_table_status.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print('Recorded all 28 witness halves, exact local minima 1..13, and remaining lower-bound/source obligations.')
