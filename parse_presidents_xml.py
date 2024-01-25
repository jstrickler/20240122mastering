import lxml.etree as et

doc = et.parse('DATA/presidents.xml')

print(f"{doc = }")

root = doc.getroot()
print(f"{root = }")

#  E.find()  E.findall()  E.findtext()

# xpath  patterns for XML

for president in doc.findall('.//president'):
    last_name = president.findtext('.//name/last')
    party = president.findtext('.//party')
    print(f"{last_name:15} {party}")
    


