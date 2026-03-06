# Lists project
# The Pokies

import random

# Create reels and symbol bank lists
reels = []
current_reel = []
symbol_bank = ["🍒", "7", "🔔", "💎", "💲"]
wildcard_symbol = "⭐"
reel_count = 3
match_count = 0

spin = input("spin?(y/n) ")

while spin == "y":
    
    reels = []
    
    for reel in range(reel_count):   # Resets after filling a reel
        current_reel = []
        # Puts symbols in reels
        for symbol in range(3):
            random_symbol = random.choice(symbol_bank + [wildcard_symbol])
            current_reel.append(random_symbol)
        reels.append(current_reel)
        
    # Lists of winning patterns
    diagonal_line = [reels[0][0], reels[1][1], reels[2][2]]
    straight_line = [reels[0][1], reels[1][1], reels[2][1]]
    
    # Checks for a win
    if diagonal_line.count(diagonal_line[0]) + diagonal_line.count(wildcard_symbol) == reel_count:
        print("Diagonal Win!!")
        
    elif straight_line.count(straight_line[0]) + straight_line.count(wildcard_symbol) == reel_count:
        print("Straight Line Win!!")
            
    else:
        print("No win")
        
    # Prints reels in a formatted way
    for row in range(3):
        print(reels[0][row], reels[1][row], reels[2][row])
    spin = input("spin?(y/n) ")
       
print("Thanks for playing!")
