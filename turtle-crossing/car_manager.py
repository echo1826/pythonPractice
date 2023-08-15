COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import randint

class CarManager:
    def __init__(self):
        self.timer = 0
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle("square")
        car.penup()
        car.goto(280, randint(-250 , 250))
        car.color(COLORS[randint(0, len(COLORS) - 1)])
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT