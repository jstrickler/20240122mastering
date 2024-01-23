list1 = list()   # empty list
print(f"{len(list1) = }")
s = "scarlet"
colors = ['red', s, 'purple', 'pink', 'mauve']
print(f"{len(colors) = }")
print(f"{colors = }")
print(f"{colors[0] = }")
list2 = []  # also empty list

cities = list()
print(f"{cities = }")
cities.append("Madrid")
cities.append("Tokyo")
cities.append("Chicago")
cities.insert(0, "Denver")
cities.insert(2, "Sao Paulo")
print(f"{cities = }")
more_cities = ["Toronto", "New Orleans", "Albany"]
cities.extend(more_cities)
print(f"{cities = }")
#  LIST.insert(pos, obj)   LIST.append(obj)    LIST.extend(iterable)

del cities[4]  # remove element
print(f"{cities = }")

x = 5
del x

cities.remove('New Orleans')
print(f"{cities = }")

city = cities.pop()
print(f"{city = }")
print(f"{cities = }")
city = cities.pop(1)
print(f"{city = }")
print(f"{cities = }")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
print(f"{fruits[len(fruits)-1] = }")
print(f"{fruits[-1] = }")
print(f"{fruits[-2] = }")

state = "Missippippi"
print(state[0], state[5], state[-1])
print()

print(f"{fruits = }")
print(f"{fruits[2:7] = }")
# start:sentinel
print(f"{fruits[0:4] = }")
print(f"{fruits[:4] = }")
print(f"{fruits[13:] = }")

s = "North Carolina"
print(s[:5])
print(s[6:])
print(s[-4:])

print(f"{cities = }")
print()

for city in cities:
    print(city)
print()

# for VAR in ITERABLE:
#    ...

for fruit in fruits[:10]:
    print(fruit.upper())
print()

city = "Durham"
for char in city:
    print(char)
print()



