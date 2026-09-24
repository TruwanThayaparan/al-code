# Challenge 51 - Text-speak converter
# Created: 24/09/2026
# Last Updated: 24/09/2026

word_book = {
    "lol": "laugh out loud",
    "omg": "oh my god",
    "idc": "i don't care",
    "icl": "i can't lie",
    "idk": "i don't know"
}

def translate_string(text):
    lines = text.splitlines()
    converted_lines = []
    
    for line in lines:
        words = line.split()
        converted_words = []
        for p in words:
            clean_word = p.lower()
            if word_book.get(clean_word):
                converted_words.append(word_book[clean_word])
            else:
                converted_words.append(p)
        converted_lines.append(" ".join(converted_words))
        
    return "\n".join(converted_lines)

def tsconvert():
    rig = input("Enter a string: ")
    converted = translate_string(rig)
    print(f"Converted: {converted}\n")

def file_convert():
    filename = input("Enter the name of the file to read (e.g., input.txt): ").strip()
    try:
        with open(filename, "r") as file:
            file_content = file.read()
        
        print("\nOriginal File Content:")
        print(file_content)
        
        converted_content = translate_string(file_content)
        
        print("\nConverted File Content:")
        print(f"{converted_content}\n")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please make sure it exists.\n")

def adnt():
    while True:
        w = input("Enter the abbreviation to add ('q' to return): ").strip().lower()
        if w == "q":
            return
        if w == "":
            print("Nothing was entered. Try again.")
            continue
        s = input("Enter the full form: ").strip()
        if s == "":
            print("Nothing was entered. Try again.")
            continue
        word_book[w] = s
        print(f"Successfully added '{w}' -> '{s}'\n")

def view_terms():
    print("\nCurrent Dictionary:")
    for abbr, full_form in word_book.items():
        print(f"  {abbr} -> {full_form}")
    print("\n")
    
def main():
    print("Welcome to the Text-Speak Converter.")
    while True:
        print("1. Convert text input\n2. Add new terms\n3. View terms\n4. Convert text from a file\n5. Exit")
        rig = input("Enter an option (1, 2, 3, 4, or 5): ").strip()
        if rig == "1":
            tsconvert()
        elif rig == "2":
            adnt()
        elif rig == "3":
            view_terms()
        elif rig == "4":
            file_convert()
        elif rig in ("5", "q", "quit", "exit"):
            print("Goodbye.")
            break
        else:
            print("Invalid input. Please try again.\n")

main()
