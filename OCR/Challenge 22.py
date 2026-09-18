# Challenge 22 - Simple Life Calculator (WIP)

def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

def time_tables():
    table_start = get_valid_int("Enter starting table number: ")
    
    while True:
        table_end = get_valid_int("Enter finishing table number: ")
        if table_end > table_start:
            break
        print("Finishing number must be greater than the starting number.\n")
        
    mult_min = get_valid_int("Enter minimum multiplier figure: ")
    
    while True:
        mult_max = get_valid_int("Enter maximum multiplier figure: ")
        if mult_max > mult_min:
            break
        print("Maximum figure must be greater than the minimum figure.\n")

    print("\n" + "="*30)
    print("Times tables generated:")
    print("="*30 + "\n")
    
    for i in range(table_start, table_end + 1):
        print(f"--- {i} Times Table ---")
        for j in range(mult_min, mult_max + 1):
            print(f"{i} * {j} = {i * j}")
        print()

def menu():
    while True:
        print("Simple Life Calculator:")
        print("1. VAT \n2. Tax \n3. Times table \n4. Exit")
        answ = input("Enter an option (1, 2, 3, or 4): ").strip()
        if answ == "1":
            pass
        elif answ == "2":
            pass
        elif answ == "3":
            time_tables()
        elif answ == "4":
            print("Goodbye!")
            break
        else:
            print("You must enter 1, 2, 3, or 4.")
        print()

menu()
