from collections import defaultdict

d = {'wombat': 'Australia', 'pine marten': 'Canada'}

print(f"{d['wombat'] = }")
# print(f"{d['honey badger'] = }")
print(f"{d.get('honey badger', 'no such beast') = }")

def def_value():
    return "no such beast"

#   defaultdict(lambda: "no such beast")
animals = defaultdict(def_value, d)
print(f"{animals = }")
print(f"{animals['pine marten'] = }")
print(f"{animals['fruit bat'] = }")

print(f"{animals = }")
print()

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruits_by_letter = defaultdict(list)
for fruit in fruits:
    fruits_by_letter[fruit[0]].append(fruit)

for letter, list_of_fruits in fruits_by_letter.items():
    print(letter, list_of_fruits)









