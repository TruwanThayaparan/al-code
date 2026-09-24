# Challenge 40 - Base of Numbers
# Created: 24/09/2026
# Last Updated: 24/09/2026

def base_conv(d, base):    
    if d == 0:
        return "0"
        
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while d > 0:
        remainder = d % base
        result.append(chars[remainder])
        d = d // base
        
    return "".join(reversed(result))

def main():
    print("Welcome to the Base of Numbers Converter.")
    while True:
        try:
            den = input("Enter a denary integer ('q' to quit): ").strip().lower()
            if den in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
            
            den = int(den) 

            if den < 0:
                print("Please enter a non-negative integer.\n")
                continue
            
            base_input = input("Enter the base to convert into (e.g., 2, 8, 16): ").strip()
            base = int(base_input)
            
            if base < 2 or base > 36:
                print("You must enter a base between 2 and 36.\n")
                continue
            
            converted_val = base_conv(den, base)
            print(f"Base-{base} equivalent: {converted_val}\n")
            
        except ValueError:
            print("Invalid input. You must enter a valid integer.\n")
        
main()
