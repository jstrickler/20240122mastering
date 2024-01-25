
import re

DATA_WIDTH = 30

rx_record = re.compile(
    r'<OBJECT_ID>(.*?)</OBJECT_ID>\s*<OBJECT_SEQ_NO>(.*?)</OBJECT_SEQ_NO>\s*<OBJECT_DATA>(.*?)</OBJECT_DATA>',
    re.I | re.S)

rx_obj_id = re.compile(r'<OBJECT_ID>(.*?)</OBJECT_ID>', re.I)

info = {}

with open("../DATA/rxml_data.xml") as xml_in:
    alldata = xml_in.read()

    # loop through each record
    for rec in rx_record.finditer(alldata):
        info[rec.group(1)] = [rec.group(2), rec.group(3)]

    xml_in.seek(0)  # rewind file for 2nd pass

    # find line numbers for each object ID
    for num, line in enumerate(xml_in):
        m = rx_obj_id.search(line)
        if m:
            id = m.group(1)
            info[id].append(num)

# build a header string
header = f"OBJ ID  SEQ  {'DATA':{DATA_WIDTH}s} PG"
print('-' * (len(header) + 1))
print(header)
print('-' * (len(header) + 1))

# loop through info; print key, elements of value
# (i.e., OBJID, SEQ, CONTENT, LINE_NUM)
for k, v in sorted(info.items(), key=lambda e: int(e[1][2])):
    print(f"{k:>6s}   {v[0]:3s} {v[1][:20]:{DATA_WIDTH}s} {v[2]:03d}")
