"""Capture compilation evidence and trust boundaries for the current Lean sources."""
from pathlib import Path
import hashlib, json, platform, subprocess

root = Path(__file__).resolve().parents[2]
lean = root / 'research_round4/tools/lean-4.19.0-windows/bin/lean.exe'
out = root / 'research_round4/formal/compilation_gate_0001'
out.mkdir(parents=True, exist_ok=False)
version = subprocess.run([str(lean), '--version'], capture_output=True, text=True, check=True).stdout.strip()
records = []
for relative in ['research_round4/formal/geometry/Geometry.lean', 'research_round4/formal/small_cases/SmallCases.lean']:
    source = root / relative
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    proc = subprocess.run([str(lean), str(source)], cwd=root, capture_output=True, text=True, timeout=120)
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    assert before == after
    (out / (source.stem + '.stdout.txt')).write_text(proc.stdout, encoding='utf-8')
    (out / (source.stem + '.stderr.txt')).write_text(proc.stderr, encoding='utf-8')
    records.append({'source': relative, 'sha256': before, 'exit_code': proc.returncode,
                    'has_sorry_axiom': 'sorryAx' in proc.stdout,
                    'stdout': source.stem + '.stdout.txt', 'stderr': source.stem + '.stderr.txt'})
    assert proc.returncode == 0 and 'sorryAx' not in proc.stdout
result = {'checkpoint': 'R4-GATE-0001', 'lean_version': version,
          'lean_executable_sha256': hashlib.sha256(lean.read_bytes()).hexdigest(),
          'host': platform.platform(), 'records': records,
          'trust_boundary': 'Native-decide and bv_decide lemmas depend on Lean.ofReduceBool and trust the Lean compiler. All listed axioms are captured in stdout. No sorryAx is permitted.',
          'scope': 'Only named theorems in the two sources are formalized; the main general-k and four-color bound proofs remain written proofs with separate exact arithmetic.'}
(out / 'manifest.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
