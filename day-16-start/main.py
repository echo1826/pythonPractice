from turtle import Turtle, Screen
import another_module

# print(another_module.another_variable)

# Turtle class that can draw things in a window
turtle_obj = Turtle()
print(turtle_obj)
turtle_obj.shape('turtle')

# Screen class that represents the window in which the turtle draws in
my_screen = Screen()
print(my_screen.canvheight)
# exit on click will allow the window to continue showing until we click
my_screen.exitonclick()
