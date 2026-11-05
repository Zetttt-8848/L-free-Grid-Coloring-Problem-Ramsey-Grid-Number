"""Mechanical PDF preflight and contact sheet; final visual review is separate."""
from pathlib import Path
from hashlib import sha256
import json
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT / 'round2_report.pdf'
log = (ROOT / 'round2_report.log').read_text(errors='replace')
for forbidden in ('Overfull', 'undefined references', 'undefined citations', 'Rerun to get cross-references right'):
    assert forbidden not in log, forbidden
reader = PdfReader(pdf)
assert 17 <= len(reader.pages) <= 19
lengths = [len(page.extract_text() or '') for page in reader.pages]
assert min(lengths) > 250
fulltext = '\n'.join(page.extract_text() or '' for page in reader.pages)
assert '??' not in fulltext
paths = sorted((ROOT / 'audits').glob('final_page-*.png'))
assert len(paths) == len(reader.pages)
cw, ch, cols = 352, 478, 4
sheet = Image.new('RGB', (cols*cw, ((len(paths)+cols-1)//cols)*ch), '#d8d8d8')
draw = ImageDraw.Draw(sheet)
for i, path in enumerate(paths):
    im = Image.open(path).convert('RGB')
    im.thumbnail((cw-16, ch-32))
    x, y = (i % cols)*cw, (i // cols)*ch
    sheet.paste(im, (x+(cw-im.width)//2, y+8))
    draw.text((x+12, y+ch-20), f'Page {i+1}', fill='black')
sheet.save(ROOT / 'audits/final_contact.png')
result = {'mechanical_status': 'PASS', 'pages': len(reader.pages),
          'pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
          'page_extracted_character_counts': lengths,
          'overfull_lines': 0, 'unresolved_references': 0,
          'visual_review': 'Separate inspection of final_contact.png and the page renders is required.'}
(ROOT / 'audits/PDF_PREFLIGHT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
