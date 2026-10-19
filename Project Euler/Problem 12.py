# P12 - Highly Divisible Triangular Number
import math

def find_divisors(n):
    divisors = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors

triangle_number = 1
x = 2
while True:
    triangle_number += x
    x += 1
    if find_divisors(triangle_number) > 500:
        print(f"Result: {triangle_number}")
        break
