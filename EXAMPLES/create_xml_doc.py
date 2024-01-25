import lxml.etree as ET

data = [
    ['123', 'Elm', 'St'],
    ['456', 'Shark', 'Way'],
    ['9283', 'Wombat', 'Parkway'],
]

root = ET.Element('streets')

for number, name, kind in data:
    s = ET.SubElement(root, 'street', kind=kind)
    ET.SubElement(s, 'number').text = number
    ET.SubElement(s, 'name').text = name

print(ET.tostring(root, pretty_print=True).decode())
