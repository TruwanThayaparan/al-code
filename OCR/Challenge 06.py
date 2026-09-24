# Challenge 6 - Unit Converter (temp, currency, volume)
# Created: 24/09/2026
# Last Updated: 24/09/2026

def prompt_con(ut):
    while True:
        ol = input("Enter the unit your current value is in: ").strip().lower()
        if ol not in ut:
            print(f"Invalid unit! You must enter one of the following: {', '.join(ut)}.")
            continue
        break

    while True:
        ne = input("Enter the unit you want the value to be converted to: ").strip().lower()
        if ne not in ut:
            print(f"Invalid unit! You must enter one of the following: {', '.join(ut)}.")
            continue
        if ne == ol:
            print("Invalid input! You must enter a different unit to the one your value is already in.")
            continue
        break

    return ol, ne

def prompt_val():
    while True:
        try:
            return float(input("Enter the value: "))
        except ValueError:
            print("Invalid input. You must enter a number.")

def convert(mode):
    if mode == "temperature":
        u_type = ("fahrenheit", "celsius", "kelvin")
    elif mode == "currency":
        u_type = ("gbp", "usd", "eur")
    elif mode == "volume":
        u_type = ("litres", "gallons", "cups")

    old, new = prompt_con(u_type)
    rvalo = prompt_val()
    rvaln = 0.0

    if mode == "temperature": # dictionaries are better
        if old == "fahrenheit" and new == "kelvin": rvaln = (rvalo - 32) * 5/9 + 273.15
        elif old == "fahrenheit" and new == "celsius": rvaln = (rvalo - 32) * 5/9 
        elif old == "celsius" and new == "kelvin": rvaln = rvalo + 273.15
        elif old == "celsius" and new == "fahrenheit": rvaln = (rvalo * 9/5) + 32
        elif old == "kelvin" and new == "fahrenheit": rvaln = (rvalo - 273.15) * 9/5 + 32 
        elif old == "kelvin" and new == "celsius": rvaln = rvalo - 273.15
        
        display_old, display_new = old.capitalize(), new.capitalize()

        symbol_old = "" if old == "kelvin" else "°"
        symbol_new = "" if new == "kelvin" else "°"

        print(f"Converting {rvalo}{symbol_old} {display_old} to {display_new}, you get ~{rvaln:.2f}{symbol_new}.\n")
        return
        
    elif mode == "currency":
        if old == "gbp" and new == "usd": rvaln = rvalo * 1.3276
        elif old == "gbp" and new == "eur": rvaln = rvalo * 1.1635
        elif old == "usd" and new == "gbp": rvaln = rvalo * 0.7532
        elif old == "usd" and new == "eur": rvaln = rvalo * 0.8763
        elif old == "eur" and new == "gbp": rvaln = rvalo * 0.8595
        elif old == "eur" and new == "usd": rvaln = rvalo * 1.1411
        
        display_old, display_new = old.upper(), new.upper()

    elif mode == "volume":
        if old == "litres" and new == "gallons": rvaln = rvalo / 4.546
        elif old == "litres" and new == "cups": rvaln = rvalo * 4.166
        elif old == "gallons" and new == "litres": rvaln = rvalo * 4.546
        elif old == "gallons" and new == "cups": rvaln = rvalo * 16
        elif old == "cups" and new == "litres": rvaln = rvalo / 4.166
        elif old == "cups" and new == "gallons": rvaln = rvalo / 16
        
        display_old, display_new = old, new

    print(f"Converting {rvalo} {display_old} to {display_new}, you get ~{rvaln:.2f}.\n")

def main():
    print("Welcome to the Unit Converter:")
    print("1. Temperature")
    print("2. Currency")
    print("3. Volume")
    print("4. Exit")
    while True:
        b = input("Please choose an option (1, 2, 3, or 4): ").strip().lower()
        if b not in ("1", "2", "3", "4", "temp", "temperature", "currency", "volume", "exit"):
            print("This is an invalid option."); continue

        if b in ("1", "temp", "temperature"):
            convert("temperature")
        elif b in ("2", "currency"):
            convert("currency")
        elif b in ("3", "volume"):
            convert("volume")
        else:
            print("Goodbye!")
            break

main()
