# Challenge 37 - Fizz Buzz
# Created: 10/09/2026
# Last Updated: 10/09/2026

def prime_check(i):
    if i <= 1: return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def fizzbuzz(a, b, m):
    for i in range(1, m + 1):
        if prime_check(i):
            print("OOPS!")
            continue

        if i % a == 0 and i % b == 0:
            print("FizzBuzz")
        elif i % a == 0:
            print("Fizz")
        elif i % b == 0:
            print("Buzz")
        else:
            print(i)
    print("\n")
    
def main():
    constraint_a = 3
    constraint_b = 5
    print("Fizz Buzz Provider")
    print("1. Start")
    print("2. Change Base Numbers (CBN)")
    print("3. Exit\n")
    while True:
        try:
            ans = input("Choose an option: ").strip().lower()
            if ans in ("3", "exit", "quit", "q"):
                break
            if ans in ("2", "cbn", "base changer"):
                print(f"Base Number 1: {constraint_a}")
                print(f"Base Number 2: {constraint_b}")
                try:
                    constraint_a = int(input("Enter base number 1: "))
                    constraint_b = int(input("Enter base number 2: "))
                except ValueError:
                    print("Operation cancelled.\n")
            if ans in ("1", "start", "begin"):
                try:
                    maximum = int(input("What number should the program count to? "))
                    fizzbuzz(constraint_a, constraint_b, maximum)
                except ValueError:
                    print("Operation cancelled.\n")
        except ValueError:
            print()

main()
