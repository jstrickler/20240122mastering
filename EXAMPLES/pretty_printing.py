from pprint import pprint

struct = {  # nested data structure
    'part1': [
        ['a', 'b', 'c'], ['d', 'e', 'f']
    ],
    'part2': {
        'red': 55923589258,
        'blue': [83039, 94838498, -384843],
        'purple': ['Chicago', 'New York', 'L.A.'],
    },
    'part3': ['g', 'h', 'i'],
}

print('Without pprint:')
print(struct)  # print normally
print()

print('With pprint:')
pprint(struct, sort_dicts=False)  # pretty-print
print()

print('With pprint (depth=2):')
pprint(struct, depth=2, indent=1)  # only print top two levels of structure
print()

print('With pprint (width=40):')
pprint(struct, width=40)
print()

print('With pprint (compact=True):')
pprint(struct, compact=True)
print()

print('With pprint (underscore_numbers=True):')
pprint(struct, underscore_numbers=True)
print()
