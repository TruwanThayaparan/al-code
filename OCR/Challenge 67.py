# Challenge 67 - What have the Romans ever done for us?
# Created: 02/10/2026
# Last Updated: 02/10/2026

def num_to_roman(n):
    if not(0 < n < 4000):
        return False, "Constraint: number must be between 1 and 3999."
    roman_mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_string = ""
    
    for value, numeral in roman_mapping:
        while n >= value:
            roman_string += numeral
            n -= value
            
    return True, roman_string

def main():
    while True:
        try:
            nom = input("Enter a number ('q' to quit): ").strip().lower()
            if nom in ("q", "quit", "exit"):
                break
            else:
                nom = int(nom)
                err, num = num_to_roman(nom)
                if not err:
                    print(num)
                else:
                    print(f"{nom} in Roman Numerals is {num}.")
        except ValueError:
            print("You must enter a number between 1 and 3999.")

main()
