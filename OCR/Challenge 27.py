# Challenge 27 - Word Subtraction
# Created: 18/09/2026
# Last Updated: 18/09/2026

def text_to_ascii_numbers(text: str) -> int:
    return sum(ord(char) for char in text)

def remove_dupes(wa, wb):
    ra = "".join([char for char in wa if char.lower() not in wb.lower()])
    rb = "".join([char for char in wb if char.lower() not in wa.lower()])
    return ra, rb

def main():
    print("Welcome to Word Subtraction. Enter nothing at any point to end the program.")
    while True:
        word_a = input("Enter a word: ")
        if not word_a.strip(): print("Goodbye!"); break
        word_b = input("Enter a second word: ")
        if not word_b.strip(): print("Goodbye!"); break
        n1 = text_to_ascii_numbers(word_a)
        n2 = text_to_ascii_numbers(word_b)
        print(f"Word 1 ASCII total: {n1}")
        print(f"Word 2 ASCII total: {n2}")
        print(f"Subtraction (W2-W1): {n2 - n1}")
        result_a, result_b = remove_dupes(word_a, word_b)
        print(f'Removed shared letters: "{result_a}" and "{result_b}"')
        print()
main()
