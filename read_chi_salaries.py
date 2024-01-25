import csv
import re
import pandas
import matplotlib.pyplot as plt


data_file = 'DATA/city-of-chicago-salaries.csv'

employee_data = {}
with open(data_file) as data_in:
    header_line = data_in.readline()  # read 1st line of file
    rdr = csv.reader(data_in)
    for row in rdr:
        row[3] = row[3].lstrip('$')
        row[0] = re.sub('\s+', ' ', row[0])
        employee_data[row[0]] = row[1:]
print('-' * 60)

print(employee_data['WALTON, HOMER'])
print('-' * 60)

df = pandas.read_csv(data_file)
print(df.head(10))
print()

vc = df.value_counts('Department')
vc.plot(kind="barh")
plt.show()


df['raw_salary'] = df['Employee Annual Salary'].str.lstrip('$').astype(float)
print(df.head())

print(df['raw_salary'].mean())

df.to_excel('chicagostuff.xlsx', 'salaries')

