from turtle import Turtle

with open("./high-score.txt") as high_score_file:
    HIGH_SCORE = high_score_file.read()


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score} High Score {self.high_score}", False, align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("./high-score.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.score}")
                self.high_score = self.score
        self.score = 0
        self.update_score()
    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 15, "normal"))