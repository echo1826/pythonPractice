from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_one = Paddle((-350, 0))
player_two = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

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
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(player_two.paddle) < 50 and ball.xcor() > 320 or ball.distance(player_one.paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

    ball.move()



screen.exitonclick()