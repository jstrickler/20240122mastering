import sys

value = 13

if value > 75:
    print("kangaroo")
    print("koala")
    if value > 80:
        print("blue-ringed octopus")
elif value > 50:  # else if
    print("wombat")
    print("wallaby")
elif value > 25:
    print("quokka")
else:
    print("platypus")
    print("kookaburra")


#  R, C, C++, C#, Java, AWK, Scala, Rust, Objective-C, PHP, Perl, 

# if elif else def class try except finally with for while 

garbanzo = 25

if garbanzo:
    print("It's a chickpea")


print("ALL DONE")

# FALSE:
# 0, 0.0, None, False
# len(x) == 0

# TRUE
# True
# non-0 number
# len(x) > 0
# most other objects

#  A ? B : C      if A then B else C

# B if A else C

debug = True

color = "red" if debug else "green"
print(f"{color = }")

# == != > < >= <=
#  num > str  INVALID

if (color == 'red') and (value > 50):
    print("armageddon")

# and or

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("please specify argument on command line")
    exit()






