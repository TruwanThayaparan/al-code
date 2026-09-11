# Challenge 31 - Forwards and Backwards
# Created: 11/09/2026
# Last updated: 11/09/2026

def main():
    print("This is a palindrome checker.")
    while True:
        text = input("Enter something ('q' to quit): ")
        if text in ('q', 'quit', 'exit'):
            break
        text_rev = text[::-1]
        #text_rev = "".join(reversed(text))
        print(text_rev)
        if text == text_rev:
            print("This is a palindrome!\n")
        else:
            print("This is not a palindrome.\n")

main()
