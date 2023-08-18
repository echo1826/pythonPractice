import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. Quiz")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
data = pandas.read_csv("50_states.csv")
num_answered = 0

while num_answered != 50:
    answer = screen.textinput(title=f"{num_answered}/50 States Correct", prompt="Give a state name")
    row = data[data.state == answer.title()]
    if len(row):
        pen.goto(row.x.values[0], row.y.values[0])
        pen.write(answer.title())
        num_answered += 1


screen.exitonclick()