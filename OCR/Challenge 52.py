# Challenge 52 - Is this card valid?
# Created: 05/10/2026
# Last Updated: 05/10/2026

cardnumber = 4111111111111111 

cardnumstr = str(cardnumber)
length = len(cardnumstr)
vendor = "Unknown/Invalid Vendor"

if cardnumstr.startswith('4') and (length == 13 or length == 16):
    vendor = "Visa"
elif (51 <= int(cardnumstr[:2]) <= 55 or 2221 <= int(cardnumstr[:4]) <= 2720) and length == 16:
    vendor = "MasterCard"
elif (cardnumstr.startswith('34') or cardnumstr.startswith('37')) and length == 15:
    vendor = "American Express"
elif (cardnumstr.startswith('6011') or cardnumstr.startswith('65') or 644 <= int(cardnumstr[:3]) <= 649) and length == 16:
    vendor = "Discover"

tot = []
for i, digit_char in enumerate(reversed(cardnumstr)):
    digit = int(digit_char)
    if i % 2 == 1:
        tot.append(digit * 2)
    else:
        tot.append(digit)

tot.reverse()

for index in range(len(tot)):
    item_str = str(tot[index])
    if len(item_str) == 2:
        tot[index] = int(item_str[0]) + int(item_str[1])

al = sum(tot)

if al % 10 == 0 and vendor != "Unknown/Invalid Vendor":
    print(f"The card is a VALID {vendor} card. (Checksum total: {al})")
else:
    print(f"The card is INVALID. (Vendor identified: {vendor}, Checksum total: {al})")
