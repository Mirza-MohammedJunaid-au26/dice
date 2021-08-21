import random


def roll_dice(min, max):
    while True:
        print("Rolling Dice....") 
        print(f"Your Number : {random.randint(min, max)}")
        choice = input(" Do you want to Roll the Dice Again ? (y/n) ")
        if choice.lower == 'n':
            break
roll_dice(1, 6)
