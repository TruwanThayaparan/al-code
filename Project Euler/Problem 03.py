# P3 - Largest Prime Factor
def max_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
            
    return n

print(max_prime_factor(600851475143)) # outputs '6857'
