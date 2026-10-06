# Challenge 46 - Complex Numbers
# Created: 06/10/2026
# Last Updated: 06/10/2026

def caddition(n1: complex, n2: complex) -> complex:
    return n1 + n2

def cmultiplication(n1: complex, n2: complex) -> complex:
    return n1 * n2

def cnegation(n1: complex, n2: complex) -> tuple:
    return -n1, -n2

def cinversion(n1: complex, n2: complex) -> tuple:
    try:
        inv_n1 = n1 ** -1
    except ZeroDivisionError:
        inv_n1 = complex(float('inf'), float('inf'))
        
    try:
        inv_n2 = n2 ** -1
    except ZeroDivisionError:
        inv_n2 = complex(float('inf'), float('inf'))
        
    return inv_n1, inv_n2

def csubtraction(n1: complex, n2: complex) -> complex:
    _, neg_n2 = cnegation(n1, n2)
    return caddition(n1, neg_n2)

def cdivision(n1: complex, n2: complex) -> complex:
    _, inv_n2 = cinversion(n1, n2)
    return cmultiplication(n1, inv_n2)

def main():
    print("--- Complex Calculator BASIC ---")
    print("Enter nothing to quit.")
    
    while True:
        raw_n1 = input("\nEnter a complex number: ").strip()
        if not raw_n1:
            print("Goodbye!")
            break
            
        try:
            n1 = complex(raw_n1)
        except ValueError:
            print("Not a complex number.")
            continue

        raw_n2 = input("Enter another complex number: ").strip()
        if not raw_n2:
            print("Goodbye!")
            break
            
        try:
            n2 = complex(raw_n2)
        except ValueError:
            print("Not a complex number.")
            continue
    
        cad = caddition(n1, n2)
        csu = csubtraction(n1, n2)
        cmu = cmultiplication(n1, n2)
        cdi = cdivision(n1, n2)
        cne1, cne2 = cnegation(n1, n2)
        cin1, cin2 = cinversion(n1, n2)
        
        print(f"Addition: {n1} + {n2} = {cad}")
        print(f"Subtraction: {n1} - {n2} = {csu}")
        print(f"Multiplication: {n1} * {n2} = {cmu}")
        print(f"Division: {n1} / {n2} = {cdi}")
        print(f"Negation: {n1} -> {cne1}, {n2} -> {cne2}")
        print(f"Inversion: {n1} -> {cin1}, {n2} -> {cin2}")

main()
