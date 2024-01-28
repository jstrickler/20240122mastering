from math import pi
from typing import Union, Iterable, Any, Optional, Tuple, Dict, List

Numeric = Union[int, float]


def circle_area(diameter: int) -> float:
    return ((diameter/2) ** 2) * pi

print(circle_area(42.3))
print(circle_area(22))

result: float

result = circle_area(55)

def do_colors(color_list: Iterable[str]) -> None:
    for color in color_list:
        print(color)

c1 = ['red', 'purple', 'orange']
do_colors(c1)
c2 = 'green', 'pink', 'mauve', 'black'
do_colors(c2)
c3 = [5, 10, 15]
do_colors(c3)

def spam(arg: Optional[str] = None):
    if arg is not None:
        print(arg)

spam()
spam('abc')
spam(123)

def ham() -> List[int]:
    return [1, 2, 3]

x = ham()







