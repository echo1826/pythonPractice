import random
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

is_finished = False
num_toothpicks = 13
current_turn = random.randint(1, 2)
while not is_finished:
    print("|" * num_toothpicks)
    print(f"There are {num_toothpicks} toothpicks left")
    
    if current_turn == 1 or current_turn == player2_name:
        current_turn = player1_name
    else:
        current_turn = player2_name
    take_away = int(input(f"How many do you take, {current_turn}?\n"))
    while take_away != 1 and take_away != 2 and take_away != 3:
        take_away = int(input("You can only take 1, 2, or 3:\n"))
    num_toothpicks -= take_away
    if num_toothpicks <= 0:
        is_finished = True
print(f"The winner is {current_turn}!")