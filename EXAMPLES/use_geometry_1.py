import alpha.mathlib.geometry as geometry   # find and run geometry.py
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
print(f"{geometry.PI = }")

# module search algorithm
# 1. current folder
# 2. folders in PYTHONPATH environment variable
# 3. folders in sys.prefix/lib
print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)


