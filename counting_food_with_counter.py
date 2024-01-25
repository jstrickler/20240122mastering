from collections import Counter

with open('DATA/breakfast.txt') as breakfast_in:
    food_items = breakfast_in.read().splitlines()

food_counts = Counter(food_items)
food_counts['curry'] += 1
print(f"{food_counts = }")
print(f"{food_counts['bacon'] = }")

print(f"{food_counts.most_common(3) = }")
