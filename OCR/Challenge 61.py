# Challenge 61 - Your name is...
# Created: 13/09/2026
# Last Updated: 13/09/2026

name = input("Enter your name: ")
age = input("Enter your age: ")
form = input("Enter your form: ")
full = f"Your name is {name}, you are {age} years old, and you are in form {form}.\n"

print(full)
with open("basicinfo.txt", "a") as f:
    f.write(full)
