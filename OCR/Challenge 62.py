# Challenge 62 - R@nd0m P@ssw0rd generator (slightly edited version of my Hack-proof solution)
# Created: 02/10/2026
# Last Updated: 02/10/2026

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

def gen_strong_ascii_pw():
    length = random.randint(12, 16) 
  
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation) 
    
    extended_ascii = [chr(i) for i in range(128, 256)]
    
    all_chars = string.ascii_letters + string.digits + string.punctuation + extended_ascii
    remaining = [random.choice(all_chars) for _ in range(length - 4)]
    
    password_list = [lower, upper, digit, special] + remaining
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    with open("generated_passwords.txt", "a", encoding="utf-8") as f:
        f.write(f"{password}\n")
        
    return password

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def pw_gen():
    print("--- REGISTRATION ---")
    while True:
        usr = input("Enter your username: ").strip() 
        if not usr:
            print("You must enter a username.")
            continue
            
        user_exists = False
        try:
            with open("basicinfo.txt", "r", encoding="utf-8") as f:
                if any(line.split(',')[0] == usr for line in f if ',' in line):
                    print("Username already taken!")
                    user_exists = True
        except FileNotFoundError:
            pass

        if not user_exists:
            break

    suggested_secure = gen_strong_ascii_pw()
    print(f"Suggested Secure Password (Saved to file): {suggested_secure}\n")
    
    while True:
        pw = input("Enter your chosen password: ").strip()
        pc = error_check(pw)

        if pc == True:
            hashed_pw = hash_password(pw)
            with open("basicinfo.txt", "a", encoding="utf-8") as f:
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
        with open(secret_filename, "w", encoding="utf-8") as f:
            f.write("You Did It!")

    print(f"--- Opening Secure Document '{secret_filename}' ---")
    with open(secret_filename, "r", encoding="utf-8") as f:
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
            with open('basicinfo.txt', 'r', encoding='utf-8') as file:
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
