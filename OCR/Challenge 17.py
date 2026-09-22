# Challenge 17 - Number Table
# Creation Date: 22/09/2026
# Last Updated On: 22/09/2026

def make_table(op, hv):
    max_val = hv * hv if op == "*" else hv + hv
    min_val = -hv if op == "-" else 0
    pad = max(len(str(max_val)), len(str(min_val)), 2)
    
    print(f"{op:<{pad}} |", end=" ")
    for i in range(0, hv + 1):
        print(f"{i:<{pad}}", end=" ")
    print()

    print("-" * ((pad + 3) + (hv + 1) * (pad + 1)))
    
    for i in range(0, hv + 1):
        print(f"{i:<{pad}} |", end=" ")
        for j in range(0, hv + 1):
            if op == "+":
                res = i + j
            elif op == "-":
                res = i - j
            elif op == "*":
                res = i * j
            else:
                res = i // j if j != 0 else "X"
            
            print(f"{res:<{pad}}", end=" ")
        print("")

def main():
    while True:
        user_input = input("Enter an operation and a natural number (e.g., '+ 4'): ").strip()
        parts = user_input.split()
        
        if len(parts) != 2:
            print("Invalid format. Please enter a symbol followed by a number separated by a space.")
            continue
            
        op, n_str = parts
        
        if op not in ("+", "-", "*", "/"):
            print("Invalid operator. Must be +, -, *, or /.")
            continue
            
        try:
            n = int(n_str)
            if n <= 0:
                print("The number must be a natural number greater than 0.")
                continue
        except ValueError:
            print("The second argument must be a valid whole number.")
            continue
            
        make_table(op, n)
        break

main()
