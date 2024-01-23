person = "Tom Hanks"
city = "Los Angeles"
value = 38.13826843984

#   str(arg) + " " + str(arg) + " " .... + str(arg) + "\n"
print(person, city, value)
print("one")
print("two")
print("three")
print(person, city, value, sep="/")
print(person, city, value, sep="#")
print(person, city, value, sep=", ")
my_sep = "+"
print(person, city, value, sep=my_sep)



print("one", end=" ")
#  if .....
# print("two", end=" ")
print("three")
print()
print()
print("four")

print(city + ": " + person)
print(f"{city}: {person}")
print(f"{person} lives in {city}")

s = f"{city}: {person}"
print(s)

print(f"Value is {value}")
print(f"Value is {value:.2f}")


