# Challenge 53 - Mortgage Calculator
# Created: 02/10/2026
# Last Updated: 02/10/2026

import math

def calculate_periodic_rate(annual_rate, compounding, periods_per_year):
    r = annual_rate / 100
    if compounding == "continually":
        return math.exp(r / periods_per_year) - 1
    
    comp_map = {"monthly": 12, "weekly": 52, "daily": 365}
    m = comp_map[compounding]
    
    return (1 + r / m) ** (m / periods_per_year) - 1

def main():
    print("--- Mortgage Calculator ---")
    while True:
        while True:
            typ = input("\nHow often do you need to pay (monthly, weekly, daily): ").strip().lower()
            if typ in ("monthly", "weekly", "daily"):
                break
            elif not typ:
                print("Program ended.")
                return
            else:
                print("Invalid. Enter monthly, weekly, or daily (enter nothing to quit).")
            
        while True:
            compounding = input("Select compounding interval (monthly, weekly, daily, continually): ").strip().lower()
            if compounding in ("monthly", "weekly", "daily", "continually"):
                break
            print("Invalid input. Please choose a valid compounding interval.")

        while True:
            try:
                loan = float(input("How much is the loan: £"))
                if loan <= 0:
                    raise ValueError("Loan must be greater than zero!")
                break
            except ValueError as e:
                print(e if "greater" in str(e) else "Not a positive number.")

        while True:
            try:
                interest_rate = float(input("How much is the annual interest rate (%): "))
                if interest_rate < 0:
                    raise ValueError("You can't get paid for having a mortgage!")
                elif interest_rate >= 100:
                    raise ValueError("Impossibly high interest rate.")
                break
            except ValueError as e:
                print(e if "mortgage" in str(e) or "high" in str(e) else "Not a positive number.")

        while True:
            try:
                years = float(input("How many years is the loan term: "))
                if years <= 0:
                    raise ValueError("Term must be greater than zero.")
                break
            except ValueError as e:
                print(e if "greater" in str(e) else "Not a positive number.")
        
        while True:
            try:
                overpay_pct = float(input("Enter optional monthly overpayment percentage (e.g., 10 for 10%, 0 for none): "))
                if overpay_pct < 0:
                    raise ValueError("Overpayment percentage cannot be negative.")
                break
            except ValueError as e:
                print(e if "negative" in str(e) else "Invalid number.")

        if typ == "monthly":
            periods_per_year = 12
            period_label = "Months"
        elif typ == "weekly":
            periods_per_year = 52
            period_label = "Weeks"
        elif typ == "daily":
            periods_per_year = 365
            period_label = "Days"

        total_periods = math.ceil(years * periods_per_year)
        
        periodic_rate = calculate_periodic_rate(interest_rate, compounding, periods_per_year)

        if periodic_rate > 0:
            min_payment = loan * (periodic_rate * (1 + periodic_rate) ** total_periods) / ((1 + periodic_rate) ** total_periods - 1)
        else:
            min_payment = loan / total_periods

        balance = loan
        periods_taken = 0
        total_interest_paid = 0
        total_paid_overall = 0
        
        base_overpayment = (min_payment * (overpay_pct / 100))

        while balance > 0.01 and periods_taken < 12000:
            periods_taken += 1
            
            interest_charge = balance * periodic_rate
            total_interest_paid += interest_charge
            balance += interest_charge
            
            target_payment = min_payment + base_overpayment
            
            actual_payment = min(target_payment, balance)
            balance -= actual_payment
            total_paid_overall += actual_payment

        print(f"\n--- Results ---")
        print(f"Scheduled term length: {total_periods} {period_label}")
        print(f"Standard payment per period: £{min_payment:.2f}")
        
        if overpay_pct > 0:
            print(f"Actual payment per period (with overpayment): £{min_payment + base_overpayment:.2f}")
            print(f"Actual time to pay back: {periods_taken} {period_label} ({periods_taken / periods_per_year:.1f} years)")
            print(f"Time saved: {total_periods - periods_taken} {period_label}")
        else:
            print(f"Time to pay back: {periods_taken} {period_label}")

        print(f"Total interest paid: £{total_interest_paid:.2f}")
        print(f"Total overall cost: £{total_paid_overall:.2f}")

main()
