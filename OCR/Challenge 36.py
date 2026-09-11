# Challenge 36 - Triangulate (no ext)
# Created: 11/09/2026
# Last Updated: 11/09/2026

from math import isclose

def triangle_checker(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "No side can be negative or 0."
    if a + b > c and a + c > b and b + c > a:
        pass
    else:
        return "Not a triangle"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if isclose(a**2 + b**2, c**2) \
        or isclose(a**2 + c**2, b**2) \
        or isclose(b**2 + c**2, a**2):
            return "Right-angled and Isosceles."
        return "Isosceles"
        
    if isclose(a**2 + b**2, c**2) \
    or isclose(a**2 + c**2, b**2) \
    or isclose(b**2 + c**2, a**2):
        return "Right-angled."
    else:
        return "Scalene"

def main():
    while True:
        try:
            side1 = float(input("Enter side 1 of triangle: "))
            side2 = float(input("Enter side 2 of triangle: "))
            side3 = float(input("Enter side 3 of triangle: "))
            print(triangle_checker(side1, side2, side3))
        except ValueError:
            print("Invalid input.")
        
        if input("Continue? ").strip().lower() == "no":
            break

main()
