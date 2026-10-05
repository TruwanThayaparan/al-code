# arithmetic test without extension 2 (commit)

import random

def main():
    def gen_questions(c, oper):
        questions = []
        numasn = []
        numbsn = []
        
        for i in range(c):
            unit = random.choice(oper)
            
            if unit == "+" or unit == "-":
                numa = random.randint(1, 99)
                numb = random.randint(1, 99)
                if unit == "-" and numa < numb:
                    numa, numb = numb, numa 
            elif unit == "*":
                numa = random.randint(1, 12)
                numb = random.randint(1, 12)
            elif unit == "/":
                rans = random.randint(1, 12)
                numb = random.randint(1, 12)
                numa = rans * numb 

            questions.append(unit)
            numasn.append(numa)
            numbsn.append(numb)
            
        return questions, numasn, numbsn

    quecount = 10
    que, nx, ny = gen_questions(quecount, ["+", "-", "*", "/"])

    while True:
        name = input("Enter your name: ").capitalize().strip()
        if name:
            break
        print("You must enter your name to continue.")

    forms = ["A", "B", "C"]
    while True:
        form = input("Enter your class (A/B/C): ").upper().strip()
        if form in forms:
            break
        print("Invalid class.")

    correct = 0
    for i in range(quecount):
        while True:
            try:
                ans = int(input(f"What is {nx[i]} {que[i]} {ny[i]}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        
        if que[i] == "+":
            rans = nx[i] + ny[i]
        elif que[i] == "-":
            rans = nx[i] - ny[i]
        elif que[i] == "*":
            rans = nx[i] * ny[i]
        elif que[i] == "/":
            rans = nx[i] // ny[i] 

        if ans == rans:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer was {rans}.")

    print(f"\nAll questions complete, {name}! You got {correct} out of {quecount} correct.")
    
    fname = f"class_{form.lower()}_results.txt"
    with open(fname, "a") as f:
        f.write(f"{name},{correct}\n") 
    print(f"Your score has been saved to {fname}.")

def obtain_stats():
    return

main()

obtain_stats()
