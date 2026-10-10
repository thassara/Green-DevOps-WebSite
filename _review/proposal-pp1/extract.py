from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from PIL import Image, ImageOps, ImageDraw
import json, re

OUT=Path(__file__).parent
NS={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
SOURCES={'proposal':Path(r'C:\Users\MADUSHA\Downloads\GreenDevOps (ProposalP).pptx.pptx'),'pp1':Path(r'C:\Users\MADUSHA\Downloads\GreenDevOpsPP1.pptx')}
for key,source in SOURCES.items():
    dest=OUT/key
    (dest/'media').mkdir(parents=True,exist_ok=True)
    data={'source':str(source),'size':source.stat().st_size,'slides':[],'media':[]}
    texts=[]
    with ZipFile(source) as z:
        core=z.read('docProps/core.xml').decode('utf-8') if 'docProps/core.xml' in z.namelist() else ''
        (dest/'core.xml').write_text(core,encoding='utf-8')
        slides=sorted([x for x in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',x)],key=lambda s:int(re.search(r'slide(\d+)',s).group(1)))
        for name in slides:
            num=int(re.search(r'slide(\d+)',name).group(1)); root=etree.fromstring(z.read(name))
            paragraphs=[''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in root.xpath('.//a:p',namespaces=NS)]
            paragraphs=[p for p in paragraphs if p.strip()]
            relname=f'ppt/slides/_rels/slide{num}.xml.rels'
            relations={}
            if relname in z.namelist():
                relroot=etree.fromstring(z.read(relname))
                relations={e.attrib['Id']:{'target':e.attrib['Target'],'type':e.attrib['Type']} for e in relroot}
            media=[v for v in relations.values() if any(t in v['type'] for t in ['/image','/video','/audio','/media','/oleObject'])]
            notes=[]
            for rel in relations.values():
                if '/notesSlide' in rel['type']:
                    n='ppt/'+rel['target'].replace('../','')
                    if n in z.namelist():
                        nr=etree.fromstring(z.read(n)); notes=[''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in nr.xpath('.//a:p',namespaces=NS)]
            sl={'number':num,'paragraphs':paragraphs,'media':media,'notes':notes}
            data['slides'].append(sl)
            texts.append(f'=== SLIDE {num} ===\n'+'\n'.join(paragraphs)+'\nMEDIA: '+json.dumps(media)+'\nNOTES: '+'\n'.join(notes))
        for info in z.infolist():
            if not info.filename.startswith('ppt/media/') or info.is_dir():continue
            md={'name':info.filename,'bytes':info.file_size,'compressed_bytes':info.compress_size}
            if Path(info.filename).suffix.lower() in ['.png','.jpg','.jpeg','.gif','.bmp','.tif','.tiff','.emf','.wmf','.svg']:
                p=dest/'media'/Path(info.filename).name;p.write_bytes(z.read(info.filename))
                try:
                    with Image.open(p) as im:md['dimensions']=im.size;md['mode']=im.mode
                except Exception as ex:md['image_error']=str(ex)
            data['media'].append(md)
    (dest/'text.txt').write_text('\n\n'.join(texts),encoding='utf-8')
    (dest/'inventory.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    useful=[m for m in data['media'] if 'dimensions' in m and m['dimensions'][0]>300 and m['dimensions'][1]>160]
    for start in range(0,len(useful),12):
        batch=useful[start:start+12];sheet=Image.new('RGB',(1200,320*((len(batch)+2)//3)),(232,235,231));d=ImageDraw.Draw(sheet)
        for ix,m in enumerate(batch):
            im=Image.open(dest/'media'/Path(m['name']).name).convert('RGB');im.thumbnail((390,275))
            x=(ix%3)*400+(400-im.width)//2;y=(ix//3)*320
            sheet.paste(im,(x,y+30));d.text(((ix%3)*400+8,y+7),f"{Path(m['name']).name} {m['dimensions']} {m['bytes']//1024}KB",fill='black')
        sheet.save(dest/f'contact-{start//12+1}.jpg',quality=88)
    print(key,len(data['slides']),'slides',len(data['media']),'media', 'non-image:',[m for m in data['media'] if 'dimensions' not in m])
