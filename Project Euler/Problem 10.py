def prime_check(i):
    if i <= 1: return False
    if i == 2: return True
    if i % 2 == 0: return False
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            return False
    return True

total = 0
x = 2_000_000

while x > 0:
    x -= 1
    if prime_check(x):
        total += x

print(f"Total of prime numbers under 2 million is: {total}")
