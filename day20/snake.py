from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        
        self.create_snake()

    def create_snake(self):
        for position in STARTING_COORDINATES:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_segment = self.segments[i - 1]
            self.segments[i].goto(next_segment.pos())
        self.segments[0].forward(20)