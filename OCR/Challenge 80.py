# challenge 80 - happy hopper
# created: 17/09/2026
# last updated: 17/09/2026

def happy_hop_check(sn):
    n = len(sn)
    
    if n == 1:
        return True
        
    expected_diffs = set(range(1, n))
    actual_diffs = set()
    
    for s in range(n - 1):
        diff = abs(sn[s + 1] - sn[s])
        
        if diff < 1 or diff >= n:
            return False
            
        actual_diffs.add(diff)
        
    return actual_diffs == expected_diffs

def main():
    while True:
        hhs = input("Enter a sequence of integers (e.g., '1 4 2 3'): ")
        split_numbers = hhs.split()
        if not split_numbers:
            print("You need to enter something!")
            continue

        try:
            split_numbers = [int(n) for n in split_numbers]
        except ValueError:
            print("Error: All inputs must be integers.\n")
            continue    

        if happy_hop_check(split_numbers):
            print("This sequence of integers is a happy hopper.\n")
        else:
            print("This sequence of integers is not a happy hopper.\n")

main()
