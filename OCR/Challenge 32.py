# Challenge 32 - Code it up
# Created: 23/09/2026
# Last Updated: 23/09/2026

def raw_character_shift(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        result += chr(ord(char) + shift)
            
    return result

def main():
    while True:
        message = input("Enter a message (enter nothing to quit): ")
        if not message:
            break

        while True:
            try:
                secret_key = int(input("Enter secret key: "))
                if not (-1114111 <= secret_key <= 1114111):
                    print("Please enter a key within the safe range (-1114111 to 1114111).")
                    continue
                break
            except ValueError:
                print("You must enter an integer.")

        while True:
            typ = input("Encrypt or decrypt? ").lower().strip()
            if typ not in ("encrypt", "decrypt"):
                print("This is an invalid choice.")
            else:
                break

        answ = raw_character_shift(message, secret_key, mode=typ)
        print(f"The string {message} {typ}ed is: {answ}") 

main()
