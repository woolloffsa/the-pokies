# Lists project
# The Pokies

import random

# Create reels and symbol bank lists
SYMBOL_BANK = ["🍒", "7", "🔔", "💎", "💲"]
WILDCARD_SYMBOL = "⭐"
REEL_COUNT = 3
SPIN_COST = 1
BALANCE = 10

# function definitions

def generate_reels(bank, wildcard, count):
    """Generates the reels"""
    reels = []
    current_reel = []
   
    for reel in range(REEL_COUNT):   # Resets after filling a reel
        current_reel = []
        # Puts symbols in reels
        for symbol in range(3):
            random_symbol = random.choice(SYMBOL_BANK + [WILDCARD_SYMBOL])
            current_reel.append(random_symbol)
        reels.append(current_reel)
       
    return reels


def is_win(reels, wildcard, target_count):
    """Checks for a win"""
    match_count = 0
    # Lists of winning patterns
    diagonal_line = [reels[0][0], reels[1][1], reels[2][2]]
    straight_line = [reels[0][1], reels[1][1], reels[2][1]]
    # Checks for a win
    if diagonal_line.count(diagonal_line[0]) + diagonal_line.count(WILDCARD_SYMBOL) == REEL_COUNT:
        print("Diagonal Win!!")
        win = 10
       
    elif straight_line.count(straight_line[0]) + straight_line.count(WILDCARD_SYMBOL) == REEL_COUNT:
        print("Straight Line Win!!")
        win = 5
           
    else:
        print("No win")
        win = 0

    return win


def display_reels(reels):
    """Prints reels in a formatted way"""
    for row in range(3):
        print(reels[0][row], reels[1][row], reels[2][row])


# main routine
if __name__ == "__main__":

    # Add try except
    spin = input("spin?(y/n) ")

    while spin == "y":
        reels = generate_reels(SYMBOL_BANK, WILDCARD_SYMBOL, REEL_COUNT)
        display_reels(reels)
        is_win(reels, WILDCARD_SYMBOL, REEL_COUNT)
        current_win = is_win(reels, WILDCARD_SYMBOL, REEL_COUNT)
        BALANCE -= SPIN_COST
        BALANCE += current_win
        print("Your current balance is ${}".format(BALANCE))
        spin = input("spin?(y/n) ")
       
    print("Thanks for playing!")
