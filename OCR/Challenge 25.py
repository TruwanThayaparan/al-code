# challenge 25 - ordering (unfinished)
# created: 11/09/2026
# last updated: 11/09/2026

def order(nums, t):
    while True:
        typ = input("Order by ascension or descension: ").strip().lower()
        if typ not in ("ascend", "ascending", "ascension", "asc") and typ not in ("descend", "descending", "descension", "desc"):
            print("Invalid.")
            continue
        break

    if typ in ("ascend", "ascending", "ascension", "asc"):
        res = sorted(nums)
    else:
        res = sorted(nums, reverse=True)

    if t:
        print("Result: " + "".join(map(str, res)))
    else:
        print("Result: " + " ".join(map(str, res)))
    
    print("\n")

def num_sort():
    while True:
        try:
            txt = input("Enter 10 numbers (or 'return'): ").strip().lower()
            if txt == "return":
                return
            txtsp = txt.split()
            if len(txtsp) != 10:
                print("You must enter 10 integers.")
                continue
            for i in range(len(txtsp)):
                txtsp[i] = int(txtsp[i])
            order(txtsp, False)
            return
        except ValueError:
            print("You must enter 10 integers.")

def alpha_sort(keep_spaces):
    txt = input("Enter a string: ").lower()
    
    if not keep_spaces:
        for i in txt:
            if i != " ":
                jargon.append(i)
        order(jargon, True)
    else:
        words = txt.split(" ")
        typ = ""
        while True:
            typ = input("Order by ascension or descension: ").strip().lower()
            if typ not in ("ascend", "ascending", "ascension", "asc") and typ not in ("descend", "descending", "descension", "desc"):
                print("Invalid.")
                continue
            break
            
        is_reverse = False
        if typ not in ("ascend", "ascending", "ascension", "asc"):
            is_reverse = True
        
        sorted_words = []
        for word in words:
            sorted_word = "".join(sorted(list(word), reverse=is_reverse))
            sorted_words.append(sorted_word)
            
        print("Result: " + " ".join(sorted_words))
        print("\n")

def main():
    print("1. Order numbers by asc/desc")
    print("2. Order strings into alphabetical order (don't keep spaces)")
    print("3. Order strings into alphabetical order (keep spaces)")
    print("4. Quit")
    while True:
        mode = input("Enter (1, 2, 3, 4): ")
        if mode not in ("1", "2", "3", "4"):
            print("Invalid type.")
            print(" ")
            continue

        print(" ")
        if mode in ("quit", "q", "exit", "4"):
            break
        elif mode == "1":
            num_sort()
        elif mode == "2":
            alpha_sort(False)
        else:
            alpha_sort(True)

main()
