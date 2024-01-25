import lxml.etree as et

with open('../DATA/words.txt') as words_in:
    word_list = words_in.read().splitlines()

MAX_DEPTH = 20000

root = et.Element(word_list.pop(0))

current_tag = root

for _ in range(MAX_DEPTH - 1):
    current_tag = et.SubElement(current_tag, word_list.pop(0))

# print(et.tostring(root, pretty_print=True).decode())
print(current_tag.tag)
x = root.find(f'.//{current_tag.tag}')
print(f"{x = }")
print(f"{x.tag = }")


