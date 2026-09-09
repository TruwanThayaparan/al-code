# Challenge 15 - Pangrams
# Created: 09/09/2026
# Last Updated: 09/09/2026

char_set = set("abcdefghijklmnopqrstuvwxyz") # cleaner than having list of all letters
sorted_char_list = sorted(list(char_set)) 

def pangram_check(pgl):
    words = []
    for x in pgl:
        lettersonly = ""
        for char in x:
            if char.isalpha():
                lettersonly += char.lower()
            
        removedupesort = sorted(set(lettersonly))
        words.append(sorted_char_list == removedupesort)
        
    return words
  
def main():
    pan = []
    while True:
        text = input("Enter something into the pangram checker (type 'c' to check your inputs and 'q' to quit): ")
        if text.lower() in ("quit", "q", "exit"):
            break
        elif text.lower() in ("c", "check"):
            res = pangram_check(pan)
            for i in res:
                print(i)
            pan = []
        else:
            pan.append(text)

main()

'''
alt:
lettersonly = "".join([char.lower() for char in text if char.isalpha()])
lettersonly = "".join([char.lower() for char in x if
'''
