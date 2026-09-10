# Challenge 38 - Sing Along
# Created: 10/09/2026
# Last updated: 10/09/2026

from time import sleep

def countbottles(gre):
    t = None
    for i in range(gre, 0, -1):
        print("\n")
        if i == 2:
            t = "2 green bottles"
            u = "1 green bottle"
        elif i == 1:
            t = "1 green bottle"
            u = "no green bottles"
        else:
            t = f"{i} green bottles"
            u = f"{i-1} green bottles"

        print(f"{t} hanging on the wall,")
        print(f"{t} hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There'll be {u} hanging on the wall.")
        #sleep(0.5)

def main():
    while True:
        try:
            gre = int(input("Enter the number to count from: "))
            if gre < 1:
                raise ValueError
            countbottles(gre)
            break
        except ValueError:
            print("You must enter a positive integer.")

main()

'''
shortened (use semi colons to shorten further):
n = int(input("Enter number: "))

for i in range(n, 0, -1):
    current = f"{i} green bottle" + ("s" if i != 1 else "")
    remaining = "no green bottles" if i == 1 else f"{i-1} green bottle" + ("s" if i != 2 else "")
    
    print(f"\n{current} hanging on the wall,")
    print(f"{current} hanging on the wall,")
    print("And if one green bottle should accidentally fall,")
    print(f"There'll be {remaining} hanging on the wall.")
'''
