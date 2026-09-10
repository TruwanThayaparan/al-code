# Challenge 41 - Prime Factorisation
# Created: 10/09/2026
# Last Updated: 10/09/2026

def prime_factor(n):
    i = 2
    factors = []
    while n > 1:
      if n % i == 0:
          factors.append(i)
          n = n // i
      else:
          i += 1
  
    return factors
    
def main():
    while True:
        try:
            x = input("Enter a number (prime factorisation): ").strip().lower()
            if x in ("q", "quit", "exit"):
                break
            x = int(x)
            if x <= 1:
                raise ValueError
            print(prime_factor(x))
        except ValueError:
            print("You must enter a positive integer greater than 1.")
  
main()
