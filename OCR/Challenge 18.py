# Challenge 18 - Years in a Range
# Created: 09/09/2026
# Last Updated: 28/09/2026

def range_check(mi, ma):
    rep = False
    for i in range(mi, ma + 1):
        year_str = str(i)
        if len(year_str) != len(set(year_str)):
            rep = True
            print(f"{i} has repeated digits.")

    if rep == False:
        print("No years within the given range had repeated digits.")

    print("\n")

def main():
    q_p = False
    print("This program checks if the years within a given range have repeated digits. To end the program, enter 'q' at any stage.\n")
    while True:
        try:
            min_bound = input("Minimum bound: ")
            if min_bound in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
            min_bound = int(min_bound)
            if min_bound < 0:
                raise ValueError
        except ValueError:
            print("You must enter a positive whole number.")
            continue

        while True:
            try:
                max_bound = input("Maximum bound: ")
                if max_bound in ('q', 'quit', 'exit'):
                    print("Goodbye!")
                    q_p = True
                    break
                max_bound = int(max_bound)
                if max_bound < 0:
                    raise ValueError
                if min_bound > max_bound:
                    print("Minimum bound cannot be greater than maximum bound.")
                    continue
                break
            except ValueError:
                print("You must enter a positive whole number.")
                continue

        if q_p == True:
            break

        range_check(min_bound, max_bound)

main()
