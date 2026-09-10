# Challenge 48 - Reverse it
# Created: 10/09/2026
# Last updated: 10/09/2026

from collections import Counter
from string import ascii_letters

def count_vowels_consonants(text):
    vowels_lower = set("aeiou")
    consonants_lower = set("bcdfghjklmnpqrstvwxyz")
    
    c = Counter(text.lower())
    
    vowel_total = sum(c[v] for v in vowels_lower)
    consonant_total = sum(c[ch] for ch in consonants_lower)
    
    return vowel_total, consonant_total

def main():
    while True:
        text = input("Enter something ('q' to quit): ")
        if text in ('q', 'quit', 'exit'):
            break
        text_rev = "".join(reversed(text))
        print(text_rev)
        if text == text_rev:
            print("This is a palindrome!")
        v, c = count_vowels_consonants(text_rev)
        print(f"Vowels: {v}, Consonants: {c}\n")

main()
