# Challenge 72 - Lists
# Created: 07/10/2026
# Last Updated: 07/10/2026

import random

def main():
    while True:
        try:
            rstart = int(input("Enter starting number: "))
            break
        except ValueError:
            print("You must enter an integer.")

    while True:
        try:
            rend = int(input("Enter ending number: "))
            if rend <= rstart:
                print("Ending number must be greater than starting number.")
            else:
                break
        except ValueError:
            print("You must enter an integer.")

    ml = list(range(rstart, rend + 1))

    randomelement = random.randint(rstart, rend)
    randomplace = random.randint(0, len(ml))
    ml.insert(randomplace, randomelement)
    
    print(f"\nOriginal list (length {len(ml)}):")
    print(ml)
    print("-" * 50)

    final_list = []

    while len(ml) > 0:
        current_len = len(ml)
        
        min_select = max(1, current_len // 20)
        max_select = max(1, current_len // 10)
        
        randomselection = random.randint(min_select, max_select)
        
        if randomselection > current_len:
            randomselection = current_len

        max_start_index = current_len - randomselection
        start_index = random.randint(0, max_start_index)
        end_index = start_index + randomselection

        sublist = ml[start_index:end_index]
        final_list.append(sublist)
        del ml[start_index:end_index]

    print("\nProcess finished! Remaining original list:", ml)
    print("\nNew list of sublists (unsorted):")
    for idx, sub in enumerate(final_list):
        print(f"Sublist {idx + 1} (Size {len(sub)}): {sub}")

    sorted_data = sorted(final_list, key=len)
    
    print("\nSorted list of sublists (by length):")
    for idx, sub in enumerate(sorted_data):
        print(f"Sublist {idx + 1} (Size {len(sub)}): {sub}")

main()
