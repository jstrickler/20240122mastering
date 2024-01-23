city = 'Orlando'
temp = 85
count = 5
avg = 3.4563892382


print(f"It is {temp}\u00B0 in {city}")  # variables inserted into string

# .2f means round a float to 2 decimal points
print(f"count is {count:03d} avg is {avg:.2f}")
print(f"count is {count:3d} avg is {avg:.2f}")

print(f"2 + 2 is {2 + 2}")  # any expression is OK


# < 3.6  modern
print(f"It is {temp:.2f}\u00B0 in {city:s}")  # variables inserted into string
# 3.6>   old
print("It is {}\u00B0 in {}".format(temp, city))  # variables inserted into string
# < 2.6  legacy
print("it is %d\u00B0 in %s" % (temp, city))
