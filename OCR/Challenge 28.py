# challenge 28 - name that number
# created -> 15th september 2026
# last updated -> 15th september 2026

import urllib.request
import re

avail = True
try:
    url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
    print("Loading dictionary... Please wait.")
    with urllib.request.urlopen(url) as response:
        raw_data = response.read().decode('utf-8')
        english_words = {word.strip().lower() for word in raw_data.splitlines()}
    print("Dictionary loaded successfully!\n")
except Exception:
    print("ERROR: Connection cannot be made to website. Checking for built-in offline dictionary...")
    try:
        with open('/usr/share/dict/words', 'r') as file:
            english_words = {line.strip().lower() for line in file}
        print("Switched to your computer's built-in offline dictionary.")
    except FileNotFoundError:
        try:
            with open('words.txt') as idsave:
                english_words = {word.strip().lower() for word in idsave.read().splitlines()}
        except Exception:
            print("Cannot load. Dictionary feature is unavailable.")
            avail = False

print()
letter_to_digit = {
    'A': '2', 'B': '2', 'C': '2', 'a': '2', 'b': '2', 'c': '2',
    'D': '3', 'E': '3', 'F': '3', 'd': '3', 'e': '3', 'f': '3',
    'G': '4', 'H': '4', 'I': '4', 'g': '4', 'h': '4', 'i': '4',
    'J': '5', 'K': '5', 'L': '5', 'j': '5', 'k': '5', 'l': '5',
    'M': '6', 'N': '6', 'O': '6', 'm': '6', 'n': '6', 'o': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'p': '7', 'q': '7', 'r': '7', 's': '7',
    'T': '8', 'U': '8', 'V': '8', 't': '8', 'u': '8', 'v': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9', 'w': '9', 'x': '9', 'y': '9', 'z': '9'
}

def text_to_phone(text):
    return "".join(letter_to_digit.get(char, char) for char in text)

def verify_words_in_input(text):
    input_words = re.findall(r'[a-zA-Z]+', text)
    
    if not input_words:
        return
        
    print("--- Dictionary Check ---")
    for word in input_words:
        lower_word = word.lower()
        if lower_word in english_words:
            print(f"'{word}' is a valid English word.")
        else:
            print(f"'{word}' is NOT in the dictionary.")
    print("------------------------")

def main():
    while True:
        ph = input("Enter phone number ('q' to quit): ")
        if ph.lower() == 'q':
            break
            
        if avail:
            verify_words_in_input(ph)

        print(f"Converted number: {text_to_phone(ph)}\n")

main()
