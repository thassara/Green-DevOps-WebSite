from zipfile import ZipFile
from pathlib import Path
from io import BytesIO
import struct, json
from lxml import etree

OUT=Path(__file__).parent
sources={'proposal':Path(r'C:\Users\MADUSHA\Downloads\GreenDevOps (ProposalP).pptx.pptx'),'pp1':Path(r'C:\Users\MADUSHA\Downloads\GreenDevOpsPP1.pptx')}
for key,path in sources.items():
    records=[]
    with ZipFile(path) as z:
        for n in z.namelist():
            if '/embeddings/' not in n:continue
            blob=z.read(n)
            # These compound file containers contain an Office Open XML Package stream.
            # Find the zip then follow central-directory lengths to strip trailing OLE data.
            start=blob.find(b'PK\x03\x04'); end=blob.find(b'PK\x05\x06',start)
            if start<0 or end<0:raise ValueError(n)
            data=blob[start:end+22]
            try:
                with ZipFile(BytesIO(data)) as x:
                    ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                    strings=[''.join(si.xpath('.//m:t/text()',namespaces=ns)) for si in etree.fromstring(x.read('xl/sharedStrings.xml')).xpath('.//m:si',namespaces=ns)]
                    rows=[]
                    for row in etree.fromstring(x.read('xl/worksheets/sheet1.xml')).xpath('.//m:row',namespaces=ns):
                        cells=[]
                        for c in row:
                            vals=c.xpath('./m:v/text()',namespaces=ns)
                            val=vals[0] if vals else ''
                            if c.get('t')=='s':val=strings[int(val)]
                            cells.append(c.get('r','')+': '+val)
                        rows.append(' | '.join(cells))
                    rec=n+'\n'+'\n'.join(rows);records.append(rec);print(key,rec)
            except Exception as ex:
                print(key,n,repr(ex))
    (OUT/key/'embedded-tables.txt').write_text('\n\n'.join(records),encoding='utf-8')
