import csv
from collections import Counter
from itertools import groupby
import pandas as pd

# first approach:  using tools from standard library:
print('=' * 60)
print("Builtin tools")
print('=' * 60)

# for line count and distinct values in a column:
with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    line_count = 0   # for counting lines
    party_list = []  # list of all parties (not distinct)
    for csv_record in rdr: # loop over lines in CSV file
        line_count += 1
        party = csv_record[-1]  # get last column
        party_list.append(party)  # add party to party list

# a Counter is a specialized dictionary
party_counter = Counter(party_list)  # for counting distinct parties

print(f"presidents file has {line_count} lines")
for party, count in party_counter.items():  #loop over key/value pairs
    print(party, count)
print()
print('-' * 60)
# for groupby:
def by_party(president):
    return president[-1]

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    records = sorted(rdr, key=by_party) # sort by last field (party)
    g = groupby(records, key=by_party)
    for party, data in g:
        last_names = [d[2] for d in data]
        print(party, last_names)
        print()

print('=' * 60)
print("Pandas")
print('=' * 60)

# second approach: Using Pandas
column_names = "FirstName LastName Birthplace Birthstate Party".split()
df = pd.read_csv(
    '../DATA/presidents.csv',
    index_col=0,
    names=column_names,
    dtype={'Party': str},
)
print(df.head(), '\n')

# number of lines (rows)
print("Number of rows:", len(df), '\n')

# counts per party
print("Distinct counts:")
print(df.value_counts('Party'), '\n')

# group by party
for party, group in df.groupby('Party'):
    print(party)
    print(group[["FirstName", "LastName"]])
    print()
