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
        print("".join(map(str, res)))
    else:
        print(" ".join(map(str, res)))
    
    print("\n")

def num_sort():
    while True:
        try:
            txt = input("Enter 10 numbers: ").strip().lower()
            if txt in ("return"):
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

def alpha_sort():
    txt = input("Enter a string: ").strip().lower()
    jargon = []
    for i in txt:
        if i == " ":
            continue
        jargon.append(i)
        
    order(jargon, True)

def main():
    print("1. Order numbers by asc/desc")
    print("2. Order strings into alphabetical order")
    print("3. Quit")
    while True:
        mode = input("Enter (1, 2, 3): ")
        if mode not in ("1", "2", "3"):
            print("Invalid type.")
        if mode in ("quit", "q", "exit", "3"):
            break
        if mode == "1":
            num_sort()
        if mode == "2":
            alpha_sort()

main()
