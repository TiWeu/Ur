import random

# Constants
number_of_sides = 4
number_of_pips = 2

class Dice():
    def __init__(self):
        # Chance to roll a pip
        self.chance = (number_of_pips / number_of_sides) * 100

    def roll_dice(self):
        # Random number between 1 and 100 -> if the number is smaller or equal the chance a pip is rolled
        roll = random.uniform(1, 100)
        if roll <= self.chance:
            return 1
        else:
            return 0