from turtle import Turtle, Screen
from random import choice
# from colorgram import extract
# color_data = extract("hirst.jpg", 30)
# color = []
# for i in color_data:
#     one_color = (i.rgb.r, i.rgb.g, i.rgb.b)
#     color.append(one_color)
# print(color)

color = [(214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)]
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
my_screen = Screen()
my_screen.colormode(255)
tim.penup()
tim.goto(-225,-250)
for i in range(10):
    for _ in range(10):
        tim.dot(20, choice(color))
        tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


my_screen.exitonclick()
