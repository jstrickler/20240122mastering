#   "//myshareddrive/Users/jstrick/Desktop/pybasics/DATA/knights.txt"
file_path = "DATA/knights.txt"

with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        print(title, name)