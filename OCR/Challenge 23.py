# Challenge 23 - Fibbing
# Created: 11/09/2026
# Last Updated: 11/09/2026

def fibonacci_loop(n):
    fib = []
    total = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        # e = a; a = b; b = e + b
        # print(a)
        fib.append(a)
        total += a

    fib2 = list(reversed(fib))
    return fib, fib2, total

def main():
    while True:
        try:
            fib = input("Generate Fibonacci sequence up to what place (q to quit)? ")
            if fib in ("quit", "q", "exit"):
                break
            fib = int(fib)
            if fib < 1:
                raise ValueError
            fl, flr, tot = fibonacci_loop(fib)
            print(f"Sequence: {fl} \nReversed: {flr}\nTotal: {tot}\n")
        except ValueError:
            print("You must enter a positive integer.") 

main()
