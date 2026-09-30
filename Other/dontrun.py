# don't run
import os
from random import randint
import sys
from time import sleep

def print_warning(message):
    sys.stderr.write(f"\n{message}\n")
    sys.stderr.flush()

for frame in range(5):
    for i in range(100):
        x = " " * randint(1, 20) 
        print(f"{x}{i}{x}", end=" ") 
    
    sleep(0.1)
    print() 
    
    print_warning(f"{5 - frame} seconds left: Stop the program now!")
    sleep(1)

bl = """
Y88b   d88P                             888                        888      888                 
 Y88b d88P                              888                        888      888                 
  Y88o88P                               888                        888      888                 
   Y888P  .d88b.  888  888     .d8888b  88888b.   .d88b.  888  888 888  .d88888                 
    888  d88""88b 888  888     88K      888 "88b d88""88b 888  888 888 d88" 888                 
    888  888  888 888  888     "Y8888b. 888  888 888  888 888  888 888 888  888                 
    888  Y88..88P Y88b 888          X88 888  888 Y88..88P Y88b 888 888 Y88b 888                 
    888   "Y88P"   "Y88888      88888P' 888  888  "Y88P"   "Y88888 888  "Y88888                 
                                                                                                
                                                                                                
                                                                                                
d8b                      888 d8b          888                                   888             
88P                      888 Y8P          888                                   888             
8P                       888              888                                   888             
"  888  888  .d88b.      888 888 .d8888b  888888 .d88b.  88888b.   .d88b.   .d88888             
   888  888 d8P  Y8b     888 888 88K      888   d8P  Y8b 888 "88b d8P  Y8b d88" 888             
   Y88  88P 88888888     888 888 "Y8888b. 888   88888888 888  888 88888888 888  888             
    Y8bd8P  Y8b.         888 888      X88 Y88b. Y8b.     888  888 Y8b.     Y88b 888             
     Y88P    "Y8888      888 888  88888P'  "Y888 "Y8888  888  888  "Y8888   "Y88888                                                    
"""
print(bl)
sleep(1)

# Color and Style Palette
COLOR_EMOJI_1 = "🟥"  # Red Square
COLOR_EMOJI_2 = "🟦"  # Blue Square
COLOR_EMOJI_3 = "🟧"  # Orange Square
COLOR_EMOJI_4 = "🟨"  # Yellow Square
COLOR_EMOJI_5 = "🟩"  # Green Square
COLOR_EMOJI_6 = "🟪"  # Purple Square
EMPTY_EMOJI   = "⬜"  # White Square 
EMPTY_EMOJI2  = "⬛"  # Black Square

for frame in range(10):
    # Dynamic sizing fallback defaults to 80x24 if not running in a real terminal
    try:
        terminal_columns, terminal_lines = os.get_terminal_size()
    except OSError:
        terminal_columns, terminal_lines = 80, 24

    # Emojis count as double width characters in many terminals or need adjustments.
    # Since most emoji blocks are wide, we divide columns by 2 to prevent wrapping text.
    width = max(1, terminal_columns // 2)
    rows = max(1, terminal_lines - 1)  # Leave 1 line safety margin to prevent scrolling issues

    # Frame 1: Red (stderr)
    for _ in range(rows):
        sys.stderr.write(COLOR_EMOJI_1 * width + "\n")
    sys.stderr.flush()
    sleep(0.07)
    
    # Frame 2: Blue (stdout)
    for _ in range(rows):
        print(COLOR_EMOJI_2 * width)
    sleep(0.07)
    
    # Frame 3: Orange
    for _ in range(rows):
        print(COLOR_EMOJI_3 * width)
    sleep(0.07)

    # Frame 4: Yellow
    for _ in range(rows):
        print(COLOR_EMOJI_4 * width)
    sleep(0.07)

    # Frame 5: Green
    for _ in range(rows):
        print(COLOR_EMOJI_5 * width)
    sleep(0.07)

    # Frame 6: Purple
    for _ in range(rows):
        print(COLOR_EMOJI_6 * width)
    sleep(0.07)
    
    # Frame 7: Clear/Blank White
    for _ in range(rows):
        print(EMPTY_EMOJI * width)
    sleep(0.07)

    # Frame 8: Clear/Blank Black
    for _ in range(rows):
        print(EMPTY_EMOJI2 * width)
    sleep(0.07)
