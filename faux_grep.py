import re
import fileinput
from argparse import ArgumentParser

description = """
Faux Grep

Searches one or more files for a search term, and prints
lines containing the search term.
"""

parser = ArgumentParser(description=description)
parser.add_argument("-f", dest="show_file_names", action="store_true",
                    help="Show file names") 
parser.add_argument("-i", dest="ignore_case", help="Ignore case", action="store_true")

parser.add_argument("search_term", help="Search term")

parser.add_argument("file_names", nargs="*", help="files to search")

args = parser.parse_args()   # parse sys.argv

re_flag = re.I if args.ignore_case else 0

rx_term = re.compile(args.search_term, re_flag)

for line in fileinput.input(args.file_names):
    if rx_term.search(line):
        if args.show_file_names:
            print(fileinput.filename(), end=" ")
        print(line.rstrip())
