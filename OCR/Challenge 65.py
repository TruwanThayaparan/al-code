# Challenge 65 - Spam filter
# Created: 07/10/2026
# Last Updated: 07/10/2026

import random

menu_dishes = ["Pasta", "Biryani", "Pizza", "Chicken Tenders", "Noodles"]

print("--- Monty Python Menu Generator ---")

for dish in menu_dishes:
    beginning_spam = f"Spam and {dish}"
    end_spam = f"{dish} and Spam"
    
    if " " in dish:
        words = dish.split()
        mid_index = random.randint(1, len(words) - 1)
        middle_spam = " ".join(words[:mid_index]) + " and Spam and " + " ".join(words[mid_index:])
    elif len(dish) > 1:
        mid_index = random.randint(1, len(dish) - 1)
        middle_spam = dish[:mid_index] + "Spam" + dish[mid_index:]
    else:
        middle_spam = dish + "Spam"

    print(f"Original: {dish}")
    print(f"  → Beginning: {beginning_spam}")
    print(f"  → End:       {end_spam}")
    print(f"  → In-between: {middle_spam}")
    print("-" * 35)
