from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
out=Path(__file__).parent
with ZipFile(r'C:\Users\MADUSHA\Downloads\Green DevOps PP2.pptx.pptx') as z:
 print('\n'.join(f'{x.file_size:,} {x.filename}' for x in sorted(z.infolist(), key=lambda x:x.file_size,reverse=True)[:25]))
 for name in z.namelist():
  if name.startswith('ppt/embeddings/'):
   data=z.read(name); (out/Path(name).name).write_bytes(data); print(name,len(data),data[:50])
  if name.endswith('.rels'):
   root=E.fromstring(z.read(name))
   for r in root:
    if r.get('TargetMode')=='External': print('EXTERNAL',name,r.attrib)
 try:
  import olefile
  for src in out.glob('*.bin'):
   if olefile.isOleFile(src):
    with olefile.OleFileIO(src) as o:
     print(src,o.listdir())
     for part in o.listdir():
      if any(s in '/'.join(part).lower() for s in ['package','contents','workbook','book']):
       data=o.openstream(part).read(); path=out/(src.stem+'_'+('_'.join(part)).replace('\x01','')+'.data'); path.write_bytes(data); print(path,data[:50])
 except ImportError: print('olefile not installed')
