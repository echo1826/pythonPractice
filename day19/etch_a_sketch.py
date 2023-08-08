from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(5)

def move_backward():
    turtle.backward(5)

def rotate_right():
    turtle.right(5)

def rotate_left():
    turtle.left(5)

def reset():
    turtle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(reset, "c")


screen.exitonclick()