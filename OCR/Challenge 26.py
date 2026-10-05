# Challenge 26 - Truth or not
# Created: 05/10/2026
# Last Updated: 05/10/2026

def generate_binary(n, current_string=""):
    if len(current_string) == n:
        print(" ".join(current_string))
        return
    
    generate_binary(n, current_string + "0")
    generate_binary(n, current_string + "1")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    print("--- Truth Table Maker ---")
    while True:
        try:
            _bin = input("Enter the number of inputs (enter nothing to quit): ")
            if _bin:
                _bin = int(_bin)
            else:
                print("Goodbye."); break

            if _bin > len(alphabet):
                raise ValueError("Too many inputs!")

            if _bin < 1:
                raise ValueError("Please enter at least 1 input.")
        except Exception as e:
            print("Please enter a valid integer." if "literal" in str(e) else e)
            continue
            
        total_rows = 2 ** _bin
        print(f"Number of inputs: {_bin}")
        print(f"Number of output lines (rows) needed: {total_rows}\n")
            
        print(" ".join(alphabet[0:_bin]))
        print("-" * (_bin * 2 - 1)) 
            
        generate_binary(_bin)
        print("\n" + "="*20 + "\n") 

main()
