# Challenge 5 - Fruit Machine
# Created: 13/09/2026
# Last Updated: 13/09/2026

import random

def main():
    symbols = ["Cherry", "Bell", "Lemon",
            "Orange", "Star", "Skull"]
    credit = 100
    while True:
        print(f"Credit: £{credit/100:.2f}")
        roll = input("Roll the fruit machine? (yes/no): ").strip().lower()
        if roll in ("no", "n"):
            print("Goodbye!")
            break
        elif roll not in ("yes", "y"):
            print("Invalid input.")
            print()
            continue

        credit -= 20
        
        print()
        random_three = random.choices(symbols, k=3)
        r1, r2, r3 = random_three

        print(f"Fruit Machine: {random_three}")

        if r1 == r2 == r3:
            if r1 == "Skull":
                credit = 0
            elif r2 == "Bell":
                credit += 500
            else:
                credit += 100
        elif r1 == r2 or r2 == r3 or r1 == r3:
            if random_three.count("Skull") == 2:
                credit = max(0, credit - 100)
            else:
                credit += 50
                    
        if credit < 20:
            print()
            print(f"Credit: £{credit/100:.2f}")
            print("You lose! Not enough credit left to spin.")
            break

        print()


main()
