# don't run
from random import randint
from time import sleep
import sys

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
for i in range(10):
    for i in range(100):
        print("█" * 100)
    sleep(.1)
    for i in range(100):
        print(" " * 100)
    sleep(.1)
