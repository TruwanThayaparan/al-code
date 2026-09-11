# Challenge 29 - Item Merge
# Created: 11/09/2026
# Last Updated: 11/09/2026

from collections import Counter

# week a
gl1 = [
    "Apples",
    "Chicken",
    "Milk",   
    "Cheddar Cheese",
    "Bread",
    "Eggs",
    "Spinach",
    "Greek Yogurt",
    "Bananas"    
]

# week b
gl2 = [
    "Bacon",
    "Cheddar Cheese",
    "Orange Juice",
    "Eggs",
    "Milk",
    "Avocado",
    "Smoked Salmon",
    "Bagels",
    "Spinach"
]

# week c
gl3 = [
    "Apples",
    "Milk",
    "Eggs",
    "Bread",
    "Tomatoes",
    "Butter",
    "Greek Yogurt",
    "Bananas",
    "Coffee"
]

# week d
gl4 = [
    "Milk",
    "Chicken",
    "Cheddar Cheese",
    "Eggs",
    "Bread",
    "Orange Juice",
    "Avocado",
    "Potatoes",
    "Onions"
]

all_items = gl1 + gl2 + gl3 + gl4
item_counts = Counter(all_items)
unique_items = [item for item, count in item_counts.items() if count == 1]

print(f"All unique items: {unique_items}")
print("\n")

rl1 = {item for item in gl1 if item_counts[item] == 1}
rl2 = {item for item in gl2 if item_counts[item] == 1}
rl3 = {item for item in gl3 if item_counts[item] == 1}
rl4 = {item for item in gl4 if item_counts[item] == 1}

print("Unique items for individual lists:")
print(sorted(rl1) if rl1 else "No unique items this week")
print(sorted(rl2) if rl2 else "No unique items this week")
print(sorted(rl3) if rl3 else "No unique items this week")
print(sorted(rl4) if rl4 else "No unique items this week")

print("\n")
comlist = gl1 + gl2 + gl3 + gl4
comslist = set(comlist)

print("Appended lists:")
print(comslist)
print("\n")

print("Most popular:")
top_three = item_counts.most_common(3)
print(top_three)
