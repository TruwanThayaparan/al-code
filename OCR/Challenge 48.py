# challenge 48 - reverse it (draft)
# created: 10/09/2026
# last updated: 10/09/2026

from collections import Counter
from string import ascii_letters

def count_vowels_consonants(text):
    vowels_lower = set("aeiou")
    consonants_lower = set("bcdfghjklmnpqrstvwxyz")
    
    c = Counter(text.lower())
    
    vowel_total = sum(c[v] for v in vowels_lower)
    consonant_total = sum(c[ch] for ch in consonants_lower)
    
    return vowel_total, consonant_total

text = input("enter something: ")
textrev = "".join(reversed(text))
print(textrev)

v, c = count_vowels_consonants(textrev)
print(f"Vowels: {v}, Consonants: {c}")
