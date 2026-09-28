# Challenge
import random

def rps():
    print("\n--- Rock Paper Scissors ---")
    print("Enter nothing at any point to return.")
    choices = ["Rock", "Paper", "Scissors"]
    wins, losses, draws, games = 0, 0, 0, 0
    
    while True:
        ch = input("Pick an option from Rock, Paper and Scissors: ").strip().capitalize()
        if not ch:
            print(f"\nWins: {wins}\nLosses: {losses}\nDraws: {draws}\nTotal Games: {games}")
            print("Returning to main menu...\n")
            break 
        
        if ch == "1": ch = "Rock"
        elif ch == "2": ch = "Paper"
        elif ch == "3": ch = "Scissors"
        
        if ch not in choices:
            print("Invalid option. Try again.")
            continue
            
        games += 1
        compch = random.choice(choices)
        
        if compch == ch:
            print(f"Draw! (Both chose {ch})\n")
            draws += 1
        elif (compch == "Rock" and ch == "Scissors") or \
             (compch == "Paper" and ch == "Rock") or \
             (compch == "Scissors" and ch == "Paper"):
            print(f"You lost! (Computer chose {compch})\n")
            losses += 1
        else:
            print(f"You win! (Computer chose {compch})\n")
            wins += 1

def gtn():
    print("\n--- Guess the Number ---")
    print("The computer has picked a number between 1 and 100.")
    print("Enter nothing at any point to return.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess_input = input("Enter your guess (1-100): ").strip()
        if not guess_input:
            print("Returning to main menu...\n")
            break
            
        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue
            
        guess = int(guess_input)
        if not (1 <= guess <= 100):
            print("The number you entered is not in range!\n")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.\n")
            break

def gtnc():
    print("\n--- Guess the Number (Computer Guesses) ---")
    print("Enter nothing at any point to return.")
    
    while True:
        guessn = input("Enter a number between 1 and 1000 which the computer will have to guess: ").strip()
        if not guessn:
            print("Returning to main menu...\n")
            break
            
        if not guessn.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guessn = int(guessn)

        if not (1 <= guessn <= 1000):
            print("The number you entered is not in range!\n")
            continue

        print("\nSimulation activated.")
        attempts = 0
        low = 1
        high = 1000
        
        while low <= high:
            attempts += 1
            guess = (low + high) // 2
            print(f"Attempt {attempts}: ")
            
            if guess < guessn:
                print(f"Computer guessed too low ({guess}).")
                low = guess + 1
            elif guess > guessn:
                print(f"Computer guessed too high ({guess}).")
                high = guess - 1
            else:
                print(f"The computer guessed the number ({guessn}) in {attempts} attempts!\n")
                break

def main():
    while True:
        print("=== MINI GAMES MENU ===")
        print("1. Rock Paper Scissors")
        print("2. Guess the Number (You Guess)")
        print("3. Guess the Number (Computer Guesses)")
        print("4. Quit")
        opt = input("Enter an option (1, 2, 3, or 4): ").strip()
        
        if opt == "1":
            rps()
        elif opt == "2":
            gtn()
        elif opt == "3":
            gtnc()
        elif opt == "4":
            print("Goodbye.")
            break
        else:
            print("This is not a valid option.\n")

main()
