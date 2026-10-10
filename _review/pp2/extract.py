from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json, posixpath, io
from PIL import Image, ImageOps, ImageDraw

src=Path(r'C:\Users\MADUSHA\Downloads\Green DevOps PP2.pptx.pptx')
out=Path(__file__).parent
(out/'media').mkdir(exist_ok=True,parents=True)
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
parts=[]; inventory=[]; slides=[]
with ZipFile(src) as z:
    pres=E.fromstring(z.read('ppt/presentation.xml'))
    rels={r.get('Id'):r.get('Target') for r in E.fromstring(z.read('ppt/_rels/presentation.xml.rels'))}
    for i,elem in enumerate(pres.findall('p:sldIdLst/p:sldId',ns),1):
        name=posixpath.normpath('ppt/'+rels[elem.get('{'+ns['r']+'}id')])
        root=E.fromstring(z.read(name))
        relname=posixpath.dirname(name)+'/_rels/'+posixpath.basename(name)+'.rels'
        srels={r.get('Id'):r.get('Target') for r in E.fromstring(z.read(relname))} if relname in z.namelist() else {}
        text=[]
        for paragraph in root.findall('.//a:p',ns):
            txt=''.join(paragraph.itertext()) if False else ''.join(paragraph.xpath('.//a:t/text()',namespaces=ns))
            if txt.strip(): text.append(txt)
        medias=[]
        for target in srels.values():
            target=posixpath.normpath(posixpath.dirname(name)+'/'+target)
            if '/media/' in target: medias.append(target)
        notes=[]
        for rid,target in srels.items():
            if 'notesSlides' in target:
                nroot=E.fromstring(z.read(posixpath.normpath(posixpath.dirname(name)+'/'+target)))
                notes=nroot.xpath('.//a:t/text()',namespaces=ns)
        parts.append(f'=== SLIDE {i} ({name}) ===\n'+'\n'.join(text)+'\nMEDIA: '+', '.join(medias)+'\nNOTES: '+'\n'.join(notes)+'\n')
        slides.append({'slide':i,'part':name,'text':text,'media':medias,'notes':notes})
    for item in z.infolist():
        if item.filename.startswith('ppt/media/'):
            data=z.read(item.filename); dest=out/'media'/Path(item.filename).name; dest.write_bytes(data)
            row={'part':item.filename,'bytes':len(data),'compressed_bytes':item.compress_size,'slides':[s['slide'] for s in slides if item.filename in s['media']]}
            try:
                im=Image.open(io.BytesIO(data)); row.update({'width':im.width,'height':im.height,'format':im.format})
            except Exception: pass
            inventory.append(row)
(out/'slides.txt').write_text('\n'.join(parts),encoding='utf-8')
(out/'slides.json').write_text(json.dumps(slides,indent=2),encoding='utf-8')
(out/'media-inventory.json').write_text(json.dumps(inventory,indent=2),encoding='utf-8')
images=[i for i in inventory if 'width' in i]
for n in range(0,len(images),20):
    batch=images[n:n+20]; sheet=Image.new('RGB',(1600,1100),'#e5e7eb'); d=ImageDraw.Draw(sheet)
    for j,row in enumerate(batch):
        im=Image.open(out/'media'/Path(row['part']).name).convert('RGB'); im.thumbnail((390,185))
        x=(j%4)*400+(400-im.width)//2; y=(j//4)*220
        sheet.paste(im,(x,y)); d.text(((j%4)*400+6,y+188),f"{Path(row['part']).name} | slides {row['slides']}",fill='black')
        d.text(((j%4)*400+6,y+203),f"{row['width']} x {row['height']} | {row['bytes']:,} B",fill='black')
    sheet.save(out/f'media-contact-{n//20+1}.jpg',quality=90)
print(json.dumps({'slides':len(slides),'media_count':len(inventory),'source_bytes':src.stat().st_size,'media_bytes':sum(i['bytes'] for i in inventory),'largest_media':sorted(inventory,key=lambda r:r['bytes'],reverse=True)[:8]},indent=2))
