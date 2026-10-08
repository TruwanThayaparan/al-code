def prime_check(i):
    if i <= 1: return False
    if i == 2: return True
    if i % 2 == 0: return False
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            return False
    return True

primes_found = 0
x = 0

while primes_found < 10001:
    x += 1
    if prime_check(x):
        primes_found += 1

print(f"The 10,001st prime number is: {x}")
