# Challenge 42 - Tilers mate
# Created: 21/09/2026
# Last Updated: 21/09/2026

import math

def main():
    print("--- Tilers Mate ---")
    
    while True:
        try:
            width = float(input("Please enter the width of your floor (m): "))
            if width <= 0:
                raise ValueError
            break
        except ValueError:
            print("The width of the floor must be a positive number.")

    while True:
        try:
            length = float(input("Please enter the length of your floor (m): "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("The length of the floor must be a positive number.")   
            
    area = width * length
    print(f"\nThe area of this floor is {area:.2f}m².")
    
    print("\nAvailable Tile options:")
    print("1. Small Tile (0.3m x 0.6m) - £2.70 each")
    print("2. Large Tile (0.6m x 0.6m) - £9.00 each")
    
    ta1, ta2, tap = 0.3, 0.6, 2.70
    tb1, tb2, tbp = 0.6, 0.6, 9.00
    
    while True:
        opt = input("Enter an option (1 or 2): ").strip()
        if opt not in ("1", "2"):
            print("This is an invalid choice.")
        else:
            break
        
    if opt == "1":
        lentiles = math.ceil(length / ta1)
        widtiles = math.ceil(width / ta2)
        tile_cost_subtotal = (lentiles * widtiles) * tap
    else:
        lentiles = math.ceil(length / tb1)
        widtiles = math.ceil(width / tb2)
        tile_cost_subtotal = (lentiles * widtiles) * tbp

    while True:
        try:
            vat_rate = float(input("\nEnter VAT percentage (e.g., 20): "))
            if not (0 <= vat_rate <= 100):
                raise ValueError
            break
        except ValueError:
            print("VAT must be between 0% and 100%.")
        
    grout_cost = area * 10.00  
    labour_cost = area * 50.00
    
    total_tiles = lentiles * widtiles
    subtotal_no_vat = tile_cost_subtotal + labour_cost + grout_cost
    vat_total = subtotal_no_vat * (vat_rate / 100)
    total_with_vat = subtotal_no_vat + vat_total

    print("\n" + "="*30)
    print("       CUSTOMER QUOTE       ")
    print("="*30)
    print(f"Total tiles required:  {total_tiles} tiles")
    print(f"Tiles Subtotal:        £{tile_cost_subtotal:.2f}")
    print(f"Grout Cost:            £{grout_cost:.2f}")
    print(f"Labour Cost:           £{labour_cost:.2f}")
    print("-"*30)
    print(f"TOTAL (Excluding VAT): £{subtotal_no_vat:.2f}")
    print(f"VAT ({vat_rate}%):         £{vat_total:.2f}")
    print(f"TOTAL (Including VAT): £{total_with_vat:.2f}")
    print("="*30)

main()
