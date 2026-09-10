# Challenge 41 - Prime Factorisation
# Created: 10/09/2026
# Last Updated: 10/09/2026

from collections import Counter

def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
      if n % i == 0:
          factors.append(i)
          n = n // i
      else:
          i += 1
  
    if n > 1:
        factors.append(n)

    counts = Counter(factors)
    output_parts = []
    
    for item, count in counts.items():
        if count > 1:
            output_parts.append(f"{item}^{count}")
        else:
            output_parts.append(f"{item}")
            
    formatted_string = " * ".join(output_parts)

    return factors, formatted_string
    
def main():
    while True:
        try:
            x = input("Enter a number (prime factorisation): ").strip().lower()
            if x in ("q", "quit", "exit"):
                break
            x = int(x)
            if x <= 1:
                raise ValueError
            factors, formatted = prime_factor(x)
            print(f"List of prime factors: {factors}")
            print(f"Mathematical form: {formatted}\n")
        except ValueError:
            print("You must enter a positive integer greater than 1.\n")
  
main()
