# Challenge 3 - Thief!
# Created: 09/09/2026
# Last Updated: 09/09/2026

import itertools

def combos(spl):
    unique_permutations = set(itertools.permutations(spl))

    print(f"List of the {len(unique_permutations)} possible combinations:")
    for i in sorted(unique_permutations):
        # print(i)
        print("".join(i))

def main():
    while True:
        flag = False
        numbers = input("Enter any 4 digits (e.g. '1 2 3 4'): ")
        split_numbers = numbers.split()
        if len(split_numbers) != 4:
            print("You must enter 4 digits.\n")
            continue
        
        if not all(len(n) == 1 and n.isdigit() for n in split_numbers):
            print("Error: All inputs must be single digits (0-9).\n")
            continue
        
        if flag == False:
            combos(split_numbers)
            break

main()

'''
old:
for n in split_numbers:
    try:
        if len(n) != 1:
            print(f"{n} is not of the right length (must be 1). Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
            flag = True
            break

        n = int(n)
    except ValueError:
        print(f"{n} is not a digit. Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n")
        flag = True
        break
'''
