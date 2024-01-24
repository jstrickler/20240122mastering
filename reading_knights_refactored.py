#   "//myshareddrive/Users/jstrick/Desktop/pybasics/DATA/knights.txt"
from pprint import pprint

FILE_PATH = "DATA/KNIGHTS.txt"

def main():
    data = read_data()
    pretty_print(data)
    print(get_info(data, "Bedevere"))
    print()
    print_titles(data)


def read_data():
    info = {}

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            info[name] = title, color, quest, comment
    return info

def pretty_print(knight_info):
    pprint(knight_info)
    print()

def get_info(knight_info, knight_name):
    return knight_info[knight_name]

def print_titles(knight_info):
    for knight, data in knight_info.items():
        print(f"{data[0]:4} {knight:10}")

main()