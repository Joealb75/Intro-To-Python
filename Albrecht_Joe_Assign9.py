import random

MIN = 1
MAX = 6

play = input("Would you like to roll the dice? ( Y = Yes, N = No) : ").upper()


def roll_dice(previous_roll):

    dice = random.randrange(MIN, MAX)  # Picks a number in a random range of 1-6

    if previous_roll == 0:
        return dice

    while previous_roll == dice:        # Gets stuck here if the current roll is the same as the previous roll.
        dice = random.randrange(MIN, MAX)

    if previous_roll != dice:   # If the previous roll and the current roll are != it will return the current roll.
        return dice


previous_roll = 0  # Initialize the previous roll

while play == "Y" or play == "YES":

    d_roll = roll_dice(previous_roll)
    print(d_roll)
    previous_roll = d_roll  # Updates the previous roll with the current roll
    play = input("Would you like to roll the dice? ( Y = Yes, N = No) : ").upper()
