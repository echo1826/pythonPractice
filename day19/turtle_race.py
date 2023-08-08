from turtle import Turtle, Screen
from random import randint

screen = Screen()

# sets the screen to width = 500px and height = 400px
screen.setup(width=500, height=400)


user_choice = screen.textinput(
    "Turtle Race Winner", "Who will win the race? Enter a color:")

colors = ["red", "blue", "orange", "yellow", "purple", "green"]

y = -100

turtles = []

for color in colors:
    turtle = Turtle()
    turtle.penup()
    turtle.color(color)
    turtle.goto(-230, y)
    y = y + 50



finish_line = 240

while True:
    turtles = screen.turtles()
    random_turtle = turtles[randint(0, 5)]
    rand_distance = randint(0, 10)
    random_turtle.forward(rand_distance)
    if random_turtle.xcor() >= 240:
        winner = random_turtle.color()
        break

if winner[1] == user_choice:
    print("You won")
else:
    print("You lost")

screen.exitonclick()
