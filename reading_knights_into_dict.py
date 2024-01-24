#   "//myshareddrive/Users/jstrick/Desktop/pybasics/DATA/knights.txt"
from pprint import pprint

file_path = "DATA/knights.txt"


knight_info = {}

with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print()
print(f"{knight_info['Lancelot'] = }\n")
print(f"{knight_info['Lancelot'][1] = }\n")

for knight, data in knight_info.items():
    print(f"{data[0]:4} {knight:10} {data[2]}")
print()
