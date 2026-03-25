# Lists project
# The Pokies

import random

# Create reels and symbol bank lists
SYMBOL_BANK = ["🍒", "7", "🔔", "💎", "💲"]
wildcard_symbol = "⭐"
REEL_COUNT = 3

#

def generate_reels(bank, wildcard, count):
    reels = []
    current_reel = []
   
    for reel in range(REEL_COUNT):   # Resets after filling a reel
        current_reel = []
        # Puts symbols in reels
        for symbol in range(3):
            random_symbol = random.choice(SYMBOL_BANK + [wildcard_symbol])
            current_reel.append(random_symbol)
        reels.append(current_reel)
       
    return reels


def is_win(reels, wildcard, target_count):
    match_count = 0
    # Lists of winning patterns
    diagonal_line = [reels[0][0], reels[1][1], reels[2][2]]
    straight_line = [reels[0][1], reels[1][1], reels[2][1]]
    # Checks for a win
    if diagonal_line.count(diagonal_line[0]) + diagonal_line.count(wildcard_symbol) == REEL_COUNT:
        print("Diagonal Win!!")
       
    elif straight_line.count(straight_line[0]) + straight_line.count(wildcard_symbol) == REEL_COUNT:
        print("Straight Line Win!!")
           
    else:
        print("No win")


def display_reels(reels):
    # Prints reels in a formatted way
    for row in range(3):
        print(reels[0][row], reels[1][row], reels[2][row])


# main routine
if __name__ == "__main__":
   
    spin = input("spin?(y/n) ")

    while spin == "y":
       reels = generate_reels(SYMBOL_BANK, wildcard_symbol, REEL_COUNT)
       display_reels(reels)
       win = is_win(reels, wildcard_symbol, REEL_COUNT)
       spin = input("spin?(y/n) ")
       
    print("Thanks for playing!")
