# don't run!!!
import os
import random
import sys
import time

def clear_screen():
    # ANSI escape sequences to clear screen and reset cursor position
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()

def print_warning(message):
    sys.stderr.write(f"\x1b[31;1m\n!!! {message} !!!\n\x1b[0m")
    sys.stderr.flush()

# --- Phase 1: High-Speed Countdown Glitch ---
for frame in range(5):
    clear_screen()
    glitch_text = ""
    for _ in range(150):
        spaces = " " * random.randint(1, 30)
        num = random.randint(100, 999)
        glitch_text += f"{spaces}{num}{spaces}"
    
    print(glitch_text[:2000])
    print_warning(f"CRITICAL OVERLOAD IN {5 - frame} SECONDS")
    time.sleep(0.4)  # Faster countdown

clear_screen()
bl = """
\x1b[31m
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
\x1b[0m"""
print(bl)
time.sleep(0.8)

# --- Phase 2: Fullscreen Hyper-Flicker Loop ---
PALETTE = ["🟥", "🟦", "🟧", "🟨", "🟩", "🟪", "⬜", "⬛"]

try:
    while True:  # Infinite loop for maximum impact (Press Ctrl+C to stop)
        try:
            cols, lines = os.get_terminal_size()
        except OSError:
            cols, lines = 80, 24

        width = max(1, cols // 2)
        
        # Mode A: Solid flashing colors
        for color in PALETTE:
            frame_buffer = "".join([color * width + "\n" for _ in range(lines)])
            sys.stdout.write("\x1b[H" + frame_buffer)
            sys.stdout.flush()
            time.sleep(0.03)  # Cut delay in half for blinding speed


except KeyboardInterrupt:
    clear_screen()
    print("\x1b[32;1mExecution halted safely.\x1b[0m")
