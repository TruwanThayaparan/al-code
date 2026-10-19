# P48 - Self Powers
total = 0
for i in range(1, 1001):
    total += i**i

d = str(total)
l = len(d)
print(d[l-10:l])


MOD = 10**10
total = 0 

for i in range(1, 1001):
    total = (total + pow(i, i, MOD)) % MOD

print(total) # Output: 9110846700
