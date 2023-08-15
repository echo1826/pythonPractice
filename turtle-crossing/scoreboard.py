FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200 , 250)
        self.current_level = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
