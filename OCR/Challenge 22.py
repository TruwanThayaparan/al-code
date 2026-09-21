# Challenge 22 - Simple Life Calculator
# Created: 14/09/2026
# Last Updated: 21/09/2026

def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

def get_valid_float(prompt: str, is_percentage: bool) -> float:
    while True:
        try:
            val = float(input(prompt))
            if is_percentage:
                if not (0 <= val <= 100):
                    print("Invalid input. Please enter a percentage between 0 and 100.\n")
                    continue
            else:
                if val <= 0:
                    print("Invalid input. Please enter a number greater than 0.\n")
                    continue
            return val
        except ValueError:
            print("Invalid input. Please enter a number.")

def time_tables():
    table_start = get_valid_int("Enter starting table number: ")
    
    while True:
        table_end = get_valid_int("Enter finishing table number: ")
        if table_end >= table_start:
            break
        print("Finishing number must be equal to or greater than the starting number.\n")
        
    mult_min = get_valid_int("Enter minimum multiplier figure: ")
    
    while True:
        mult_max = get_valid_int("Enter maximum multiplier figure: ")
        if mult_max >= mult_min:
            break
        print("Maximum figure must be equal to or greater than the minimum figure.\n")

    print("\n" + "="*30)
    print("Times tables generated:")
    print("="*30 + "\n")
    
    for i in range(table_start, table_end + 1):
        print(f"--- {i} Times Table ---")
        for j in range(mult_min, mult_max + 1):
            print(f"{i} * {j} = {i * j}")
        print()

def tax_calc():
    print("1. Calculate income after tax")
    print("2. Calculate income before tax")
    print("3. Calculate tax %")
    while True:
        m = input("Select an option (1, 2, or 3): ")
        if m not in ("1", "2", "3"):
            print("Invalid choice. Please try again.")
            continue
        break

    if m == "1":
        taxed = get_valid_float("Tax %: ", True)
        income = get_valid_float("Income before tax: ", False)
        res = income - ((taxed/100) * income)
        print(f"Income after tax: £{res:.2f}")
    elif m == "2":
        while True:
            taxed = get_valid_float("Tax %: ", True)
            if taxed == 100:
                print("Your tax cannot be 100% as it causes an infinite division calculation!\n")
                continue
            break            
        income = get_valid_float("Income after tax: ", False)
        res = income / (1 - (taxed/100))
        print(f"Income before tax: £{res:.2f}")
    elif m == "3":
        olincome = get_valid_float("Income before tax: ", False)
        while True:
            neincome = get_valid_float("Income after tax: ", False)
            if neincome <= olincome:
                break
            print("Income after tax must be lower than or equal to income before tax.\n")
        taxation = ((olincome - neincome) / olincome) * 100
        print(f"Tax (to 2 decimal places): {taxation:.2f}%")

def vat_calc():
    print("1. Calculate price after VAT")
    print("2. Calculate price before VAT")
    print("3. Calculate VAT %")
    while True:
        m = input("Select an option (1, 2, or 3): ")
        if m not in ("1", "2", "3"):
            print("Invalid choice. Please try again.")
            continue
        break

    if m == "1":
        vated = get_valid_float("VAT %: ", True)
        price = get_valid_float("Price before VAT: ", False)
        res = price + ((vated/100) * price)
        print(f"Price after VAT: £{res:.2f}")
    elif m == "2":
        vated = get_valid_float("VAT %: ", True)
        price = get_valid_float("Price after VAT: ", False)
        res = price / (1 + (vated/100))
        print(f"Price before VAT: £{res:.2f}")
    elif m == "3":
        olprice = get_valid_float("Price before VAT: ", False)
        while True:
            neprice = get_valid_float("Price after VAT: ", False)
            if neprice >= olprice:
                break
            print("Price after VAT must be greater than or equal to price before VAT.\n")
        vating = ((neprice - olprice) / olprice) * 100
        print(f"VAT (to 2 decimal places): {vating:.2f}%")

def menu():
    while True:
        print("Simple Life Calculator:")
        print("1. Tax \n2. VAT \n3. Times table \n4. Exit")
        answ = input("Enter an option (1, 2, 3, or 4): ").strip()
        if answ == "1":
            tax_calc()
        elif answ == "2":
            vat_calc()
        elif answ == "3":
            time_tables()
        elif answ == "4":
            print("Goodbye!")
            break
        else:
            print("You must enter 1, 2, 3, or 4.")
        print()

menu()
