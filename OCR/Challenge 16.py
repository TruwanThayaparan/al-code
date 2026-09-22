# Challenge 16 - Kaprekar
# Created: 22/09/2026
# Last Updated: 22/09/2026

def main():
    while True:
        while True:
            try:
                kcheck = input("Enter a number ('q' to quit): ").strip().lower()
                if kcheck.lower() in ('q', 'quit', 'exit'):
                    print("Goodbye."); return
                kcheck = int(kcheck)
                if kcheck <= 0:
                    print("Please enter a positive integer.")
                    continue
            except ValueError:
                print("This is not a number.")
                continue
            break

        init = kcheck
        init_len = len(str(init)) 
        
        kcheck = kcheck * kcheck # ** 2
        kcheck_str = str(kcheck)
        
        left_part = kcheck_str[:-init_len]
        right_part = kcheck_str[-init_len:]
        
        first = int(left_part) if left_part else 0
        second = int(right_part) if right_part else 0
        
        is_right_valid = int(right_part) > 0 if right_part else False

        if first + second == init and (is_right_valid or init == 1):
            print(f"{init} squared is {kcheck}")
            print(f"{first} + {second} = {first+second}; this number is Kaprekar.\n")
        else:
            print(f"{init} squared is {kcheck}")
            print(f"{first} + {second} = {first+second}; this number is not Kaprekar.\n")

main()
