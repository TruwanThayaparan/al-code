# Challenge 30 - Year Addition
# Created: 11/09/2026
# Last Updated: 21/09/2026

def guess(yr):
    points = 0
    strikes = 0
    tries = []
    while True:
        while True:
            try:
                p = int(input(f"{yr} divides by what integer without remainder? "))
                if p <= 0:
                    raise ValueError
                if p in tries:
                    print("You already guessed this number.")
                    continue
                tries.append(p)
                break
            except ValueError:
                print("You must enter a positive integer!")
        if yr % p == 0:
            points += 1
            print(f"Correct! Points: {points}")
        else:
            strikes += 1
            if strikes != 3:
                print(f"Strike {strikes}! Try again.")
            else:
                print(f"Strike 3! Game over. Points: {points}\n")
                break
        

def main():
    while True:
        try:
            year = input("Enter a year (XXXX) or 'q' to quit: ").strip().lower()
            if year in ("q", "quit", "exit"):
                break

            if len(year) != 4 or not year.isdigit():
                raise ValueError

            if int(year) < 0:
                raise ValueError
                
            total = sum(int(n) for n in year)
            print(f"The total of the digits in {year} is {total}.\n")
            
            guess(int(year))

        except ValueError:
            print("You must enter a positive integer in the format XXXX.\n")

main()
