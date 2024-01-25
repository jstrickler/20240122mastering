import lxml.etree as et

root_tag = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip().split(':')
        knight = et.SubElement(root_tag, "knight", title=title)
        et.SubElement(knight, "name").text = name
        c = et.SubElement(knight, 'color')
        c.text = color
        et.SubElement(knight, "quest").text = quest
        et.SubElement(knight, 'comment').text = comment

print(et.tostring(root_tag, pretty_print=True).decode())
