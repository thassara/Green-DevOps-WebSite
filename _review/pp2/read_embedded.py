from pathlib import Path
import struct, io, json
from zipfile import ZipFile
from lxml import etree as E
out=Path(__file__).parent
results=[]
for src in out.glob('*.bin'):
 data=src.read_bytes(); sector=1<<struct.unpack_from('<H',data,30)[0]
 def sec(i): return data[(i+1)*sector:(i+2)*sector]
 fatids=[n for n in struct.unpack_from('<109I',data,76) if n<0xfffffffa]
 fat=[]
 for n in fatids: fat.extend(struct.unpack('<'+str(sector//4)+'I',sec(n)))
 def chain(start,table=fat,parts=None):
  ret=b''; seen=set()
  while start<0xfffffffa and start not in seen:
   seen.add(start); ret+=sec(start) if parts is None else parts[start*64:(start+1)*64]; start=table[start]
  return ret
 directory=chain(struct.unpack_from('<I',data,48)[0]); entries=[]
 for offset in range(0,len(directory),128):
  row=directory[offset:offset+128]; n=struct.unpack_from('<H',row,64)[0]
  if n: entries.append((row[:n-2].decode('utf-16le'),*struct.unpack_from('<IQ',row,116)))
 mini=chain(entries[0][1])[:entries[0][2]]
 minifatdata=chain(struct.unpack_from('<I',data,60)[0]); minifat=struct.unpack('<'+str(len(minifatdata)//4)+'I',minifatdata) if minifatdata else []
 package=next(e for e in entries if e[0]=='Package'); pkg=(chain(package[1],minifat,mini) if package[2]<4096 else chain(package[1]))[:package[2]]
 dest=out/(src.stem+'.xlsx'); dest.write_bytes(pkg)
 z=ZipFile(io.BytesIO(pkg)); ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 strings=[]
 if 'xl/sharedStrings.xml' in z.namelist():
  root=E.fromstring(z.read('xl/sharedStrings.xml'))
  strings=[''.join(si.xpath('.//s:t/text()',namespaces=ns)) for si in root]
 sheets=[]
 for name in z.namelist():
  if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
   root=E.fromstring(z.read(name)); rows=[]
   for row in root.findall('.//s:row',ns):
    values=[]
    for cell in row:
     v=cell.find('s:v',ns); val=v.text if v is not None else ''.join(cell.xpath('.//s:t/text()',namespaces=ns))
     if cell.get('t')=='s': val=strings[int(val)]
     values.append(f"{cell.get('r')}: {val}")
    rows.append(' | '.join(values))
   sheets.append({'name':name,'rows':rows})
 results.append({'object':src.name,'sheets':sheets})
(out/'embedded-tables.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
