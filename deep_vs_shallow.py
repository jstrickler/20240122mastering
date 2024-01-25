import copy

a = [1, 2, 3]
b = a  #  alias, not a new object
b.append(4)
print(f"{a = }")
print(f"{b = }")

c = list(a)
b.append(5)
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
print(id(a), id(b), id(c))
print(f"{a is b = }")
print(f"{a is c = }")

a.append(['a', 'b', 'c'])
print(f"{a = }")
d = list(a)
print(f"{d = }")
a[-1].append('d')
print(f"{a = }")
print(f"{d = }")

e = copy.deepcopy(a)
a[-1].append('wombat')
print(f"{a = }")
print(f"{e = }")
