# Challenge 9 - Happy Numbers
# Created: 09/09/2026
# Last Updated: 19/10/2026

import sys

def check_happy_numbers(hn):
    while True:
        total = sum(int(i) ** 2 for i in str(hn))
        hn = total

        if hn == 1:
            return True
        elif hn == 4:
            return False

def angc(ang):
    if 1 <= ang <= 5:
        print("Please enter a positive whole number.\n")
    elif 6 <= ang <= 10:
        print("You must enter a positive whole number.\n")
    elif 11 <= ang <= 15:
        print("Enter a positive whole number.\n")
    elif 16 <= ang <= 20:
        print("Enter a positive (+) whole number.\n")
    elif 21 <= ang <= 25:
        print("Enter a positive (+) whole number (no - symbol, . symbol, or 0)\n")
    elif 26 <= ang <= 30:
        print("If you keep entering incorrect crap, I will cancel the program!\n")
    elif 31 <= ang <= 35:
       print("Don't push it.\n")
    elif ang == 37:
        print("STOP. Last Chance! \n")
    elif ang >= 40:
        print("Program terminated due to repeated non-compliance.")
        sys.exit() 

def main():
    ang = 0 
    print("This is a happy number checker. Enter 'q' to end the program.")
    
    while True:
        try:
            hapn = input("Enter a positive whole number: ")
            if hapn.lower() in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break
                
            hapn = int(hapn)
            if hapn < 1:
                raise ValueError
        
            t = check_happy_numbers(hapn)
            if t:
                print(f"{hapn} is a happy number! \n")
            else:
                print(f"{hapn} is an unhappy number. \n")
                
        except ValueError:
            ang += 1
            angc(ang)
            
if __name__ == "__main__":
    main()
