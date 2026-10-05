# Challenge 8 - Arithmetic test
# Created: 05/10/2026
# Last Updated: 05/10/2026

import random
import json
import os

def gen_questions(c, oper):
    questions = []
    numasn = []
    numbsn = []
    
    for _ in range(c):
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
        else:
            raise ValueError("Invalid unit passed.")

        questions.append(unit)
        numasn.append(numa)
        numbsn.append(numb)
        
    return questions, numasn, numbsn

def main():
    print("--- Arithmetic Test ---")
    quecount = 10
    opers = ["+", "-", "*", "/"]
    for op in opers:
        if op not in ["+", "-", "*", "/"]:
            print(f"Error: '{op}' is not a valid math operator. Please remove it.")
            return

    que, nx, ny = gen_questions(quecount, opers)

    while True:
        name = input("Enter your name: ").strip().capitalize()
        if name:
            break
        print("You must enter your name to continue.")

    forms = ["A", "B", "C"]
    while True:
        form = input("Enter your class (A, B, C): ").strip().upper()
        if form in forms:
            break
        print("Invalid class. You must enter your class as A, B, or C.")

    correct = 0
    for i in range(quecount):
        while True:
            try:
                ans = int(input(f"Question {i + 1}: What is {nx[i]} {que[i]} {ny[i]}? "))
                break
            except ValueError:
                print("Invalid input. You must enter a whole number.")
        
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
    
    fname = f"class_{form.lower()}_results.json"
    
    if os.path.exists(fname):
        with open(fname, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    if name not in data:
        data[name] = []
    data[name].append(correct)
    data[name] = data[name][-3:]

    with open(fname, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"Your score has been saved to {fname}.\n")

def obtain_stats():
    print("--- TEACHER MANAGEMENT SYSTEM ---")
    forms = ["A", "B", "C"]
    
    while True:
        form = input("Which class stats would you like to view? (A/B/C): ").upper().strip()
        if form in forms:
            break
        print("Invalid class selection.")

    fname = f"class_{form.lower()}_results.json"
    
    if not os.path.exists(fname):
        print(f"No records found for Class {form}.")
        return

    with open(fname, "r") as f:
        data = json.load(f)

    if not data:
        print(f"No student data found in Class {form}.")
        return

    print(f"\nResults for Class {form} (Alphabetical Order, Highest Score First):")
    print("-" * 50)
    
    for student in sorted(data.keys()):
        scores = data[student]
        sorted_scores = sorted(scores, reverse=True)
        scores_str = ", ".join(map(str, sorted_scores))
        print(f"{student}: {scores_str}")
    print("-" * 50)

main()
print()
obtain_stats()
