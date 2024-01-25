import csv

with open('knight_data.csv', 'w') as knights_out:
    wtr = csv.writer(knights_out, lineterminator="\n")
    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            fields = line.split(':')
            wtr.writerow(fields)