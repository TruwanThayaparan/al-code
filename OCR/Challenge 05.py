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
        credit -= 20
        
        print()
        random_three = random.choices(symbols, k=3)
        print(f"Fruit Machine: {random_three}")

        if random_three[0] == random_three[1] == random_three[2]:
            if random_three[0] == "Skull":
                credit = 0
            elif random_three[0] == "Bell":
                credit += 500
            else:
                credit += 100
        elif random_three[0] == random_three[1]:
            if random_three[0] == "Skull":
                credit -= 100
            else:
                credit += 50

        elif random_three[1] == random_three[2]:
            if random_three[1] == "Skull":
                credit -= 100
            else:
                credit += 50   

        elif random_three[2] == random_three[0]:
            if random_three[2] == "Skull":
                credit -= 100
            else:
                credit += 50
                    
        if credit < 20:
            if credit <= 0:
                credit = 0
            print()
            print(f"Credit: £{credit/100:.2f}")
            print("You lose! Not enough credit left to spin.")
            break

        print()


main()
