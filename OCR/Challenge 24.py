# Challenge 24 - Hack-proof
import hashlib
import string
import random
import os

def error_check(pasw):
    erlo = []
    if len(pasw) < 8:
        erlo.append("Password must be at least 8 characters long.")
    if not any(c.isupper() for c in pasw):
        erlo.append("Password must contain upper-case letters.")
    if not any(c.islower() for c in pasw):
        erlo.append("Password must contain lower-case letters.")
    if not any(not c.isalnum() and not c.isspace() for c in pasw):
        erlo.append("Password must contain special characters.")

    return True if not erlo else erlo

'''
def gen_basic_pw():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(random.randint(8,16)))
'''

def gen_complex_pw():
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(chars) for _ in range(random.randint(8,16)))
        if error_check(password) == True:
            return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def pw_gen():
    print("--- REGISTRATION ---")
    while True:
        usr = input("Enter your username: ").strip() 
        if not usr:
            print("You must enter a username.")
        else:
            break

    #suggested_basic = gen_basic_pw()
    suggested_complex = gen_complex_pw()
    #(f"\nSuggested Basic Password: {suggested_basic}")
    print(f"Suggested Secure Password: {suggested_complex}\n")
    
    while True:
        pw = input("Enter your chosen password: ").strip()
        pc = error_check(pw)

        if pc == True:
            hashed_pw = hash_password(pw)
            with open("basicinfo.txt", "a") as f:
                f.write(f"{usr},{hashed_pw}\n")
            print("Account successfully created and secured!\n")
            break
        else:
            print("ERRORS DETECTED:")
            for p in pc: 
                print(f"- {p}")
            print()

def open_secure_document():
    secret_filename = "secret_document.txt"
    if not os.path.exists(secret_filename):
        with open(secret_filename, "w") as f:
            f.write("You Did It!")

    print(f"--- Opening Secure Document '{secret_filename}' ---")
    with open(secret_filename, "r") as f:
        print("\n================ DOCUMENT CONTENT ================")
        print(f.read())
        print("==================================================\n")

def enter():
    print("--- LOGIN ---")
    while True:
        usrn = input("Enter username: ").strip()
        pwn = input("Enter password: ").strip()
        
        authenticated = False
        
        try:
            with open('basicinfo.txt', 'r') as file:
                for line in file:
                    if ',' in line:
                        saved_usr, saved_hashed_pw = line.strip().split(',', 1)
                        if usrn == saved_usr and hash_password(pwn) == saved_hashed_pw:
                            authenticated = True
                            break
        except FileNotFoundError:
            print("No accounts database found. Please register first.")
            return

        if not authenticated:
            print("Incorrect username or password. Try again.\n")
        else:
            print("Login successful!\n")
            open_secure_document()
            break

pw_gen()
enter()
