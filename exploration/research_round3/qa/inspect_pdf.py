"""Make final-page contact sheets and record structural PDF checks."""
from pathlib import Path
from hashlib import sha256
import json
import re
from PIL import Image, ImageDraw
from pypdf import PdfReader

R3 = Path(__file__).resolve().parent.parent
pdf = R3 / 'round3_report.pdf'
reader = PdfReader(pdf)
pages = [p.extract_text() or '' for p in reader.pages]
text = '\n'.join(pages)
assert all(p.strip() for p in pages)
assert 'Pending final review' not in text and 'Review draft' not in text
assert '551211731377452489346057152' in text
assert '21' in pages[0] and '465' in pages[0]
tex = (R3 / 'round3_report.tex').read_text()
for name in ['report_decisions.tex', 'report_general.tex', 'report_audits.tex']:
    tex += (R3 / name).read_text()
assert len(re.findall(r'\\section\{', tex)) == 10
log = (R3 / 'round3_report.log').read_text(errors='replace')
assert not re.search(r'Overfull|undefined|LaTeX Warning|Package .* Warning', log)

preview = R3 / 'qa/preview'
images = sorted(preview.glob('final-*.png'), key=lambda p: int(p.stem.split('-')[-1]))
assert len(images) == len(pages), (len(images), len(pages))
sheets = []
for start in range(0, len(images), 6):
    chunk = images[start:start+6]
    width, height = Image.open(chunk[0]).size
    sheet = Image.new('RGB', (3*(width+12), 2*(height+36)), '#d0d0d0')
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(chunk):
        x, y = (i%3)*(width+12), (i//3)*(height+36)
        draw.text((x+12, y+6), f'Page {start+i+1}', fill='black')
        with Image.open(path) as im:
            sheet.paste(im.convert('RGB'), (x+6, y+26))
    target = preview / f'contact-{start//6+1}.png'
    sheet.save(target)
    sheets.append(target.relative_to(R3).as_posix())
out = {'status': 'PASS', 'pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
       'pages': len(pages), 'main_sections': 10, 'all_pages_nonempty': True,
       'tex_log_clean': True, 'review_placeholders_absent': True,
       'contact_sheets': sheets,
       'visual_inspection_status': 'manual review recorded separately'}
(R3 / 'qa/PDF_STRUCTURE_CHECK.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
