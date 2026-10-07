# Challenge 36 - Triangulate (no ext)
# Created: 11/09/2026
# Last Updated: 07/10/2026

import math

def triangle_checker(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "No side can be negative or 0."
    
    if not (a + b > c and a + c > b and b + c > a):
        return "Not a triangle"
    
    is_right = (math.isclose(a**2 + b**2, c**2) or 
                math.isclose(a**2 + c**2, b**2) or 
                math.isclose(b**2 + c**2, a**2))
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Right-angled and Isosceles." if is_right else "Isosceles"
    else:
        return "Right-angled and Scalene." if is_right else "Scalene"

def side_finder(a, b, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    c_squared = a**2 + b**2 - 2 * a * b * math.cos(angle_radians)
    return math.sqrt(c_squared)
    
def main():
    print("--- Triangle Checker and Side Solver ---")
    print("1. Check if a shape is a triangle")
    print("2. Figure out 3rd side where 2 sides and 1 angle are given")
    print("3. Quit")

    while True:
        ch = input("\nEnter an option (1, 2, 3): ").strip()

        if ch == "1":
            while True:
                try:
                    side1 = float(input("Enter side 1 of triangle: "))
                    side2 = float(input("Enter side 2 of triangle: "))
                    side3 = float(input("Enter side 3 of triangle: "))
                    print(f"Result: {triangle_checker(side1, side2, side3)}")
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

        elif ch == "2":
            while True:
                try:
                    side1 = float(input("Enter side 1 of triangle: "))
                    side2 = float(input("Enter side 2 of triangle: "))
                    
                    if side1 <= 0 or side2 <= 0:
                        print("Side lengths must be greater than 0.")
                        continue
                        
                    ang = float(input("Enter included angle (in degrees): "))
                    
                    if ang <= 0 or ang >= 180:
                        print("Angle must be between 0 and 180 degrees.")
                        continue
                        
                    third_side = side_finder(side1, side2, ang)
                    print(f"The length of the 3rd side is: {third_side:.4f}")
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

        elif ch == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()
