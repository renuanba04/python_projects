# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
# for color in colors:
#     r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random

colors_list = [(125, 88, 63), (194, 159, 94), (138, 63, 80), (74, 105, 73), (67, 86, 117), (173, 153, 49), (79, 23, 38), (120, 34, 50), (65, 52, 38), (244, 235, 238), (24, 47, 74), (214, 202, 129), (133, 165, 133), (193, 82, 99), (45, 56, 110), (78, 71, 34), (131, 36, 30), (41, 59, 45), (97, 163, 72), (139, 152, 167), (204, 93, 73), (177, 147, 154), (41, 77, 66), (118, 119, 145), (65, 153, 165), (41, 77, 83), (216, 177, 184)]

def hirst_dot_painting(x_pos, y_pos):
    my_screen = Screen()
    my_screen.colormode(255)
    timmy = Turtle()
    timmy.teleport(x_pos, y_pos)
    timmy.speed("fast")
    timmy.hideturtle()
    for _ in range(10):
        for _ in range(10):
            timmy.dot(20, random.choice(colors_list))
            curr_x = timmy.pos()[0]
            timmy.teleport(curr_x + 50)

        curr_y = timmy.pos()[1]
        timmy.teleport(x_pos, y=curr_y + 50)
    my_screen.exitonclick()

def square_painting(x_pos, y_pos):
    my_screen = Screen()
    my_screen.colormode(255)
    timmy = Turtle()
    timmy.shape("square")
    timmy.teleport(x_pos, y_pos)
    timmy.speed("fast")
    timmy.hideturtle()
    for y in range(1, 11):
        for x in range(1, 11):
            timmy.color(random.choice(colors_list))
            timmy.stamp()
            curr_x = timmy.pos()[0]
            timmy.teleport(curr_x + 50)

        curr_y = timmy.pos()[1]
        timmy.teleport(x_pos, y= curr_y + 50)
    my_screen.exitonclick()

my_function = random.choice([hirst_dot_painting, square_painting])
my_function(-200, -200)
