import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. Quiz")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer = screen.textinput(title="Guess The State", prompt="Give a state name")


screen.exitonclick()