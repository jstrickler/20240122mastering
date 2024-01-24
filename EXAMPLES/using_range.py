
#  range(stop)   range(start, stop)   range(start, stop, step)

for i in range(5):   # range(0, 5)
    print(i)
print('-' * 60)

for i in range(1, 11):
    print(i, "spaghetti!!")
print('-' * 60)

numbers = list(range(1, 26))
print(f"{numbers = }")

flags = [False] * 25
print(f"{flags = }")
