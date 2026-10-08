# Challenge 73 - Travel Club (weak version)
# Created: 08/10/2026
# Last Updated: 08/10/2026

def calculate_club_contributions(costs, percentages=None, total_people=7):
    total_cost = sum(costs)
    print(f"--- Travel Club Invoice ---")
    print(f"Total Trip Cost: £{total_cost:.2f}\n")
    
    if percentages is None:
        each_person = total_cost / total_people
        print("Splitting Expenses Equally:")
        for i in range(total_people):
            print(f"  Person {i + 1} owes: £{each_person:.2f}")
            
    else:
        if sum(percentages) != 100:
            raise ValueError("Percentages don't add up to 100%.")
            
        print("Splitting Expenses by Percentage:")
        for i, pct in enumerate(percentages):
            individual_share = (pct / 100) * total_cost
            print(f"  Person {i + 1} ({pct}%): £{individual_share:.2f}")

trip_costs = [100, 200, 400, 800] # example values
calculate_club_contributions(trip_costs, total_people=7)

print("\n" + "="*30 + "\n")

custom_weights = [10, 12, 14, 16, 18, 18, 12] # example values
calculate_club_contributions(trip_costs, percentages=custom_weights)
