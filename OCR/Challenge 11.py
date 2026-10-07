# Challenge 11 - Regex Query Tool
# Created: 07/10/2026
# Last Updated: 07/10/2026

import re

def regcheck(source_text):
    while True:
        pattern = input("\n2. Enter Regex Pattern: ")
        
        if pattern.lower() == "exit": 
            print("Returning to main menu...")
            return
        if not pattern:
            print("Pattern cannot be empty.")
            continue
            
        try:
            regex = re.compile(pattern)
            matches = list(regex.finditer(source_text))
            match_count = len(matches)
            
            if match_count == 0:
                print("-> Status: No matches found.")
            else:
                match_word = "match" if match_count == 1 else "matches"
                print(f"-> Status: Success! Found {match_count} {match_word}:")
                    
                for idx, match in enumerate(matches, 1):
                    print(f"   Match {idx}: '{match.group()}' (Positions: {match.start()} to {match.end()})")
        
        except re.error as e:
            print(f"-> Regex Error: {e}")

def run_regex_tool():
    print("=== Regex Query Tool ===")
    print("Type 'exit' at any prompt to quit.\n")
    
    while True:
        source_text = input("\n1. Enter Source Text: ")
        
        if source_text.lower() == "exit": 
            print("Program ended.")
            break
        if not source_text:
            print("Source text cannot be empty.")
            continue
            
        regcheck(source_text)

run_regex_tool()
