
a = 5
b = 10
c = 20.22
d = 0o123        # Octal
e = 0xdeadbeef   # Hex
f = 0b10011101   # Binary 
g = .00008303e22    # float in SN

print("a, b, c", a, b, c)
print("a + b", a + b)
print("a + c", a + c)
print("d", d)
print("e", e)
print("f", f)
print("g", g)
print()

a = 23
b = 7

print(a + b, a - b, a * b)
print(a / b, a // b) 
print(a ** b, a % b)

x = 5
x += 10  # x = x + 10
x *= 4
x /= 3
print("x is", x)

# not supported:  x++ and friends

print((a ** b) / x)
print()


a = "123"
b = 456

print(a + str(b))
print(int(a) + b)
