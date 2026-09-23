# Challenge 34 - What's the day?
# Created: 23/09/2026
# Last Updated: 23/09/2026

import datetime

def main():
    while True:
        while True:
            try:
                day = int(input("Enter a day (1-31): "))
                if not (1 <= day <= 31):
                    print("This is not a valid day.")
                else:
                    break
            except ValueError:
                print("This is not an integer.")

        while True:
            try:
                month = int(input("Enter a month (1-12): "))
                if not (1 <= month <= 12):
                    print("This is not a valid month.")
                else:
                    break
            except ValueError:
                print("This is not an integer.")
            
        while True:
            try:
                year = int(input("Enter a year: "))
                if not (9999 >= year > 0):
                    print("This is not a valid year.")
                else:
                    break
            except ValueError:
                print("This is not an integer.")
      
        is_valid = True
        
        if month in (4, 6, 9, 11) and day == 31:
            is_valid = False
            
        elif month == 2:
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            
            if day > 29:
                is_valid = False
            elif day == 29 and not is_leap:
                is_valid = False

        if not is_valid:
            print("Invalid date combination.\n")
        else:
            valid_date = datetime.date(year, month, day)
            day_of_week = valid_date.strftime("%A") 
            print(f"Success! You entered a valid date: {day:02d}/{month:02d}/{year:04d}")
            print(f"This date was on a {day_of_week}.")
            
        rep = input("Would you like to enter another date? (yes/no): ").strip().lower()
        if rep in ("n", "no"):
            print("Goodbye."); break
        print("\n")

main()
