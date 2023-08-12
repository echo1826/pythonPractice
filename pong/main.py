from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_one = Paddle((-385, 0))
player_two = Paddle((380, 0))


screen.listen()
screen.onkey(player_two.up, "Up")
screen.onkey(player_two.down, "Down")
screen.onkey(player_one.up, "w")
screen.onkey(player_one.down, "s")



game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(0.1)
    player_one.paddle.forward(20)
    player_two.paddle.forward(20)


screen.exitonclick()