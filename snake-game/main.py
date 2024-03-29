from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# canvas for the game
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.increase_size()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_running = False
        scoreboard.reset()
        snake.reset()

    # detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_running = False
            scoreboard.reset()
            snake.reset()



screen.exitonclick()






