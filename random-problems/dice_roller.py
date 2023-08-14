import random

num_dice = int(input("How many dice are we rolling? "))
num_dice_side = int(input("How many sides on each die? "))

answer = ""
while answer != "q":
    output = ""
    for dice in range(1, num_dice + 1):
        roll = str(random.randint(1, num_dice_side))
        output += roll + '|'
    print(output)
    answer = input("Roll again? ('q' to quit) ")

