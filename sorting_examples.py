
fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

#  str.lower(s)

f1 = sorted(fruits, key=str.lower)   #  max(...)  min(...)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=len)
print(f"{f2 = }\n")

def len_and_name(fruit):
    return len(fruit), fruit.lower()

f3 = sorted(fruits, key=len_and_name)
print(f"{f3 = }\n")

def wacky(f):
    return f[1]

f4 = sorted(fruits, key=wacky)
print(f"{f4 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[-1]  # return DOB for the person

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def lname_fname(person):
    return person[1], person[0]

for person in sorted(people, key=lname_fname):
    print(person)
print('-' * 60)

#  lambda p: value    anonymous, in-line function definition
for person in sorted(people, key=lambda x: (x[-1])):
    print(person)
print('-' * 60)

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)
print(f"{list(airports.items()) = }")

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items(), key=lambda item: (item[1], item[0])):
    print(code, city)
print('-' * 60)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruits.sort()
print(f"{fruits = }\n")

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

n1 = sorted(nums, reverse=True)
print(f"{n1 = }\n")







