# Challenge 21 - Data Entry
# Created: 21/10/2026
# Last Updated: 21/10/2026

import json
import os

FILENAME = "climbing_club_members.json"

def load_members():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading file. Starting with an empty database.")
            return []
    return []

def save_members(members):
    try:
        with open(FILENAME, 'w') as file:
            json.dump(members, file, indent=4)
        print(f"\n[System] Successfully saved all details to '{FILENAME}'.")
    except IOError:
        print("\n[Error] Could not save details to file.")

def get_membership_input():
    print("\n--- Enter Membership Details ---")
    name = input("Full Name: ").title().strip()
    while True:
        try:
            age = int(input("Age: "))
            if age < 13:
                raise ValueError
            break
        except ValueError:
            print("You must enter a number greater than 12.")

    while True:
        skill_level = input("Skill Level (Beginner/Intermediate/Advanced): ").strip().capitalize()
        if skill_level in ("Beginner", "Intermediate", "Advanced"):
            break
        print("Invalid skill level.")

    while True:
        emergency_contact = input("Emergency Contact Number: ").strip()
        if emergency_contact.isdigit():
            break
        print("Invalid contact number.")

    print("\n=== Please Confirm Details ===")
    print(f"Name:              {name}")
    print(f"Age:               {age}")
    print(f"Skill Level:       {skill_level}")
    print(f"Emergency Contact: {emergency_contact}")
    print("==============================")
    
    confirm = input("Are these details correct? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        return {
            "name": name,
            "age": age,
            "skill_level": skill_level,
            "emergency_contact": emergency_contact
        }
    else:
        print("\n[System] Details cleared. Please try again.")
        return None

def search_members(members):
    if not members:
        print("\n[System] No members available to search.")
        return
        
    query = input("\nEnter member name to search for: ").strip().lower()
    found = False
    
    print(f"\n--- Search Results for '{query}' ---")
    for member in members:
        if query in member['name'].lower():
            print(f"\nName: {member['name']}")
            print(f"Age: {member['age']}")
            print(f"Skill Level: {member['skill_level']}")
            print(f"Emergency Contact: {member['emergency_contact']}")
            found = True
            
    if not found:
        print("No matching members found.")

def display_all_members(members):
    if not members:
        print("\n[System] No members registered yet.")
        return
    print("\n--- Registered Rock Climbing Club Members ---")
    for idx, member in enumerate(members, 1):
        print(f"{idx}. {member['name']} ({member['skill_level']})")

def main():
    members = load_members()
    
    while True:
        print("\n==========================================")
        print("   ROCK CLIMBING CLUB MEMBERSHIP SYSTEM   ")
        print("==========================================")
        print("1. Add New Membership(s)")
        print("2. View All Members")
        print("3. Search for a Member")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            adding = True
            while adding:
                member_data = get_membership_input()
                if member_data:
                    members.append(member_data)
                    save_members(members)
                
                again = input("\nWould you like to add another member? (yes/no): ").strip().lower()
                if again not in ['yes', 'y']:
                    adding = False
                    
        elif choice == '2':
            display_all_members(members)
            
        elif choice == '3':
            search_members(members)
            
        elif choice == '4':
            print("\nThank you for using the Membership System. Goodbye!")
            break
        else:
            print("\n[Invalid Selection] Please choose a valid menu number.")

main()
