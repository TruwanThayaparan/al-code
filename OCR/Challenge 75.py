# Challenge 75 - String permutation
# Created: 07/10/2026
# Last Updated: 07/10/2026

from collections import Counter

def longest_common_permutation(x: str, y: str) -> str:
    common_counts = Counter(x) & Counter(y)
    return "".join(sorted(common_counts.elements()))

def main():
    print("=== STRING PERMUTATION ===")
    print("Enter nothing at any prompt to quit.")
    while True:
        x = input("Enter a word: ")
        if not x:
            print("Goodbye.")
            break
        y = input("Enter another word: ")
        if not y:
            print("Goodbye.")
            break
        
        print(longest_common_permutation(x, y))

main()

'''
def longest_common_permutation(x: str, y: str) -> str:
    count_x = Counter(x)
    count_y = Counter(y)
    
    result = []
    
    for char in sorted(set(count_x.keys()) & set(count_y.keys())):
        min_count = min(count_x[char], count_y[char])
        result.append(char * min_count)
        
    return "".join(result)
'''
