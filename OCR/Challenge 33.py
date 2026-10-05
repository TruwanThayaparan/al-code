# Challenge 33 - Mor-se Coding
# Created: 05/10/2026
# Last Updated: 05/10/2026

MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',
    
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    
    ' ': '|'
}

MORSE_CODE_DICT_REV = {value: key for key, value in MORSE_CODE_DICT.items()}

def main():
    print("Morse Code Encoder and Decoder")
    print("1. Encode\n2. Decode\n3. Exit")
    while True:
        opt = input("Choose an option: ").strip()
        if opt == "1":
            sent = input("Enter a string to encode: ").strip().upper()
            encoded = ""
            for char in sent:
                code = MORSE_CODE_DICT.get(char, '?')
                encoded += code + " "     
            print(f"Encoded Morse Code: {encoded.strip()}")       
        elif opt == "2":
            sent = input("Enter a string to decode: ").strip().upper()
            decoded = ""
            for code in sent.split(" "):
                if code == "":
                    continue
                decoded += MORSE_CODE_DICT_REV.get(code, '?')
            print(f"Decoded Text: {decoded}")
        elif opt == "3":
            print("Goodbye."); break
        else:
            print("Invalid option selected.")

main()
