# Lists project
# The Pokies

import random

# Create reels and symbol bank lists
reels = []
current_reel = []
symbol_bank = ["🍒", "7"]

spin = input("spin?(y/n) ")

while spin == "y":
    for reel in range(3):   # Resets after filling a reel
        current_reel = []
        for symbol in range(3): # Puts symbols in reels
            random_symbol = random.choice(symbol_bank)
            current_reel.append(random_symbol)
        reels.append(current_reel)
    # Checks for a straight across win
    if reels[0][1] == reels[1][1] and reels[1][1] == reels[2][1]:
        print("You Win!!")
    else:
        print("No win")
    reels = []
    spin = input("spin?(y/n) ")
