# Challenge 22 - Simple Life Calculator (WIP)

def time_tables():
    while True:
        try:
            table_start = int(input("Enter starting table number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
    
    while True:
        try:
            table_end = int(input("Enter finishing table number: "))
            if table_end <= table_start:
                print("Finishing number must be greater than the starting number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    while True:
        try:
            mult_min = int(input("Enter minimum multiplier figure: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            
    while True:
        try:
            mult_max = int(input("Enter maximum multiplier figure: "))
            if mult_max <= mult_min:
                print("Maximum figure must be greater than the minimum figure.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    print("\n" + "="*30)
    print("Times tables generated:")
    print("="*30 + "\n")
    
    for i in range(table_start, table_end + 1):
        print(f"--- {i} Times Table ---")
        for j in range(mult_min, mult_max + 1):
            print(f"{i} * {j} = {i * j}")
        print()

time_tables()
