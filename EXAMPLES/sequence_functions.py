import psutil
import os

colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("colors: len is {}; min is {}; max is {}".format(len(colors), min(colors), max(colors)))
print("months: len is {}; min is {}; max is {}".format(len(months), min(months), max(months)))
print()

print("sorted:", end=' ')
for m in sorted(colors):   # sorted() returns a sorted list
    print(m, end=' ')
print()

phrase = ('dog', 'bites', 'man')
print(" ".join(reversed(phrase)))  # reversed() returns a reversed iterator
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

full_names = zip(first_names, last_names)  # zip() returns an iterator of tuples created from corresponding elements
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print("{} {}".format(first_name, last_name))

proc = psutil.Process(os.getpid())

print(proc.memory_full_info().rss)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b == c)
print(a is b)   #  id(a) == id(b)
print(a is c)
print(id(a), id(b), id(c))

j = 35
k = 35
print(j is k)
name1 = "Bob"
name2 = "Bob"
print(name1 is name2)
name1 = "Fred"
print(name1 is name2)
print(f"{name2 = }")




