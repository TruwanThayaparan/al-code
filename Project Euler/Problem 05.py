# v3
import math
from functools import reduce
result = reduce(math.lcm, range(1, 21))
print(result)

# v2
import math
result = 1
for i in range(1, 21):
    result = (result * i) // math.gcd(result, i)
print(result) 

# v1
x = 20
while True:
    x += 20
    f = True
    for i in range(1, 21):
        if x % i != 0:
            f = False
            break
    
    if f:
        print(x)
        break
