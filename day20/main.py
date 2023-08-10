from turtle import Screen
import time
from snake import Snake

# canvas for the game
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


while True:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()






