import os     #  includes os.path
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")

print(f"{os.path.exists(file_path) = }")

file_size = os.path.getsize(file_path)
print(f"{file_size = }")

raw_ts = os.path.getmtime(file_path)
print(f"{raw_ts = }")
file_ts = datetime.fromtimestamp(raw_ts)
print(f"{file_ts = }")

print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")

print(f"{os.path.abspath(file_path) = }")

print(f"{os.path.split(file_path) = }")
print(f"{os.path.splitext(file_path) = }")

print(f"{os.path.isdir(file_path) = }")
print(f"{os.path.isfile(file_path) = }")
print()

contents1 = os.listdir(FOLDER)
print(f"{contents1 = }\n")

for item in sorted(contents1):
    file_path = os.path.join(FOLDER, item)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"{file_size:8d} {item}")
print('-' * 60)

for item in sorted(os.scandir(FOLDER), key=lambda x: x.name.lower()):
    print(f"{item.stat().st_size:8d} {item.name}")


