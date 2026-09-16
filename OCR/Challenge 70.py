# Challenge 70 - Of mice and men
# Created: 16/09/2026
# Last Updated: 16/09/2026

import random 

def game():
    guesses = 0
    rnc = f"{random.randint(0, 9999):04d}"
    #print(rnc)
    while True:
        try:
            guess = input("Input a 4-digit positive integer (XXXX, where X is 0 to 9): ")
            if len(guess) != 4 or not guess.isdigit():
                raise ValueError
            guesses += 1
            if guess == rnc:
                t_guess = "guess" if guesses == 1 else "guesses"
                print(f"Congratulations! You guessed it ({rnc}) in {guesses} {t_guess}.")
                break

            mice = 0
            men = 0

            rnc_remaining = []
            guess_remaining = []

            for i in range(4):
                if guess[i] == rnc[i]:
                    mice += 1
                else:
                    rnc_remaining.append(rnc[i])
                    guess_remaining.append(guess[i])

            for d in guess_remaining:
                if d in rnc_remaining:
                    men += 1
                    rnc_remaining.remove(d) 

            tmice = ("mouse" if mice == 1 else "mice")
            tmen = ("man" if men == 1 else "men")
            print(f"You have {mice} {tmice} and {men} {tmen}.\n")
                    
                
        except ValueError:
            print("You must enter a 4-digit positive integer.\n")
def main():
    gamen = 1
    print("Game 1:")
    while True:
        game()
        kg = input("Continue? ").strip().lower() 
        if kg in ("no", "n"):
            print("Goodbye.")
            break
        else:
            gamen += 1
            print(f"\nGame {gamen}:")
main()
