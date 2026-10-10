from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from PIL import Image, ImageOps, ImageDraw
import json

src=Path(r'C:\Users\MADUSHA\Downloads\GreenDevOps_Journal_Revised_Phase1 (1).docx')
out=Path(r'D:\4Y2S\Repo\web2\_review\journal'); out.mkdir(parents=True,exist_ok=True)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def texts(el):
    return ''.join(el.xpath('.//w:t/text() | .//m:t/text()',namespaces=ns))
lines=[]; index=[]
with ZipFile(src) as z:
    root=etree.fromstring(z.read('word/document.xml'))
    body=root.find('w:body',ns)
    for i, el in enumerate(body):
        tag=etree.QName(el).localname
        if tag=='p':
            t=texts(el)
            st=el.xpath('./w:pPr/w:pStyle/@w:val',namespaces=ns)
            rid=el.xpath('.//a:blip/@r:embed',namespaces=ns)
            line=f'[{i:03d} P {st[0] if st else "Normal"}] {t}'
            if rid: line += ' [IMAGES '+', '.join(rid)+']'
            lines.append(line)
            index.append({'block':i,'tag':tag,'text':t,'style':st,'image_rids':rid})
        elif tag=='tbl':
            lines.append(f'[{i:03d} TABLE]')
            rows=[]
            for row in el.findall('w:tr',ns):
                cells=[texts(c) for c in row.findall('w:tc',ns)]
                rows.append(cells); lines.append(' | '.join(cells))
            index.append({'block':i,'tag':tag,'rows':rows})
    rels=etree.fromstring(z.read('word/_rels/document.xml.rels'))
    relmap={e.get('Id'):e.get('Target') for e in rels}
    for name in z.namelist():
        if name.startswith('word/media/'):
            p=out/Path(name).name;p.write_bytes(z.read(name))
    extras=[]
    for name in z.namelist():
        if any(k in name for k in ('footnote','endnote','comment','header','footer')) and name.endswith('.xml'):
            try: extras.append(f'{name}\n{texts(etree.fromstring(z.read(name)))}')
            except: pass
    lines.extend(['\nEXTRA PARTS']+extras)
    (out/'relations.json').write_text(json.dumps(relmap,indent=2),encoding='utf-8')
    (out/'package.json').write_text(json.dumps(z.namelist(),indent=2),encoding='utf-8')
(out/'ordered_text.txt').write_text('\n'.join(lines),encoding='utf-8')
(out/'blocks.json').write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding='utf-8')
imgs=[]
for p in sorted(out.glob('image*')):
    try:
        im=Image.open(p).convert('RGB'); imgs.append((p,im))
    except: pass
cols=3;tw=600;th=450
sheet=Image.new('RGB',(cols*tw,((len(imgs)+cols-1)//cols)*th),'#eeeeee'); draw=ImageDraw.Draw(sheet)
for j,(p,im) in enumerate(imgs):
    draw.text(((j%cols)*tw+10,(j//cols)*th+5),f'{p.name} {im.width}x{im.height}',fill='black')
    im.thumbnail((tw-20,th-35));sheet.paste(im,((j%cols)*tw+10,(j//cols)*th+30))
sheet.save(out/'contact-sheet.jpg')
print(f'Blocks: {len(index)}; figures: {len(imgs)}; words: {len(" ".join(lines).split())}')
