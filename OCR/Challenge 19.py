# CHALLENGE 19 - Logic Gate
# Created - 23/09/2026
# Last Updated - 23/09/2026

def lg_check(lg, u1, u2):
    if lg == "OR":
        return u1 | u2
    elif lg == "AND":
        return u1 & u2
    elif lg == "XOR":
        return u1 ^ u2
    elif lg == "NOR":
        return (u1 | u2) ^ 1
    elif lg == "NAND":
        return (u1 & u2) ^ 1

def main():
    print("This is a Logic Gate checker. Enter 'q' to quit.")
    while (True):
        gate = input("Enter a logic gate (OR/AND/XOR/NAND/NOR): ").strip()
        if gate.upper() not in ("OR", "AND", "XOR", "NAND", "NOR"):
            if gate.lower() in ("q", "quit", "exit"):
                break
            else:
                print("This gate is invalid.")
                continue

        while True:
            a1 = input("Enter first input (0 or 1): ")
            if a1 not in ("0", "1"):
                print("Invalid input.")
            else:
                break

        while True:
            a2 = input("Enter second input (0 or 1): ")
            if a2 not in ("0", "1"):
                print("Invalid input.")
            else:
                break

        print(f"Result: {lg_check(gate.upper(), int(a1), int(a2))}")

main()
