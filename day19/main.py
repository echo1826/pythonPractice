from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_right():
    turtle.forward(10)

screen.listen()
screen.onkey(move_right, "Right")
screen.exitonclick()