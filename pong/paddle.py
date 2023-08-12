from turtle import Turtle



class Paddle:
    def __init__(self, position):
        self.paddle = Turtle("square")
        self.paddle.shapesize(1, 5)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)
        self.paddle.setheading(90)

    def up(self):
        self.paddle.setheading(90)
        
    def down(self):
        self.paddle.setheading(270)