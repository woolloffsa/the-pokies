# Lists project
# The Pokies

import random

# Create reels and symbol bank lists
reels = []
current_reel = []
symbol_bank = ["🍒", "7", "🔔", "💎", "💲"]

spin = input("spin?(y/n) ")

while spin == "y":
    for reel in range(3):   # Resets after filling a reel
        current_reel = []
        for symbol in range(3): # Puts symbols in reels
            random_symbol = random.choice(symbol_bank)
            current_reel.append(random_symbol)
        reels.append(current_reel)
    # Lists of winning patterns
    diagonal_line = [reels[0][0], reels[1][1], reels[2][2]] 
    straight_line = [reels[0][1], reels[1][1], reels[2][1]]
    # Checks for a win
    if diagonal_line.count(diagonal_line[0]) == 3:  
        print("You Win!!")
    elif straight_line.count(straight_line[0]) == 3:
        print("You Win")
    else:
        print("No win")
    row = 0
    for i in range(3):
        print(reels[0][row], reels[1][row], reels[2][row])
        row += 1
    reels = []
    spin = input("spin?(y/n) ")
