

x = 100  # (file) global variable

def spam():
    y = 99  # local name (local variable)
    print(x)

spam()

print(f"{x = }")

