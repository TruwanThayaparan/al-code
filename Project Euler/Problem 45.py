# P45 - Triangular, Pentagonal, and Hexagonal
import math

def is_pentagonal(x): # inverse of: n(3n-1)/2
    m = (math.sqrt(24 * x + 1) + 1) / 6
    return m.is_integer()

k = 144 # from 40755

while True:
    hk = k * (2 * k - 1)
    
    if is_pentagonal(hk): # every hexagonal number is a triangular number
        print(f"Match found!")
        print(f"Hexagonal Index (k): {k}")
        print(f"The Number is: {hk}")
        break
        
    k += 1
