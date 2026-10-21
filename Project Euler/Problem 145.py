# P145 - Reversible Numbers
def count_reversible_instantly(limit):
    max_digits = len(str(limit - 1))
    total = 0
    
    for d in range(1, max_digits + 1):
        if d % 4 == 0 or d % 4 == 2:
            total += 20 * (30 ** (d // 2 - 1))
        elif d % 4 == 3:
            total += 100 * (500 ** (d // 4))
            
    return total

print(count_reversible_instantly(1_000_000_000)) # outputs 608,720
