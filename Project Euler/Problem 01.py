# Problem 1 - Multiples of 3 or 5

# version a
n = 1000
total = 0
for i in range(n):
    if i % 3 == 0:
        print(f"{i} = Multiple of 3")
        total += i
    elif i % 5 == 0:
        print(f"{i} = Multiple of 5")
        total += i
    else:
        print(f"{i} = None")
    
print(total)

# version b
max3, max5, max15 = n - 1, n - 1, n - 1
min3, min5, min15 = 1, 1, 1
while max3 % 3 != 0:
    max3 -= 1
while min3 % 3 != 0:
    min3 += 1

while max5 % 5 != 0:
    max5 -= 1
while min5 % 5 != 0:
    min5 += 1

while max15 % 15 != 0:
    max15 -= 1
while min15 % 15 != 0:
    min15 += 1

term3 = max3/min3
term5 = max5/min5
term15 = max15/min15
sum3 = (term3/2) * (min3 + max3)
sum5 = (term5/2) * (min5 + max5)
sum15 = (term15/2) * (min15 + max15)

total2 = ((sum3 + sum5)- sum15)
print(f"{total2:.0f}")

# version c
def sum_multiples_up_to(limit, k):
    n = (limit - 1) // k
    return k * n * (n + 1) // 2

limit = 1000

total = (sum_multiples_up_to(limit, 3) + 
         sum_multiples_up_to(limit, 5) - 
         sum_multiples_up_to(limit, 15))

print(total)
