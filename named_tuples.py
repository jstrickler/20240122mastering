from collections import namedtuple
import csv

point = 5, 9

print(f"{point[0] = }")
print(f"{point[1] = }")

person = "Bill", "Gates", "Microsoft", "1955-10-28"

class Point:
    pass

Point = namedtuple('Point', "x y")   #  namedtuple('Point', ['x', 'y'])

p1 = Point(5, 9)
p2 = Point(10, 3)
p3 = Point(8, 8)

for p in p1, p2, p3:
    print(p.x, p.y)

print(type(p1).__name__)


Person = namedtuple('Person', 'first_name last_name product dob')

person1 = Person("Bill", "Gates", "Microsoft", "1955-10-28")
print(person1.first_name, person1.last_name)

# Name,Position Title,Department,Employee Annual Salary

employees = []

with open('DATA/city-of-chicago-salaries.csv') as chi_in:
    rdr = csv.reader(chi_in)
    headers = next(rdr)  # consume next element of iterator
    field_names = [field.lower().replace(' ', '_') for field in headers]
    Employee = namedtuple('Employee', field_names)
    for row in rdr:
        try:
            row[-1] = float(row[-1].lstrip('$'))
        except Exception:
            row[-1] = 0.0
        employees.append(Employee(*row))

for employee in employees[:10]:
    print(employee.name, employee.employee_annual_salary)