# Challenge 9 - Happy Numbers
# Created: 09/09/2026
# Last Updated: 09/09/2026

def check_happy_numbers(hn):
    hno = hn
    while True:
        total = 0
        for i in str(hn): # or use total = sum(int(i) ** 2 for i in str(hn))
            total += int(i)*int(i)
            #print(total)
        
        #print(total)
        hn = total

        if hn == 1:
            #print(f"{hno} is a happy number.")
            return True
        elif hn == 4:
            #print(f"{hno} is an unhappy number.")
            return False

def main():
    print("This is a happy number checker. Enter 'q' to end the program.")
    while True:
        try:
            hapn = input("Enter a positive whole number: ")
            if hapn in ('q', 'quit', 'exit'):
                break
            hapn = int(hapn)
            if hapn < 1:
                raise ValueError
            t = check_happy_numbers(hapn)
            print(t)
        except ValueError:
            print("You must enter a positive whole number.")
            
def main_auto():
    x = 1
    hnt = []
    hnf = 0
    while hnf < 8:
        isit = check_happy_numbers(x)
        if isit == True:
            hnt.append(x)
            hnf += 1

        x += 1
    
    print("The first eight happy numbers are as followed:")
    print(hnt)

main_auto()
