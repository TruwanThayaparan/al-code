# CHALLENGE 35 - GAME OF CHANCE
# CREATED: 14/09/2026
# LAST UPDATED: 14/09/2026

import random

def main():
    money = 10000 
    
    while True:
        print(f"Current Balance: £{money/100:.2f}")
        
        try:
            roll_input = input("Enter numbers between 0 and 30 separated by spaces (or 'q' to quit): ").strip()
            if roll_input.lower() in ("q", "quit", "exit"):
                print("Goodbye!")
                break
                
            if not roll_input:
                print("You must enter at least one number."); print()
                continue

            chosen_numbers = []
            for item in roll_input.split():
                val = int(item)
                if not (0 <= val <= 30):
                    raise ValueError("Out of range")
                chosen_numbers.append(val)
                
        except ValueError:
            print("Error: You must only enter numbers between 0 and 30.")
            print()
            continue

        print(f"You chose {len(chosen_numbers)} number(s): {chosen_numbers}")
        while True:
            print()
            try:
                bets_input = input(f"Enter the bet amount (£1 to £10) for each of those {len(chosen_numbers)} numbers: ").strip()
            
                bet_amounts = [int(item) for item in bets_input.split()]
            
                if len(bet_amounts) != len(chosen_numbers):
                    print(f"Error: You entered {len(chosen_numbers)} numbers but {len(bet_amounts)} bets. They must match.")
                    continue
                
                invalid_bet = False
                total_costs_pence = 0
                for bet in bet_amounts:
                    if not (1 <= bet <= 10):
                        print("Error: Each individual bet must be between £1 and £10.")
                        invalid_bet = True
                        break
                    total_costs_pence += (bet * 100)
                
                if invalid_bet:
                    continue
                
                if total_costs_pence > money:
                    print("Error: You can't bet more money than you actually have.")
                    continue
                
                break
            except ValueError:
                print("Error: Payout amounts must be whole positive integers.")
                continue
        
        money -= total_costs_pence

        print()
        numrand = random.randint(0, 30)
        print(f"Random number chosen: {numrand}")
        
        if numrand in chosen_numbers:
            matched_index = chosen_numbers.index(numrand)
            wager_pence = bet_amounts[matched_index] * 100
            
            print(f"It's a match on your bet for {numrand}!")
            
            bonus = 1
            if numrand % 2 == 0:
                print("-> Even number multiplier (2x)")
                bonus *= 2
            if numrand in (10, 20, 30):
                print("-> Multiple of 10 multiplier (3x)")
                bonus *= 3
            if numrand < 5:
                print("-> Less than 5 multiplier (2x)")
                bonus *= 2
            if numrand in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
                print("-> Prime number multiplier (5x)")
                bonus *= 5
                
            payout = wager_pence * bonus
            money += payout
            print(f"You won back: £{payout/100:.2f}!")
        else:
            print("None of your numbers matched the winning spin.")
                
        if money <= 0:
            print(f"\nFinal Balance: £{money/100:.2f}")
            print("You lose! Not enough money left to bet again.")
            break

        print("\n" + "="*40 + "\n")

main()
