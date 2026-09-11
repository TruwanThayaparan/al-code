# challenge 25 - ordering (unfinished)
# created: 11/09/2026
# last updated: 11/09/2026

def sort(nums):
    while True:
        typ = input("Order by ascension or descension: ").strip().lower()
        if typ not in ("ascend", "ascending", "ascension", "asc") and typ not in ("descend", "descending", "descension", "desc"):
            print("Invalid.")
            continue
        break

    if typ in ("ascend", "ascending", "ascension", "asc"):
        print(sorted(nums))
    else:
        print(list(reversed(sorted(nums))))

def main():
    while True:
        try:
            txt = input("Enter 10 numbers: ").strip().lower()
            if txt in ("quit", "q", "exit"):
                break
            txtsp = txt.split()
            if len(txtsp) != 10:
                print("You must enter 10 integers.")
                continue
            for i in range(len(txtsp)):
                txtsp[i] = int(txtsp[i])
            sort(txtsp)
        except ValueError:
            print("You must enter 10 integers.")

main()
