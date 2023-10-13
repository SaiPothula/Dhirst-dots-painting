###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

# This project will create D hirst dots painting

import colorgram
from turtle import Turtle, Screen
from random import choice

rgb_colors = []
colors = colorgram.extract('image.jpg', 100)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_colors.append(new_color)

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)
my_turtle.speed("fastest")
dots_in_row = 5
space_bw_dots = 30
dots_in_col = 10
dot_size = 20
for y in range(0,dots_in_col*space_bw_dots,space_bw_dots):
    for x in range(dots_in_row):
        my_turtle.dot(dot_size, choice(rgb_colors))
        my_turtle.penup()
        my_turtle.forward(space_bw_dots)
    my_turtle.goto(0, y+space_bw_dots)
    print(f"y={y}, {my_turtle.position()}")


screen.exitonclick()
