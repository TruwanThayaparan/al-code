# goldbach's conjecture - challenge 71 solution
# created: 2026-09-21
# last updated: 2026-09-21

def prime_check(i):
    if i <= 1: return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def main():
    while True:
        try:
            nm = input("Enter a positive even number greater than 2 ('q' to quit): ").strip().lower()
            if nm in ('q', 'quit', 'exit'):
                break
            nm = int(nm)
            if nm % 2 != 0:
                raise ValueError
            elif nm <= 2:
                raise ValueError
            gb(nm)
        except ValueError:
            print("One must enter a positive even number greater than 2!")

def gb(nm):
    if nm == 4:
        print(f"4 can be made by the sum of the following two prime numbers: \n2, 2")
        return
    x = 3

    while x <= nm // 2:
        if prime_check(x) and prime_check(nm - x):
            print(f"{nm} can be made by the sum of the following two prime numbers: \n{x}, {nm - x}")
            break
        x += 2

main()
