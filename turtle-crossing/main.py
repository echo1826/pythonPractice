import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_manager.timer % 6 == 0:
        car_manager.generate_car()
    car_manager.timer += 1
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
    
    if player.finish():
        scoreboard.update_score()
        car_manager.increase_speed()

scoreboard.game_over()
screen.exitonclick()