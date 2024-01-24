import sqlite3

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        contents = file_in.read()
except FileNotFoundError as err:
    print(err)

nums = [800, 80, 1000, "123", 32, -4, 255, "abc", -8, 400, 5, 5000]

for num in nums:
    try:
        inum = int(num)
    except (IndexError, ValueError) as err:
        print(type(err), err)
    except KeyError as err:
        print(err)
    else:  # no exceptions
        print(f"{inum = }")

conn = None
cursor = None
try:
    conn = sqlite3.connect("wombats.db")
    cursor = conn.cursor()
except sqlite3.DatabaseError as err:
    print(err)
    print("GOODBYE!")
    exit()
else:
    cursor.execute("select 5 + 10")
    print(cursor.fetchone())
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()



print("ALL DONE")


