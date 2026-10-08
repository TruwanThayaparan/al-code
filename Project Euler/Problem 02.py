# Problem 2 - Even Fibonacci Numbers

# version a
def fibonacci_loop(limit):
    total = 0
    a, b = 0, 1
    while a <= limit:
        a, b = b, a + b
        if a % 2 == 0:
            total += a

    return total

print(fibonacci_loop(4_000_000))

# version b
def sum_even_fibonacci(limit):
    total = 0
    a, b = 2, 8
    
    while a <= limit:
        total += a
        a, b = b, 4 * b + a
        
    return total

print(sum_even_fibonacci(4_000_000))
