# Challenge 10 - Number Names
# Created: 23/09/2026
# Last Updated: 23/09/2026

num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]

actual_values = list(range(21)) + [30, 40, 50, 60, 70, 80, 90]
num_to_word = dict(zip(actual_values, num_list))

def integer_to_words(nc):
    if nc in num_to_word:
        return num_to_word[nc]
        
    if nc < 100:
        tens = (nc // 10) * 10
        ones = nc % 10
        return f"{num_to_word[tens]}-{num_to_word[ones]}"
        
    if nc < 1000:
        hundreds = nc // 100
        remainder = nc % 100
        if remainder == 0:
            return f"{num_to_word[hundreds]} hundred"
        return f"{num_to_word[hundreds]} hundred and {integer_to_words(remainder)}"
        
    if nc < 1000000:
        thousands = nc // 1000
        remainder = nc % 1000
        if remainder == 0:
            return f"{integer_to_words(thousands)} thousand"
        sep = " and " if remainder < 100 else ", "
        return f"{integer_to_words(thousands)} thousand{sep}{integer_to_words(remainder)}"
        
    if nc < 1000000000:
        millions = nc // 1000000
        remainder = nc % 1000000
        if remainder == 0:
            return f"{integer_to_words(millions)} million"
        sep = " and " if remainder < 100 else ", "
        return f"{integer_to_words(millions)} million{sep}{integer_to_words(remainder)}"

    if nc < 1000000000000:
        billions = nc // 1000000000
        remainder = nc % 1000000000
        if remainder == 0:
            return f"{integer_to_words(billions)} billion"
        sep = " and " if remainder < 100 else ", "
        return f"{integer_to_words(billions)} billion{sep}{integer_to_words(remainder)}"

    if nc < 1000000000000000:
        trillions = nc // 1000000000000
        remainder = nc % 1000000000000
        if remainder == 0:
            return f"{integer_to_words(trillions)} trillion"
        sep = " and " if remainder < 100 else ", "
        return f"{integer_to_words(trillions)} trillion{sep}{integer_to_words(remainder)}"
        
    return "None"

def number_to_words(raw_string):
    raw_string = raw_string.strip()
    
    prefix = ""
    if raw_string.startswith("-"):
        prefix = "minus "
        raw_string = raw_string[1:]
        
    if "." in raw_string:
        integer_part, decimal_part = raw_string.split(".", 1)
    else:
        integer_part, decimal_part = raw_string, ""
        
    try:
        # Defaults to 0 if someone inputs just ".5"
        int_val = int(integer_part) if integer_part else 0 
    except ValueError:
        return "Error: Invalid integer component."
        
    words_built = integer_to_words(int_val)
    if words_built == "None":
        return "Error: Number too large for custom converter."
        
    result = prefix + words_built
    
    if decimal_part:
        decimal_words = []
        for digit in decimal_part:
            if digit.isdigit():
                decimal_words.append(num_to_word[int(digit)])
            else:
                return "Error: Invalid decimal component."
        result += " point " + " ".join(decimal_words)
        
    return result

def main():
    print("Number Name Generator (type 'q' to quit)")
    while True:
        user_input = input("Enter any number: ").strip()
        if user_input.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if not user_input:
            continue
            
        print(f"Output: {number_to_words(user_input)}\n")

main()
