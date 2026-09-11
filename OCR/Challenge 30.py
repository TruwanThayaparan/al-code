# Challenge 30 - Year Addition
# Created: 11/09/2026
# Last Updated: 11/09/2026

def guess(yr):
    for i in range(1, 4):
        while True:
            try:
                print(f"\nGuess {i} of 3:")
                p = int(input(f"{yr} divides by what integer without remainder? "))
                if p <= 0:
                    raise ValueError
                break
            except ValueError:
                print("You must enter a positive integer!")
        if yr % p == 0:
            return True
        else:
            if i != 3:
                print("Wrong! Try again.")
        
    return False

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
                
            nums = []
            for i in year:
                nums.append(i)

            total = sum(int(n) for n in nums)
            print(f"The total of the digits in {year} is {total}.\n")
            
            win = guess(int(year))
            if win == True:
                print("You won!\n")
            else:
                print("You lost.\n")

        except ValueError:
            print("You must enter a positive integer in the format XXXX.\n")

main()
