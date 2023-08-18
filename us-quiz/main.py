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
all_states = data.state.to_list()
num_answered = 0
answer_correct = []

while num_answered != 50:
    answer = screen.textinput(title=f"{num_answered}/50 States Correct", prompt="Give a state name")
    row = data[data.state == answer.title()]
    if answer.title() == "Exit":
        break
    if len(row):
        pen.goto(row.x.values[0], row.y.values[0])
        pen.write(answer.title())
        num_answered += 1
        answer_correct.append(answer.title())

for state in answer_correct:
    all_states.remove(state)

pandas.DataFrame(all_states).to_csv("missing_states.csv")

screen.exitonclick()