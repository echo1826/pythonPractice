import random

first_dice = random.randint(1, 6)
second_dice = random.randint(1, 6)

while first_dice != 1 or second_dice != 1:
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    print(first_dice, second_dice)

print("SNAKE EYES!")