# Challenge 1 - Factorial Finder 
# Created: 09/09/2026
# Last Updated: 09/09/2026

def find_factorial_loop(val):
    if val < 0:
        raise ValueError
    if val == 0 or val == 1:
        return 1

    total = 1
    while val > 1:
        total *= val
        val -= 1
    return total
    
def find_factorial_recursive(val):
    if val < 0:
        raise ValueError
    if val == 0 or val == 1:
        return 1

    result = val * find_factorial_recursive(val - 1)
    return result

def main():
    print("This is a Factorial Finder.")
    while True:
        num = input("Enter a number (to quit, type 'q'): ")
        if num in ("quit", "q", "exit"):
            break

        try:
            num = int(num)
        except ValueError:
            print("You must enter a positive whole number (0 or greater).\n")
            continue

        try:
            ans_loop = find_factorial_loop(num)
            ans_rec = find_factorial_recursive(num)
            print(f"[LOOP METHOD] The factorial of {num} is {ans_loop}.")
            print(f"[RECURSION METHOD] The factorial of {num} is {ans_rec}.\n")
        except ValueError:
            print("You must enter a positive whole number (0 or greater).\n")
        except RecursionError:
            print("This number is too big to complete via recursion.\n")

main()
