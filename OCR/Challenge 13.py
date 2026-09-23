# Challenge 13 - Caesar Cipher
# Created: 23/09/2026
# Last Updated: 23/09/2026

def caesar_cipher(text, shift, mode='encrypt') -> str:
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
            
    return result

def main():
    while True:
        message = input("Enter a message ('q' to quit): ")
        if message in ("q", "quit", "exit"):
            break

        while True:
            try:
                secret_key = int(input("Enter secret key: "))
                if not (1 <= secret_key <= 25):
                    raise ValueError
                break
            except ValueError:
                print("You must enter an integer between 1 and 25")

        while True:
            typ = input("Encrypt or decrypt? ").lower().strip()
            if typ not in ("encrypt", "decrypt"):
                print("This is an invalid choice")
            else:
                break

        answ = caesar_cipher(message, secret_key, mode=typ)
        print(f"The string {message} {typ}ed is: {answ}") 

main()
