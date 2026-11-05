from pathlib import Path
from pypdf import PdfReader
import hashlib, json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research_round4' / 'sources'
inputs = {
    'round3': ROOT / 'research_round3' / 'L-free Grid_Upper bound Research.pdf',
    'mammel_v1': ROOT / '2502.05162v1.pdf',
    'round2': ROOT / 'research_round2' / 'round2_report.pdf',
    'canakci_v1': ROOT / '2312.01159v1.pdf',
    'graham_reconstruction': ROOT / 'graham_solymosi_RkL_upper_bound_reconstruction.pdf',
}
manifest = {}
for key, path in inputs.items():
    if not path.is_file():
        manifest[key] = {'path': str(path), 'exists': False}
        continue
    reader = PdfReader(path)
    folder = OUT / key
    folder.mkdir(parents=True, exist_ok=True)
    texts = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text(extraction_mode='layout')
        (folder / f'page_{i:03}.txt').write_text(text, encoding='utf-8')
        texts.append(f'\n===== PDF PAGE {i} =====\n{text}\n')
    (OUT / f'{key}_complete.txt').write_text(''.join(texts), encoding='utf-8')
    manifest[key] = {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'pages': len(reader.pages), 'page_characters': [len(x) for x in texts]}
(OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print(json.dumps(manifest, indent=2))
