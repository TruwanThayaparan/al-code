# Challenge 76 - That’s a lot of number
# Created: 10/09/2026
# Last Updated: 10/09/2026

lines = []
with open('example.txt', 'r') as file: # replace example.txt with the place where the numbers are stored
    for line in file:
        lint = line.strip()
        if lint:
            lines.append(int(lint))

total = str(sum(lines))
print(total[0:10])

'''
total = 0
for line in lines:
    total = total + line
'''
