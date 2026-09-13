# Challenge 39 - Even more Odd
# Created: 13/09/2026
# Last Updated: 13/09/2026

def order(txt_list):
    chars = []
    nums = []
    
    for item in txt_list:
        if item.isalpha():
            chars.append(item)
        else:
            nums.append(int(item))

    chars_sorted = sorted(chars, reverse=True)
    nums_sorted = sorted(nums)

    print("Result (Numbers): " + " ".join(map(str, nums_sorted)))
    even_list = []
    odd_list = []
    for i in nums_sorted:
        if i % 2 == 0:
            #print("even")
            even_list.append(i)
        else:
            #print("odd")
            odd_list.append(i)

    odd_list.extend(even_list) 
    print("Result (Odd, Even): " + " ".join(map(str, odd_list)))
    chars_sorted.extend(odd_list)
    print("Result (Characters, Odd, Even): " + " ".join(map(str, chars_sorted)))
    print("\n")
  
def main():
    while True:
        try:
            txt = input("Enter 10 inputs ('q' to quit): ").strip()
            if txt.lower() in ("q", "quit", "exit"):
                break
            txtsp = txt.split()
            if len(txtsp) != 10:
                print("You must enter 10 inputs.")
                continue

            valid = True
            for item in txtsp:
                is_numeric = False # negative check
                try:
                    int(item)
                    is_numeric = True
                except ValueError:
                    pass

                if not (is_numeric or item.isalpha()):
                    print(f"Invalid input: '{item}'. Must be an integer or a letter.")
                    valid = False
                    break
            
            if not valid:
                continue

            order(txtsp)
        except ValueError:
            print("ERROR: Try again.")

main()
