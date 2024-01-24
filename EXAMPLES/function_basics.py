import os

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print("m is {:.3f} n is {:.3f}".format(m, n))

x = 28
print(f"{sqrt(x) = }")


def hello(whom="world"):
    print(f"Hello, {whom}")

hello('world')
hello(whom='Mom')
hello('New York')

hello("Dad")
hello()

def find_text(search_term, *file_paths, ignore_case=False, show_file_name=False):
    for file_path in file_paths:
        basename = os.path.basename(file_path)
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    if show_file_name:
                        print(basename, end=" ")
                    print(line, end="")

find_text("bird", '../DATA/alice.txt', '../DATA/parrot.txt', show_file_name=True)

def wacky(p_only, /, pos1, pos2, *opt, kw1, kw2, **optkw):
    pass

def wacky2(p_only, /, pos1, pos2, *, kw1, kw2, **optkw):
    pass


wacky("abc", "def", "ghi", "jkl", "mno", kw1="pqr", kw2="stu", wombat="vwx", muffin="yz")











