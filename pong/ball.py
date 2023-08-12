from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        self.up()
        self.right()

    def up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())